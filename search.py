import json
# import pandas

data = json.load(open("websters_dictionary.json"))


def find_matches(search_text="", appear_in_order=True, single_word_matches=True):
    if not search_text:
        search_text = input("Enter letters: ")
    letter_list = [x for x in search_text]

    matches = []

    for key in data:
        lowercase_key = key.lower()
        count = 0
        if single_word_matches:
            if " " in key:
                continue
        if not appear_in_order:
            for letter in letter_list:
                if letter in lowercase_key:
                    count += 1
                    break
            if count == len(letter_list):
                matches.append(key)
        else:
            place = 0
            for i in range(0, len(letter_list), 1):
                if letter_list[i] in lowercase_key:
                    for k in range(place, len(lowercase_key), 1):
                        if letter_list[i] == lowercase_key[k]:
                            place = k + 1
                            count += 1
                            break
                else:
                    break
            if count == len(letter_list):
                matches.append(key)

    matches.sort()
    return matches


# def results_to_csv(text, matches):
#     df = pandas.DataFrame(columns=["Match", "Definitions"])
#     for match in matches:
#         df = df.append({"Match": match, "Definitions": data[match]}, ignore_index=True)
#     df.to_csv(filename)


if __name__ == '__main__':
    order = input("Match in order? (y,n) ").lower()
    if order[0] == 'n':
        find_matches(appear_in_order=False)
    else:
        find_matches()
