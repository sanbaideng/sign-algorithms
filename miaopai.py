import hashlib

# udid参数: android_id+MacAddress+Model+Manufacturer
# android_id：88896b9e25fe8a4c
# MacAddress:32:DF:7A:24:E7:18
# Model:Nexus 6P
# Manufacturer:null
udid=hashlib.md5(b"88896b9e25fe8a4c32:DF:7A:24:E7:18Nexus 6Pnull").hexdigest().upper()

# devId: imei+mac
# imei:867532812546220
# mac:32:DF:7A:24:E7:18
devId=hashlib.md5(b'86753281254622032:DF:7A:24:E7:18').hexdigest().upper()
