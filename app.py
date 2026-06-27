"""Unit tests for the Flask application."""

import unittest
from app import app


class TestApp(unittest.TestCase):
    """Test the main application routes."""

    def setUp(self):
        self.client = app.test_client()

    def test_index_route(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        body = response.get_data(as_text=True)
        self.assertIn("CI/CD final project is running", body)

    def test_health_route(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertIn("ok", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
