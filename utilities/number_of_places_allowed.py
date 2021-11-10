def number_of_places_allowed(club, competition, cost):
    max_competition_places = int(competition["numberOfPlaces"])
    max_places_allowed = int(club["points"]) / cost
    if max_places_allowed > max_competition_places:
        return max_competition_places
    elif max_places_allowed > 12:
        return 12
    return max_places_allowed
