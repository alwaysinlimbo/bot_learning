# config.py
# Конфигурация для работы с API CoinGecko

API_URL = "https://api.coingecko.com/api/v3/simple/price"

PARAMS = {
    "vs_currencies": "usd",   # Валюта, в которой показывать цену
    "ids": "bitcoin"          # ID криптовалюты
}

HEADERS = {
    "x-cg-demo-api-key": "CG-9QiuZQdLy8uLZThdSSvfcdHu"
}

TIMEOUT = 10  # Таймаут запроса в секундах