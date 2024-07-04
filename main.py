import requests
import send_email as se
apikey = "34efc8e030c84c6789d6d229b1052883"
query = "Danish Chaudhary"
url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={apikey}&language=en"

request = requests.get(url)
content = request.json()
message ="Subject: Today's News \n"
for article in content["articles"][0:20]:
    if article['title'] is not None:
        message = message + article["title"] + "\n" \
                  + article["description"] +"\n" + \
                  article["url"] + 2*"\n"

message = message.encode("utf-8")
se.sending_email("chaudharydanish024@gmail.com", message)
