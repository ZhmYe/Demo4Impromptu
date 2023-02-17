from django.http.response import JsonResponse
from pydantic import Json
from backend import error
from backend.function import check_login, check_method, generate_token, \
    get_username_by_token, get_post_json
from pyecharts.commons.utils import JsCode
import json
import pyecharts.options as opts
from pyecharts.charts import Graph, Timeline
import random
import os
from django.conf import settings
import time
with open('./data/tx.json', encoding="utf-8") as f:
    transactions = json.load(f)
    f.close()
type_dic = {}
for i in range(len(transactions)):
    type_dic[transactions[i]["label"]] = i
def get_short_name(name):
    length = len(name)
    return name[:9] + "..." + name[len(name) - 9: len(name)]
@check_method('GET')
def defaultTx_view(request):
    select_transaction = transactions[:8]
    return JsonResponse({
        'message': 'ok',
        "transactions": [{
            "from_account": get_short_name(transaction["from_account"]),
            "to_account": get_short_name(transaction["to_account"]),
            "tx_hash": get_short_name(transaction["tx_hash"]),
            "timeStamp": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        } for transaction in select_transaction]
    })
@check_method("GET")
def transaction_view(request):
    index = int(request.GET.get('index'))
    if (index >= len(transactions)):
        index = index % len(transactions)
    # print(blockNumber)
    # result = []
    # for transaction in transactions:
        # if str(transaction["blocknumber"]) == str(blockNumber):
            # result.append(transaction)
    flag = False
    result = ''
    for type_name in type_dic:
        if type_dic[type_name] == index and type_name != 'null':
            flag = True
            result = type_name
            break
    return JsonResponse({
        "message": 'ok',
        "transaction": {
            "from_account": get_short_name(transactions[index]["from_account"]),
            "to_account": get_short_name(transactions[index]["to_account"]),
            "tx_hash": get_short_name(transactions[index]["tx_hash"]),
            "timeStamp": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        },
        "flag": flag,
        "result":  result
    })
@check_method('GET')
def aberration_view(request):
    type_name = request.GET.get("type")
    # print(type_name)
    aberration_tx = []
    account = []
    value = 0
    for transaction in transactions:
        # print(transaction["label"])
        if transaction["label"] == type_name:
            aberration_tx.append(transaction)
            if transaction["from_account"] not in account:
                account.append(transaction["from_account"])
            if transaction["to_account"] not in account:
                account.append(transaction["to_account"])
            value += float(transaction["value"])
    # print(aberration_tx)
    source = aberration_tx[0]["from_account"]
    return JsonResponse({
        "message": 'ok',
        "source": source,
        "account": len(account),
        "value": value,
        "tx": len(aberration_tx),
        "label": type_name
    })