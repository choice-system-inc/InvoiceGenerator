import json
import importlib

def read_setting():
    # url
    with open('./setting/url.ini', "r", encoding="utf-8") as read:
        el = read.readlines()
    url = str(el[0]).strip()
    # id and pass
    with open('./setting/pass.ini', "r", encoding="utf-8") as read:
        json_data = json.load(read)
    user_id = str(list(json_data.keys())[0])
    password = json_data[user_id]
    return url, user_id, password

def read_template_by_id(id, custom_code):
    with open('./data-templates/' + str(id) + '.json', "r", encoding="utf-8") as read:
        json_data = json.load(read)
    if int(custom_code) > 0:
        pre_title = json_data["title"]
        base_title = str(pre_title).split('@@@')
        base_title.insert(1, " " + str(custom_code))
        new_title = "".join(base_title)
        json_data["title"] = new_title
    return json_data