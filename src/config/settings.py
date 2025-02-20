from typing import LiteralString

DEFAULT_URL = "http://localhost:5000"
API_URI = "/api"
API_VERSION = "/v1"
BASE_URL: LiteralString = f"{DEFAULT_URL}{API_URI}{API_VERSION}"
FILE_ENDPOINT: LiteralString = f"{BASE_URL}/file"
STRUCTURE_ENDPOINT: LiteralString = f"{BASE_URL}/structure"