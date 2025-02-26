# file-manager-client/README.md

# File Manager Client

This project is a simplified client for a file management service. It allows users to upload, retrieve, and delete files easily through an API.

## Project Structure

- `src/`: Contains the client's source code.
  - `client.py`: Defines the `FileManagerClient` class with methods to interact with the service.
  - `adapter/`: Contains the adapter that handles the service's requests and responses.
  - `utils/`: Contains utilities such as the HTTP client for making requests.
  - `models/`: Defines classes for the service's requests and responses.

## Installation

To install the client, clone the repository and use `setup.py` to install the dependencies:

```bash
git clone https://github.com/ThubanTech/file-manager-client.git
cd file-manager-client
pip install .
```

## Usage

Here is a basic example of how to use the `FileManagerClient`:

```python
from src.client import FileManagerClient

client = FileManagerClient(base_url='https://api.example.com')

# Upload a file
file_entity = client.upload_file(bucket_id='my_bucket', directory='my_directory', file='path/to/file.txt')

# Retrieve a file
file_entity = client.get_file(bucket_id='my_bucket', file_path='my_directory/file.txt')

# Delete a file
success = client.delete_file(bucket_id='my_bucket', file_path='my_directory/file.txt')
```

## Contributions

Contributions are welcome. If you wish to contribute, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
