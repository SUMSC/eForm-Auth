import time
import hashlib


def checkMyauth(id_tag: str, secret: str, clienttime: str, passwd: str) -> bool:
    systemtime = int(time.time())  # 10位Unix时间戳，秒级
    if int(systemtime) - int(clienttime) > 60 * 60:
        return False
    secret1 = hashlib.md5()
    secret1.update((id_tag + passwd + clienttime).encode('utf8'))
    # print("mysecret:{}".format(secret1.hexdigest()))
    if secret1.hexdigest() == secret:
        return True
    return False
