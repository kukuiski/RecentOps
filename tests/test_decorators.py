import pytest
from src.decorators import log


# Тестирование логирования успешного выполнения функции
def test_log_success_file(tmp_path):
    # Создаем временный файл для логов
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def test_func(x, y):
        return x + y

    result = test_func(2, 3)

    # Проверяем результат функции
    assert result == 5

    # Проверяем содержимое файла
    with open(log_file, 'r') as f:
        log_content = f.read()

    assert log_content == "test_func ok\n"


# Тестирование логирования исключений в файл
def test_log_exception_file(tmp_path):
    # Создаем временный файл для логов
    log_file = tmp_path / "log.txt"

    @log(filename=str(log_file))
    def test_func(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        test_func(2, 0)

    # Проверяем содержимое файла
    with open(log_file, 'r') as f:
        log_content = f.read()

    assert "test_func error" in log_content
    assert "Inputs: (2, 0), {}" in log_content


# Тестирование логирования в консоль (без файла)
def test_log_success_console(capsys):
    @log()
    def test_func(x, y):
        return x + y

    result = test_func(2, 3)

    # Проверяем результат функции
    assert result == 5

    # Перехватываем вывод в консоль
    captured = capsys.readouterr()

    assert captured.out == "test_func ok\n"


# Тестирование логирования исключений в консоль
def test_log_exception_console(capsys):
    @log()
    def test_func(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        test_func(2, 0)

    # Перехватываем вывод в консоль
    captured = capsys.readouterr()

    assert "test_func error" in captured.out
    assert "Inputs: (2, 0), {}" in captured.out
