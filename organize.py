import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.doc', '.docx', '.pdf', '.rtf', '.txt'],
    "AUDIO": ['.mp3', '.wav', '.m4a', '.m4b'],
    "VIDEO": ['.mp4', '.avi', '.mov'],
    "IMAGES" : ['.jpg', '.jpeg', '.png', '.gif']
}

def getDirectory(file_extension):
    for directory, extensions in SUBDIRECTORIES.items():
        for extension in extensions:
            if extension == file_extension:
                return directory


# organizing function
# 1. loop through all files in the directory where the python scrip runs
# 2. if file is a folder, then skip and continue next file
# 3. get the file path
# 4. get file extension for the obtained file path (file name)
# 5. call getDirectory and pass the file extension
# 6. if not returned 'None' (None can be returned if a file type not found in the dictionary), get the directory path
# 7. create the directory if it doesn't exist
# 8. join the file path with the directory path (move file to new folder)

def organizeDirectory():
    for file in os.scandir():
        if file.is_dir():
            continue
        file_path = Path(file)
        file_type = file_path.suffix.lower()
        directory = getDirectory(file_type)
        if directory:
            directory_path = Path(directory)

            if not directory_path.is_dir():
                directory_path.mkdir()
            file_path.rename(directory_path.joinpath(file_path))

organizeDirectory()

