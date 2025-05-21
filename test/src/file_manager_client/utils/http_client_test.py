from unittest.mock import Mock
import pytest
from src.file_manager_client.utils.http_client import HttpClient


@pytest.mark.parametrize(
    "retrieved_headers, expected_name",
    [
        ({"Content-Disposition": "attachment; filename=report.pdf"}, "report.pdf"),
        ({"Content-Disposition": 'attachment; filename="example.txt"'}, "example.txt"),
        (
            {
                "Content-Disposition": "attachment; filename*=UTF-8''%E2%82%AC%20rates.pdf"
            },
            "€ rates.pdf",
        ),
        (
            {"Content-Disposition": "attachment; filename*=UTF-8''hello%20world.txt"},
            "hello world.txt",
        ),
        (
            {"Content-Disposition": "attachment; filename*=UTF-8''%F0%9F%92%A9.txt"},
            "💩.txt",
        ),
        (
            {
                "Content-Disposition": "attachment; filename=plain.txt; filename*=UTF-8''utf8.txt"
            },
            "utf8.txt",
        ),
        (
            {
                "Content-Disposition": "attachment; filename=cracter-verde.txt; filename*=UTF-8''c%C3%A1racter-verde.txt"
            },
            "cáracter-verde.txt",
        ),
    ],
)
def test_retrieve_filename_from_headers(retrieved_headers, expected_name):
    mock_request = Mock()
    mock_request.headers = retrieved_headers

    client = HttpClient()
    filename = client._get_filename_from_headers(mock_request)
    assert filename == expected_name
