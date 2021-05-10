from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'Hello man'

@app.route('/extract')
def extract():
    pass

@app.route('/products')
def products():
    pass

@app.route('/opinions/<product_id>')
def productId(product_id):
    pass

@app.route('/charts/<product_id>')
def charts(product_id):
    pass