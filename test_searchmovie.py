import pytest

def search_movie(filmy, tytul):
    for film in filmy:
        if film['tytul'].lower() == tytul.lower():
            return film
    return None

def test_search_movie_found():
    filmy = [{'tytul': 'Inception', 'gatunek': 'Sci-Fi', 'rezyser': 'Christopher Nolan'}]
    wynik = search_movie(filmy, 'Inception')
    assert wynik is not None
    assert wynik['tytul'] == 'Inception'

def test_search_movie_not_found():
    filmy = [{'tytul': 'Inception', 'gatunek': 'Sci-Fi', 'rezyser': 'Christopher Nolan'}]
    wynik = search_movie(filmy, 'Titanic')
    assert wynik is None

def test_search_movie_case_insensitive():
    filmy = [{'tytul': 'Inception', 'gatunek': 'Sci-Fi', 'rezyser': 'Christopher Nolan'}]
    wynik = search_movie(filmy, 'inception')
    assert wynik is not None
    assert wynik['tytul'] == 'Inception'

def test_search_movie_empty_list():
    filmy = []
    wynik = search_movie(filmy, 'Inception')
    assert wynik is None

if __name__ == "__main__":
    pytest.main()
