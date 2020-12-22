#!/usr/bin/env python3

import time
from collections import deque, defaultdict
from scipy.optimize import curve_fit
import random
import math

graph = {
    'b': {'r', 'l', 't', 'y', 'o'},
    'r': {'b', 'l', 'e', 'c', 'o'},
    'l': {'b', 'r', 't', 'e', 'o'},
    't': {'y', 'b', 'l', 'n', 'o'},
    'y': {'b', 't', 'n', 's', 'o'},
    'e': {'r', 'c', 'g', 'l', 'o'},
    'o': {'b', 'r', 'l', 't', 'y', 'e', 'n', 'c', 'g', 'w', 's', 'h'},
    'n': {'s', 'w', 'y', 't', 'o'},
    'c': {'r', 'e', 'g', 'h', 'o'},
    'g': {'h', 'w', 'e', 'c', 'o'},
    'w': {'s', 'n', 'g', 'h', 'o'},
    's': {'y', 'n', 'w', 'h', 'o'},
    'h': {'s', 'w', 'g', 'c', 'o'}
}


def find_words(graph, max_length=5):
    Q = deque(graph)
    while Q:
        path = Q.pop()
        yield path
        if len(path) < max_length:
            for w in graph[path[-1]]:
                Q.append(path + w)


def is_word_in_graph(word):
    return word in find_words(graph, max_length=len(word))


def fit_exponential(x, y):
    def func(x, a, b, c):
        return a * (b ** x) + c

    coefficients, _ = curve_fit(func, x, y, p0=[0.0000007, 6, 0.001])
    return lambda x: func(x, *coefficients)


def read_words(path):
    with open(path) as file:
        return (line.strip().lower() for line in file.readlines())


SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 60 * SECONDS_PER_MINUTE
SECONDS_PER_DAY = 24 * SECONDS_PER_HOUR
SECONDS_PER_TROPICAL_YEAR = 365 * SECONDS_PER_DAY + 5 * SECONDS_PER_HOUR + 48 * SECONDS_PER_MINUTE + 45.216

TIME_UNITS = (
    ("planck time units", 5.39e-44),
    ("new york seconds", 5.39e-44),
    ("yoctoseconds", 1e-24),
    ("zeptoseconds", 1e-21),
    ("attoseconds", 1e-18),
    ("femtoseconds", 1e-15),
    ("picoseconds", 1e-12),
    ("light-inches", 8.4725e-11),
    ("nanoseconds", 1e-9),
    ("light-feet", 1.0167e-9),
    ("light-yards", 3.0501e-9),
    ("shakes", 1e-9),
    ("light-miles", 5.3682e-6),
    ("microseconds", 1e-6),
    ("nautical light-miles", 6.177586613723e-6),
    ("milliseconds", 1e-3),
    ("fourths", 1 / 60 / 60),
    ("thirds", 1 / 60),
    ("jiffies", 1 / 60),
    ("nanocenturies", SECONDS_PER_TROPICAL_YEAR / 10000000),
    ("quasihemidemisemiseconds", SECONDS_PER_MINUTE / 128),
    ("blinks", SECONDS_PER_MINUTE / 100),
    ("seconds", 1),
    ("microfortnights", SECONDS_PER_DAY * 14 / 1000000),
    ("decaseconds", 10),
    ("minutes", SECONDS_PER_MINUTE),
    ("warhols", 15 * SECONDS_PER_MINUTE),
    ("moments", 90),
    ("binghams", math.pi * SECONDS_PER_MINUTE), # average lateness to meetings which approaches pi to the limit
    ("hectoseconds", 100),
    ("soft boiled egg timers", 4 * SECONDS_PER_MINUTE),
    ("hard boiled egg timers", 9 * SECONDS_PER_MINUTE),
    ("decaminutes", 10 * SECONDS_PER_MINUTE),
    ("kiloseconds", 1000),
    ("microcenturies", SECONDS_PER_TROPICAL_YEAR / 10000),
    ("hours", SECONDS_PER_HOUR),
    ("hectominutes", 100 * SECONDS_PER_MINUTE),
    ("kilominutes", 1000 * SECONDS_PER_MINUTE),
    ("kermits", SECONDS_PER_DAY / 100),
    ("sidereal days",  23 * SECONDS_PER_HOUR + 56 * SECONDS_PER_MINUTE + 4.0905),
    ("days", SECONDS_PER_DAY),
    ("weeks", 7 * SECONDS_PER_DAY),
    ("megasecond", 1e+6),
    ("fortnights", 14 * SECONDS_PER_DAY),
    ("months", SECONDS_PER_TROPICAL_YEAR / 12),
    ("friedmans", SECONDS_PER_TROPICAL_YEAR / 6),
    ("dog years", SECONDS_PER_TROPICAL_YEAR / 7),
    ("years", SECONDS_PER_TROPICAL_YEAR),
    ("dog years", 7 * SECONDS_PER_TROPICAL_YEAR), # yes, I know there are two entirely contradictory definitions of dog years here -- it depends on your perspective
    ("decades", 10 * SECONDS_PER_TROPICAL_YEAR),
    ("gigaseconds", 1e+9),
    ("jubilees", 50 * SECONDS_PER_TROPICAL_YEAR),
    ("centuries", 100 * SECONDS_PER_TROPICAL_YEAR),
    ("millenia", 1000 * SECONDS_PER_TROPICAL_YEAR),
    ("megawarhols", 15 * SECONDS_PER_MINUTE * 1e+6),
    ("teraseconds", 1e+12),
    ("megayears", 1e+6 * SECONDS_PER_TROPICAL_YEAR),
    ("gigawarhols", 15 * SECONDS_PER_MINUTE * 1e+9),
    ("petaseconds", 1e+15),
    ("galactic years", 2.3e+8 * SECONDS_PER_TROPICAL_YEAR),
    ("aeons", 1e+9 * SECONDS_PER_TROPICAL_YEAR),
    ("exaseconds", 1e+18),
    ("zettaseconds", 1e+21),
    ("yottaseconds", 1e+24)
)


def helpful_time(seconds):
    unit, factor = random.choice(TIME_UNITS)
    return f"{seconds / factor:0.0000g} {unit}"


class Timer:

    def __init__(self):
        self._start = time.time()
        self._mark = self._start

    def elapsed(self):
        return time.time() - self._mark

    def total(self):
        return time.time() - self._start

    def mark(self):
        self._start = time.time()


def main(words_path):
    words = list(read_words(words_path))
    times = defaultdict(list)
    job_timer = Timer()
    seen_words = []
    matches = 0

    for word in words:
        seen_words.append(word)
        word_timer = Timer()

        if is_word_in_graph(word):
            print(f"Match: {word}!")
            matches += 1

        times[len(word)].append(word_timer.elapsed())

        if len(times) > 3:
            word_lengths, compute_times = tuple(zip(*[
                (length, compute_time)
                for length, compute_times_for_length in times.items()
                for compute_time in compute_times_for_length
            ]))

            f_time_for_length = fit_exponential(word_lengths, compute_times)
            estimated_total = sum(f_time_for_length(len(w)) for w in words)
            print(f"Found {matches} matches in {len(seen_words)}/{len(words)} words -- "
                  f"{job_timer.total() / estimated_total:0.0%} complete -- "
                  f"{helpful_time(estimated_total - job_timer.total())} remaining")


DEFAULT_WORDS_PATH = "/usr/share/dict/words"

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 2:
        print(f"Usage: {__file__} [path/to/words/lists]")
        exit(-1)

    words_path = DEFAULT_WORDS_PATH
    if len(sys.argv) == 2:
        words_path = sys.argv[1]

    main(words_path)
