from locust import HttpUser, task
from server import create_app


class ProjectPerfTest(HttpUser):
    def on_start(self):
        app = create_app({"TESTING": True})
        app.run()

    @task
    def display_competition_list_and_points_balance(self):
        self.client.post("/showSummary", {"email": "john@simplylift.co"})

    @task
    def update_points(self):
        pass
