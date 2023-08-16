import json

with open('misc/greetingCombine.txt', 'r') as greeting_in_txt:
    lines = greeting_in_txt.readlines()

greeting_data = {}
for line in lines:
    parts = line.strip().split(' ', 1) 
    if len(parts) == 2:
        name, greeting = parts
        greeting_data[name] = greeting

with open('misc/greeting.json', 'w') as greeting_in_json:
    json.dump(greeting_data, greeting_in_json, indent=3)

print(greeting_data)