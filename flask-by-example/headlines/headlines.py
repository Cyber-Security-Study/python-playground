"""
    HEADLINES
    ~~~~~~~~~
    Flask by example
"""

import feedparser
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

RSS_FEEDS = {
    'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    'fox': 'http://feeds.foxnews.com/foxnews/latest',
    'iol': 'http://www.iol.co.za/cmlink/1.640'
}


@app.route('/')
def get_news():
    query = request.args.get('publication')
    if not query or query.lower() not in RSS_FEEDS:
        publication = 'bbc'
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    weather = get_weather()
    return render_template(
        'home.html',
        articles=feed['entries'],
        weather=weather
    )


def get_weather():
    payload = {
        'q': 'London, uk',
        'units': 'metric',
        'appid': 'dd5001c4843d408c7a4ed6fc8b490e04'
    }
    r = requests.get(
        'http://api.openweathermap.org/data/2.5/weather',
        params=payload
    )
    parsed = r.json()
    weather = None
    # if r.status_code == requests.codes.ok:
    if parsed.get('weather'):
        weather = {
            'description': parsed['weather'][0]['description'],
            'temperature': parsed['main']['temp'],
            'city': parsed['name']
        }
    return weather


if __name__ == '__main__':
    app.run(port=5000, debug=True)
