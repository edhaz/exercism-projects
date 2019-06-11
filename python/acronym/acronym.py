import re

def abbreviate(words):
    split_words = re.findall(r"[a-zA-Z']+|[.,!?;]", words)
    return ''.join(word[0] for word in split_words if word[0].isalpha()).upper()