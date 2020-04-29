import base64
import hashlib

import requests


def generateAuthorization(url):
    v0 = {i.split("=")[0]: i.split("=")[1] for i in url.split("?")[1].split("&")}
    v1 = sorted(v0.items(), key=lambda x: x[0], reverse=False)
    v2 = "93273ef46a0b880faf4466c48f74878f" + "".join([i[0] + "=" + i[1] for i in v1])
    v3 = hashlib.sha1(v2.encode('utf-8')).hexdigest()
    v4 = "20170324_android" + ":" + v3
    v5 = base64.b64encode(v4.encode("utf-8"))
    return v5.decode()


if __name__ == '__main__':
    url = "https://app.api.lianjia.com/newhouse/apisearch?has_filter=0&city_id=440300&from=search_result&from_container=0&page=0&request_ts=1588149231"
    headers = {'Page-Schema': 'newhouse%2Fprojectlist',
               'Cookie': 'lianjia_udid=8650438303586337;lianjia_ssid=b7d73b65-198b-415a-bf92-d80a622b26b8;lianjia_uuid=21d9724e-b9a6-4b57-a5fd-aaeb673bf92f;longitude=124.071753;latitude=33.513853',
               'User-Agent': 'HomeLink9.12.0;samsung SM-G9350; Android 5.1.1',
               'Lianjia-Channel': 'Android_Huawei',
               'Lianjia-Device-Id': '8650438303586337',
               'Device-Info': 'scale=1.2;screenwidth=720;screenheight=1280',
               'Lianjia-City-Id': '440300',
               'Lianjia-Version': '9.12.0',
               'Authorization': generateAuthorization(url),
               'Lianjia-Im-Version': '1.3.3',
               'Lianjia-NH-AB': '',
               'Host': 'app.api.lianjia.com',
               'Connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip'}
    r = requests.get(url, headers=headers, timeout=5)
    print(r.json()["data"]["resblock_list"]["list"][0])
