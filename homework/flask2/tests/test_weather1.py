from unittest import TestCase, main as unittest_main
from app import app
#test /weather


class PlaylistsTests(TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config["Testing"] = True

    def test_weather(self):
        result = self.client.get('/weather?city=Kiev')
        self.assertEqual(result.status, '200 OK')
        page_content = result.get_data(as_text=True)
        self.assertIn("Kiev", page_content)


if __name__ == '__main__':
    unittest.main()
