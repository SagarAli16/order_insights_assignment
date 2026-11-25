
# Order Insights Assignment – Week 3

## Project Overview
This project focuses on analyzing and cleaning order data using Python, Pandas, Matplotlib, and Seaborn. It also includes an interactive dashboard built with Streamlit.

## Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit

## Project Structure
- `data/` – Contains the original orders dataset.
- `output/` – Contains the cleaned dataset, data quality report, charts, and dashboard screenshot.
- `task2.py` to `task9.py` – Python assignment tasks.
- `app.py` – Streamlit dashboard.
- `requirements.txt` – Required Python packages.
- `README.md` – Project documentation.

## Data Cleaning
The dataset was cleaned by:
- Removing duplicate records.
- Removing records with missing essential details.
- Removing invalid quantity, unit price, and order values.
- Cleaning spaces and standardizing region and category names.
- Converting dates and numeric columns into appropriate data types.

## Dashboard Features
- Dashboard title
- Total orders KPI
- Region filter
- Sales by region chart
- Filtered order data table

## How to Run the Project

### 1. Create a Virtual Environment
```bash
python -m venv .venv
```

### 2. Activate the Virtual Environment
```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Required Packages
```bash
python -m pip install -r requirements.txt
```

### 4. Run the Dashboard
```bash
python -m streamlit run app.py
```

## Output
The project includes a cleaned CSV file, data quality report, three charts, and a Streamlit dashboard screenshot.

## Conclusion
This project demonstrates data cleaning, data analysis, visualization, and interactive dashboard development using Python.