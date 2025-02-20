# README.md

# File Manager Client

Python client to interact with the file management service.

## Installation

```bash
pip install git+https://github.com/ThubanTech/file-manager-client.git
```

## Basic Usage

```python
from file_manager_client import FileManagerClient

# Initialize client
client = FileManagerClient(base_url="http://your-service-url")

# Upload a file
result = client.upload_file(
    bucket_id="my-bucket",
    directory="documents",
    file="./local_file.txt"
)

# Get a file
file = client.get_file(
    bucket_id="my-bucket",
    file_path="documents/local_file.txt"
)

# Delete a file
client.delete_file("my-bucket", "documents/local_file.txt")
```

## Features

- Simplified file management
- Robust error handling
- Support for file uploads from path or file-like objects
- Configurable timeouts

## Requirements

- Python 3.9+
- requests

## Project Structure

```
file-manager-client/
├── src/
│   ├── adapter/
│   ├── models/
│   ├── utils/
│   └── client.py
├── examples/
│   ├── basic_usage.py
│   └── advanced_usage.py
└── setup.py
```

## Documentation

For detailed examples, check the `examples/` directory.

## Error Handling

The client includes specific exceptions for different cases:

- `FileNotFoundException`
- `FileUploadException`
- `FileUpdateException`
- `FileDeletionException`
