file_path1 = 'misc/greeting1.txt'
file_path2 = 'misc/greetingcombine.txt'

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def check_lines_in(lines_to_check, combined_lines):
    # Check the existance of the lines of param 1 in param 2
    missing_lines = [line for line in lines_to_check if line not in combined_lines]
    return missing_lines

def main():
    lines_to_check = read_file(file_path1)
    combined_lines = read_file(file_path2)

    missing_lines = check_lines_in(lines_to_check, combined_lines)

    if not missing_lines:
        print(f"All lines in {file_path1} are present in {file_path2}")
    else:
        print(f"The following lines from {file_path1} are missing in {file_path2}:")
        for line in missing_lines:
            print(line.strip())

if __name__ == "__main__":
    main()