import json

def read_json(path):
    with open(path, 'r', encoding='UTF-8') as f:
        return json.load(f)

def write_json(path, data):
    with open(path, 'w', encoding='UTF-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def add(path, data):
    d = read_json(path)
    d['users'].append(data)
    write_json('data.json', d)

# with open('data.json', 'r', encoding='UTF-8') as f:
#     d = json.load(f)
# d = read_json('data.json')

newUser = {'id': 5, 'name': 'Test', 'lastname': 'Test'}
add('data.json', newUser)
# d['users'].append(newUser)

# write_json('data_1.json', d)

# for row in d['users']:
#   print(row)

# with open('data_1.json', 'w', encoding='UTF-8') as f:
#     json.dump(d, f, indent=4, ensure_ascii=False)