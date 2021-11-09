from flask import url_for


def test_move_on_book_page_from_welcome_page(client, clubs, competitions):
    club = clubs[0]
    competition = competitions[0]
    response = client.post("/showSummary", data=dict(email=club["email"]))
    response = response.data.decode()
    book_page = url_for("book", club=club["name"], competition=competition["name"])
    assert response.find(book_page) != -1
    response = client.get(book_page)
    response = response.data.decode()
    assert response.find(f"Booking for {competition['name']} || GUDLFT") != -1


def test_book_place_in_competition_from_book_page(client, clubs, competitions):
    club = clubs[0]
    competition = competitions[0]
    book_page = url_for("book", club=club["name"], competition=competition["name"])
    response = client.get(book_page)
    purchase_place = url_for("purchase_places")
    response = response.data.decode()
    assert response.find(purchase_place) != -1
    assert (
        response.find(f'<input type="hidden" name="club" value="{club["name"]}">') != -1
    )
    assert (
        response.find(
            f'<input type="hidden" name="competition" value="{competition["name"]}">'
        )
        != -1
    )
    response = client.post(
        purchase_place,
        data=dict(club=club["name"], competition=competition["name"], places=12),
    )
    response = response.data.decode()
    assert response.find("Great-booking complete!") != -1
