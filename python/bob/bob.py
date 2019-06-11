def hey(phrase):
    phrase = phrase.strip()
    if not phrase:
        return 'Fine. Be that way!'
    elif phrase.isupper():
        if phrase[-1] == '?':
            return "Calm down, I know what I'm doing!"
        return 'Whoa, chill out!'
    elif phrase[-1] == '?':
        return 'Sure.'
    return 'Whatever.'
