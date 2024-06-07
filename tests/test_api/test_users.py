import unittest
from api import app

class TestUserAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_users(self):
        response = self.app.get('/api/v1/users')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_create_user(self):
        response = self.app.post('/api/v1/users',
                                 json={
                                     'email':
                                     'test@test.com',
                                     'password':
                                     'test'
                                     })
        self.assertEqual(response.status_code, 201)
        self.assertIn('email', response.json)
        self.assertEqual(response.json['email'], 'test@test.com')
