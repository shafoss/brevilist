import re


def get_unique_words(data_dict):
    words = set()
    for value in data_dict.values():
        split_values = re.split('\W+', value)
        for val in split_values:
            words.add(val.lower())
    return words


def count_words(data_dict):
    counter = Counter()
    for value in data_dict.values():
        counter.update(re.split('\W+', value.lower()))
    return counter
