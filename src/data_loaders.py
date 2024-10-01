import csv
import logging
from typing import Any

import pandas as pd

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/data_loaders_logfile.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_data_from_csv(file_path: str) -> Any:
    """Читает из CSV-файла и возвращает транзакции в виде словаря"""
    result = []
    try:
        with open(file_path) as csv_file:
            result = list(csv.DictReader(csv_file))
            if result:
                logger.info(f"Файл {file_path} успешно прочитан")
            else:
                logger.warning(f"Файл {file_path} не содержит данных")
    except (FileNotFoundError, TypeError, ValueError) as e:
        logger.error(f"Ошибка чтения CSV: {e}")
    return result


def read_data_from_excel(file_path: str) -> Any:
    """Читает из Excel-файла и возвращает транзакции в виде словаря"""
    result = []
    try:
        result = pd.read_excel(file_path).to_dict(orient="records")
        if result:
            logger.info(f"Файл {file_path} успешно прочитан")
        else:
            logger.error(f"Файл {file_path} не содержит данных")
    except (FileNotFoundError, TypeError, ValueError) as e:
        logger.error(f"Ошибка чтения Excel: {e}")
    return result
