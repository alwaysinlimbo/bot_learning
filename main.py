# main.py
from api import get_bitcoin_price

def main():
    """Главная функция программы."""
    price = get_bitcoin_price()
    
    if price is not None:
        print(f"Курс Биткоина: {price} USD")
    else:
        print("Не удалось получить курс Биткоина")

if __name__ == "__main__":
    main()