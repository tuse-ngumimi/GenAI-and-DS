# Admission Data Explorer

A Python data analysis project that explores applicant data: gender distribution, program preferences and admission outcomes. It cleans messy data, computes key metrics, draws charts and exports a summary report.

**Tools:** Python, Pandas, Matplotlib, Seaborn, Jupyter Notebook

## How to run
```bash
pip install -r requirements.txt
python generate_mock_data.py        # creates data/applications.csv
python admission_explorer.py        # runs everything, saves results in output/
jupyter notebook Admission_Data_Explorer.ipynb   # step-by-step version
```

## What it does
1. Loads `applications.csv` (with error handling for missing, empty or malformed files)
2. Cleans the data: fixes text, removes impossible values, drops duplicates, fills missing values
3. Computes the acceptance rate, gender ratios and top 5 programs by demand
4. Draws bar charts, pie charts and a histogram
5. Writes a plain-English insight summary
6. Exports `summary_report.csv` and `summary_report.html`

## AI-powered insight
- **Rule-based (default):** a text template with simple thresholds.
- **Gemini API (optional):** get a free key at https://aistudio.google.com/apikey, then
  ```bash
  export GEMINI_API_KEY="your-key"
  python admission_explorer.py --ai
  ```
  If the key is missing or the request fails, it falls back to the rule-based summary. Don't commit your key to GitHub.

## Files
| File | Purpose |
|---|---|
| `generate_mock_data.py` | Creates a messy mock dataset (missing values, duplicates, bad entries) |
| `admission_explorer.py` | The full pipeline as a script |
| `Admission_Data_Explorer.ipynb` | The same analysis, step by step |
| `output/` | Clean data, charts and reports |
