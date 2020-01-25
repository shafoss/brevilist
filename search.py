import json
import re
from collections import Counter

data = json.load(open("websters_dictionary.json"))


def get_matches(search_pattern):
    search_pattern = search_pattern
    matches = []
    for key in data.keys():
        if re.search(search_pattern, key.lower()):
            matches.append(key)
    return matches


def get_ordered_search_pattern(letter_list):
    search_pattern = '.*'.join(map(str, letter_list))
    return search_pattern


def get_unordered_search_pattern(letter_list):
    letter_set = set(letter_list)
    counter = Counter(letter_list)
    for letter in counter:
        if counter[letter] > 1:
            repeated_letter = '.*'.join(letter * counter[letter])
            letter_set.remove(letter)
            letter_set.add(repeated_letter)
    search_pattern = '(?=.*' + ')(?=.*'.join(map(str, letter_set)) + ')'
    return search_pattern


def do_search(search_text, appear_in_order=True):
    letter_list = [x for x in search_text.lower()]

    if appear_in_order:
        search_pattern = get_ordered_search_pattern(letter_list)
    else:
        search_pattern = get_unordered_search_pattern(letter_list)

    matches = get_matches(search_pattern)
    matches.sort()
    results = {match.capitalize(): data[match] for match in matches}
    return results
