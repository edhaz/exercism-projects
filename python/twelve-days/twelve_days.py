from functools import lru_cache

lyrics = [
    ("first", "and a Partridge in a Pear Tree."),
    ("second", "two Turtle Doves,"),
    ("third", "three French Hens,"),
    ("fourth", "four Calling Birds,"),
    ("fifth", "five Gold Rings,"),
    ("sixth", "six Geese-a-Laying,"),
    ("seventh", "seven Swans-a-Swimming,"),
    ("eighth", "eight Maids-a-Milking,"),
    ("ninth", "nine Ladies Dancing,"),
    ("tenth", "ten Lords-a-Leaping,"),
    ("eleventh", "eleven Pipers Piping,"),
    ("twelfth", "twelve Drummers Drumming,")
]


def recite(start_verse, end_verse):
    return [build_line(day) for day in range(start_verse, end_verse + 1)]


@lru_cache(maxsize=12)
def build_line(day):
    nth = lyrics[day - 1][0]
    first_line = f"On the {nth} day of Christmas my true love gave to me:"
    gift_line = "a Partridge in a Pear Tree." if day == 1 else build_verse(day)
    return f"{first_line} {gift_line}"


def build_verse(day):
    return " ".join([lyrics[num][1] for num in reversed(range(day))])
