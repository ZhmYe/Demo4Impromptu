# from util import *
import json
from tqdm import tqdm
import functools
import math
# 交易
class Transaction:
    def __init__(self, tx_json):
        # print(tx_json)
        self.blockNumber = tx_json["blockNumber"]
        self.hash = tx_json["tx_hash"]
        self.fromAccount = tx_json["source"]
        self.toAccount = tx_json["target"]
        self.value = float(tx_json["value"])
        self.contract = tx_json["contract"]
    def to_json(self):
        return {
            "blockNumber": self.blockNumber,
            "tx_hash": self.hash,
            "target": self.toAccount,
            "source": self.fromAccount,
            "value": self.value,
            "contract": self.contract
        }
# 账户信息，一个地址所涉及的所有转入、转出交易及相关信息
class AccountInfo:
    def __init__(self, address):
        self.address = address
        self.transfer = []
        self.transferOut = []
    def add_transfer(self, transaction:Transaction):
        self.transfer.append(transaction)
    def add_transferOut(self, transaction: Transaction):
        self.transferOut.append(transaction) 
    def get_transfer_number(self):
        return len(self.transfer)
    def get_transferOut_number(self):
        return len(self.transferOut)
    def get_total_transaction_number(self):
        return len(self.transfer) + len(self.transferOut)
    # 按照区块号对账户涉及的转入、转出交易进行聚类
    def cluster_by_blockNumber(self):
        transfer_cluster, transferOut_cluster = {}, {}
        for transaction in self.transfer:
            if transaction.blockNumber not in transfer_cluster:
                transfer_cluster[transaction.blockNumber] = [ transaction ]
            else:
                transfer_cluster[transaction.blockNumber].append(transaction)
        for transaction in self.transferOut:
            if transaction.blockNumber not in transferOut_cluster:
                transferOut_cluster[transaction.blockNumber] = [ transaction ]
            else:
                transferOut_cluster[transaction.blockNumber].append(transaction)
        return transfer_cluster, transferOut_cluster
def get_border_ouput(fill_in):
    return "======================={}=======================".format(fill_in), "======================={}=======================".format(fill_in + " End")
class FilterEngine:
    def __init__(self, time_interval=1000, value_difference=1e18):
        # self.calculater = IntervalChecker(time_interval)
        self.interval = time_interval
        self.valueDifference = value_difference
        self.abnormal = []
        self.abnormal_tx_hash = []
        self.abnormal_account = []
    # 读取交易
    def load_transactions(self, transactions):
        border_output_start, border_output_end = get_border_ouput("Load Transactions")
        print(border_output_start)
        self.transactions = []
        for transaction in tqdm(transactions):
            # print(transaction)
            self.transactions.append(Transaction(transaction))
        print("Load Transaction Number: {}".format(len(self.transactions)))
        print(border_output_end)
    # 获取某一个账户地址涉及的所有转入、转出交易    
    def get_transactions_by_address(self, address):
        border_output_start, border_output_end = get_border_ouput("Filter Transactions by Address")
        print(border_output_start)
        account = AccountInfo(address)
        for transaction in tqdm(self.transactions):
            # fromAccount是该账户，则这笔交易是其转出交易
            if transaction.fromAccount == address:
                account.add_transferOut(transaction)
            # toAccount是该账户，则这笔交易是其转入交易
            if transaction.toAccount == address:
                account.add_transfer(transaction)
        print("{} has {} transactions: {} Transfer, {} TransferOut".format(address, account.get_total_transaction_number(), account.get_transfer_number(), account.get_transferOut_number()))
        print(border_output_end)
        return account
    # 过滤规则：
        # 某一个账户所涉及的转入、转出交易中
        # 若在time_interval内某一批转入交易所涉及的金额，与某一批转出交易所涉及的金额之差不超过value_difference
        # 则认为该账户存在异常，并返回上述交易
    # 检测指定地址
    def filter_by_address(self, address):
        self.abnormal_account.append(address)
        account = self.get_transactions_by_address(address)
        transfer_cluster, transferOut_cluster = account.cluster_by_blockNumber()
        blockNumbers = []
        abnormal = []
        abnormal_account = []
        # 得到转入交易的所有涉及区块号
        for blockNumber in transfer_cluster:
            if int(blockNumber) not in blockNumbers:
                blockNumbers.append(int(blockNumber))
        for blockNumber in transferOut_cluster:
            if int(blockNumber) not in blockNumbers:
                blockNumbers.append(int(blockNumber))
        blockNumbers.sort()
        # blockNumbers = [str(blockNumber) for blockNumber in blockNumbers] # 转换为字符串，方便后续使用
        border_output_start, border_output_end = get_border_ouput("Filter Abnormal Transactions")
        print(border_output_start)
        for blockNumber in blockNumbers:
            transfer_transaction, transferOut_transaction = [], []
            blockNumber_range = [_ for _ in range(blockNumber - self.interval, blockNumber + 1)]
            flag = False # 异常的转出不会在转入之前，所以在转入交易blockNumber存在前，不加入转出交易
            for period in blockNumber_range:
                if period in transfer_cluster:
                    flag = True
                    transfer_transaction.extend(transfer_cluster[period])
                if period in transferOut_cluster and flag: 
                    # 这里保证不会出现一笔转出交易在所有转入交易之前
                    transferOut_transaction.extend(transferOut_cluster[period])
            # print(len(transfer_transaction), len(transferOut_transaction))
            filter_abnormal, filter_account = self.filter(transfer_transaction, transferOut_transaction)
            abnormal.extend(filter_abnormal)
            abnormal_account.extend(filter_account)
        new_abnormal_number = 0
        for transaction in abnormal:
            if transaction["tx_hash"] not in self.abnormal_tx_hash:
                self.abnormal.append(transaction)
                self.abnormal_tx_hash.append(transaction["tx_hash"])
                new_abnormal_number += 1
        print("Filter new Abnormal Transactions: {}".format(new_abnormal_number))
        print(border_output_end)
        for item in abnormal_account:
            if item not in self.abnormal_account:
                self.filter_by_address(item)
    def filter(self, transfer_transaction, transferOut_transaction):
        abnormal_account = []
        abnormal = []
        abnormal_tx_hash = []
        transferOut_total_sum, transfer_total_sum = 0, 0
        # 先统计转出交易的总value
        for transaction in transferOut_transaction:
            transferOut_total_sum += transaction.value
        for transaction in transfer_transaction:
            transfer_total_sum += transaction.value
        # |转入总金额 - 转出总金额| <= valueDifference
        if math.fabs(transferOut_total_sum - transfer_total_sum) <= self.valueDifference:
            # 此时两者全部返回
            for transaction in transfer_transaction:
                if transaction.hash not in abnormal_tx_hash:
                    abnormal_tx_hash.append(transaction.hash)
                    abnormal.append(transaction.to_json())
                    abnormal_account.append(transaction.fromAccount)
            for transaction in transferOut_transaction:
                if transaction.hash not in abnormal_tx_hash:
                    abnormal_tx_hash.append(transaction.hash)
                    abnormal.append(transaction.to_json())
                    abnormal_account.append(transaction.toAccount)
        elif transferOut_total_sum > transfer_total_sum + self.valueDifference:
            # 此时转入交易全部保留
            for transaction in transfer_transaction:
                if transaction.hash not in abnormal_tx_hash:
                    abnormal_tx_hash.append(transaction.hash)
                    abnormal.append(transaction.to_json())
                    abnormal_account.append(transaction.fromAccount)
            # 爬山算法
                # 每次取出转出交易中最大的一笔来覆盖转入交易总额 + self.valueDifference
            # 首先对transferOut_transaction进行逆序排序
            transferOut_transaction.sort(key=functools.cmp_to_key(lambda x, y: x.value - y.value))
            tmpSum = 0
            for transaction in transferOut_transaction:
                tmpSum += transaction.value
                if tmpSum <= transfer_total_sum + self.valueDifference:
                    if transaction.hash not in abnormal_tx_hash:
                        abnormal_tx_hash.append(transaction.hash)
                        abnormal.append(transaction.to_json())
                        abnormal_account.append(transaction.toAccount)
                else:
                    break
        else:
            # 此时转出交易全部保留
            for transaction in transferOut_transaction:
                if transaction.hash not in abnormal_tx_hash:
                    abnormal_tx_hash.append(transaction.hash)
                    abnormal.append(transaction.to_json())
                    abnormal_account.append(transaction.toAccount)
            # 爬山算法
                # 每次取出转入交易中最大的一笔来覆盖转出交易总额 + self.valueDifference
            # 首先对transfer_transaction进行逆序排序
            transfer_transaction.sort(key=functools.cmp_to_key(lambda x, y: y.value - x.value))
            tmpSum = 0
            for transaction in transfer_transaction:
                tmpSum += transaction.value
                if tmpSum <= transferOut_total_sum + self.valueDifference:
                    if transaction.hash not in abnormal_tx_hash:
                        abnormal_tx_hash.append(transaction.hash)
                        abnormal.append(transaction.to_json())
                        abnormal_account.append(transaction.fromAccount)
                else:
                    break
        return abnormal, list(set(abnormal_account))