import argparse
import os


def get_lines(filename):
    with open(filename, 'r') as f:
        line_number = len(f.readlines())
    print("{} has {} lines".format(filename, line_number))
    return line_number


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--suffix", "-s",
                        help="only count files with specific suffix")
    parser.add_argument("base_dir", help="base directory to tranverse")
    args = parser.parse_args()

    total = 0
    max_line_file_name = ""
    max_line_number = -1
    for root, dirs, files in os.walk(args.base_dir):
        for filename in files:
            if not args.suffix or filename.endswith(args.suffix):
                fullname = os.path.join(root, filename)
                line_numbers = get_lines(fullname)
                total += line_numbers
                if line_numbers > max_line_number:
                    max_line_number = line_numbers
                    max_line_file_name = fullname
    if max_line_file_name:
        print("max line file is {} with {} lines".format(max_line_file_name,
                                                         max_line_number))
    print("total lines is {}".format(total))


if __name__ == '__main__':
    main()
