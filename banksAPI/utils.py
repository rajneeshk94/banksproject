import csv
import requests


def get_csv_data():
    url = "https://raw.githubusercontent.com/Amanskywalker/indian_banks/main/bank_branches.csv"
    data = requests.get(url).content.decode('utf-8').splitlines()
    reader = csv.DictReader(data)
    return list(reader)
    