from model import Game, connect_to_db, db
from party import app


def load_games():
    """Load games from data/games.csv into database."""

    for i, row in enumerate(open("data/games.csv")):
        row = row.rstrip()
        name, description = row.split("|")

        game = Game(name=name, description=description)

        # We need to add to the session or it won't ever be stored
        db.session.add(game)

    # Once we're done, we should commit our work
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()
    load_games()
