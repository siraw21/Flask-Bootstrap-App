from flask import Flask, render_template, request
import requests
from config import NEWS_API_KEY


app = Flask(__name__)

# Homepage - Route
@app.route("/")
def index():
   query = request.args.get("query", "Latest")
   url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
   response = requests.get(url)
   news_data = response.json()
   # print(news_data)

   return render_template("index.html")






if __name__ == "__main__":
   app.run(debug=True)