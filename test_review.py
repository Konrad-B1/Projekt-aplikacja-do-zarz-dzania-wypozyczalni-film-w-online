import pytest

def leave_review(film, recenzja):
    if 'recenzje' not in film:
        film['recenzje'] = []
    film['recenzje'].append(recenzja)
    return film

def test_leave_review_new_review():
    film = {'tytul': 'Inception', 'gatunek': 'Sci-Fi', 'rezyser': 'Christopher Nolan'}
    wynik = leave_review(film, 'Amazing movie!')
    assert 'recenzje' in wynik
    assert len(wynik['recenzje']) == 1
    assert wynik['recenzje'][0] == 'Amazing movie!'

def test_leave_review_multiple_reviews():
    film = {'tytul': 'Inception', 'gatunek': 'Sci-Fi', 'rezyser': 'Christopher Nolan', 'recenzje': ['Great!']}
    wynik = leave_review(film, 'Amazing movie!')
    assert len(wynik['recenzje']) == 2
    assert wynik['recenzje'][1] == 'Amazing movie!'

def test_leave_review_duplicate_review():
    film = {'tytul': 'Inception', 'gatunek': 'Sci-Fi', 'rezyser': 'Christopher Nolan', 'recenzje': ['Great!']}
    wynik = leave_review(film, 'Great!')
    assert len(wynik['recenzje']) == 2
    assert wynik['recenzje'][1] == 'Great!'

def test_leave_review_empty_review():
    film = {'tytul': 'Inception', 'gatunek': 'Sci-Fi', 'rezyser': 'Christopher Nolan'}
    wynik = leave_review(film, '')
    assert len(wynik['recenzje']) == 1
    assert wynik['recenzje'][0] == ''

if __name__ == "__main__":
    pytest.main()
