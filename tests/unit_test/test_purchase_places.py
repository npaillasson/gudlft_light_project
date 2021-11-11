import random
from server import PRICE_OF_A_REGISTRATION


def test_it_is_possible_to_reserve_12_places_in_a_competition_that_is_not_full(
    client, clubs, competitions
):
    club = clubs[0]
    competition = competitions[0]
    response = client.post(
        "/purchasePlaces",
        follow_redirects=True,
        data=dict(club=club["name"], competition=competition["name"], places=12),
    )
    response = response.data.decode()
    assert response.find("Great-booking complete!") != -1


def test_impossible_to_reserve_more_places_than_available_in_the_competition(
    client, clubs, competitions
):
    club = clubs[0]
    number_of_points_before_booking = int(club["points"])
    competition = competitions[1]
    number_of_places_before_booking = int(competition["numberOfPlaces"])
    response = client.post(
        "/purchasePlaces",
        follow_redirects=True,
        data=dict(club=club["name"], competition=competition["name"], places=12),
    )
    response = response.data.decode()
    assert response.find("Something went wrong-please try again") != -1
    assert int(club["points"]) == number_of_points_before_booking
    assert int(competition["numberOfPlaces"]) == number_of_places_before_booking


def test_impossible_to_buy_more_places_than_the_club_balance_allows(
    client, clubs, competitions
):
    club = clubs[1]
    number_of_points_before_booking = int(club["points"])
    competition = competitions[0]
    number_of_places_before_booking = int(competition["numberOfPlaces"])
    response = client.post(
        "/purchasePlaces",
        follow_redirects=True,
        data=dict(club=club["name"], competition=competition["name"], places=12),
    )
    response = response.data.decode()
    assert response.find("Something went wrong-please try again") != -1
    assert int(club["points"]) == number_of_points_before_booking
    assert int(competition["numberOfPlaces"]) == number_of_places_before_booking


def test_impossible_to_buy_more_than_12_places_at_once(client, clubs, competitions):
    club = clubs[0]
    number_of_points_before_booking = int(club["points"])
    competition = competitions[0]
    number_of_places_before_booking = int(competition["numberOfPlaces"])
    response = client.post(
        "/purchasePlaces",
        follow_redirects=True,
        data=dict(club=club["name"], competition=competition["name"], places=13),
    )
    response = response.data.decode()
    assert response.find("Something went wrong-please try again") != -1
    assert int(club["points"]) == number_of_points_before_booking
    assert int(competition["numberOfPlaces"]) == number_of_places_before_booking


def test_the_page_returns_an_error_if_the_competition_is_full(
    client, clubs, competitions
):
    club = clubs[0]
    number_of_points_before_booking = int(club["points"])
    competition = competitions[2]
    number_of_places_before_booking = int(competition["numberOfPlaces"])
    response = client.post(
        "/purchasePlaces",
        follow_redirects=True,
        data=dict(club=club["name"], competition=competition["name"], places=12),
    )
    response = response.data.decode()
    assert response.find("Something went wrong-please try again") != -1
    assert int(club["points"]) == number_of_points_before_booking
    assert int(competition["numberOfPlaces"]) == number_of_places_before_booking


def test_the_page_returns_an_error_if_the_competition_is_outdated(
    client, clubs, competitions
):
    club = clubs[0]
    number_of_points_before_booking = int(club["points"])
    competition = competitions[3]
    number_of_places_before_booking = int(competition["numberOfPlaces"])
    response = client.post(
        "/purchasePlaces",
        follow_redirects=True,
        data=dict(club=club["name"], competition=competition["name"], places=12),
    )
    response = response.data.decode()
    assert response.find("Something went wrong-please try again") != -1
    assert int(club["points"]) == number_of_points_before_booking
    assert int(competition["numberOfPlaces"]) == number_of_places_before_booking


def test_the_page_returns_an_error_if_the_club_tries_to_book_less_than_0_place(
    client, clubs, competitions
):
    club = clubs[0]
    number_of_points_before_booking = int(club["points"])
    competition = competitions[1]
    number_of_places_before_booking = int(competition["numberOfPlaces"])
    response = client.post(
        "/purchasePlaces",
        follow_redirects=True,
        data=dict(club=club["name"], competition=competition["name"], places=-1),
    )
    response = response.data.decode()
    assert response.find("Something went wrong-please try again") != -1
    assert int(club["points"]) == number_of_points_before_booking
    assert int(competition["numberOfPlaces"]) == number_of_places_before_booking


def test_after_a_successful_reservation_the_number_of_available_places_in_the_competition_is_updated(
    client, clubs, competitions
):
    number_of_places_required = random.randrange(1, 13)
    club = clubs[0]
    competition = competitions[0]
    number_of_places_before_booking = int(competition["numberOfPlaces"])
    places_after_booking = number_of_places_before_booking - number_of_places_required
    client.post(
        "/purchasePlaces",
        follow_redirects=True,
        data=dict(
            club=club["name"],
            competition=competition["name"],
            places=number_of_places_required,
        ),
    )
    assert int(competition["numberOfPlaces"]) == places_after_booking


def test_after_a_successful_reservation_the_number_of_points_of_the_club_is_updated(
    client, clubs, competitions
):
    number_of_places_required = random.randrange(1, 13)
    club = clubs[0]
    number_of_points_before_booking = int(club["points"])
    points_after_booking = number_of_points_before_booking - (
        number_of_places_required * PRICE_OF_A_REGISTRATION
    )
    competition = competitions[0]
    client.post(
        "/purchasePlaces",
        follow_redirects=True,
        data=dict(
            club=club["name"],
            competition=competition["name"],
            places=number_of_places_required,
        ),
    )
    assert int(club["points"]) == points_after_booking
