from spaceman import is_guess_in_word, get_guessed_word, is_word_guessed
import pytest

#automatically runs tests for is_guess_in_word
def test_is_guess_in_word():
    assert is_guess_in_word('c', 'ficticious') == True
    assert is_guess_in_word('$', 'ficticious') == False
    assert is_guess_in_word('1', 'ficticious') == False
    assert is_guess_in_word('a', 'ficticious') == False
    assert is_guess_in_word('C', 'ficticious') == True

#automatically runs tests for get_guessed_word
def test_get_guessed_word():
    assert get_guessed_word('applesauce', 'applesauses') == False
    assert get_guessed_word('applesause', 'applesauce') == True
    assert get_guessed_word('applesauce', 'pplesuce') == False

#automatically runs tests for is_word_guessed
def test_is_word_guessed():
    assert is_word_guessed('waterfall', 'waterfall') == True 
    assert is_word_guessed('waterfall', 'waterfal') == False
    assert is_word_guessed('waterfall', 'wtrfll') == False

if '__name__' == '__main__':
    test_is_guess_in_word()
    test_get_guessed_word()
    test_is_word_guessed()