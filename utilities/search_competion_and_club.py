def get_competition(competitions, competition_name):
    return [
        competition
        for competition in competitions
        if competition["name"] == competition_name
    ][0]


def get_club(clubs, club_name):
    return [club for club in clubs if club["name"] == club_name][0]
