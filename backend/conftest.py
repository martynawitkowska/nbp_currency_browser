from datetime import date, timedelta

import pytest

from currencies.models import CurrencyName, CurrencyDate, CurrencyValue


@pytest.fixture
def currency(db, multiple_currency_names):
    currency_name = CurrencyName.objects.get(code="USD")
    currency_date = CurrencyDate.objects.create(date=date(2023, 5, 23))
    currency_value = CurrencyValue.objects.create(
        exchange_rate=1.5, currency_date=currency_date, currency_name=currency_name
    )

    return currency_date


@pytest.fixture
def currency_2(db, multiple_currency_names):
    currency_name = CurrencyName.objects.get(code="USD")
    currency_date = CurrencyDate.objects.create(date=date(2023, 5, 23) - timedelta(days=2))
    currency_value = CurrencyValue.objects.create(
        exchange_rate=15.34, currency_date=currency_date, currency_name=currency_name
    )

    return currency_date


@pytest.fixture
def currency_date(db):
    return CurrencyDate.objects.create(date=date(2023, 5, 12))


@pytest.fixture
def currency_name(db):
    return CurrencyName.objects.create(name="dolar amerykański", code="USD")


@pytest.fixture
def multiple_currency_names(db):
    currency_names = [
        CurrencyName(name="euro", code="EUR"),
        CurrencyName(name="dolar amerykański", code="USD"),
        CurrencyName(name="frank szwajcarski", code="CHF"),
    ]
    CurrencyName.objects.bulk_create(currency_names)
