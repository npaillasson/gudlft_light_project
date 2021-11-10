def number_of_places_allowed(club, cost):
    max_places_allowed = int(club["points"]) / cost
    if max_places_allowed > 12:
        return 12
    return max_places_allowed
