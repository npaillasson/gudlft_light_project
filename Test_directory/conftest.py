import pytest
import server
from server import create_app
from Test_directory.fixtures import competitions, clubs


@pytest.fixture
def app(mocker, competitions=competitions, clubs=clubs):
    mocker.patch("server.load_competitions", return_value=competitions)
    mocker.patch("server.load_clubs", return_value=clubs)
    app = create_app({"TESTING": True})
    return app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        with app.app_context():
            yield client
