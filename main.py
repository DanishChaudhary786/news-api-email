import requests
import send_email as se
apikey = "34efc8e030c84c6789d6d229b1052883"
# query = input("Enter your query: ")
url = f"https://newsapi.org/v2/everything?q=apple&sortBy=publishedAt&apiKey={apikey}"

request = requests.get(url)
content = request.json()
message =""
for article in content["articles"]:
    message = message + article["title"] + "\n" + article["description"] + 2*"\n"

message = message.encode("utf-8")
se.sending_email("danish.chaudhary@wotnot.io", message)
