import pandas as pd
from import_export import Import as ab_import


def add():
    columns = []
    data = [[]]
    df = ab_import.load()
    for column in df.columns:
        columns.append(column)
        data[0].append(-1 if column == "id" else input(f"Введите поле {column}: "))

    newdf = pd.DataFrame(data, columns=columns)
    ab_import.import_data(newdf)
    print("Добавили запись:")
    print(newdf.to_string(index=False))
    return
