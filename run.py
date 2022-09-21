import os

from project.models import Genre, Movie, Director, User
from project.server import create_app, db

app = create_app(os.getenv("FLASK_ENV", "development"))


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "User": User,
        "Movie": Movie,
        "Director": Director
    }


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
