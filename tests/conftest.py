import pytest


@pytest.fixture
def valid_card_numbers():
    return [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456")
    ]


@pytest.fixture
def invalid_card_numbers():
    return [
        "123456789012",  # Меньше 16 символов
        "12345678901234567890",  # Больше 16 символов
        "1234-5678-9012-3456",  # Содержит символы, отличные от цифр
        ""
    ]


@pytest.fixture
def valid_account_numbers():
    return [
        ("73654108430135874305", "**4305"),
        ("12345678901234562439", "**2439")
    ]


@pytest.fixture
def invalid_account_numbers():
    return [
        "1234567890123456243",  # Меньше 20 символов
        "123456789012345624391",  # Больше 20 символов
        "#12345678901234562439",  # Содержит символы, отличные от цифр
        ""
    ]


@pytest.fixture
def filter_by_state_data():
    return [
        # Входные данные для тестов filter_by_state
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ]
    ]


@pytest.fixture
def sort_by_date_data():
    return [
        # Входные данные для тестов sort_by_date
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ]
    ]


@pytest.fixture
def filter_by_state_cases():
    return [
        # Кейсы для тестов filter_by_state
        (
            "EXECUTED",
            [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
            ]
        ),
        (
            "CANCELED",
            [
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
            ]
        ),
        (
            "NOT_EXISTING_STATE",
            []
        )
    ]


@pytest.fixture
def sort_by_date_cases():
    return [
        # Кейсы для тестов sort_by_date
        (
            True,
            [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
            ]
        ),
        (
            False,
            [
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
            ]
        )
    ]
