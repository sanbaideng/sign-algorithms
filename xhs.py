from urllib import parse
import hashlib


# 听说shield很难。。。

def sign_with_query_items(data):
    udid = data['deviceId']
    # 将请求参数按key排序
    data = {k: data[k] for k in sorted(data.keys())}
    # 拼接成字符串
    data_str = ''
    for k, v in data.items():
        data_str += '{}={}'.format(k, v)
    data_str = parse.quote(data_str, 'utf-8')

    # 将url encode之后的字符串的每个字符与对应的udid字符进行异或原形
    xor_str = ''
    udid_length = len(udid)
    for i in range(len(data_str)):
        data_char = data_str[i]
        udid_index = int(i % udid_length)
        udid_char = udid[udid_index]
        rst = ord(udid_char) ^ ord(data_char)
        xor_str += str(rst)

    # 对异或后的字符串MD5
    md5 = hashlib.md5()
    md5.update(xor_str.encode())
    md5_str = md5.hexdigest()

    # 将MD5后的字符串和udid拼接起来，再次MD5
    md5_str += udid
    md5 = hashlib.md5()
    md5.update(md5_str.encode())
    md5_str = md5.hexdigest()
    return md5_str


if __name__ == '__main__':
    url = "https://www.xiaohongshu.com/api/sns/v10/search/notes?keyword=%E6%96%87%E6%A1%88&filters=%5B%5D&sort=&page=1&page_size=20&source=explore_feed&search_id=487239B01AB4009FA8AD353937A3914E&api_extra=&page_pos=0&allow_rewrite=1&geo=eyJsYXRpdHVkZSI6MzEuMjQ3MTkyLCJsb25naXR1ZGUiOjEyMS40OTIzNzh9%0A&word_request_id=&platform=android&deviceId=7ea97135-ff17-3933-ad75-33016034e452&device_fingerprint=20200429144136d4b0c7363f24a89399c258d1e677152f01065e55be756062&device_fingerprint1=20200429144136d4b0c7363f24a89399c258d1e677152f01065e55be756062&versionName=6.43.0&channel=YingYongBao&sid=session.1588142578377100130509&lang=zh-Hans&t=1588142699&fid=158814249010ee29247568ec9d1a36707a0b9583ce0b"
    params = {
        "deviceId": "7ea97135-ff17-3933-ad75-33016034e452",
        "device_fingerprint": "20200429144136d4b0c7363f24a89399c258d1e677152f01065e55be756062",
        "device_fingerprint1": "20200429144136d4b0c7363f24a89399c258d1e677152f01065e55be756062",
        "fid": "158814249010ee29247568ec9d1a36707a0b9583ce0b",
        "lang": "zh-Hans",
        "page": "1",
        "page_pos": "0",
        "page_size": "20",
        "platform": "android",
        "sid": "session.1588142578377100130509",
        "sort": "",
        "source": "explore_feed",
        "t": "1588142699"
    }
    print(sign_with_query_items(params))
