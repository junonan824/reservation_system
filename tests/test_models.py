import unittest
from app import create_app, db
from app.models import User, Reservation, Review

class ModelTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app.config['TESTING'] = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_creation(self):
        user = User(username="testuser", email="test@example.com", password="testpass")
        db.session.add(user)
        db.session.commit()
        self.assertTrue(User.query.filter_by(username="testuser").first())

if __name__ == '__main__':
    unittest.main()