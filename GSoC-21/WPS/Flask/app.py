from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home") # to create another route for home page
def hello():
    return render_template("home.html")

@app.route("/about")
def about():
    return "About"

if __name__ == "__main__": # another way to prevent start server again to see chnages # run using Python app.py
    app.run(debug=True) 