# api.py
import requests
from config import API_URL, PARAMS, HEADERS, TIMEOUT


def get_bitcoin_price():
    """
    Получает текущую цену Биткоина в USD через API CoinGecko.
    
    Returns:
        float: Цена Биткоина в USD или None в случае ошибки.
    """
    try:
        response = requests.get(
            API_URL,
            params=PARAMS,
            headers=HEADERS,
            timeout=TIMEOUT
        )
        
        # Проверяем статус ответа
        if response.status_code == 200:
            data = response.json()
            # Извлекаем цену
            btc_price = data["bitcoin"]["usd"]
            return btc_price
        else:
            print(f"Ошибка API. Код: {response.status_code}")
            print(f"Ответ: {response.text}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None