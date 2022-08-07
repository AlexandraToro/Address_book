import os
import pandas as pd
from import_export.options import database
from import_export import Export as ab_export

#добавляет в текущий файл новые данные
#ab_import.import_file("fio_import.csv")

# загрузка данных
# читаем CSV файл, возвращаем DataFrame
# нет обработки ошибок
def load_data(filename):
    return pd.read_csv(filename, sep=";")

# импорт
# 1) зачитываем текущую базу
# 2) добавляем новые данные (вопрос: нужна проверка на дубликаты?)
# 3) при добавлении создаем новый уникальный id
# 4) сохраняем в текущую базу 
def import_file(filename):
    db = load_data(database)
    imported = load_data(filename)
    max_id = db["id"].max() + 1
    imported['id'] = range(max_id, max_id+len(imported))
    result = pd.concat([db, imported])
    ab_export.save_data(database, "csv", result)
    return imported

def import_data():
    filename = ""
    while len(filename) == 0:
        filename = input("Введите имя CSV Файла для импорта:")
        if not os.path.exists(filename):
            print(f"Файл {filename} не существует!")
            filename = ""
        else:
            df = import_file(filename)
            print("%d учеников импортировано" % len(df))

    return