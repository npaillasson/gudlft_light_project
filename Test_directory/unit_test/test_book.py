class TestBooKPage:
    def test_book_page_return_code_200_with_valid_club_and_competition(self, client):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/book/<competition>/<club>' page is requested (GET) with a valid competition and a valid club name
        THEN check that the response is valid
        """

        response = client.get("/book/Test competition Festival/Test Club_1")
        assert response.status_code == 200

    def test_book_page_return_welcome_template_if_club_is_not_valid(self, client):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/book/<competition>/<invalid_club>' page is requested (GET) with an invalid club name
        THEN check that the response is valid
        """
        response = client.get("/book/Test competition Festival/This Club doesnt exists")
        response = response.data.decode()
        assert response.find("Something went wrong-please try again") != -1

    def test_book_page_return_welcome_template_if_competition_is_not_valid(
        self, client
    ):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/book/<invalid_competition>/<club>' page is requested (GET) with an invalid competition name
        THEN check that the response is valid
        """
        response = client.get("/book/invalid competition/Test Club 1")
        response = response.data.decode()
        assert response.find("Something went wrong-please try again") != -1

    def test_its_impossible_to_book_if_the_number_of_places_requested_exceeds_the_number_of_places_available(
        self,
        client,
        competitions,
    ):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/book/<invalid_competition>/<club>' page is requested (GET) with an invalid competition name
        THEN check that the response is valid
        """
        response = client.get("/book/Test sold out competition/Test Club 1")
        response = response.data.decode()
        assert response.find("Something went wrong-please try again") != -1
