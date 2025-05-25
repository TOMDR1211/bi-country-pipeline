# 🛰️ BI Automation to BigQuery

ETL pipeline written in Python that pulls data from the [RESTCountries API](https://restcountries.com/), processes it with `pandas`, and loads it into Google BigQuery.

---

## 📁 Project Structure

```
.
├── app/
│   ├── api_connector.py     # Pulls data from the REST API
│   ├── main.py              # Handles transformation and DataFrame creation
│   └── load_bq.py           # Loads processed data into BigQuery
│
├── credentials/
│   └── BigQuery/            # Holds the service account key (not pushed)
│
├── .env                     # Environment variables (ignored in .gitignore)
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🧰 Tech Stack

- **Python**: `pandas`, `pandas-gbq`, `python-dotenv`
- **BigQuery**: Google Cloud project with service account authentication

---

## 🔑 Setup

1. **Clone the repo**  
   ```bash
   git clone https://github.com/TOMDR1211/bi-country-pipeline.git
   cd bi-country-pipeline
   ```

2. **Create and activate virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables in `.env`**  
   ```env
   GCP_PROJECT_ID=your-project-id
   BQ_DATASET_ID=your-dataset-id
   GOOGLE_APPLICATION_CREDENTIALS=path/to/your/credentials.json
   ```

---

## 🚀 Run

```bash
python app/main.py       # Pull + Transform
python app/load_bq.py    # Load to BigQuery
```

---

## 📌 Notes

- The `.gitignore` prevents credentials and sensitive files from being tracked.
- All data transformations are done with `pandas` prior to upload.

---

## 📄 License

MIT License