import pytest
import requests
from notion_api import get_database

PAGE_ID = "04c4ad5eef734176a663efa635dd20b7"
DATABASE_ID = "04c4ad5eef734176a663efa635dd20b7"
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

def test_get_database():
    response = get_database(PAGE_ID)
    # assert response['object'] == 'page'
    # assert 'properties' in response

# def test_create_page():
#     response = create_page(DATABASE_ID, PROPERTIES)
#     assert response['object'] == 'page'
#     assert response['properties']['Name']['title'][0]['text']['content'] == 'Test Page'

