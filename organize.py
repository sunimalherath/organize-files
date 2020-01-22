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


print(getDirectory('.doc'))
