import hashlib
from urllib import parse
import time
import requests


def getClientHash(imei):
    return str(hashlib.md5(imei.encode()).hexdigest())


if __name__ == '__main__':
    imei = "8675328115463139"
    headers = {"X-Location": "",
               "X-Client-Version": "6.7.2",
               "X-Channel-Code": "lsp-yyb",
               "X-Client-Agent": "Xiaomi_MIX_5.1.1",
               "X-IMSI": "46000",
               "X-Long-Token": "",
               "X-Platform-Version": "5.1.1",
               "X-Client-Hash": getClientHash(imei),
               "X-User-ID": "",
               "X-Platform-Type": "2",
               "X-Client-ID": imei,
               "X-Serial-Num": str(int(time.time())),
               "Host": "app.pearvideo.com",
               "Connection": "Keep-Alive",
               "User-Agent": "okhttp/3.11.0",
               "Accept-Encoding": "gzip, deflate"}
    url = f"http://app.pearvideo.com/clt/jsp/v4/search.jsp?k={parse.quote('超人')}"
    r = requests.get(url, headers=headers)
    print(r.json())
