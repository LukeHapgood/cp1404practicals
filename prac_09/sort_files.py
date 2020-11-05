import shutil
import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))

    os.chdir('FilesToSort')
    for directory_name, subdirectories, filenames in os.walk('.'):

        for file in filenames:
            position = 0
            for char in file:
                if char == '.':
                    subdirectory = file[position + 1:]
                position += 1
            try:
                os.mkdir(subdirectory)
            except FileExistsError:
                pass
            shutil.move(file, subdirectory)

main()