class TestClubsArray:
    def test_get_clubs_array_return_200_with_valid_clubs(self, client):
        response = client.get("/clubsArray")
        assert response.status_code == 200

    def test_clubs_array_contains_the_correct_number_of_clubs(self, client, clubs):
        response = client.get("/clubsArray")
        response = response.data.decode()
        numbers_of_clubs_in_base = len(clubs)
        numbers_of_li_in_array = response.count("</li>")
        assert numbers_of_li_in_array == numbers_of_clubs_in_base

    def test_clubs_array_display_the_correct_information(self, client, clubs):
        response = client.get("/clubsArray")
        response = response.data.decode()
        for club in clubs:
            assert (
                response.find(f"{club['name']}<br>Number of points: {club['points']}")
                != -1
            )

    def test_clubs_array_return_the_correct_template(self, client):
        response = client.get("/clubsArray")
        response = response.data.decode()
        assert response.find("<title>Clubs Array</title>") != -1
