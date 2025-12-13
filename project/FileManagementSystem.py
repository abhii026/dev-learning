import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

def readfileandfolder():
    items = list(BASE_DIR.rglob("*"))
    if not items:
        print("No files found.")
        return
    for i, item in enumerate(items, start=1):
        print(f"{i}: {item.name}")

def createFile():
    try:
        name = input("File name: ").strip()
        p = BASE_DIR / name
        if not p.exists():
            with open(p, "w") as fs:
                data = input("Enter data inside your file: ")
                fs.write(data)
            print("File created successfully.")
        else:
            print("File already exists.")
    except Exception as err:
        print(f"An error occurred as {err}")

def readFile():
    try:
        name = input("Enter file name to read: ").strip()
        p = BASE_DIR / name
        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                print("\n----- File Content -----")
                print(fs.read())
        else:
            print("File does not exist.")
    except Exception as err:
        print(f"An error occurred as {err}")
def updatefile():
    try:
        name = input("Enter file name to update: ").strip()
        p = BASE_DIR / name

        if not p.exists() or not p.is_file():
            print("File does not exist.")
            return

        while True:
            print("\n1. Change file name")
            print("2. Overwrite the data in file")
            print("3. Append data to file")
            print("4. Exit")

            try:
                res = int(input("Select (1 to 4): "))
            except ValueError:
                print("Please enter a number only.")
                continue

            match res:
                case 1:
                    name2 = input("Enter new file name: ").strip()
                    p2 = BASE_DIR / name2

                    if p2.exists():
                        print("File with this name already exists.")
                        continue

                    p.rename(p2)
                    print(f"File renamed from {p.name} to {p2.name}")
                    p = p2

                case 2:
                    with open(p, "w") as fs:
                        data = input("Enter data to overwrite: ")
                        fs.write(data)
                    print("Data overwritten successfully.")

                case 3:
                    with open(p, "a") as fs:
                        data = input("Enter data to append: ")
                        fs.write("\n" + data)
                    print("Data appended successfully.")

                case 4:
                    print("Exiting update menu...")
                    break

                case _:
                    print("Invalid choice")

    except Exception as err:
        print(f"An error occurred as {err}")


def deletefile():
    try:
        name = input("Enter file name to delete: ").strip()
        p = BASE_DIR / name

        if not p.exists():
            print("File does not exist.")
            return

        confirm = input(f"Are you sure you want to delete '{name}'? (Y/N): ").strip().lower()

        if confirm == "y":
            os.remove(p)
            print("File deleted successfully.")
        else:
            print("Delete operation cancelled.")
    except Exception as err:
        print(f"An error occurred as {err}")


while True:
    print("\n1. Press 1 to check existing files")
    print("2. Press 2 for writing")
    print("3. Press 3 for reading")
    print("4. Press 4 for updation")
    print("5. Press 5 for deletion")
    print("6. Press 6 for exit")

    choice = int(input("Select (1-6): "))

    match choice:
        case 1:
            readfileandfolder()
        case 2:
            createFile()
        case 3:
            readFile()
        case 4:
            updatefile()
        case 5:
            deletefile()
        case 6:
            print("Exiting...")
            break
        case _:
            print("Invalid choice")