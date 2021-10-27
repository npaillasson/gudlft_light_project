class TestClass:
    def test_summary_page_return_code_200_if_email_exists(self, client):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/showSummary' page is requested (POST) with a valid email
        THEN check that the response is valid
        """
        response = client.post("/showSummary", data=dict(email="test@testclub.co"))
        assert response.status_code == 200

    def test_summary_page_return_code_400_if_email_doesnt_exists(self, client):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/showSummary' page is requested (POST) with an invalid email
        THEN check that the response is an error 400
        """
        response = client.post(
            "/showSummary", data=dict(email="thisemail@doesntexits.co")
        )
        assert response.status_code == 400
