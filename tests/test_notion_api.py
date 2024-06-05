# tests/test_notion_api.py
import pytest
import requests
from notion_api import get_page, create_page

# Пример тестовых данных
PAGE_ID = "your_page_id_here"
DATABASE_ID = "your_database_id_here"
PROPERTIES = {
    "Name": {
        "title": [
            {
                "text": {
                    "content": "Test Page"
                }
            }
        ]
    }
}

def test_get_page():
    response = get_page(PAGE_ID)
    assert response['object'] == 'page'
    assert 'properties' in response

def test_create_page():
    response = create_page(DATABASE_ID, PROPERTIES)
    assert response['object'] == 'page'
    assert response['properties']['Name']['title'][0]['text']['content'] == 'Test Page'

# Добавьте другие тесты для различных функций
