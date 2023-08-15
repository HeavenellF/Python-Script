file_path_combine = 'misc/greetingCombine.txt'

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def find_duplicate_names(lines):
    name_greeting_dict = {}
    duplicates = {}

    for line in lines:
        parts = line.strip().split()
        if len(parts) >= 2:
            name = parts[0]
            greeting = ' '.join(parts[1:])
            if name in name_greeting_dict:
                if name_greeting_dict[name] != greeting:
                    duplicates.setdefault(name, []).append(name_greeting_dict[name])
                    duplicates[name].append(greeting)
            else:
                name_greeting_dict[name] = greeting

    return duplicates

def main():
    combined_lines = read_file(file_path_combine)
    duplicate_names = find_duplicate_names(combined_lines)

    if not duplicate_names:
        print("No duplicate names with different greetings found.")
    else:
        print("Duplicate names with different greetings:")
        for name, greetings in duplicate_names.items():
            print(f"{name}: {', '.join(greetings)}")

if __name__ == "__main__":
    main()