import requests
from requests.structures import CaseInsensitiveDict
from csv import DictWriter

def get_contact_details(ContactId: int) -> dict:
    "Given a rocketmatter ContactID, fetch ContactData from their API"
    
    url = "https://rm33artemis.rocketmatter.net/eller_law/API_V2/Contacts.svc/json/GetContactData"

    headers = CaseInsensitiveDict()
    headers["Host"] = "rm33artemis.rocketmatter.net"
    headers["Connection"] = "keep-alive"
    headers["Cookie"] = ".ASPXANONYMOUS=gmjXI5nZ0TtbRgbKF1G-gHC45fq9VuXHsgmtBxjtHTyCvdoeEPnXv8ZLPSvSQnCh_Yl1Y9eCEcrOa9Gd1V26tRY1ifnw9LkajSMtA8Mw2iG3Ili-9RXTpU652UeIJR1o2JK7nw2; ASP.NET_SessionId=25szv2fbosvq3jlh5g45u4oo; rm-session=852515a7-cb22-4cef-b233-3be07ee94b4c; .ASPXAUTH=EC1305F35790039447E4550187595A618433276234FA0A8901BEFD9AB52A59AE98A688CFFDD28C9E0D15AF2C60F71363385441DE0A1960805845AE0F659C5084DDC6B30D4D65331F474ECD566BF0A304CFF3D91E; .ASPROLES=jvcYFbKhSv25rB9hQRyzRDHXEjcOlLaSqDstQedHRPEDd5JZaACD7CUMr85VR0MJZBZm_QNODuCyA0lZyK3_SD8hAbbVzmlFdThBZj3dPiZnlPH0FQMmL2VzPtXGPR13s6_v_yo7tT0F1KTx65UW1kqkSLYREAZnmzQJYh2bx-RIOwinDwnmCtkpCf9AXazDmnu1QUcqkeE1AN8uNgI8tCih4VdenOrUgRuSZvXt9A-VxGKx3b2i3EPInQ29SQKvQfGiuRkQDSy_K0KD4tKCn_NyFFakHxC9N0KI_t6MCjdRkaIC78b-toa4uKGpUolWLsX7qXAYX11Fb8ycBIFkyKlPH-n3ToNOHArPnHuXoPVL9WdA_9c-JLxkLlU5a6GzYafwL6qVEswz8gxsLE3niItuSL0eKYI7WkB2NaiacRcWlg_BQfcJZLLuEGqD7DeUPvGPRLSmb-BF6krbIwlvZhNcaXGqQnfN3vdSU-dpZbgIV3c60"
    headers["Content-Type"] = "application/json"

    data = f'{{"ContactId": {ContactId}}}'

    resp = requests.post(url, headers=headers, data=data)

    print(f"{ContactId}: {resp.status_code}")

    resp.encoding = 'utf-8-sig'

    resp_data = resp.json()["Contact"]

    return resp_data

if __name__ == "__main__":
    
    contacts = []

    for i in range(1000):
        resp_data = get_contact_details(i)
        if resp_data:
            contacts.append(resp_data)

    keys = contacts[0].keys()

    with open("ETB_Contacts_API.csv", "w", newline='') as out_file:
        dict_writer = DictWriter(out_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(contacts)

# clusters of 1000

    for i in range(1000, 2000):
        resp_data = get_contact_details(i)
        if resp_data:
            contacts.append(resp_data)

    with open("ETB_Contacts_API.csv", "a", newline='') as out_file:
        dict_writer = DictWriter(out_file, keys)
        dict_writer.writerows(contacts)

    for i in range(2000, 3000):
        resp_data = get_contact_details(i)
        if resp_data:
            contacts.append(resp_data)

    with open("ETB_Contacts_API.csv", "a", newline='') as out_file:
        dict_writer = DictWriter(out_file, keys)
        dict_writer.writerows(contacts)

    for i in range(3000, 4000):
        resp_data = get_contact_details(i)
        if resp_data:
            contacts.append(resp_data)

    with open("ETB_Contacts_API.csv", "a", newline='') as out_file:
        dict_writer = DictWriter(out_file, keys)
        dict_writer.writerows(contacts)

    for i in range(4000, 5000):
        resp_data = get_contact_details(i)
        if resp_data:
            contacts.append(resp_data)

    with open("ETB_Contacts_API.csv", "a", newline='') as out_file:
        dict_writer = DictWriter(out_file, keys)
        dict_writer.writerows(contacts)

    for i in range(5000, 6000):
        resp_data = get_contact_details(i)
        if resp_data:
            contacts.append(resp_data)

    keys = contacts[0].keys()

    with open("ETB_Contacts_API.csv", "a", newline='') as out_file:
        dict_writer = DictWriter(out_file, keys)
        dict_writer.writerows(contacts)

    contacts = []

    for i in range(6000, 7000):
        resp_data = get_contact_details(i)
        if resp_data:
            contacts.append(resp_data)

    keys = contacts[0].keys()

    with open("ETB_Contacts_API.csv", "a", newline='') as out_file:
        dict_writer = DictWriter(out_file, keys)
        dict_writer.writerows(contacts)

    contacts = []

    for i in range(7000, 8049):
        resp_data = get_contact_details(i)
        if resp_data:
            contacts.append(resp_data)

    keys = contacts[0].keys()

    with open("ETB_Contacts_API.csv", "a", newline='') as out_file:
        dict_writer = DictWriter(out_file, keys)
        dict_writer.writerows(contacts)
