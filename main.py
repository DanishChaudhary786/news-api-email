import requests

apikey = "34efc8e030c84c6789d6d229b1052883"
# query = input("Enter your query: ")
url = f"https://newsapi.org/v2/everything?q=apple&sortBy=publishedAt&apiKey={apikey}"

request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(article["title"])