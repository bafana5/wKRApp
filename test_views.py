from wKRApp import app
import unittest 

class FlaskTestCase(unittest.TestCase):
    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the login page loads correctly
    def test_signin_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Please sign in' in response.data)

    # Ensure login behaves correctly given the correct credentials
    def test_correct_admin_signin(self):
        tester = app.test_client(self)
        response = tester.post('/', 
                               data=dict(username="Admin", password="admin"),
                               follow_redirects=True)
        self.assertIn(b'You were just logged in', response.data)

    # Ensure login behaves correctly given the empty credentials
    def test_empty_signin_fields(self):
        tester = app.test_client(self)
        response = tester.post('/', 
                               data=dict(username="", password=""),
                               follow_redirects=True)
        self.assertIn(b'Invalid credentials. Please try again.', response.data)

    # Ensure logout behaves correctly
    def test_admin_logout(self):
        tester = app.test_client(self)
        tester.post('/', 
                    data=dict(username="Admin", password="admin"),
                    follow_redirects=True)
        response = tester.get('/logout', follow_redirects=True)
        self.assertTrue(b'You were just logged out' in response.data)
     
    # Ensure that admin page requires user to signin
    def test_admin_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/admin', follow_redirects=True)
        self.assertIn(b'You need to login first.', response.data)

    # Ensure that kra page requires user to signin
    def test_kra_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/kra', follow_redirects=True)
        self.assertIn(b'You need to login first.', response.data)

    # Ensure that users page requires user to signin
    def test_users_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/users', follow_redirects=True)
        self.assertIn(b'You need to login first.', response.data)

    # Ensure that user_roles page requires user to signin
    def test_user_roles_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/user_roles', follow_redirects=True)
        self.assertIn(b'You need to login first.', response.data)

    # Ensure that workflow page requires user to signin
    def test_workflow_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/workflow', follow_redirects=True)
        self.assertIn(b'You need to login first.', response.data)

    # Ensure that career_ladders page requires user to signin
    def test_career_ladderse_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/career_ladders', follow_redirects=True)
        self.assertIn(b'You need to login first.', response.data)

    # Ensure that new_role page requires user to signin
    def test_new_role_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/new_role', follow_redirects=True)
        self.assertIn(b'You need to login first.', response.data)

    # Ensure that new_user page requires user to signin
    def test_new_user_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/new_user', follow_redirects=True)
        self.assertIn(b'You need to login first.', response.data)

    # Ensure that logout requires login
    def test_login_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'You need to login first.', response.data)

if __name__ == '__main__':
	unittest.main()

