from urllib import parse
import time
import hashlib
import requests

# 在com.meitu.secret.SigEntity调用native方法

def gen_sig(url, sigtime):
    url = parse.unquote(url)
    v1 = [i.split("=")[1] for i in url.split("&") if "sig" not in i]
    v1.sort()
    v0 = url.split("?")[0].split("com/")[1]
    vr = v0 + "".join(v1).replace("+", " ") + "bdaefd747c7d594f" + str(sigtime) + "Tw5AY783H@EU3#XC"
    sig = encrypt(vr)
    return url + "&sig=" + sig + "&sigVersion=1.3" + "&&sigTime=" + str(sigtime)


def encrypt(v0):
    v1 = hashlib.new('md5', v0.encode()).hexdigest()
    v2 = v1[1::2]
    v3 = v1[::2]
    return "".join(i + j for i, j in zip(v2, v3))


if __name__ == '__main__':
    headers = {
        "Ab-Version": "4.6.1",
        "Host": "api.meipai.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.12.1"
    }
    page = 10
    keyword = parse.quote("超人")
    client_id = 1089857302
    device_id = 867981021260088
    model = "Nexus 6P"
    imei = 867981021260088
    mac = parse.quote("00:00:00:00:00:00")
    stat_gid = 2191069366
    android_id = "88896b9e25fe8aaa5"
    local_time = int(time.time() * 1000)
    sigTime = local_time + 254
    url = f"https://api.meipai.com/search/user_mv.json?count=30&page={page}&order_by=0&type=0&q={keyword}&source=history&source_page=1&with_banner=1&language=zh-Hans&client_id={client_id}&device_id={device_id}&version=8595&channel=taobao&model={model}&os=7.1.2&origin_channel=taobao&imei={imei}&mac={mac}&stat_gid=2191069354&android_id={android_id}&local_time={local_time}&network=wifi&resolution=1920*1080&teenager_status=0"
    url = gen_sig(url, sigTime)
    r = requests.get(url, headers=headers)
    print(r.json()["mv"][0])
