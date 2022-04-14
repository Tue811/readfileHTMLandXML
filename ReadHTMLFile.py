import requests
from bs4 import BeautifulSoup

req = requests.get("https://kfcvietnam.com.vn/vi/thuc-don/14/combo-1-nguoi.html")

soup = BeautifulSoup(req.text, "html.parser")

for scipt in soup({"scipt","style"}):
    scipt.extract()

text = soup.get_text()

lines = (line.strip() for line in text.splitlines())

chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

text = '\n'.join(chunks for chunks in chunks if chunks)
print(text)