import requests
import json


def parse_events_from_http(stream):
    req = requests.request("GET", "playing-with-projections.herokuapp.com/stream/{}".format(stream))
    data = req.content.decode("utf-8")

    events = json.loads(data)
    return events


def parse_events_from_file(stream):
    with open("../data/" + stream + ".json") as json_file:
        events = json.load(json_file)

    return events


events = parse_events_from_file("2")
all_types = [e["type"] for e in events]
print(all_types)
