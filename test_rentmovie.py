import pytest

def rent_movie(uzytkownik, film):
    if 'wypozyczone_filmy' not in uzytkownik:
        uzytkownik['wypozyczone_filmy'] = []
    uzytkownik['wypozyczone_filmy'].append(film)
    return uzytkownik

def test_rent_movie_new_user():
    uzytkownik = {}
    film = {'tytul': 'Inception', 'gatunek': 'Sci-Fi', 'rezyser': 'Christopher Nolan'}
    wynik = rent_movie(uzytkownik, film)
    assert 'wypozyczone_filmy' in wynik
    assert len(wynik['wypozyczone_filmy']) == 1
    assert wynik['wypozyczone_filmy'][0]['tytul'] == 'Inception'

def test_rent_movie_existing_user():
    uzytkownik = {'wypozyczone_filmy': [{'tytul': 'Inception', 'gatunek': 'Sci-Fi', 'rezyser': 'Christopher Nolan'}]}
    film = {'tytul': 'Interstellar', 'gatunek': 'Sci-Fi', 'rezyser': 'Christopher Nolan'}
    wynik = rent_movie(uzytkownik, film)
    assert len(wynik['wypozyczone_filmy']) == 2
    assert wynik['wypozyczone_filmy'][1]['tytul'] == 'Interstellar'

def test_rent_movie_duplicate():
    uzytkownik = {'wypozyczone_filmy': [{'tytul': 'Inception', 'gatunek': 'Sci-Fi', 'rezyser': 'Christopher Nolan'}]}
    film = {'tytul': 'Inception', 'gatunek': 'Sci-Fi', 'rezyser': 'Christopher Nolan'}
    wynik = rent_movie(uzytkownik, film)
    assert len(wynik['wypozyczone_filmy']) == 2
    assert wynik['wypozyczone_filmy'][1]['tytul'] == 'Inception'

def test_rent_movie_multiple_users():
    uzytkownik_1 = {'wypozyczone_filmy': [{'tytul': 'Inception', 'gatunek': 'Sci-Fi', 'rezyser': 'Christopher Nolan'}]}
    uzytkownik_2 = {'wypozyczone_filmy': []}
    film = {'tytul': 'Interstellar', 'gatunek': 'Sci-Fi', 'rezyser': 'Christopher Nolan'}
    wynik_1 = rent_movie(uzytkownik_1, film)
    wynik_2 = rent_movie(uzytkownik_2, film)
    assert len(wynik_1['wypozyczone_filmy']) == 2
    assert len(wynik_2['wypozyczone_filmy']) == 1
    assert wynik_2['wypozyczone_filmy'][0]['tytul'] == 'Interstellar'

if __name__ == "__main__":
    pytest.main()
