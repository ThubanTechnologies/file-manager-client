from dataclasses import dataclass
from typing import Optional, Any, Dict, Union
from io import BytesIO

@dataclass
class FileResponse:
    """Response model for file operations."""
    content: Union[Dict[str, Any], BytesIO]
    filename: Optional[str] = None
    content_type: Optional[str] = None
    content_length: Optional[int] = None
    is_file: bool = False
