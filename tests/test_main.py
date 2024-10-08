import unittest
from unittest.mock import patch

import pandas as pd

from src.main import main


class TestMainFunction(unittest.TestCase):

    @patch("src.main.read_data_from_csv")
    @patch("src.main.read_data_from_excel")
    @patch("src.main.read_normalized_json")
    @patch("src.main.ask_user_format")
    @patch("src.main.ask_user_state")
    @patch("src.main.ask_two_options")
    @patch("src.main.ask_word")
    @patch("src.main.print_operations")
    def test_main_json_format(
        self,
        mock_print_operations,
        mock_ask_word,
        mock_ask_two_options,
        mock_ask_user_state,
        mock_ask_user_format,
        mock_read_normalized_json,
        mock_read_data_from_excel,
        mock_read_data_from_csv,
    ):
        # Мокаем ввод пользователя, чтобы выбрать формат JSON
        mock_ask_user_format.return_value = "1"
        mock_ask_user_state.return_value = "COMPLETED"
        mock_ask_two_options.side_effect = [
            True,  # Сортировка
            True,  # Фильтрация по RUB
            False,  # Фильтрация по слову
            False  # Добавляем еще один элемент, чтобы избежать StopIteration
        ]   # Без сортировки, без фильтрации по RUB, без фильтра по слову
        mock_ask_word.return_value = "тест"

        # Мокаем функцию read_normalized_json, чтобы вернуть DataFrame
        mock_df = pd.DataFrame(
            {
                "state": ["COMPLETED", "PENDING"],
                "date": ["2021-01-01", "2021-01-02"],
                "currency_code": ["RUB", "USD"],
                "description": ["покупка", "тест"],
            }
        )
        mock_read_normalized_json.return_value = mock_df

        # Запускаем основную функцию
        main()

        # Проверяем, что был выбран и прочитан JSON-файл
        mock_read_normalized_json.assert_called_once()

        # Проверяем, что операции были напечатаны
        mock_print_operations.assert_called_once()

    @patch("src.main.read_data_from_csv")
    @patch("src.main.ask_user_format")
    @patch("src.main.ask_user_state")
    @patch("src.main.ask_two_options")
    @patch("src.main.print_operations")
    def test_main_csv_format(
        self,
        mock_print_operations,
        mock_ask_two_options,
        mock_ask_user_state,
        mock_ask_user_format,
        mock_read_data_from_csv,
    ):
        # Мокаем ввод пользователя, чтобы выбрать формат CSV
        mock_ask_user_format.return_value = "2"
        mock_ask_user_state.return_value = "COMPLETED"
        mock_ask_two_options.side_effect = [
            True,  # Сортировка по дате
            True,  # Фильтрация по RUB
            False,  # Фильтрация по слову
            False  # Отфильтровать транзакции по слову в описании
        ]        # Сортировка, фильтрация по RUB, без фильтрации по слову

        # Мокаем функцию read_data_from_csv, чтобы вернуть список словарей (формат CSV)
        mock_read_data_from_csv.return_value = [
            {"state": "COMPLETED", "date": "2021-01-01", "currency_code": "RUB", "description": "покупка"},
            {"state": "PENDING", "date": "2021-01-02", "currency_code": "USD", "description": "тест"},
        ]

        # Запускаем основную функцию
        main()

        # Проверяем, что был выбран и прочитан CSV-файл
        mock_read_data_from_csv.assert_called_once()

        # Проверяем, что операции были напечатаны
        mock_print_operations.assert_called_once()

    @patch("src.main.ask_word")
    @patch("src.main.read_data_from_excel")
    @patch("src.main.ask_user_format")
    @patch("src.main.ask_user_state")
    @patch("src.main.ask_two_options")
    @patch("src.main.print_operations")
    def test_main_excel_format(
            self,
            mock_print_operations,
            mock_ask_two_options,
            mock_ask_user_state,
            mock_ask_user_format,
            mock_read_data_from_excel,
            mock_ask_word
    ):
        # Мокаем ввод пользователя, чтобы выбрать формат Excel
        mock_ask_user_format.return_value = "3"
        mock_ask_user_state.return_value = "PENDING"
        mock_ask_two_options.side_effect = [
            False,  # Без сортировки
            False,  # Без фильтрации по RUB
            True  # С фильтрацией по слову
        ]

        # Мокаем функцию ask_word, чтобы не использовать input
        mock_ask_word.return_value = "тест"

        # Мокаем функцию read_data_from_excel, чтобы вернуть DataFrame
        mock_df = pd.DataFrame({
            "state": ["COMPLETED", "PENDING"],
            "date": ["2021-01-01", "2021-01-02"],
            "currency_code": ["RUB", "USD"],
            "description": ["покупка", "тест"]
        })
        mock_read_data_from_excel.return_value = mock_df

        # Запускаем основную функцию
        main()

        # Проверяем, что Excel файл был прочитан и данные обработаны
        mock_read_data_from_excel.assert_called_once()
        mock_print_operations.assert_called_once()


if __name__ == "__main__":
    unittest.main()
