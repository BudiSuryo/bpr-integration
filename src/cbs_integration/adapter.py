class CBSAdapter:
    def get_balance(self, account_number):
        return 1000000
    def create_transaction(self, data):
        return {'transaction_id':'TX123','status':'pending','data':data}