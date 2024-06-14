import pytest
import requests
from notion_api import get_database, create_database

parent_page_id = "9a6a7be7edd349f588c9f066965d731c"
PAGE_ID = "c860cb8ca7bf4e7eaba9d22fb9c61a57"
DATABASE_ID = "c860cb8ca7bf4e7eaba9d22fb9c61a57"
title = "Example Database"
PROPERTIES = {
        "Name": {
            "title": {}
        },
        "Tags": {
            "multi_select": {
                "options": [
                    {"name": "Tag1"},
                    {"name": "Tag2"}
                ]
            }
        }
    }

def test_get_database():
    response = get_database(DATABASE_ID)
    # assert response['object'] == 'page'
    # assert 'properties' in response

def test_create_page():
    response = create_database(parent_page_id, title, PROPERTIES)
    assert response['object'] == 'page'
    assert response['properties']['Name']['title'][0]['text']['content'] == 'Test Page'

