from chainwalletSdk.method import WalletClient

client = WalletClient()
client.appId = "20202112233"
client.token = "YnQGCbCurtNuQEDGKbUAXQktH372lbFW"
client.domain = "http://127.0.0.1:8802/finance"

# 获取网络和币的配置表
def test_getChainAndCoin():
    res = client.getChainAndCoin("20202112233", "1")
    print(res)


# 转账
def test_toTransfer():
    res = client.toTransfer("OrderSn-001", "0001", 1, 1, "1", "aabc")
    print(res)


# 获取用户地址
def test_getUserAddress():
    res = client.getUserAddress("104725", 2, 3)
    print(res)

# 获取服务商地址
def test_getHotAddress():
    res = client.getHotAddress(1)
    print(res)

# 获取建议油费地址
def test_suggestGasPrice():
    res = client.suggestGasPrice()
    print(res)

# 获取余额
def test_getBalance():
    res = client.getBalance("TYxpVgdRs7FURtgtX8p4tcRk14z5VAzdX5", 2, 3)
    print(res)

# 查询支持的所有链类型和币类型
def test_getChainAndCoinList():
    res = client.getChainAndCoinList()
    print(res)

# 更新商户
def test_updateMerchant():
    res = client.updateMerchant("", "https://japi.dev.acebetsabo.com/usdtcallback", "http://127.0.0.1", 0)
    print(res)

# 获取商户归集余额
def test_getMerchantCollectBalance():
    res = client.getMerchantCollectBalance("20202112233", "1")
    print(res)

# 获取用户余额
def test_getUserBalance():
    res = client.getUserBalance("20202112233", '104725')
    print(res)

# 获取提币订单详情
def test_getWithdrawOrderInfo():
    res = client.getWithdrawOrderInfo("wdcd4jv5973rhrf6o6bs00")
    print(res)

# 获取提币订单列表
def test_findWithdrawOrderList():
    res = client.findWithdrawOrderList("", "", 0)
    print(res)

# 获取存款订单列表
def test_findDeposOrderList():
    res = client.findDeposOrderList("", "", "")
    print(res)


# 获取收银台地址
def test_getPayment():
    res = client.getPayment("10000", "200", 1, 2, "123321123")
    print(res)

# 查询收银台订单
def test_checkPayment():
    res = client.checkPayment("8cpaycefgk9o48dr1u92957rg")
    print(res)


