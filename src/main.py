import pandas as pd

file_path = 'C:\\Users\\axelr\\Documents\\python-projects\\cs-trade-tracker\\data\\cs_trades_DB.xlsx'

try:
    df = pd.read_excel(file_path)
    print("file load succesfully")
except FileNotFoundError:
    print(f"Error: File is not in {file_path}")