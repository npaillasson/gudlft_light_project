def test_book_page_return_code_200_with_valid_club_and_competition(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/book/<competition>/<club>' page is requested (GET) with a valid competition and a valid club name
    THEN check that the response is valid
    """
    response = client.get("/book/Test competition Festival/Test Club")
    assert response.status_code == 200


def test_book_page_return_welcome_template_if_club_is_not_valid(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/book/<competition>/<invalid_club>' page is requested (GET) with an invalid club name
    THEN check that the response is valid
    """
    response = client.get("/book/Test competition Festival/This Club doesnt exists")
    response = response.data.decode()
    assert response.find("Something went wrong-please try again") != -1


def test_book_page_return_welcome_template_if_competition_is_not_valid(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/book/<invalid_competition>/<club>' page is requested (GET) with an invalid competition name
    THEN check that the response is valid
    """
    response = client.get("/book/invalid competition/Test Club")
    response = response.data.decode()
    assert response.find("Something went wrong-please try again") != -1
