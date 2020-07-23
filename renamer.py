# Get those imports
import os

def main():
    # Get file details
    suffix = 0
    path = input("Enter the folder in which you'd like files to be renamed: ")
    fileType = input("Enter the filetype of the images: ")
    # Loopy loop
    for fileName in os.listdir(path):
        source = path + fileName
        destination = path + "renamer" + str(suffix) + "." + fileType

        # Change the name
        os.rename(source,destination)

        suffix+=1

if __name__ == '__main__':
    main()