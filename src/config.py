# -*- coding: utf-8 -*-
import os
import sys
from dotenv import load_dotenv, find_dotenv

#get root path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
#get parent path
PARENT_DIR = os.path.dirname(ROOT_DIR)


#add sample.env to parent path to load_dotenv
path = PARENT_DIR+'/sample.env'


load_dotenv(find_dotenv(path)) # take environment variables from .env.

FMP_API_KEY = os.getenv("FMP_API_KEY")
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")

BASE_URL_FMP = "https://financialmodelingprep.com/api/v3"
BASE_URL_BINANCE = "https://fapi.binance.com/fapi/v1/"
