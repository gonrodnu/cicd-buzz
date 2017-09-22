import os
import signal
from flask import Flask, send_from_directory
from buzz import generator

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
    page = '<html>' \
           '<head><link rel="stylesheet" href="/resources/blockquote.css"></head>' \
           '<body style="background-color:powderblue;"><blockquote>'
    page += generator.generate_buzz()
    page += '</blockquoute></body></html>'
    return page

@app.route('/resources/<path:path>')
def send_js(path):
    return send_from_directory('resources/web_resources', path)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT')) # port 5000 is the default