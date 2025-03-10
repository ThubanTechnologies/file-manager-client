from typing import BinaryIO, Union
from .adapter.file_adapter import FileAdapter
from .utils.http_client import HttpClient
from .models.requests import POSTFile, GETFile, PUTFile, DELETEFile
from .models.responses import FileEntity

class FileManagerClient:
    """Simplified client for the file manager."""

    def __init__(self, base_url: str, timeout: int = 30):
        """
        Initialize the client.
        
        Args:
            base_url: Base URL of the service
            timeout: Maximum wait time for requests
        """
        http_client = HttpClient(timeout=timeout)
        self.adapter = FileAdapter(base_url, http_client)

    def upload_file(self, bucket_id: str, directory: str, file: Union[str, BinaryIO]) -> FileEntity:
        """
        Upload a file to the service.
        
        Args:
            bucket_id: Bucket ID
            directory: Target directory
            file: File to upload (can be path or file object)
        """
        if isinstance(file, str):
            with open(file, 'rb') as f:
                request = POSTFile(bucket_id=bucket_id, directory=directory, file=f)
                return self.adapter.save_file(request)
        else:
            request = POSTFile(bucket_id=bucket_id, directory=directory, file=file)
            return self.adapter.save_file(request)

    def get_file(self, bucket_id: str, file_path: str) -> FileEntity:
        """
        Get a file from the service.
        
        Args:
            bucket_id: Bucket ID
            file_path: File path
        """
        request = GETFile(bucket_id=bucket_id, file_path=file_path)
        return self.adapter.get_file(request)
    
    def update_file(self, bucket_id: str, directory: str, file: Union[str, BinaryIO]) -> FileEntity:
        """
        Update a file in the service.
        
        Args:
            bucket_id: Bucket ID
            directory: Target directory
            file: File to update (can be path or file object)
        """
        if isinstance(file, str):
            with open(file, 'rb') as f:
                request = PUTFile(bucket_id=bucket_id, directory=directory, file=f)
                return self.adapter.update_file(request)
        else:
            request = PUTFile(bucket_id=bucket_id, directory=directory, file=file)
            return self.adapter.update_file(request)

    def delete_file(self, bucket_id: str, file_path: str) -> bool:
        """
        Delete a file from the service.
        
        Args:
            bucket_id: Bucket ID
            file_path: File path
        """
        request = DELETEFile(bucket_id=bucket_id, file_path=file_path)
        return self.adapter.delete_file(request)
