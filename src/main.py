import pandas as pd

missing_data = pd.read_csv('../data/Missing.csv')
scanned_data = pd.read_csv('../data/Scanned.csv')

matching_rows = missing_data[
    missing_data["productCode"].isin(scanned_data["productCode"])
]

matching_rows.to_csv('../data/Matching.csv', index=False)