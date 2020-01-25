import json


def parse_results(matches):
    data = []
    results = json.loads(matches.replace("'", "\""))
    for key, value in results.items():
        d = {"Match": key, "Definition": value}
        data.append(d)
    return data
