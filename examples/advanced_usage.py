import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models.response import FileResponse
from src.adapter.file_adapter import FileAdapter
from src.utils.http_client import HttpClient
from src.models.requests import POSTFile, GETFile, PUTFile, DELETEFile
from src.adapter.exceptions import FileManagerAdapterException
from src.config import config

def main():
    # 1. Initialize HTTP client and adapter
    http_client = HttpClient(timeout=30)
    base_url = config.BASE_URL
    adapter = FileAdapter(base_url, http_client=http_client)

    try:
        # 2. Upload a file
        with open('example.txt', 'rb') as file:
            upload_request = POSTFile(
                bucket_id="my-bucket",
                directory="documents",
                file=file
            )
            result = adapter.save_file(upload_request)
            print(f"File uploaded {result}")

        # 3. Get a file
        get_request = GETFile(
            bucket_id="my-bucket",
            file_path="documents/example.txt"
        )
        file: FileResponse = adapter.get_file(get_request)
        print(f"File content: {file.content}")

        # 4. Update a file
        with open('updated_example.txt', 'rb') as file:
            update_request = PUTFile(
                bucket_id="my-bucket",
                directory="documents/example.txt",
                file=file
            )
            updated_file = adapter.update_file(update_request)
            print(f"File updated: {updated_file}")

        # 5. Delete a file
        delete_request = DELETEFile(
            bucket_id="my-bucket",
            file_path="documents/example.txt"
        )
        if adapter.delete_file(delete_request):
            print("File successfully deleted")

    except FileManagerAdapterException as e:
        print(f"Error handling file: {e}")

if __name__ == "__main__":
    main()
