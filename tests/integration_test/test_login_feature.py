from flask import url_for


def test_login_with_correct_email(client, clubs, competitions):
    club = clubs[0]
    response = client.get("/")
    response = response.data.decode()
    welcome_page = url_for("show_summary")
    assert response.find(welcome_page) != -1
    response = client.post(welcome_page, data=dict(email=club["email"]))
    response = response.data.decode()
    assert response.find("<title>Summary | GUDLFT Registration</title>") != -1
