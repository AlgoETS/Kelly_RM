# -*- coding: utf-8 -*-

from src.request_api import make_api_request
from src.config import FMP_API_KEY, BINANCE_API_KEY, BASE_URL_BINANCE, BASE_URL_FMP


async def get_historical_data(symbol, interval, limit=500):
    api_endpoint = f"{BASE_URL_BINANCE}/klines"
    params = {"symbol": symbol, "interval": interval, "limit": limit}

    return make_api_request(api_endpoint, params)


async def get_historical_price_full_crypto(symbol):
    api_endpoint = f"{BASE_URL_FMP}/historical-price-full/crypto/{symbol}"
    params = {"apikey": FMP_API_KEY}
    return make_api_request(api_endpoint, params)



async def get_historical_price_full_stock(symbol):
    api_endpoint = f"{BASE_URL_FMP}/historical-price-full/{symbol}"
    params = {"apikey": FMP_API_KEY}

    return make_api_request(api_endpoint, params)


async def get_historical_price_full_stock_batch(symbols: list, start=None, end=None):
    api_endpoint = f"{BASE_URL_FMP}/historical-price-full/{symbols.join(',')}"
    params = {
        "apikey": FMP_API_KEY
        # "from": start,
        # "to": end,
    }

    return make_api_request(api_endpoint, params)

async def get_financial_statements_lists(symbol):
    api_endpoint = f"{BASE_URL_FMP}/financial-statement-lists"
    params = {"apikey": FMP_API_KEY}
    return make_api_request(api_endpoint, params)