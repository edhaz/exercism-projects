def recite(start_verse, end_verse):

    for day in range(start_verse - 1, end_verse):
        line = []
        if day + 1 == 1:
            line.append("a Partridge in a Pear Tree")
        else:
            for n in range(day + 1, 0, -1):
                line.append(days[n - 1][1])
        song.append(opening.format(days[day][0], ", ".join(line)))


def build_verse(days):
    verse = "On the {} day of Christmas my true love gave to me: {}."
    return verse


def build_lines():
    days = [
        ("first", "and a Partridge in a Pear Tree"),
        ("second", "two Turtle Doves"),
        ("third", "three French Hens"),
        ("fourth", "four Calling Birds"),
        ("fifth", "five Gold Rings"),
        ("sixth", "six Geese-a-Laying"),
        ("seventh", "seven Swans-a-Swimming"),
        ("eighth", "eight Maids-a-Milking"),
        ("ninth", "nine Ladies Dancing"),
        ("tenth", "ten Lords-a-Leaping"),
        ("eleventh", "eleven Pipers Piping"),
        ("twelfth", "twelve Drummers Drumming")
    ]


def build_song():
    pass