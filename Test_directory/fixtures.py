import time
import pytest


@pytest.fixture
def competitions():
    competitions = [
        {
            "name": "Test competition Festival",
            "date": make_competition_date(),
            "numberOfPlaces": "25",
        },
        {
            "name": "Test sold out competition",
            "date": make_competition_date(),
            "numberOfPlaces": "0",
        },
        {
            "name": "Test few slots available",
            "date": make_competition_date(),
            "numberOfPlaces": "5",
        },
        {
            "name": "Test outdated competition",
            "date": make_competition_date(outdated=True),
            "numberOfPlaces": "10",
        },
    ]

    return competitions


@pytest.fixture
def clubs():
    clubs = [
        {"name": "Test Club_1", "email": "test@testclub1.co", "points": "13"},
        {"name": "Test Club_2", "email": "test@testclub2.co", "points": "20"},
        {"name": "Test Club_3", "email": "test@testclub3.co", "points": "5"},
    ]
    return clubs


def make_competition_date(outdated=None):
    actual_time = time.time()
    if outdated:
        competition_date = time.localtime(actual_time - 86400)
        return time.strftime("%Y-%m-%d %H:%M:%S", competition_date)
    competition_date = time.localtime(actual_time + 86400)
    return time.strftime("%Y-%m-%d %H:%M:%S", competition_date)
