from flask import url_for


def test_it_is_possible_to_access_to_points_array_from_welcome_page(client, clubs):
    logout_url = url_for("logout")
    club = clubs[0]
    response = client.post("/showSummary", data=dict(email=club["email"]))
    response = response.data.decode()
    assert response.find(logout_url) != -1
    response = client.get(logout_url, follow_redirects=True)
    assert response.status_code == 200
    response = response.data.decode()
    assert response.find("<title>GUDLFT Registration</title>") != -1
