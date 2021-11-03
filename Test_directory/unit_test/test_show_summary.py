import time


class TestClass:
    def test_summary_page_return_code_200_if_email_exists(self, client):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/showSummary' page is requested (POST) with a valid email
        THEN check that the response is valid
        """
        response = client.post("/showSummary", data=dict(email="test@testclub1.co"))
        assert response.status_code == 200

    def test_summary_page_return_the_right_template(self, client):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/' page is requested (GET)
        THEN check that the application return the right template
        """
        response = client.post("/showSummary", data=dict(email="test@testclub1.co"))
        response = response.data.decode()
        assert response.find("<title>Summary | GUDLFT Registration</title>") != -1

    def test_summary_page_return_the_index_page_code_200_and_error_mes_if_email_doesnt_exists(
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

    def test_summary_page_display_the_right_club_email(self, client):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/' page is requested (GET)
        THEN check that the application return the right template
        """
        response = client.post("/showSummary", data=dict(email="test@testclub1.co"))
        response = response.data.decode()

        assert response.find("<h2>Welcome, test@testclub1.co </h2>") != -1

    def test_summary_page_display_the_right_club_points_amount(self, client, clubs):
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
        numbers_of_clubs_in_base = 2
        numbers_of_li_in_array = response.count("<li class='competition'>")
        assert numbers_of_li_in_array == numbers_of_clubs_in_base

    def test_the_page_displays_the_right_competitions(self, client, competitions):
        response = client.post("/showSummary", data=dict(email="test@testclub1.co"))
        response = response.data.decode()
        for competition in competitions:
            competition_timestamp = time.mktime(
                time.strptime(competition["date"], "%Y-%m-%d %H:%M:%S")
            )
            if competition_timestamp < time.time():
                assert response.find(competition["name"]) == -1
            else:
                assert response.find(competition["name"]) != -1

    def test_the_booking_buttons_appears_only_if_the_competition_is_not_sold_out(
        self, client, competitions, clubs
    ):
        club = clubs[0]
        response = client.post("/showSummary", data=dict(email=club["email"]))
        response = response.data.decode()
        print(response)
        for competition in competitions:
            information = response.find(
                f"<a href=\"/book/{competition['name'].replace(' ', '%20')}/{club['name'].replace(' ', '%20')}\">"
            )
            print(
                f"<a href=\"/book/{competition['name'].replace(' ', '%20')}/{club['name'].replace(' ', '%20')}\">"
            )
            if int(competition["numberOfPlaces"]) <= 0:
                print("in if", information)
                assert information == -1
            else:
                print("out if", information)
                assert information != -1
