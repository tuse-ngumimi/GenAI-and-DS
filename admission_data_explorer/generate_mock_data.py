# messy mock dataset
import os
import numpy as np
import pandas as pd
import string

np.random.seed(42)
n = 1000

# (share of applicants, base chance of being accepted)
programs = {
    "Computer Science": (0.25, 0.42),
    "Software Engineering": (0.12, 0.45),
    "Medicine & Surgery": (0.10, 0.18),
    "Nursing": (0.09, 0.55),
    "Law": (0.08, 0.30),
    "Accounting": (0.08, 0.60),
    "Mass Communication": (0.06, 0.62),
    "Electrical Engineering": (0.06, 0.40),
    "Economics": (0.06, 0.58),
    "Public Health": (0.05, 0.65),
    "Architecture": (0.03, 0.38),
    "Microbiology": (0.02, 0.66),
}

names = list(programs)
shares = [programs[p][0] for p in names]

df = pd.DataFrame({
    "jamb_reg_no": [
        f"{np.random.randint(10000000, 99999999)}{''.join(np.random.choice(list(string.ascii_uppercase), 2))}" 
        for _ in range(n)
    ],
    "gender": np.random.choice(["Male", "Female"], n, p=[0.52, 0.48]),
    "age": np.clip(np.random.normal(19, 2, n).round(), 16, 40).astype(int),
    "state_of_origin": np.random.choice(["FCT", "Nasarawa", "Kaduna", "Niger", "Plateau", "Lagos", "Kano", "Abia", "Bayelsa", "Enugu", "Kogi", "Taraba", "Ondo", "Oyo", "Benue", "Ogun"], n),
    "program_applied": np.random.choice(names, n, p=shares),
    "exam_score": np.clip(np.random.normal(68, 12, n), 20, 100).round(1).astype(object),
    "high_school_gpa": np.clip(np.random.normal(3.3, 0.45, n), 1.5, 4.0).round(2),
})

# the admission outcome => harder programs & lower scores = lower chance
base = df["program_applied"].map(lambda p: programs[p][1])
chance = (base + (df["exam_score"].astype(float) - 68) / 80).clip(0.03, 0.95)
df["admission_status"] = np.where(np.random.rand(n) < chance, "Accepted", "Rejected")
df.loc[df.sample(frac=0.04).index, "admission_status"] = "Pending"

# missing values
for col, frac in [("gender", 0.03), ("age", 0.04), ("exam_score", 0.05), ("high_school_gpa", 0.06)]:
    df.loc[df.sample(frac=frac).index, col] = np.nan

# inconsistencies
idx = df.sample(frac=0.05).index
df.loc[idx, "gender"] = df.loc[idx, "gender"].str.lower()
idx = df.sample(frac=0.05).index
df.loc[idx, "program_applied"] = df.loc[idx, "program_applied"].str.upper() + " "

# impossible values
df.loc[df.sample(6).index, "age"] = [-5, 0, 150, 999, 7, 120]
df.loc[df.sample(5).index, "exam_score"] = ["N/A", "abc", "--", 250, -10]

# duplicates 
df = pd.concat([df, df.sample(30), df.sample(20)], ignore_index=True)
df = df.sample(frac=1).reset_index(drop=True)

os.makedirs("data", exist_ok=True)
df.to_csv("data/applications.csv", index=False)
print("Saved data/applications.csv with", len(df), "rows")

# added a broken file to test error handling
with open("data/applications_malformed.csv", "w") as f:
    f.write("applicant_id,gender,age\nAPP1,Male,19\nAPP2,Female\nAPP3,Female,20,extra,cols\n")
