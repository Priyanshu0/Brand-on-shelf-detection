import requests
import json
import os

# API key and Custom Search Engine ID
API_KEY = ''
CSE_ID = ''
SAVE_DIR = ""

def google_search(search_term, api_key, cse_id, save_dir, num=10):
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': search_term,
        'key': api_key,
        'cx': cse_id,
        'searchType': 'image',
        'num': num  # Number of images to return (max 10 per request)
    }
    response = requests.get(search_url, params=params)
    result = response.json()
    query_name = search_term.replace(" ", "_")
    if 'items' in result:
        items = result['items']
        for i, item in enumerate(items):
            link = item['link']
            download_image(link, os.path.join(save_dir, f"{query_name}_{i}.jpg"))

def download_image(url, save_path):
    try:
        response = requests.get(url)
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {save_path}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

if __name__ == "__main__":
    search_term = "Crown Royal on Walmart store shelves"
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)
    google_search(search_term, API_KEY, CSE_ID, SAVE_DIR)
