import time


def get_competition(competitions, competition_name):
    try:
        return [
            competition
            for competition in competitions
            if competition["name"] == competition_name
            and time.mktime(time.strptime(competition["date"], "%Y-%m-%d %H:%M:%S"))
            > time.time()
            and int(competition["numberOfPlaces"]) > 0
        ][0]
    except IndexError:
        return None


def get_not_outdated_competitions(competitions):
    try:
        return [
            competition
            for competition in competitions
            if time.mktime(time.strptime(competition["date"], "%Y-%m-%d %H:%M:%S"))
            > time.time()
        ]
    except IndexError:
        return None


def get_club(clubs, club_name):
    try:
        return [club for club in clubs if club["name"] == club_name][0]
    except IndexError:
        return None
