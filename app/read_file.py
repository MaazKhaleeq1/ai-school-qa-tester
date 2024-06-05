def read_file(file_path):
    # Review:
    # 1. Consider adding error handling for file not found.
    with open(file_path, 'r') as file:
        return file.read()