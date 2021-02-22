# Parsey Mcparser - 50 (CODE)
```
def ParseNamesByGroup(blob, group_name):
    #impliment code
    blob = blob.split("+++")
    arr = []
    for item in blob:
        item = item.split("[")
        for obj in item:
            if "age" in obj:
                obj = obj.split(",")
                group = obj[2]
                if group_name in group:
                    name = obj[1]
                    name = name.split(":")
                    name = name[1].strip('"')
                    arr.append(name)
    return arr
data = raw_input()
group_name = data.split('|')[0]
blob = data.split('|')[1]
result_names_list = ParseNamesByGroup(blob, group_name)
print result_names_list
```