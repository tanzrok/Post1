import web3
import json
import datetime
class Post():
    ganache_url = "HTTP://192.168.43.190:7545"
    privat_key = '5b27b199b4a188a4917280ca8bee1f393183e24e5eae606b1a70b1e9447e23cb'
    with open("abi.json", 'r') as file:
        abi = json.load(file)
    address = web3.Web3.toChecksumAddress('0x39EA753A7ef9C770d6A22cfe4ED4540d864B6b31')
    def __init__(self):
        self.w3 = web3.Web3(web3.HTTPProvider(self.ganache_url))
        self.w3.eth.defaultAccount = self.w3.eth.accounts[0]
        print (self.w3.eth.accounts)
        self.contract = self.w3.eth.contract(
            address=self.address,
            abi=self.abi)

    def reg(self, fam, name, adr, index, passw):
        User = self.w3.personal.newAccount(str(passw))
        print(User)
        nonce = self.w3.eth.getTransactionCount(self.w3.eth.accounts[0])

        tx = {
            'nonce': nonce,
            'to': User,
            'value': self.w3.toWei(2, 'ether'),
            'gas': 2000000,
            'gasPrice': self.w3.toWei('50', 'wei'),
        }

        signed_tx = self.w3.eth.account.signTransaction(tx, self.privat_key)
        tx_hash = self.w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        self.w3.toHex(tx_hash)
        self.w3.eth.defaultAccount=User
        self.w3.personal.unlockAccount(User, passw)
        print (self.w3.eth.defaultAccount)
        print(self.w3.eth.getBalance(self.w3.eth.defaultAccount))
        self.w3.miner.start(1)
        tx_hash = self.contract.functions.Registration(fam, name, adr, int(index)).transact()
        self.w3.eth.waitForTransactionReceipt(tx_hash)
        return User

    def auth(self, user_adr, passw):
        try:
            log = self.w3.personal.unlockAccount(user_adr, passw)
        except Exception:
            log = False
        return log

    def get_user(self, user_address):
        try:
            user_address = web3.Web3.toChecksumAddress(str(user_address))
            log = self.contract.functions.Users(user_address).call()
        except Exception:
            log = False
        return log

    def Set_Admin(self, user_adr):
        try:
            user = web3.Web3.toChecksumAddress(str(user_adr))
            log = self.contract.function.Set_Admin(user_adr).transact()
        except Exception:
            log = False
        return log

    def Delete_Admin(self, user_adr):
        try:
            user_adr = web3.Web3.toChecksumAddress(str(user_adr))
            log = self.contract.function.Delete_Admin(user_adr).transact()
        except Exception:
            log = False
        return log

    def Set_Postman(self, user_adr, post):
        try:
            user_adr = web3.Web3.toChecksumAddress(str(user_adr))
            log = self.contract.function.Set_Postman(user_adr, post).transact()
        except Exception:
            log = False
        return log

    def Delete_Postman(self, user_adr):
        try:
            user_adr = web3.Web3.toChecksumAddress(str(user_adr))
            log = self.contract.function.Delete_Postman(user_adr).transact()
        except Exception:
            log = False
        return log

    def Change_Ofice(self, user_adr, post):
        try:
            user_adr = web3.Web3.toChecksumAddress(str(user_adr))
            log = self.contract.function.Change_Ofice(user_adr, post).transact()
        except Exception:
            log = False
        return log

    def Change_data(self, name, adr,index):
        return self.contract.function.Change_data(str(name), str(adr), int(index)).transact()

    #def Track_Num(self):

    #не уверен над счёт функций
    def get_Weight_check(self,track):
        pack=self.contract.functions.Depart(track).call()
        return pack[7]

    def check_kon_weight(self,track):
        packN=self.contract.functions.Check_inf3(track).call()
        return packN[4]

    def Track_Num(self, sender,recipient):
        tr = []
        tr += self.contract.functions.Track().call()
        print(tr)
        d=str(datetime.date.today().strftime('%d%m%Y'))
        if tr.count(d) == 0:
            self.Track = "MR" + d +"1" + str(sender) + str(recipient)
        else:
            self.Track = "MR" + d + str(tr.count(d)+1) + str(sender) + str(recipient)
        return self.Track

    def Create_Depart(self, sender, ind_sen, recipient, ind_rec,  _type,  _class, value, weight):
        try:
            send = web3.Web3.toChecksumAddress(str(sender))
            rec = web3.Web3.toChecksumAddress(str(recipient))
        except Exception:
            log = False
        else:
            TN=self.Track_Num(ind_sen, ind_rec)
            log = self.contract.functions.Create_departure(self.Track, send, rec, _type, _class, value, weight).call()
        return log

    def info(self, track):
        return self.contract.functions.Check_inf1(track).call()
        return self.contract.functions.Check_inf2(track).call()
        return self.contract.functions.Check_inf3(track).call()

    def transfer(self, adr_rec, sum, day):
        try:
            rec = web3.Web3.toChecksumAddress(str(adr_rec))
            log = self.contract.functions.Create_Transfer(rec, sum, day)
        except Exception:
            log = False
        return log

    def info_tr(self, num):
        return self.contract.functions.Check_Transfer(num).call()

    def Approval_Transfer(self, num):
        return self.contract.functions.Approval_Transfer(num).call()




####190


post = Post()
'''packN=post.check_kon('')
pack=post.Weight_check('')
print(packN[2])
print("weight= ",pack[7])
'''
#user=post.reg('ff', 'aa', 'st', 101000, '123')
#print(user)
#users=post.get_user(post.w3.eth.accounts[1])
#print(users)
#print(post)

