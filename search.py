import json
import pandas


data = json.load(open("websters_dictionary.json"))


def find_matches(search_text="", appear_in_order=True, single_word_matches=True):
    # data = json.load(open("websters_dictionary.json"))
    df = pandas.DataFrame(columns=["Match", "Definitions"])
    l = []
    if search_text == "":
        search_text = input("Enter letters: ")
    for letter in search_text:
        l.append(letter)

    matches = []

    for key in data:
        lkey = key.lower()
        count = 0
        if single_word_matches:
            if " " in key:
                continue
        if not appear_in_order:
            for letter in l:
                if letter in lkey:
                    count += 1
                    break
            if count == len(l):
                matches.append(key)
        else:
            place = 0
            for i in range(0, len(l), 1):
                if l[i] in lkey:
                    for k in range(place, len(lkey), 1):
                        if l[i] == lkey[k]:
                            place = k + 1
                            count += 1
                            break
                else:
                    break
            if count == len(l):
                matches.append(key)

    matches.sort()
    for match in matches:
        df = df.append({"Match": match, "Definitions": data[match]}, ignore_index=True)
    # df.to_csv(letters + ".csv")
    print(df)
    print(matches)
    return matches


if __name__ == '__main__':
    order = input("Match in order? (Y,n) ").lower()
    if order[0] == 'n':
        find_matches(appear_in_order=False)
    else:
        find_matches()
