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
    for folder, extension in EXTENSIONS.items():
        if ext in extension:
            return folder
    return "others"

def sort_files(folder_path):
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        if os.path.isfile(full_path):
            dest_folder = get_destination_folder(file)
            dest_path = os.path.join(folder_path, dest_folder)
            
            os.makedirs(dest_path, exist_ok=True)
            
            shutil.move(full_path, os.path.join(dest_path, file))
            print(f"Moved: {file} to {dest_folder}")
            

def main():
    folder_path = input("Enter the path of the folder to organize: ")
    if os.path.isdir(folder_path):
        sort_files(folder_path)
        print("Files have been organized.")
    else:
        print("Invalid folder path. Please try again.")

if __name__ == "__main__":
    main()