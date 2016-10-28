from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    # creates a game and adds it to the database.
    first_game = Game(name = 'GhillieSuit', description = 'Gator huntin\'')
    second_game = Game(name = 'Okie Noodlin\'', description = 'My daddy done it, \
                               my granddaddy done it. Now I done it.')
    db.session.add(first_game, second_game)
    db.session.commit()
    


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    print "Connected to DB."
 