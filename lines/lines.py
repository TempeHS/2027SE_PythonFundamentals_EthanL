import sys
import os


def main():
    # check number of arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    # check file
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    # check file existence
    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    # Counting code line in file, ignoring empty line and notes
    count = 0
    try:
        with open(filename, "r") as file:
            for line in file:
                stripped = line.lstrip()

                # skip empty lines
                if stripped == "" or stripped == "\n":
                    continue

                # Skip notes line
                if stripped.startwith("#"):
                    continue

                count += 1

        print(count)

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
