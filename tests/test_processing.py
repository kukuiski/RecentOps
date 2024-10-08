import pytest

from src.processing import count_operations_by_category, filter_by_state, get_transactions, sort_by_date


# Тесты для filter_by_state
@pytest.mark.parametrize(
    "state, expected_output",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("NOT_EXISTING_STATE", []),
    ],
)
def test_filter_by_state(filter_by_state_data, state, expected_output):
    assert filter_by_state(filter_by_state_data[0], state) == expected_output


# Тесты для sort_by_date
@pytest.mark.parametrize(
    "reverse_order, expected_output",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(sort_by_date_data, reverse_order, expected_output):
    assert sort_by_date(sort_by_date_data[0], reverse_order) == expected_output


@pytest.fixture
def transaction_data():
    return [
        {
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": 30368,
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
        {
            "state": "EXECUTED",
            "date": "2022-06-20T18:08:20Z",
            "amount": 16836,
            "currency_name": "Yuan Renminbi",
            "currency_code": "CNY",
            "from": "Visa 2759011965877198",
            "to": "Счет 38287443300766991082",
            "description": "Перевод с карты на карту",
        },
    ]


@pytest.mark.parametrize(
    "pattern, expected_output",
    [
        (
            "Перевод организации",
            [
                {
                    "state": "EXECUTED",
                    "date": "2023-09-05T11:30:32Z",
                    "amount": 16210,
                    "currency_name": "Sol",
                    "currency_code": "PEN",
                    "from": "Счет 58803664561298323391",
                    "to": "Счет 39745660563456619397",
                    "description": "Перевод организации",
                },
            ],
        ),
        (
            "с карты на карту",
            [
                {
                    "state": "CANCELED",
                    "date": "2023-07-22T05:02:01Z",
                    "amount": 30368,
                    "currency_name": "Shilling",
                    "currency_code": "TZS",
                    "from": "Visa 1959232722494097",
                    "to": "Visa 6804119550473710",
                    "description": "Перевод с карты на карту",
                },
                {
                    "state": "EXECUTED",
                    "date": "2022-06-20T18:08:20Z",
                    "amount": 16836,
                    "currency_name": "Yuan Renminbi",
                    "currency_code": "CNY",
                    "from": "Visa 2759011965877198",
                    "to": "Счет 38287443300766991082",
                    "description": "Перевод с карты на карту",
                },
            ],
        ),
        ("не найдено", []),
    ],
)
def test_get_transactions(transaction_data, pattern, expected_output):
    assert get_transactions(transaction_data, pattern) == expected_output


@pytest.mark.parametrize(
    "categories, expected_output",
    [
        (
            ["Перевод организации", "Перевод с карты на карту"],
            {"Перевод организации": 1, "Перевод с карты на карту": 2},
        ),
        (
            ["Открытие вклада"],
            {"Открытие вклада": 0},
        ),
    ],
)
def test_count_operations_by_category(transaction_data, categories, expected_output):
    assert count_operations_by_category(transaction_data, categories) == expected_output
