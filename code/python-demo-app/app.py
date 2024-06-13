from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def favorite_movies():
    movies = [
        "The Godfather (1972)",
        "The Shawshank Redemption (1994)",
        "Titanic (1997)",
        "The Dark Knight (2008)",
        "Inception (2010)",
    ]
    return render_template("index.html", movies=movies)
