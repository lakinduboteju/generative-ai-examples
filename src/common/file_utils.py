def read_file_as_string(file_path: str) -> str:
    with open(file_path, "r") as file:
        file_contents = file.read()
        file.close()
        return file_contents
