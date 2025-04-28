import pytest
def add_movie(filmy, tytul, gatunek, rezyser):
    film = {
        'tytul': tytul,
        'gatunek': gatunek,
        'rezyser': rezyser
    }
    filmy.append(film)
    return filmy

def test_add_movie_valid():
    filmy = []
    wynik = add_movie(filmy, 'Inception', 'Sci-Fi', 'Christopher Nolan')
    assert len(wynik) == 1
    assert wynik[0]['tytul'] == 'Inception'

def test_add_movie_multiple():
    filmy = [{'tytul': 'Inception', 'gatunek': 'Sci-Fi', 'rezyser': 'Christopher Nolan'}]
    wynik = add_movie(filmy, 'Interstellar', 'Sci-Fi', 'Christopher Nolan')
    assert len(wynik) == 2
    assert wynik[1]['tytul'] == 'Interstellar'

def test_add_movie_invalid():
    filmy = []
    wynik = add_movie(filmy, '', 'Drama', 'Christopher Nolan')
    assert len(wynik) == 1
    assert wynik[0]['tytul'] == ''

def test_add_movie_empty_list():
    filmy = []
    wynik = add_movie(filmy, 'Titanic', 'Romance', 'James Cameron')
    assert wynik == [{'tytul': 'Titanic', 'gatunek': 'Romance', 'rezyser': 'James Cameron'}]

if __name__ == "__main__":
    pytest.main()
