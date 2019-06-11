import re


def word_count(phrase):
    words = {}
    for word in re.findall(r"[a-zA-Z0-9']+", phrase):
        word = word.strip('\"\'').lower()
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    return words

