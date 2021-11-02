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
