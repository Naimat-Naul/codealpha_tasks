import os
import shutil

def organize_folder(folder_path):
    """Organize files in the folder by type."""
    file_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
        "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
        "Music": [".mp3", ".wav", ".aac", ".flac"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Others": []
    }

    for category in file_categories.keys():
        category_path = os.path.join(folder_path, category)
        os.makedirs(category_path, exist_ok=True)

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        if os.path.isdir(file_path):
            continue
        
        file_extension = os.path.splitext(file_name)[1].lower()
        
        moved = False
        for category, extensions in file_categories.items():
            if file_extension in extensions:
                shutil.move(file_path, os.path.join(folder_path, category, file_name))
                moved = True
                break
        
        if not moved:
            shutil.move(file_path, os.path.join(folder_path, "Others", file_name))

    print(f"Files in {folder_path} have been organized.")

if __name__ == "__main__":
    folder_to_organize = input("Enter the folder path to organize: ").strip()
    if os.path.exists(folder_to_organize):
        organize_folder(folder_to_organize)
    else:
        print("The specified folder does not exist.")
