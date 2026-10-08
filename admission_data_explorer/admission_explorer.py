
# python admission_explorer.py
# python admission_explorer.py --input data/applications.csv --ai   

import argparse
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

REQUIRED = ["jamb_reg_no", "gender", "program_applied", "admission_status"]


def load_data(path):
    """Read the CSV and stop with a clear message if something is wrong."""
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        raise SystemExit(f"File not found: {path}. Run generate_mock_data.py first.")
    except pd.errors.EmptyDataError:
        raise SystemExit(f"File is empty: {path}")
    except pd.errors.ParserError:
        print("Some rows are malformed, skipping them...")
        df = pd.read_csv(path, on_bad_lines="skip", engine="python")

    df.columns = df.columns.str.strip().str.lower()
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise SystemExit(f"Missing required columns: {missing}")
    return df


def clean_data(df):
    """Fix text, remove impossible values, drop duplicates, fill missing data."""
    start = len(df)

    # used to standardise the text
    for col in ["gender", "program_applied", "admission_status", "state_of_origin"]:
        if col in df.columns:
            df[col] = df[col].str.strip().str.title()
    df["gender"] = df["gender"].replace({"M": "Male", "F": "Female"})

    # turn numbers into numbers and remove impossible values
    limits = {"age": (14, 60), "exam_score": (0, 100), "high_school_gpa": (0, 4)}
    for col, (low, high) in limits.items():
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            df.loc[~df[col].between(low, high), col] = np.nan

    # duplicates
    df = df.drop_duplicates()
    df = df.drop_duplicates(subset="jamb_reg_no", keep="last")

    # rows without a program or outcome are useless
    df = df.dropna(subset=["program_applied", "admission_status"])

    # filling in values => median for numbers, "Unknown" for text
    for col in limits:
        if col in df.columns:
            df[col] = df[col].fillna(df[col].median())
    df["gender"] = df["gender"].fillna("Unknown")

    print(f"Cleaned data: {start} rows -> {len(df)} rows")
    return df.reset_index(drop=True)


def get_metrics(df):
    """Acceptance rate, gender ratios and top 5 programs."""
    decided = df[df["admission_status"] != "Pending"]
    accepted = decided["admission_status"] == "Accepted"

    return {
        "total": len(df),
        "pending": int((df["admission_status"] == "Pending").sum()),
        "acceptance_rate": round(accepted.mean() * 100, 1),
        "gender_share": (df["gender"].value_counts(normalize=True) * 100).round(1).to_dict(),
        "gender_acceptance": (accepted.groupby(decided["gender"]).mean() * 100).round(1).to_dict(),
        "top5": df["program_applied"].value_counts().head(5).to_dict(),
        "by_program": (accepted.groupby(decided["program_applied"]).mean() * 100).round(1).to_dict(),
    }


def make_insight(m):
    """Rule-based summary: a text template plus simple thresholds."""
    top_program = list(m["top5"])[0]
    text = f"Most applicants prefer {top_program}. "
    text += f"The overall acceptance rate is {m['acceptance_rate']}%. "

    female = m["gender_acceptance"].get("Female", 0)
    male = m["gender_acceptance"].get("Male", 0)
    if abs(female - male) < 2:
        text += f"Acceptance is similar for both genders (female {female}%, male {male}%). "
    elif female > male:
        text += f"Female applicants are accepted more often ({female}% vs {male}%). "
    else:
        text += f"Male applicants are accepted more often ({male}% vs {female}%). "

    hardest = min(m["by_program"], key=m["by_program"].get)
    text += f"{hardest} is the most competitive program ({m['by_program'][hardest]}% accepted)."
    return text


def ai_insight(m):
    """Ask Google Gemini to summarize the metrics. Returns None if anything fails."""
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        print("GEMINI_API_KEY not set, using the rule-based summary instead.")
        return None

    model = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    prompt = ("You are a data analyst. Summarize these admission statistics in 3-4 plain "
              f"English sentences for admissions staff. Only use these numbers: {m}")
    try:
        response = requests.post(url, headers={"x-goog-api-key": key}, timeout=30, json={"contents": [{"parts": [{"text": prompt}]}]})
        response.raise_for_status()
        return response.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
    except Exception as e:
        print("AI request failed, using the rule-based summary instead:", e)
        return None


def make_charts(df, folder="output/charts"):
    """Save the charts as PNG files."""
    os.makedirs(folder, exist_ok=True)
    sns.set_theme(style="whitegrid")

    # bar chart of top 5 programs
    plt.figure(figsize=(8, 4))
    df["program_applied"].value_counts().head(5).sort_values().plot(kind="barh", color="#262953")
    plt.title("Top 5 programs by demand")
    plt.xlabel("Applications")
    plt.tight_layout()
    plt.savefig(f"{folder}/top_programs.png")
    plt.close()

    # pie chart of gender distribution
    plt.figure(figsize=(5, 5))
    df["gender"].value_counts().plot(kind="pie", autopct="%1.1f%%", startangle=90)
    plt.title("Gender distribution")
    plt.ylabel("")
    plt.savefig(f"{folder}/gender_pie.png")
    plt.close()

    # pie chart of admission outcome
    plt.figure(figsize=(5, 5))
    df["admission_status"].value_counts().plot(kind="pie", autopct="%1.1f%%", startangle=90)
    plt.title("Admission outcomes")
    plt.ylabel("")
    plt.savefig(f"{folder}/outcomes_pie.png")
    plt.close()

    # histogram of exam scores by outcome
    plt.figure(figsize=(8, 4))
    decided = df[df["admission_status"] != "Pending"]
    sns.histplot(data=decided, x="exam_score", hue="admission_status", bins=25)
    plt.title("Exam scores: accepted vs rejected")
    plt.tight_layout()
    plt.savefig(f"{folder}/exam_scores.png")
    plt.close()

    # bar chart of acceptance rate per program 
    plt.figure(figsize=(8, 5))
    rates = (decided["admission_status"] == "Accepted").groupby(decided["program_applied"]).mean() * 100
    rates.sort_values().plot(kind="barh", color="#822a9d")
    plt.title("Acceptance rate by program (%)")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(f"{folder}/acceptance_by_program.png")
    plt.close()


def save_reports(m, insight, folder="output"):
    """Write the summary as CSV and HTML."""
    os.makedirs(folder, exist_ok=True)

    summary = pd.DataFrame({
        "metric": ["total_applicants", "pending", "acceptance_rate_pct"],
        "value": [m["total"], m["pending"], m["acceptance_rate"]],
    })
    top5 = pd.Series(m["top5"], name="applications").rename_axis("program").reset_index()
    summary.to_csv(f"{folder}/summary_report.csv", index=False)
    top5.to_csv(f"{folder}/top5_programs.csv", index=False)

    charts = "".join(f'<img src="charts/{name}.png" width="480">'
                     for name in ["top_programs", "gender_pie", "outcomes_pie",
                                  "exam_scores", "acceptance_by_program"])
    html = f"""<html><head><title>Admission Report</title>
<style>body{{font-family:Arial;max-width:1000px;margin:auto}} td,th{{padding:6px 12px}}</style></head>
<body>
<h1>Admission Data Explorer Report</h1>
<h2>Summary</h2><p>{insight}</p>
{summary.to_html(index=False)}
<h2>Top 5 programs</h2>{top5.to_html(index=False)}
<h2>Charts</h2>{charts}
</body></html>"""
    with open(f"{folder}/summary_report.html", "w") as f:
        f.write(html)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/applications.csv")
    parser.add_argument("--ai", action="store_true", help="use Gemini for the summary")
    args = parser.parse_args()

    df = clean_data(load_data(args.input))
    metrics = get_metrics(df)
    insight = (ai_insight(metrics) if args.ai else None) or make_insight(metrics)

    make_charts(df)
    save_reports(metrics, insight)
    df.to_csv("output/applications_clean.csv", index=False)

    print("\nInsight:", insight)
    print("Reports saved in the output/ folder")


if __name__ == "__main__":
    main()
