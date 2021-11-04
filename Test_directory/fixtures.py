import time
import pytest
from server import PRICE_OF_A_REGISTRATION


@pytest.fixture
def competitions():
    competitions = [
        {
            "name": "Test competition Festival",
            "date": make_competition_date(),
            "numberOfPlaces": "25",
        },
        {
            "name": "Test few slots available",
            "date": make_competition_date(),
            "numberOfPlaces": "5",
        },
        {
            "name": "Test sold out competition",
            "date": make_competition_date(),
            "numberOfPlaces": "0",
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
        {
            "name": "Test Club with enough points to take more than 12 places",
            "email": "test@testclub1.co",
            "points": available_points(can_buy_more_than_12=True),
        },
        {
            "name": "Test Club with enough points to take 5 places",
            "email": "test@testclub2.co",
            "points": available_points(),
        },
        {
            "name": "Test Club without points",
            "email": "test@testclub3.co",
            "points": available_points(zero_point=True),
        },
    ]
    return clubs


def available_points(can_buy_more_than_12=None, zero_point=None):
    if can_buy_more_than_12:
        return PRICE_OF_A_REGISTRATION * 15
    elif zero_point:
        return 0
    else:
        return PRICE_OF_A_REGISTRATION * 5


def make_competition_date(outdated=None):
    actual_time = time.time()
    if outdated:
        competition_date = time.localtime(actual_time - 86400)
        return time.strftime("%Y-%m-%d %H:%M:%S", competition_date)
    competition_date = time.localtime(actual_time + 86400)
    return time.strftime("%Y-%m-%d %H:%M:%S", competition_date)
