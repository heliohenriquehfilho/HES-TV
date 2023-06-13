from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/series')
def series():
    return render_template('series.html')

@app.route('/movies')
def movies():
    return render_template('movies.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/live-streaming')
def live_streaming():
    return render_template('live_streaming.html')

if __name__ == '__main__':
    app.run(debug=True)
