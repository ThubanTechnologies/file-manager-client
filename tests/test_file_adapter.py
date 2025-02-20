import unittest
from unittest.mock import Mock, patch
from src.adapter.file_adapter import FileAdapter
from src.utils.http_client import HttpClient
from src.models.requests import POSTFile, GETFile, PUTFile, DELETEFile
from src.models.responses import FileEntity
from src.adapter.exceptions import FileManagerAdapterException

class TestFileAdapter(unittest.TestCase):
    """Test cases for FileAdapter class."""

    def setUp(self):
        """Set up test environment before each test."""
        self.http_client = Mock(spec=HttpClient)
        self.adapter = FileAdapter("http://test-url", self.http_client)

    @patch('src.adapter.file_adapter.FileEntity')
    def test_save_file_success(self, mock_file_entity):
        """Test successful file upload."""
        file_request = POSTFile(bucket_id="test-bucket", directory="test-dir", file="test-file")
        expected_response = {"name": "test.txt", "size": 100, "content": "test content"}
        self.http_client.post_file.return_value = expected_response
        
        result = self.adapter.save_file(file_request)
        
        self.http_client.post_file.assert_called_once()
        self.assertIsInstance(result, FileEntity)

    def test_get_file(self):
        file_data = GETFile(bucket_id="test_bucket", file_path="test_dir/test_file.txt")
        result = self.adapter.get_file(file_data)
        self.assertIsInstance(result, FileEntity)

    def test_update_file(self):
        file_data = PUTFile(bucket_id="test_bucket", directory="test_dir", file="test_file.txt")
        result = self.adapter.update_file(file_data)
        self.assertIsInstance(result, FileEntity)

    def test_delete_file(self):
        file_data = DELETEFile(bucket_id="test_bucket", file_path="test_dir/test_file.txt")
        result = self.adapter.delete_file(file_data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()