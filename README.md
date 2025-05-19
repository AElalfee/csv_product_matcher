# CSV Product Matcher

A simple Python utility that compares two CSV files of product data and outputs the matching records.  
Given `data/Missing.csv` and `data/Scanned.csv`, the script finds all rows in *Missing.csv* whose `productCode` also appears in *Scanned.csv*, and writes those rows to `data/Matching.csv`.

---

## 📁 Project Structure

```
.
├── data
│   ├── Missing.csv
│   ├── Scanned.csv
│   └── Matching.csv (generated)
├── src
│   └── main.py
├── pyproject.toml
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔧 Installation

1. **Python Version**  
   Make sure you have **Python 3.8+** installed.

2. **(Optional) Create a Virtual Environment**  
   Recommended to avoid package conflicts:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 How It Works

- The script loads `Missing.csv` and `Scanned.csv` from the `data/` folder.
- It filters rows from `Missing.csv` where the `productCode` is also found in `Scanned.csv`.
- Matching rows are written to `Matching.csv` in the same folder.

This is effectively a simple inner join on the `productCode` column.

---

## ▶️ Usage

1. Ensure `Missing.csv` and `Scanned.csv` are placed in the `data/` directory.
2. Run the script from the project root:

   ```bash
   python src/main.py
   ```

3. Check the `data/` folder for the newly generated `Matching.csv`.

---

## 📥 Input & Output

- **Input Files:**
  - `data/Missing.csv`: Contains rows with a `productCode` column.
  - `data/Scanned.csv`: Contains rows with a `productCode` column.

- **Output File:**
  - `data/Matching.csv`: Contains rows from `Missing.csv` where `productCode` exists in `Scanned.csv`.

> ⚠️ Ensure both CSV files contain a column named exactly `productCode`.

---

Made with 💻 in Python