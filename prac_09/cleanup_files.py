import shutil
import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))

    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for file in filenames:
            new_name = get_fixed_filename(file)
            print("Renaming {} to {}".format(file, new_name))

            source = os.path.join(directory_name, file)
            new_name = os.path.join(directory_name, get_fixed_filename(file))
            # os.rename(source, new_name)



def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    position = 0
    for char in new_name:
        if char.isupper() and position != 0 and (new_name[position - 1] not in {'_', '('}):
            new_name = new_name[:position] + '_' + new_name[position:]
            position += 1  # Adding an extra character requires moving the position forward too
        if char == '_':
            new_name = new_name[:position+1] + new_name[position+1].upper() + new_name[position+2:]
        position += 1
    return new_name


main()
