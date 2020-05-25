
import unittest
import os

from app import db, app
from app.models import User, Candidate


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['SECRET_KEY'] = 'noonecangetthepassword'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()
        can1 = Candidate(name='A', email='A-test@uwa.asd', description='Test')
        can2 = Candidate(name='B', email='B-test@uwa.asd', description='Test')
        can3 = Candidate(name='C', email='C-test@uwa.asd', description='Test')
        db.session.add(can1)
        db.session.add(can2)
        db.session.add(can3)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_is_vote_success(self):
        u1 = User(username='user1', email='user1@qq.com',
                  password='password', preference='1')
        db.session.add(u1)
        db.session.commit()
        u = User.query.get(1)
        self.assertTrue(u.preference == 1)
        self.assertTrue(u.username == 'user1')

    def test_home_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        response = self.app.get('/register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.app.get('/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_candidate_page(self):
        response = self.app.get('/candidate', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_results_page(self):
        response = self.app.get('/account', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def register(self, username, email, password, confirm_password):

        return self.app.post('/register',
                             data=dict(username=username, email=email,
                                       password=password, confirm_password=confirm_password
                                       ),
                             follow_redirects=True)

# REGISTRATION FUNCTIONALITY TESTS
    # Tests a valid registration attempt
    def test_valid_user_registration(self):
        response = self.register('user', 'user@gmail.com',
                                 'password', 'password')
        self.assertEqual(response.status_code, 200)

    # Tests an invalid registration attempt where passwords do not match
    def test_invalid_registration_passwords(self):
        response = self.register("user", "grae@email.com",
                                 "password", "invalid password")
        self.assertEqual(response.status_code, 200)

    # Tests an invalid registration attempt where email is invalid
    def test_invalid_registration_email(self):
        # missing @ symbol
        response = self.register(
            "user", "invalid email.com", "password", "password")
        self.assertEqual(response.status_code, 200)

        # missing domain
        response = self.register(
            "user", "invalid@email", "password", "password")
        self.assertEqual(response.status_code, 200)

        # invalid space inserted
        response = self.register(
            "user", "invalid@ email.com", "password", "password")
        self.assertEqual(response.status_code, 200)

    # Tests an invalid registration where the username and/or email are already taken
    def test_invalid_registration_duplicates(self):
        u1 = User(username="existing_user",
                  email="existing_user@email.com", password="password", preference="1")
        db.session.add(u1)
        db.session.commit()

        # duplicate username
        response = self.register(
            "existing_user", "user@email.com", "password", "password")
        self.assertEqual(response.status_code, 200)

        # duplicate email
        response = self.register(
            "user", "existing_user@email.com", "password", "password")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
