import json

json_str = '["abc", "\u00e5\u00e4\u00f6", "123"]'

my_list = json.loads(json_str)

for item in my_list:
    print(item)
