import requests
import json
from config import NOTION_API_TOKEN, NOTION_API_BASE_URL

headers = {
    "Authorization": f"Bearer {NOTION_API_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}


def save_response_to_file(response, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(response, f, ensure_ascii=False, indent=4)


def get_database(database_id):
    url = f"{NOTION_API_BASE_URL}/v1/databases/{database_id}"
    print(f"GET {url}")
    response = requests.get(url, headers=headers)
    print(f"Response status: {response.status_code}")
    print(f"Response content: {response.content}")
    response.raise_for_status()
    return response.json()


def create_database(parent_page_id, title, properties):
    url = f"{NOTION_API_BASE_URL}/v1/databases"
    data = {
        "parent": {"type": "page_id", "page_id": parent_page_id},
        "title": [{"type": "text", "text": {"content": title}}],
        "properties": properties
    }
    print(f"POST {url}")
    print(f"Request data: {data}")
    response = requests.post(url, headers=headers, json=data)
    print(f"Response status: {response.status_code}")
    print(f"Response content: {response.content}")
    response.raise_for_status()
    return response.json()


def filter_database_task_completed(database_id):
    url = f"{NOTION_API_BASE_URL}/v1/databases/{database_id}/query"
    data = {
        "filter": {
            "property": "Status",
            "status": {
                "equals": "Done"
            }
        }
    }
    print(f"POST {url}")
    print(f"Request data: {data}")
    response = requests.post(url, headers=headers, json=data)
    print(f"Response status: {response.status_code}")
    print(f"Response content: {response.content}")
    response.raise_for_status()
    return response.json()
