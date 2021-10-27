import pytest
from server import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    print(app.template_context_processors)
    with app.test_client() as client:
        with app.app_context():
            yield client
