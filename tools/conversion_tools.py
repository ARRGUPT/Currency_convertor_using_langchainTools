from langchain_core.tools import tool, InjectedToolArg
from typing import Annotated
import requests
from dotenv import load_dotenv
import os

load_dotenv()
exchangerate_api_key = os.getenv("EXCHANGERATE_API_KEY")

@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """
    Fetch the currency conversion factor between base and target currency.
    """
    url = f'https://v6.exchangerate-api.com/v6/{exchangerate_api_key}/pair/{base_currency}/{target_currency}'
    response = requests.get(url)
    return response.json()

@tool
def convert(base_currency_value: float, conversion_rate: Annotated[float, InjectedToolArg]) -> float:
    """
    Convert base currency value using the given conversion rate.
    """
    return base_currency_value * conversion_rate
