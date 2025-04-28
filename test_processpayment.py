import pytest

def process_payment(suma_platnosci):
    if suma_platnosci <= 0:
        raise ValueError("Kwota płatności musi być większa od zera.")
    return True

def test_process_payment_valid():
    wynik = process_payment(100)
    assert wynik is True

def test_process_payment_zero():
    with pytest.raises(ValueError):
        process_payment(0)

def test_process_payment_negative():
    with pytest.raises(ValueError):
        process_payment(-50)

def test_process_payment_large_amount():
    wynik = process_payment(1000000)
    assert wynik is True

if __name__ == "__main__":
    pytest.main()
