from pathlib import Path
from typing import Optional

import pandas as pd

from src.data_loaders import read_data_from_csv, read_data_from_excel, read_normalized_json
from src.menu import ask_two_options, ask_user_format, ask_user_state, ask_word
from src.processing import get_transactions, print_operations

# Получение абсолютного пути к директории проекта
project_root = Path(__file__).resolve().parent.parent

JSON_PATH = str(project_root / "data" / "operations.json")
CSV_PATH = str(project_root / "data" / "transactions.csv")
XLSX_PATH = str(project_root / "data" / "transactions_excel.xlsx")


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Выбираем откуда читать данные и считываем данные в DataFrame
    answer = ask_user_format()
    df: Optional[pd.DataFrame] = None
    if answer == "1":
        print("Для обработки выбран JSON-файл.")
        # Здесь читаются и нормализуются JSON-данные
        # Столбцы приводятся в тот же вид, в котором они находятся в CSV и XLSX
        df = read_normalized_json(JSON_PATH)
    elif answer == "2":
        print("Для обработки выбран CSV-файл.")
        df = pd.DataFrame(read_data_from_csv(CSV_PATH))
    else:
        print("Для обработки выбран XLSX-файл.")
        df = pd.DataFrame(read_data_from_excel(XLSX_PATH))

    print()

    # Проверяем если вдруг фрейм окажется пустой
    if df is not None:
        # Считываем все уникальные значения статусов операций и исключаем пустые и невалидные строки
        states = [state.upper() for state in df['state'].dropna().unique() if
                  isinstance(state, str) and state.strip() != ""]
        answer = ask_user_state(states)

        # Здесь добавляем .copy() для предотвращения предупреждения
        df = df.loc[df["state"].str.upper() == answer].copy()
        print(f"Операции отфильтрованы по статусу \"{answer}\"")
        print()

        # Спрашиваем, нужна ли сортировка по дате
        if ask_two_options("Отсортировать операции по дате?"):
            df.sort_values(by="date", inplace=True,
                           ascending=ask_two_options("Отсортировать по возрастанию или по убыванию?",
                                                     "По возрастанию",
                                                     "По убыванию"))

        # Спрашиваем, выводить ли только рублёвые транзакции
        if ask_two_options("Выводить только рублевые транзакции?"):
            df = df.loc[df["currency_code"] == "RUB"]

        # Фильтровать ли по слову в описании?
        if ask_two_options("Отфильтровать список транзакций по определенному слову в описании?"):
            df = pd.DataFrame(get_transactions(df.to_dict(orient="records"), ask_word("Введите слово: ")))

        print("Распечатываю итоговый список транзакций...")
        print_operations(df)
    else:
        print("На удивление, данных не обнаружено")

    return None


if __name__ == "__main__":
    main()
