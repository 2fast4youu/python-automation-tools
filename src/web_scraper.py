#!/usr/bin/env python3
"""Extract links from websites."""
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_links(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    return [{"text": a.get_text(strip=True), "url": urljoin(url, a["href"])} for a in soup.find_all("a", href=True)]
