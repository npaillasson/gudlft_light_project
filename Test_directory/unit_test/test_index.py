def test_home_page_with_fixture(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = client.get('/')
    print(response.data)
    assert response.status_code == 200