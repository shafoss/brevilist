import json
import re

data = json.load(open("websters_dictionary.json"))


def get_matches(search_pattern):
    search_pattern = search_pattern
    matches = []
    for key in data.keys():
        if re.search(search_pattern, key.lower()):
            matches.append(key)
    return matches


def do_search(search_text, appear_in_order=True):
    letter_list = [x for x in search_text.lower()]

    if appear_in_order:
        search_pattern = '.*'.join(map(str, letter_list))
    else:
        search_pattern = '(?=.*' + ')(?=.*'.join(map(str, letter_list)) + ')'
    matches = get_matches(search_pattern)

    matches.sort()
    results = {match.capitalize(): data[match] for match in matches}
    return results
