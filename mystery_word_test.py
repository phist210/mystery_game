from mystery_game import clean_sentence
from mystery_game import pull_words_min_max
from mystery_game import pull_rand_word


def test_clean_sentence_true():
    assert clean_sentence('abcdefg') == 'abcdefg'


def test_clean_sentence_false():
    assert clean_sentence('12abcDe]]') == 'abcde'


def test_pull_words_easy():
    assert pull_words_min_max(["pear", "racecar", "tarantula"], 4, 6) == ['pear']


def test_pull_words_medium():
    assert pull_words_min_max(["pear", "racecar", "tarantula"], 6, 8) == ['racecar']


def test_pull_words_hard():
    assert pull_words_min_max(["pear", "racecar", "tarantula"], 8, 99) == ['tarantula']


def test_pull_rand_word():
    assert pull_rand_word(['apple', 'banana', 'tarantula', 'flabbergasted'])


test_clean_sentence_true()
test_clean_sentence_false()
test_pull_words_easy()
test_pull_words_medium()
test_pull_words_hard()
test_pull_rand_word()
