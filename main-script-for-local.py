from modules.reader import read_setting, read_template_by_id
from modules.validation import validate_data
from modules.gas_req import requests_to_gas

import sys


if __name__ == "__main__":
    template_id = sys.argv[1]
    if len(sys.argv) > 2:
        custom_code = sys.argv[2]
    else:
        custom_code = 0
    url, user_id, user_pass = read_setting()
    send_json_data = read_template_by_id(template_id, custom_code)
    res = requests_to_gas(url, send_json_data)
    print(res)
