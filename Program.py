from import_export import Import as ab_import, Export as ab_export
from change_search import add as ab_add, delete as ab_delete, Search as ab_search
from import_export.options import database

def list_data():
    data = ab_import.load()
    print(data.to_string())
    return

commands = {
    "1": list_data,
    "2": ab_search.search,
    "3": ab_add.add,
    "4": ab_delete.delete,
    "5": ab_import.importf,
    "6": ab_export.export_data,
}

def run():
    while True:
        print("Что вы ходите сделать:")
        print("1. Вывести список учеников")
        print("2. Искать ученика")
        print("3. Добавить нового ученика")
        print("4. Удалить ученика")
        print("5. Импортировать список учеников из CSV файла")
        print("6. Экспортировать список учеников в файл (" + ", ".join(ab_export.supported_export) + ")")
        print("q. Выход")
        mode = input()
        if mode in list("123456q"):
            if mode == "q":
                break
            commands[mode]()
    
    return
