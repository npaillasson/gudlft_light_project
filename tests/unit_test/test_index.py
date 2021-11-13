def test_home_page_returns_code_200(client):

    response = client.get("/")
    assert response.status_code == 200


def test_home_page_returns_the_right_template(client):

    response = client.get("/")
    response = response.data.decode()
    assert response.find("<title>GUDLFT Registration</title>") != -1
