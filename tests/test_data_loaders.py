from unittest.mock import mock_open, patch

from src.data_loaders import read_data_from_csv, read_data_from_excel


# Тест успешного чтения данных из CSV с Mock
@patch("src.data_loaders.open", new_callable=mock_open, read_data="id;state;amount\n1;EXECUTED;1000\n2;CANCELED;2000")
@patch("src.data_loaders.csv.DictReader")
def test_read_data_from_csv_success(mock_csv_reader, mock_open):
    # Замокируем результат csv.DictReader
    mock_csv_reader.return_value = [
        {"id": "1", "state": "EXECUTED", "amount": "1000"},
        {"id": "2", "state": "CANCELED", "amount": "2000"},
    ]

    # Вызов функции
    result = read_data_from_csv("fake_path.csv")

    # Проверка результата
    assert len(result) > 0  # Проверка, что данные не пустые
    assert isinstance(result, list)  # Проверка, что результат — это список
    assert isinstance(result[0], dict)  # Проверка, что каждая строка — это словарь


# Тест успешного чтения данных из Excel с Mock
@patch("src.data_loaders.pd.read_excel")
def test_read_data_from_excel_success(mock_read_excel):
    # Замокируем результат pd.read_excel
    mock_read_excel.return_value.to_dict.return_value = [
        {"id": 1, "state": "EXECUTED", "amount": 1000},
        {"id": 2, "state": "CANCELED", "amount": 2000},
    ]

    # Вызов функции
    result = read_data_from_excel("fake_path.xlsx")

    # Проверка результата
    assert len(result) > 0  # Проверка, что данные не пустые
    assert isinstance(result, list)  # Проверка, что результат — это список
    assert isinstance(result[0], dict)  # Проверка, что каждая строка — это словарь
