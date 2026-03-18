"""Module providing a function organizing files to categorized folders"""

import os
import shutil
import json

categories = {
        "Images": [".jpg",".jpeg",".png",".gif",".webp",".svg",".bmp"],
        "Documents": [".pdf",".docx",".doc",".txt",".xlsx",".csv",".pptx"],
        "Videos": [".mp4",".mov",".avi",".mkv",".wmv"],
        "Audio": [".mp3",".wav",".flac",".aac",".ogg"],
        "Archives": [".zip",".tar",".gz",".rar",".7z"],
        "Code": [".py",".js",".html",".css",".json",".ts",".sh"],
        }

def get_category(filename):
    """Returns the category of the given file

    Parameters:
    filename (str): file name

    Returns:
    str: category

    """
    ext = os.path.splitext(filename)[1].lower()

    for c,e in categories.items():
        if ext in e:
            return c

    return "Misc"

def scan_folder(folder_path):
    """Scans the given folder and organizes the files to their respective category

    Parameters:
    folder_path (str): path to organize files
    """
    entries = []
    for f in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path,f)):
            dest_folder=os.path.join(folder_path,get_category(f))

            os.makedirs(dest_folder, exist_ok=True)

            counter=1
            name, ext = os.path.splitext(f)
            f_name=f
            while os.path.exists(os.path.join(dest_folder,f_name)):
                f_name = name + "_" + str(counter) + ext
                counter+=1

            shutil.move(os.path.join(folder_path,f),os.path.join(dest_folder,f_name))
            entries.append({
                "from":os.path.join(folder_path,f),
                "to":os.path.join(dest_folder,f_name)
            })

            print("Moving:"+f+" → "+os.path.join(dest_folder,f_name))

    write_undo_log(entries)
    print("Done! " + str(len(entries)) + " files organized.")

def write_undo_log(entries):
    """Writes to undo log for undo actions in JSON format

    Parameters:
    entries (dict): move actions formatted as {"from":src,"to":dest}
    """
    with open('undo_log.json', 'w', encoding='utf-8') as f:
        json.dump(entries,f)

def undo():
    """Undoes actions performed in undo_log.json"""
    if os.path.exists("undo_log.json"):
        with open('undo_log.json', 'r', encoding='utf-8') as f:
            e = json.load(f)
            for a in reversed(e):
                if not os.path.exists(a['to']):
                    print("Warning: file not found, skipping: ",a['to'])
                else:
                    shutil.move(a['to'],a['from'])
                    print("Undoing: ",a['to']," → ",a['from'])

        os.remove("undo_log.json")
        print("Undo complete. ",str(len(e))," files restored.")
    else:
        print("No undo log found.")

def dry_run(folder_path):
    """Scans the given folder and verbally organizes the files to their respective category

    Parameters:
    folder_path (str): path to organize files
    """
    count = 0
    for f in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path,f)):
            dest_folder=os.path.join(folder_path,get_category(f))

            print("[DRY RUN] Moving:"+f+" → "+os.path.join(dest_folder,f))

            count+=1
    print("[DRY RUN] ",str(count)," files would be moved.")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Organize files into categorized subfolders")
    parser.add_argument("folder", help="Path to the folder to organize")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--undo", action="store_true")
    args = parser.parse_args()

    if args.undo:
        undo()
    elif args.dry_run:
        dry_run(args.folder)
    else:
        scan_folder(args.folder)
