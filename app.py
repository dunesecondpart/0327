from flask import Flask, render_template

app = Flask(__name__)

const data = [
  {
    "id": 1,
    "artist_name": "Drake",
    "venue": "Scotiabank Arena",
    "city": "Toronto",
    "date": "2024-05-10",
    "description": "Don't miss the Toronto-native rapper, singer, and songwriter Drake as he brings his electrifying performance to Scotiabank Arena.",
    "ticket_price": 100
  },
  {
    "id": 2,
    "artist_name": "Justin Bieber",
    "venue": "Rogers Arena",
    "city": "Vancouver",
    "date": "2024-06-15",
    "description": "Catch Justin Bieber live in concert at Rogers Arena, Vancouver. Experience the pop sensation's chart-topping hits and incredible stage presence.",
    "ticket_price": 90
  }
]

@app.route('/', methods=['GET'])
def index():
    # Render the HTML page for GET requests
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
