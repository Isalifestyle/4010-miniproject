# api_key = "b7ac4bc4468c8208fa6899b52b919495e0c3061303b29de34f5a42208844a77e"

import requests
from bs4 import BeautifulSoup

def google_search(query):
    api_key = "b7ac4bc4468c8208fa6899b52b919495e0c3061303b29de34f5a42208844a77e"
    search_url = f"https://serpapi.com/search.json?q={query}&api_key={api_key}"
    try:
        response = requests.get(search_url)
        response.raise_for_status()
        results = response.json().get("organic_results", [])
        return [result.get("link", "") for result in results if "link" in result][:3]
    except Exception as e:
        return []

def fetch_web_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        return "\n".join([p.get_text() for p in paragraphs[:5]])
    except Exception as e:
        return f"Error fetching data from {url}: {str(e)}"

def gather_data(questions):
    data = {}
    for question in questions:
        urls = google_search(question)
        content = "\n".join([fetch_web_content(url) for url in urls])
        data[question] = content
    return data





