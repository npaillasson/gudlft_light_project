import time


def get_competition(competitions, competition_name, outdated_permitted=True):
    if outdated_permitted:
        return [
            competition
            for competition in competitions
            if competition["name"] == competition_name
        ][0]
    else:
        try:
            return [
                competition
                for competition in competitions
                if competition["name"] == competition_name
                and time.mktime(time.strptime(competition["date"], "%Y-%m-%d %H:%M:%S"))
                > time.time()
            ][0]
        except IndexError:
            return None


def get_not_outdated_competition(competitions):
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
