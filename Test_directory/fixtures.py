import pytest


@pytest.fixture
def competitions():
    competitions = [
        {
            "name": "Test competition Festival",
            "date": "2028-03-27 10:00:00",
            "numberOfPlaces": "25",
        },
        {
            "name": "Test annual competition",
            "date": "2032-03-27 10:00:00",
            "numberOfPlaces": "25",
        },
        {
            "name": "Test outdated competition",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25",
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
