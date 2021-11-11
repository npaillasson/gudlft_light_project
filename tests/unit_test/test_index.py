def test_home_page_returns_code_200(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = client.get("/")
    assert response.status_code == 200


def test_home_page_returns_the_right_template(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the application return the right template
    """
    response = client.get("/")
    response = response.data.decode()
    assert response.find("<title>GUDLFT Registration</title>") != -1
