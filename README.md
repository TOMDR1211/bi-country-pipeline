
# BI Country Data Pipeline 🌍

This project extracts, transforms, and loads (ETL) country profile data from the [REST Countries API](https://restcountries.com) into Google BigQuery. The data is modeled into meaningful dimension and fact tables for analytics purposes.

---

## 📁 Project Structure

```
Python BI Automation to BigQuery/
│
├── app/
│   ├── main.py                # Main ETL pipeline logic
│   ├── api_connector.py       # API connection and normalization
│   └── load_bq.py             # Loads final DataFrames to BigQuery
│
├── data/
│   ├── raw/                   # Backup of raw JSON data
│   └── process/               # (Optional) space for transformed files
│
├── credentials/
│   └── BigQuery/              # GCP service account JSON
│
├── .env                       # Environment variables (see below)
├── requirements.txt           # Python dependencies
└── README.md                  # You're here!
```

---

## ⚙️ Environment Configuration (`.env`)

The project uses `python-dotenv` to load sensitive variables. Your `.env` file should include:

```env
GOOGLE_APPLICATION_CREDENTIALS=credentials/BigQuery/<your-json>.json
GCP_PROJECT_ID=bi-country-data-pipeline
GCP_DATASET=dim_fact_restcountries
BQ_DATASET_ID=bi-country-data-pipeline.dim_fact_restcountries
```

---

## 🔄 ETL Process Overview

### 🔹 Extraction
Data is pulled using `requests.get()` from:
```
https://restcountries.com/v3.1/all
```

### 🔹 Transformation
Using `pandas` and `json_normalize`:
- Nested fields are flattened
- Key columns extracted: languages, lat/lng, capital, gini, etc.
- Several fact/dim tables created

### 🔹 Load
Each final DataFrame is loaded to BigQuery via `pandas_gbq.to_gbq()` with `if_exists="replace"`.

---

## 🧱 Final Tables in BigQuery

| Table Name                    | Description                                  |
|------------------------------|----------------------------------------------|
| `df_country_media`           | URLs for flags, maps, and coat of arms       |
| `df_countries`               | Country name and capital                     |
| `df_languages`               | Country-to-language breakdown                |
| `df_fct_state_profile`       | Area, population, borders, lat/lng, density  |
| `df_fct_state_gini`          | GINI index by country and year               |

---

## ▶️ How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run ETL & load
python app/load_bq.py
```

---

## 🧠 Ideas for Next Steps

- Add logging and error handling
- Automate via Airflow / Cloud Functions
- Versioning strategy for changing schemas
- Implement unit tests for API + transformation

---

## 📌 Author

Created by [תום] as a learning project to automate ETL into BigQuery and improve cloud-based BI workflows.
