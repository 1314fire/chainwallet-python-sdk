import hashlib

def makeToken(appId, token, param):
    param = dict(param)
    paramKeys = sorted(param)
    paramArray = []
    paramArray.append(appId)
    paramArray.append(token)
    for key in paramKeys:
        paramArray.append(key + "=" + str(param[key]))
    if len(paramKeys) == 0:
        paramArray.append("")
    paramStr = "&".join(paramArray)
    return hashlib.md5(paramStr.encode()).hexdigest()