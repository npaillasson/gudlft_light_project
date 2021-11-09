from flask import url_for


def test_it_is_possible_to_access_to_points_array_from_welcome_page(client, clubs):
    points_array_url = url_for("clubs_array")
    club = clubs[0]
    response = client.post("/showSummary", data=dict(email=club["email"]))
    response = response.data.decode()
    assert response.find(points_array_url) != -1
    response = client.get(points_array_url)
    response = response.data.decode()
    assert response.find("<title>Clubs Array</title>") != -1


def test_it_is_possible_to_access_to_points_array_from_index_page(client):
    points_array_url = url_for("clubs_array")
    response = client.get("/")
    response = response.data.decode()
    assert response.find(points_array_url) != -1
    response = client.get(points_array_url)
    response = response.data.decode()
    assert response.find("<title>Clubs Array</title>") != -1
