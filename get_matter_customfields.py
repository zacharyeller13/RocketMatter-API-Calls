from itsdangerous import json
import requests
from requests.structures import CaseInsensitiveDict
from csv import DictWriter

def get_matter_custom_fields(MatterID: int) -> dict:
    "Given a rocketmatter MatterID, fetch Matter Custom Fields from their API"
    url = "https://rm33artemis.rocketmatter.net/eller_law/API_V2/Matters.svc/json/GetMatterCustomFields"

    headers = CaseInsensitiveDict()
    headers["Cookie"] = ".ASPXANONYMOUS=PutMtZXO92bkVtqpMAo3J30OIyuN-MnCkIYUQkO_PfTo2XoRz7ubG0yrx9a6Hn2wLVaBVvhdUzb2qZGpUpVgeluaxkL2YLVgvPmoEZKz1f_DeYBF347u4Fd2qHS9DKHvcBgixA2; rm-session=4e554efa-ffec-4c63-a6e8-e165f08949c0; ASP.NET_SessionId=4rf2zhvxxhqnq0mw20yqndmm; .ASPXAUTH=867A38E7876CB6AC542627A83CCB0FF8DBE6F255C610C3FFF0673B56F6685BF605A3DDBF99310793708AD190DA19330A9AB398AE0FA8BA37CFC7148B78FEA8F2C35F14FAEB2F67D4D87AFCAD69D8007218AA9B0E; .ASPROLES=D4_pS9gMfi-Ju-4sNaQuqgPXKCfqhCWRjA2yWlXb8T-n_8JICTK5qXxyMwQcwK2U-8BjsM4cZMRzQOr2fqrfvMOfplP1sam9Jm_eg7EWvieyXakVeEucdOyz7PkHwaTcYLWwMC3HxYGON3QjUmWM2UgTaXXitaOzn0bVzelA2Iu7lIhRKScC_ZPUBR_PRoLXkDaSJMOmfpanStwVWfoMAU8Ag8ltTt6nq990s7SNB_9PGKBa5AwATN4ePjva9JzJR5o2tHrUzpv0z28R3FlFsOR6U_bC0SW8Gv-25ihxpdTqVr6Ep1WEV1W5mWcY9O0h6kKnyiYqZ8keaBg5a_CUFHm0I2r_HfDpHEh1KpRNo96aQYFUnchxnGYegRTWZ5ul6Q9H4x6SpMrzb8tJxpqj2WXugNcKL4lhuvtseb-bwDhAl0h5IDQFporvBBicxzpRJCD725Bf2fBI_s1AIjZ8RIeqtkLrYKikACnqUyk10g-4j1tW0"

    data = f'{{"MatterId": {MatterID}, "Filter": "", "TempCustomFieldValues": [{{}}]}}'

    resp = requests.post(url, headers=headers, data=data)

    print(f"{MatterID}: {resp.status_code}")

    resp.encoding = 'utf-8-sig'

    if resp.status_code != 401:
        resp_data = resp.json()["CustomFields"]

        return resp_data


matters = []

for id in [4314,2979,3426,4310,1554,4313,2905,3564,4317,780,4312,2758,4316]:
    resp_data = get_matter_custom_fields(id)
    if resp_data:
        matters.append(resp_data)

keys = matters[0].keys()

with open("ETB_Matters_Custom_Fields_API.csv", "w", newline='') as out_file:
    dict_writer = DictWriter(out_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(matters)