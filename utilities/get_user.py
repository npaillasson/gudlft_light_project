import json


def load_clubs(json_file="clubs.json"):
    with open(json_file) as c:
        list_of_clubs = json.load(c)["clubs"]
        return list_of_clubs


def load_competitions(json_file="competitions.json"):
    with open(json_file) as comps:
        list_of_competitions = json.load(comps)["competitions"]
        return list_of_competitions
