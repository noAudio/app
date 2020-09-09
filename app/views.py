from app import app

@app.route('/')
def index():
    return 'Hello world'

@app.route('/about')
def about():
    return 'About'
