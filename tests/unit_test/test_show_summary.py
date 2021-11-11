import time


class TestClass:
    def test_summary_page_returns_code_200_if_email_exists(self, client):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/showSummary' page is requested (POST) with a valid email
        THEN check that the response is valid
        """
        response = client.post("/showSummary", data=dict(email="test@testclub1.co"))
        assert response.status_code == 200

    def test_summary_page_returns_the_right_template(self, client):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/' page is requested (GET)
        THEN check that the application return the right template
        """
        response = client.post("/showSummary", data=dict(email="test@testclub1.co"))
        response = response.data.decode()
        assert response.find("<title>Summary | GUDLFT Registration</title>") != -1

    def test_summary_page_returns_the_index_page_code_200_and_error_message_if_email_doesnt_exist(
        self, client
    ):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/showSummary' page is requested (POST) with an invalid email
        THEN check that the response is an error 400
        """
        response = client.post(
            "/showSummary", data=dict(email="thisemail@doesntexits.co")
        )
        assert response.status_code == 200
        assert response.data.decode().find("Oops, This emails seems unknown...") != -1

    def test_summary_page_displays_the_right_club_email(self, client):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/' page is requested (GET)
        THEN check that the application return the right template
        """
        response = client.post("/showSummary", data=dict(email="test@testclub1.co"))
        response = response.data.decode()

        assert response.find("<h2>Welcome, test@testclub1.co </h2>") != -1

    def test_summary_page_displays_the_right_club_points_amount(self, client, clubs):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/' page is requested (GET)
        THEN check that the application return the right template
        """
        response = client.post("/showSummary", data=dict(email="test@testclub1.co"))
        response = response.data.decode()
        assert response.find(f"Points available: {clubs[0]['points']}") != -1

    def test_the_page_displays_the_right_number_of_competitions(
        self, client, competitions
    ):
        response = client.post("/showSummary", data=dict(email="test@testclub1.co"))
        response = response.data.decode()
        print(response)
        numbers_of_competition = 3
        numbers_of_li_in_array = response.count('<li class="competition">')
        assert numbers_of_li_in_array == numbers_of_competition

    def test_the_page_displays_the_right_competitions(self, client, competitions):
        response = client.post("/showSummary", data=dict(email="test@testclub1.co"))
        response = response.data.decode()
        for competition in competitions:
            competition_timestamp = time.mktime(
                time.strptime(competition["date"], "%Y-%m-%d %H:%M:%S")
            )
            if competition_timestamp > time.time():
                assert response.find(competition["name"]) != -1
            else:
                assert response.find(competition["name"]) == -1

    def test_the_booking_button_appears_only_if_the_competition_is_not_sold_out(
        self, client, competitions, clubs
    ):
        print(clubs)
        club = clubs[0]
        response = client.post("/showSummary", data=dict(email=club["email"]))
        response = response.data.decode()
        for competition in competitions:
            information = response.find(
                f"<a href=\"/book/{competition['name'].replace(' ', '%20')}/{club['name'].replace(' ', '%20')}\">"
            )
            if int(competition["numberOfPlaces"]) <= 0:
                assert information == -1
            else:
                assert information != -1
