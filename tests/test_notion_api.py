import pytest
import requests
from notion_api import *

parent_page_id = "9a6a7be7edd349f588c9f066965d731c"
page_id = "c860cb8ca7bf4e7eaba9d22fb9c61a57"
database_id = "c860cb8ca7bf4e7eaba9d22fb9c61a57"
title = "Example Database"

# def load_properties_from_file(filename):
#     with open(filename, 'r', encoding='utf-8') as file:
#         data = json.load(file)
#     properties = data['properties']
#     formatted_properties = {}
#     for prop_name, prop_info in properties.items():
#         if prop_info['type'] == 'status':
#             formatted_properties[prop_name] = {'status': {}}
#         else:
#             formatted_properties[prop_name] = {prop_info['type']: prop_info[prop_info['type']]}
#     return formatted_properties
#
# PROPERTIES = load_properties_from_file('database_response.json')

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
    """
    Получает response и сохраняет в database_response.json
    :return:
    """
    response = get_database(database_id)
    save_response_to_file(response, 'database_response.json')
    assert response['object'] == 'database'
    assert 'properties' in response
#
def test_create_database():
    response = create_database(parent_page_id, title, PROPERTIES)
    assert response['object'] == 'database'

    #assert response['properties']['Name']['title'][0]['text']['content'] == 'Test Page'

def test_filter_database_task_completed():
    response = filter_database_task_completed(database_id)
    for result in response.get('results', []):
        assert 'properties' in result
        assert 'Status' in result['properties']
        assert result['properties']['Status']['status']['name'] == 'Done'


