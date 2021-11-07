def test_logout(client):
    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200
    response = response.data.decode()
    assert response.find("<title>GUDLFT Registration</title>") != -1
