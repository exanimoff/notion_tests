import pytest
import requests
from notion_api import get_page

PAGE_ID = "5259b8ada2fa41dfa063aed4115d01c5"
# DATABASE_ID = "your_database_id_here"
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
    # assert response['object'] == 'page'
    # assert 'properties' in response

# def test_create_page():
#     response = create_page(DATABASE_ID, PROPERTIES)
#     assert response['object'] == 'page'
#     assert response['properties']['Name']['title'][0]['text']['content'] == 'Test Page'

