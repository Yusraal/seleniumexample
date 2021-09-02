"""This is an example of API Testing using requests library
and Rick and Morty API"""
import requests
import pytest


@pytest.mark.apitest
def test_all_characters():
    response = requests.get("https://rickandmortyapi.com/api/character")
    json_data = response.json()
    print(json_data)
