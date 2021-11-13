from flask import Flask, render_template, request, redirect, flash, url_for
from utilities.get_user import load_competitions, load_clubs
from utilities.search_competion_and_club import (
    get_club,
    get_competition,
    get_not_outdated_competitions,
)
from utilities.number_of_places_allowed import number_of_places_allowed

PRICE_OF_A_REGISTRATION = 1


def create_app(config):
    app = Flask(__name__)
    app.secret_key = "something_special"
    app.config["TESTING"] = config.get("TESTING")

    clubs = load_clubs()
    competitions = load_competitions()

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/showSummary", methods=["POST"])
    def show_summary():
        try:
            club = [club for club in clubs if club["email"] == request.form["email"]][0]
        except IndexError:
            flash("Oops, This emails seems unknown...")
            return render_template("index.html")
        return render_template(
            "welcome.html",
            club=club,
            competitions=get_not_outdated_competitions(competitions),
        )

    @app.route("/book/<competition>/<club>")
    def book(competition, club):
        found_club = get_club(clubs, club)
        found_competition = get_competition(competitions, competition)
        if found_club and found_competition:

            return render_template(
                "booking.html",
                club=found_club,
                competition=found_competition,
                max_places_allowed=number_of_places_allowed(
                    found_club, found_competition, PRICE_OF_A_REGISTRATION
                ),
            )
        else:
            flash("Something went wrong-please try again")
            return render_template(
                "welcome.html",
                club=club,
                competitions=get_not_outdated_competitions(competitions),
            )

    @app.route("/purchasePlaces", methods=["POST"])
    def purchase_places():
        competition = get_competition(competitions, request.form["competition"])
        club = get_club(clubs, request.form["club"])
        if competition and club:
            places_required = int(request.form["places"])
            cost_in_points = places_required * PRICE_OF_A_REGISTRATION
            if (
                0
                <= places_required
                <= number_of_places_allowed(club, competition, PRICE_OF_A_REGISTRATION)
            ):
                competition["numberOfPlaces"] = (
                    int(competition["numberOfPlaces"]) - places_required
                )
                club["points"] = str(int(club["points"]) - cost_in_points)
                flash("Great-booking complete!")
                return render_template(
                    "welcome.html",
                    club=club,
                    competitions=get_not_outdated_competitions(competitions),
                )
        flash("Something went wrong-please try again")
        return render_template("welcome.html", club=club, competitions=competitions)

    @app.route("/clubsArray")
    def clubs_array():
        return render_template(
            "clubs_array.html",
            clubs=clubs,
            competitions=get_not_outdated_competitions(competitions),
        )

    @app.route("/logout")
    def logout():
        return redirect(url_for("index"))

    return app


app = create_app({"TESTING": False})


if __name__ == "__main__":
    app.run()
