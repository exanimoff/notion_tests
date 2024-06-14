import pytest
import requests
from notion_api import get_database, create_database

parent_page_id = "5259b8ada2fa41dfa063aed4115d01c5"
PAGE_ID = "04c4ad5eef734176a663efa635dd20b7"
DATABASE_ID = "04c4ad5eef734176a663efa635dd20b7"
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
    response = get_database(PAGE_ID)
    # assert response['object'] == 'page'
    # assert 'properties' in response

def test_create_page():
    response = create_database(parent_page_id, title, PROPERTIES)
    assert response['object'] == 'page'
    assert response['properties']['Name']['title'][0]['text']['content'] == 'Test Page'

