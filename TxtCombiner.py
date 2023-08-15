file_path1 = 'misc/greeting1.txt'
file_path2 = 'misc/greeting2.txt'

output_path = 'misc/greetingCombine.txt'

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def write_file(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)

def main():
    lines1 = read_file(file_path1)
    lines2 = read_file(file_path2)

    combined_lines = lines1 + lines2
    unique_lines = set(combined_lines)

    write_file(output_path, unique_lines)

if __name__ == "__main__":
    main()