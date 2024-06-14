import requests
from config import NOTION_API_TOKEN, NOTION_API_BASE_URL

headers = {
    "Authorization": f"Bearer {NOTION_API_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

def get_database(page_id):
    url = f"{NOTION_API_BASE_URL}/v1/databases/{page_id}"
    print(f"GET {url}")
    response = requests.get(url, headers=headers)
    print(f"Response status: {response.status_code}")
    print(f"Response content: {response.content}")
    response.raise_for_status()
    return response.json()

# def create_page(parent_id, properties):
#     url = f"{NOTION_API_BASE_URL}/pages"
#     data = {
#         "parent": {"database_id": parent_id},
#         "properties": properties
#     }
#     print(f"POST {url}")
#     print(f"Request data: {data}")
#     response = requests.post(url, headers=headers, json=data)
#     print(f"Response status: {response.status_code}")
#     print(f"Response content: {response.content}")
#     response.raise_for_status()
#     return response.json()
