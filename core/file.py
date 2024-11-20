"""
This module contains utility functions for handling files and directories.

It includes functions for:
- Reading files and returning their content.
- Listing files in directories.
- Opening files in a directory and reading their content.
"""

import os


def read_file(path: str) -> tuple[list[int], int]:
    """Reads a file and returns its content and the number of lines.

    Args:
        path (str): Path to the file.

    Returns:
        tuple[list[int], int]: Tuple with the file content (as integers) and the number of lines.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If a line in the file cannot be converted to an integer.
    """
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Error: The file '{path}' was not found.")

    data = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                data.append(int(line.strip(), 16))
            except ValueError as e:
                raise ValueError(
                    f'Error converting line to integer: {e}'
                ) from e

    return data, len(data)


def list_files_in_dir(path: str) -> list[str]:
    """List all files in a directory.

    Args:
        path (str): Path to the directory.

    Returns:
        list[str]: List with the files in the directory.

    Raises:
        FileNotFoundError: If the directory does not exist.
        OSError: For other errors related to accessing the directory.
    """
    if not os.path.isdir(path):
        raise FileNotFoundError(
            f"Error: The directory '{path}' was not found."
        )

    try:
        return [
            file
            for file in os.listdir(path)
            if os.path.isfile(os.path.join(path, file))
        ]
    except OSError as e:
        raise OSError(f'Error accessing the directory: {e}') from e


def open_files_in_dir(path: str) -> list[dict[str, list[str]]]:
    """Open all files in a directory and return their content.

    Args:
        path (str): Path to the directory.

    Returns:
        list[dict[str, list[str]]]: List with the files' content.

    Raises:
        FileNotFoundError: If the directory does not exist.
        OSError: For other errors related to accessing the directory or files.
    """
    if not os.path.isdir(path):
        raise FileNotFoundError(
            f"Error: The directory '{path}' was not found."
        )

    files_content = []
    try:
        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_data = f.readlines()
                files_content.append(
                    {file_name: [line.strip() for line in file_data]}
                )
    except OSError as e:
        raise OSError(f'Error processing files in the directory: {e}') from e

    return files_content
