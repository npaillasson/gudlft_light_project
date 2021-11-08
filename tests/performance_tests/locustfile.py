from locust import HttpUser, task
from server import app, create_app
import server


class ProjectPerfTest(HttpUser):
    @task
    def display_competition_list_and_points_balance(self):
        self.client.post("/showSummary", {"email": "john@simplylift.co"})

    @task
    def purchase_places_and_update_club_pts_and_competition_number_of_places(self):
        self.client.post(
            "/purchasePlaces",
            {"competition": "Spring Festival", "club": "Simply Lift", "places": "2"},
        )
