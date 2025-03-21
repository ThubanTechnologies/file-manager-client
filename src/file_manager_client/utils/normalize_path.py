def normalize_path(path: str) -> str:
    """
    Normalize a file path by replacing backslashes with forward slashes
    and ensuring it does not start with a slash.
    """
    if not path:
        return path
    normalized = path.replace("\\", "/")
    return normalized.lstrip("/")