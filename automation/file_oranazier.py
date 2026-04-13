import os 
import shutil

EXTENSIONS ={
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "videos": [".mp4", ".avi", ".mkv"],
    "text": [".txt", ".md"],
    "others": []
}

def get_destination_folder(filename):
    ext = os.path.splitext(filename)[1].lower()
    for folder, extension in EXTENSIONS:
        if ext in extension:
            return folder
    return "others"
