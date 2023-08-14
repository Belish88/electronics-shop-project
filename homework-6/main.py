from src.item import Item
from src.setting import CSVTEST, NOTFILE

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv(NOTFILE)
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(CSVTEST)
    # InstantiateCSVError: Файл item.csv поврежден
