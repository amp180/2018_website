import unittest
from .app import app

class TestAppLoads(unittest.TestCase):

    def setUp(self):
        self.context = app.requests

    def test_get_homepage(self):
        r = self.context.get('/')
        assert r.ok, f'Homepage should be ok.\n{{r}}'
        assert r.content, f'Homepage should have content.\n{r}'
    
    def test_robots_redirect(self):
        r = self.context.get('/robots.txt')
        assert r.ok, f'Getting robots.txt should be ok.\n{r}'
        assert r.headers['Content-Type'].startswith('text/plain'), f'Getting /robots.txt should return text.\n{r.headers}'

    def test_favicon_redirect(self):
        r = self.context.get('/favicon.ico')
        assert r.ok, f'Getting favicon should be 200 ok. \n {r}'
        assert r.headers['Content-Type'].startswith('image'), f'Favicon should be an icon. \n{r.headers}'

if __name__ == '__main__':
    unittest.main()