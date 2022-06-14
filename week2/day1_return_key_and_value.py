def key_value_pairs(v: dict):
    for key, value in v.items():
        print(f"{key} is the key and {value} is the value")
        
print(key_value_pairs({'name':'yusuff', 'age':10}))