import unittest

from party import app
from model import db, example_data, connect_to_db


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        result = self.client.get("/")
        self.assertIn("board games, rainbows, and ice cream sundaes", result.data)
        print
        print "homepage test complete"
        

    def test_no_rsvp_yet(self):
        result = self.client.get("/")
        # Add a test to show we see the RSVP form, but NOT the party details
        self.assertEqual(result.status_code, 200)
        self.assertIn('<h2>Please RSVP</h2>', result.data)
        self.assertNotIn('<h2>Party Details</h2>', result.data)
        print
        print "no RSVP test complete"
        

    def test_rsvp(self):
        result = self.client.post("/rsvp",
                                  data={"name": "Jane",
                                        "email": "jane@jane.com"},
                                  follow_redirects=True)
        # Once we RSVP, we should see the party details, but not the RSVP form
        self.assertEqual(result.status_code, 200)
        self.assertIn('<h2>Party Details</h2>', result.data)
        self.assertNotIn('<h2>Please RSVP</h2>', result.data)
        print
        print "RSVP test complete"
        


class PartyTestsDatabase(unittest.TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database (uncomment when testing database)
        connect_to_db(app, "postgresql:///testdb")

        # Create tables and add sample data (uncomment when testing database)
        db.create_all()
        example_data()

        # with self.client as c:
            with c.session_transaction() as sess:
                sess['RSVP'] = True

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()

    def test_games(self):
        # test that the games page displays the game from example_data()
        result = self.client.get("/games")
        # Add a test to show we see the RSVP form, but NOT the party details
        
        print "status code: ", result.status_code

        self.assertEqual(result.status_code, 200)
        self.assertIn('GhillieSuit', result.data)
        print
        print "games test complete"


if __name__ == "__main__":
    unittest.main()
