from unittest.mock import patch

from src.menu import ask_user_format, ask_user_state, ask_two_options, ask_word


# Тесты для функции ask_user_format
@patch('builtins.input', side_effect=['1'])
def test_ask_user_format_option_1(_):
    assert ask_user_format() == '1'


@patch('builtins.input', side_effect=['4', '2'])
def test_ask_user_format_invalid_then_valid(_):
    assert ask_user_format() == '2'


# Тесты для функции ask_user_state
@patch('builtins.input', side_effect=['SUCCESS'])
def test_ask_user_state_valid(_):
    assert ask_user_state(['SUCCESS', 'FAILED']) == 'SUCCESS'


@patch('builtins.input', side_effect=['UNKNOWN', 'FAILED'])
def test_ask_user_state_invalid_then_valid(_):
    assert ask_user_state(['SUCCESS', 'FAILED']) == 'FAILED'


# Тесты для функции ask_two_options
@patch('builtins.input', side_effect=['Да'])
def test_ask_two_options_yes(_):
    assert ask_two_options() is True


@patch('builtins.input', side_effect=['Нет'])
def test_ask_two_options_no(_):
    assert ask_two_options() is False


# Тесты для функции ask_word
@patch('builtins.input', side_effect=['слово'])
def test_ask_word_valid(_):
    assert ask_word() == 'слово'


@patch('builtins.input', side_effect=['', 'слово'])
def test_ask_word_empty_then_valid(_):
    assert ask_word() == 'слово'
