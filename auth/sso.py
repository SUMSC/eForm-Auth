import time
import hashlib


def checkMyauth(id_tag: str, secret: str, clienttime: str, passwd: str) -> bool:
    systemtime = int(time.time())  # 10位Unix时间戳，秒级
    if int(systemtime) - int(clienttime) > 60 * 60:
        return False
    secret1 = hashlib.md5()
    secret1.update((str(id_tag) + str(passwd) + str(clienttime)).encode('utf8'))
    print("mysecret:{}".format(secret1.hexdigest()))
    print("secret1:", secret1.hexdigest(), " secret2: ", secret)
    if secret1.hexdigest() == secret:
        return True
    return True
