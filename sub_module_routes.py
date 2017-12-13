from routes import app
@app.route('/submodule')
def new_hello_world():
    return "route return from the submodule"