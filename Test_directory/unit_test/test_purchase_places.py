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
    competition = competitions[1]
    response = client.post(
        "/purchasePlaces",
        follow_redirects=True,
        data=dict(club=club["name"], competition=competition["name"], places=12),
    )
    response = response.data.decode()
    assert (
        response.find(
            "Error! Impossible to reserve more places than available in the competition"
        )
        != -1
    )


def test_impossible_to_buy_more_places_than_the_club_balance_allows(
    client, clubs, competitions
):
    club = clubs[1]
    competition = competitions[0]
    response = client.post(
        "/purchasePlaces",
        follow_redirects=True,
        data=dict(club=club["name"], competition=competition["name"], places=12),
    )
    response = response.data.decode()
    print(response)
    assert (
        response.find("Oops! you don't have enough points to make this reservation...")
        != -1
    )


def test_impossible_to_buy_more_than_12_places_at_once(client, clubs, competitions):
    club = clubs[0]
    competition = competitions[0]
    response = client.post(
        "/purchasePlaces",
        follow_redirects=True,
        data=dict(club=club["name"], competition=competition["name"], places=13),
    )
    response = response.data.decode()
    assert (
        response.find(
            "Oops! It is impossible to reserve more than 12 places at a time."
        )
        != -1
    )


def test_the_page_returns_an_error_if_the_competition_is_full(
    client, clubs, competitions
):
    club = clubs[0]
    competition = competitions[2]
    response = client.post(
        "/purchasePlaces",
        follow_redirects=True,
        data=dict(club=club["name"], competition=competition["name"], places=12),
    )
    response = response.data.decode()
    assert response.find("Something went wrong-please try again") != -1


def test_the_page_returns_a_404_error_if_the_competition_is_outdated(
    client, clubs, competitions
):
    club = clubs[0]
    competition = competitions[3]
    response = client.post(
        "/purchasePlaces",
        follow_redirects=True,
        data=dict(club=club["name"], competition=competition["name"], places=12),
    )
    response = response.data.decode()
    assert response.find("Something went wrong-please try again") != -1


def test_after_a_successful_reservation_the_number_of_available_places_in_the_competition_is_updated(
    client,
):
    pass


def test_after_a_successful_reservation_the_number_of_points_of_the_club_is_updated(
    client,
):
    pass
