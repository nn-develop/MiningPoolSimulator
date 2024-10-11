import unittest
from unittest.mock import patch, mock_open
from auth_service import AuthenticationService

class TestAuthenticationService(unittest.TestCase):
    """
    Unit tests for the AuthenticationService class.
    """

    def test_load_authorized_entities_dict(self):
        """
        Test successful loading of authorized entities from a dictionary.
        """
        service = AuthenticationService(data_type="dict", data_source={"entity1": "key1", "entity2": "key2"})
        result = service.load_authorized_entities()
        self.assertTrue(result)
        self.assertEqual(service.authorized_entities, {"entity1": "key1", "entity2": "key2"})

    def test_load_authorized_entities_invalid_dict(self):
        """
        Test failure when data_source is not a dictionary for 'dict' data type.
        """
        service = AuthenticationService(data_type="dict", data_source="not_a_dict")
        with self.assertRaises(ValueError):
            service.load_authorized_entities()

    @patch("builtins.open", new_callable=mock_open, read_data='{"entity1": "key1", "entity2": "key2"}')
    def test_load_authorized_entities_json(self, mock_file):
        """
        Test successful loading of authorized entities from a JSON file.
        """
        service = AuthenticationService(data_type="json", data_source="dummy_path.json")
        result = service.load_authorized_entities()
        self.assertTrue(result)
        self.assertEqual(service.authorized_entities, {"entity1": "key1", "entity2": "key2"})

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_load_authorized_entities_json_file_not_found(self, mock_file):
        """
        Test failure when JSON file is not found.
        """
        service = AuthenticationService(data_type="json", data_source="invalid_path.json")
        with self.assertRaises(ValueError):
            service.load_authorized_entities()

    @patch("builtins.open", new_callable=mock_open, read_data='{"entity1": "key1" "entity2": "key2"}')  # Missing comma
    def test_load_authorized_entities_json_decode_error(self, mock_file):
        """
        Test failure when JSON file contains invalid JSON format.
        """
        service = AuthenticationService(data_type="json", data_source="dummy_path.json")
        with self.assertRaises(ValueError):
            service.load_authorized_entities()

    def test_load_authorized_entities_json_invalid_source(self):
        """
        Test failure when data_source is not a valid file path for 'json' data type.
        """
        service = AuthenticationService(data_type="json", data_source={"entity1": "key1"})
        with self.assertRaises(ValueError):
            service.load_authorized_entities()

    def test_login_successful(self):
        """
        Test successful login with correct entity_id and entity_key.
        """
        service = AuthenticationService(data_type="dict", data_source=None)
        service.authorized_entities = {"entity1": "key1"}  # Manually setting authorized entities
        result = service.login("entity1", "key1")
        self.assertTrue(result)

    def test_login_failed_wrong_key(self):
        """
        Test failed login due to incorrect entity_key.
        """
        service = AuthenticationService(data_type="dict", data_source=None)
        service.authorized_entities = {"entity1": "key1"}  # Manually setting authorized entities
        result = service.login("entity1", "wrong_key")
        self.assertFalse(result)

    def test_login_failed_wrong_id(self):
        """
        Test failed login due to non-existent entity_id.
        """
        service = AuthenticationService(data_type="dict", data_source=None)
        service.authorized_entities = {"entity1": "key1"}  # Manually setting authorized entities
        result = service.login("nonexistent_entity", "key1")
        self.assertFalse(result)

    def test_login_without_loading_entities(self):
        """
        Test failure when attempting to log in without loading authorized entities first.
        """
        service = AuthenticationService(data_type="dict", data_source=None)
        with self.assertRaises(ValueError):
            service.login("entity1", "key1")

if __name__ == "__main__":
    unittest.main()
