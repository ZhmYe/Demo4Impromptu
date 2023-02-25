from django.http.response import JsonResponse
# from pydantic import Json
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
import copy
# Create your views here.
# @check_login
with open("./data/tx.json", encoding="utf-8") as f:
    transactions = json.load(f)
    f.close() 
def get_size(jump):
    if jump == 0:
        return 70
    if jump == 1:
        return 30
    if jump == 2:
        return 15
    return 10

@check_method('POST')
def search_view(request):
    params = get_post_json(request=request)
    account, jump, period = params["account"], params["jump"], ""
    nodes, edges = [], []
    up, down = [account], [account]
    nodes.append({"id": str(len(nodes)), "name": account, "label": account, "jump": 0, "size": get_size(0)})
    tmp_up, tmp_down = [], []
    dic4nodes = {account: "0"}
    max_jump = 0
    for i in range(jump):
        flag = False
        for transaction in transactions:
            if transaction["from_account"] in down:
                flag = True
                tmp_down.append(transaction["to_account"])
                edges.append({"source": transaction["from_account"], "target": transaction["to_account"]})
            if transaction["to_account"] in up:
                flag = True
                tmp_up.append(transaction["from_account"])
                edges.append({"source": transaction["from_account"], "target": transaction["to_account"]})
        for account in tmp_up:
            if account not in dic4nodes:
                dic4nodes[account] = str(len(nodes))
                nodes.append({"id": str(len(nodes)), "name": account, "label": account, "jump": i + 1, "size": get_size(i + 1)})
        for account in tmp_down:
            if account not in dic4nodes:
                dic4nodes[account] = str(len(nodes))
                nodes.append({"id": str(len(nodes)), "name": account, "label": account, "jump": i + 1, "size": get_size(i + 1)})
        if flag:
            max_jump = i + 1
        else:
            break
        up = copy.deepcopy(tmp_up)
        down = copy.deepcopy(tmp_down)
    for node in nodes:
        if node["jump"] == max_jump:
            node["isLeaf"] = True
    for edge in edges:
        edge["source"] = dic4nodes[edge["source"]]
        edge["target"] = dic4nodes[edge["target"]]
        edge["style"] = {"startArrow": True}
    return JsonResponse({
        'message': 'ok',
        "nodes": nodes,
        "edges": edges,
        "dic": dic4nodes
    })
    