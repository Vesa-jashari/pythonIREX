import csv

import requests
from bs4 import BeautifulSoup

url = 'https://www.mercedes-benz.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Successfully retrieved the page")
else:
    print(f"Failed to retrieve the page, status code: {response.status_code}")

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a')

print("Extracted Links:")
for link in links:
    href = link.get('href')
    text = link.text.strip()
    if href:
        print(f"Link Text: {text}, URL: {href}")

with open('mercedes_links.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Link Text', 'URL'])

    for link in links:
        href = link.get('href')
        text = link.text.strip()
        if href:
            writer.writerow([text, href])

print("Links have been saved to 'mercedes_links.csv'")





