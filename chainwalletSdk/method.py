from chainwalletSdk.utils import makeToken
import requests


class WalletClient():
    appId = ""
    token = ""
    domain = ""

    def doPost(self, path, param):
        secret = makeToken(appId=self.appId, token=self.token, param=param)
        headers = {
            "App": self.appId,
            "Access-Token": secret
        }
        res = requests.post(self.domain + path, json=param, headers=headers).json()
        if res['code'] != '0':
            raise Exception(res['msg'])

        return res['data']

    def getChainAndCoin(self, appId, merchantId):
        res = self.doPost("/chain_coin", {
            "app_id": appId,
            "merchant_id": merchantId
        })
        return res

    def toTransfer(self, order, uid, chain_type, coin_type, amount, to_addr):
        res = self.doPost("/transfer", {
            "order": order,
            "uid": uid,
            "chain_type": chain_type,
            "coin_type": coin_type,
            "amount": amount,
            "to_addr": to_addr
        })
        return res

    def getUserAddress(self, uid, chain_type, coin_type):
        res = self.doPost("/getAddress", {
            "uid": uid,
            "chain_type": chain_type,
            "coin_type": coin_type
        })
        return res

    def getHotAddress(self, chain_type):
        res = self.doPost("/getHotAddress", {
            "chain_type": chain_type
        })
        return res

    def suggestGasPrice(self):
        res = self.doPost("/suggestGasPrice", {})
        return res

    def getBalance(self, addr, chain_type, coin_type):
        res = self.doPost("/balance", {
            "addr": addr,
            "chain_type": chain_type,
            "coin_type": coin_type
        })
        return res

    def updateMerchant(self, merchant_name, callback_url, ip_whites, ip_white_open):
        res = self.doPost("/update/merchant", {
            "merchant_name": merchant_name,
            "callback_url": callback_url,
            "ip_whites": ip_whites,
            "ip_white_open": ip_white_open
        })
        return res

    def getMerchantCollectBalance(self, app_id, merchant_id):
        res = self.doPost("/getMerchantCollectBalance", {
            "app_id": app_id,
            "merchant_id": merchant_id
        })
        return res

    def getUserBalance(self, app_id, merchant_id, uid):
        res = self.doPost("/getUserBalance", {
            "app_id": app_id,
            "merchant_id": merchant_id,
            "uid": uid
        })
        return res

    def getWithdrawOrderInfo(self, order_no):
        res = self.doPost("/getWithdrawOrderInfo", {
            "order_no": order_no
        })
        return res

    def findWithdrawOrderList(self, start_date, end_date, transfer_type):
        res = self.doPost("/findWithdrawOrderList", {
            "start_date": start_date,
            "end_date": end_date,
            "transfer_type": transfer_type
        })
        return res

    def findDeposOrderList(self, start_date, end_date, transfer_type):
        res = self.doPost("/findDeposOrderList", {
            "start_date": start_date,
            "end_date": end_date,
            "transfer_type": transfer_type
        })
        return res

    def getChainAndCoinList(self):
        res = self.doPost("/getChainAndCoinList", {})
        return res

    def getPayment(self, uid, amount, chain_type, coin_type, order_no):
        res = self.doPost("/depos", {
            "uid": uid,
            "amount": amount,
            "chain_type": chain_type,
            "coin_type": coin_type,
            "order_no": order_no,
        })
        return res

    def checkPayment(self, plat_no):
        res = self.doPost("/checkPayment", {
            "plat_no": plat_no,
        })
        return res
