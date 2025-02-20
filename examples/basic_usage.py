import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models.responses import FileEntity
from src.client import FileManagerClient
from src.adapter.exceptions import FileManagerAdapterException

def main():

    client = FileManagerClient(base_url="http://your-service-url")

    try:
        # Upload a file using path
        result = client.upload_file(
            bucket_id="my-bucket",
            directory="documents",
            file="./local_file.txt"
        )
        print(f"File uploaded: {result.name}")

        # Get the file
        file: FileEntity = client.get_file(
            bucket_id="my-bucket",
            file_path="documents/local_file.txt"
        )
        print(f"Content: {file.content.decode('utf-8')}")

        # Delete the file
        if client.delete_file("my-bucket", "documents/local_file.txt"):
            print("File deleted successfully")

    except FileManagerAdapterException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
