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
def get_short_name(name):
    length = len(name)
    return name[:4] + "..." + name[len(name) - 4: len(name)]
def get_color(degree):
    if degree < 10:
        return "skyblue"
    elif degree < 100:
        return "LemonChiffon"
    else:
        return "pink"
def get_info():
    with open("./data/vertex.json", "r", encoding="utf-8") as f:
        nodes = json.load(f)
        # print(data)
        f.close()
    # data = data.split("\n")[:-1]
    with open("./data/edge.json", "r", encoding="utf-8") as f:
        edges = json.load(f)
        f.close()
    label_list = []
    blocknumber = {}
    for edge in edges:
        if edge["label"] not in label_list and edge["label"] != "null":
            label_list.append(edge["label"])
        if "max" not in blocknumber:
            blocknumber["max"] = edge["blocknumber"]
        else:
            if blocknumber["max"] < edge["blocknumber"]:
                blocknumber["max"] = edge["blocknumber"]
        if "min" not in blocknumber:
            blocknumber["min"] = edge["blocknumber"]
        else:
            if blocknumber["min"] > edge["blocknumber"]:
                blocknumber["min"] = edge["blocknumber"]
    return len(nodes), len(edges), len(label_list) + 1, label_list, blocknumber
def get_all_data(label, bmin, bmax):
    # with open("./media/upload_json/vertex.json", "r", encoding="utf-8") as f:
    #     total_nodes = json.load(f)
    #     # print(data)
    #     f.close()
    # data = data.split("\n")[:-1]
    with open("./data/tx.json", "r", encoding="utf-8") as f:
        total_edges = json.load(f)
        f.close()
    edges = []
    nodes = []
    dic4nodes = {}
    for edge in total_edges:
        flag = False
        if label is None or label == '' or label == 'all' or edge["label"] == label:
            if bmax == -1:
                if edge["blocknumber"] >= bmin:
                    edges.append(edge)
                    flag = True
            else:
                if edge["blocknumber"] >= bmin and edge["blocknumber"] <= bmax:
                    edges.append(edge)
                    flag = True
        if flag:
            if edge["from_account"] not in dic4nodes:
                nodes.append({"id": edge["from_account"], "degree": 1})
                dic4nodes[edge["from_account"]] = len(dic4nodes)
            else:
                nodes[dic4nodes[edge["from_account"]]]["degree"] += 1
            if edge["to_account"] not in dic4nodes:
                nodes.append({"id": edge["to_account"], "degree": 1})
                dic4nodes[edge["to_account"]] = len(dic4nodes)
            else:
                nodes[dic4nodes[edge["to_account"]]]["degree"] += 1
    # print(nodes)
    # for d in data:
    #     edge = {}
    #     key_value_list = d.split(",")
    #     for k_v in key_value_list:
    #         k, v = k_v.replace(" ", '').split(":")
    #         edge[k] = v
    #     edges.append(edge)
    # nodes = []
    # for edge in edges:
    #     if edge["from"] not in dic4nodes:
    #         dic4nodes[edge["from"]] = len(dic4nodes)
    #         nodes.append({"name": edge["from"], "degree": edge["degree"]})
    #     else:
    #             nodes[dic4nodes[edge["from"]]]["degree"] = edge["degree"]
    #     if edge["to"] not in dic4nodes:
    #         dic4nodes[edge["to"]] = len(dic4nodes)
    #         nodes.append({"name": edge["to"], "degree": 0})
        # if edge["to"] not in nodes:
            # nodes.append({edge["to"])
    dic4edges = {}
    # edge_index_list = []
    # for i in range(len(edges)):
    #     edge = edges[i]
    #     if edge["from_account"] not in dic4edges:
    #         dic4edges[edge["from_account"]] = {}
    #     if edge["to_account"] not in dic4edges[edge["from_account"]]:
    #         dic4edges[edge["from_account"]][edge["to_account"]] = i
    #         # edge_index_list.append(i)
    #     else:
    #         index = dic4edges[edge["from_account"]][edge["to_account"]]
    #         edges[index]["value"] = float(edges[index]["value"]) + float(edge["value"])
    # print(edge_index_list)
    # edges = [edges[i] for i in edge_index_list]
    for edge in edges:
        if edge["from_account"] not in dic4edges:
            dic4edges[edge["from_account"]] = {}
        if edge["to_account"] not in dic4edges[edge["from_account"]]:
            dic4edges[edge["from_account"]][edge["to_account"]] = 1
            edge["curve"] = 0.1
        else:
            dic4edges[edge["from_account"]][edge["to_account"]] += 1
            edge["curve"] = 0.1 * dic4edges[edge["from_account"]][edge["to_account"]]
    color = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown"]
    edges = [
        {
        "type":"edge", 
        "source": dic4nodes[edge["from_account"]], 
        "target": dic4nodes[edge["to_account"]],
        "degrees": [nodes[dic4nodes[edge["from_account"]]]["degree"], nodes[dic4nodes[edge["to_account"]]]["degree"]],
        "value": edge["value"],
        "label": edge["label"],
        "total_name":[edge["from_account"], edge["to_account"]],
        "blocknumber": edge["blocknumber"],
        "tx_hash": edge["tx_hash"],
        "symbol": ["", "arrow"], 
        "symbolSize": min(int(nodes[dic4nodes[edge["to_account"]]]["degree"]) + 6, 10), 
        "lineStyle": {"curve": edge["curve"],"color": "#9FA1B8", "opacity": 0.3}} for edge in edges
    ]

    nodes = [
        {
            # "x": node["x"],
            # "y": node["y"],
            "id": dic4nodes[node["id"]],
            "name": get_short_name(node["id"]),
            "total_name": node["id"],
            "type": "node",
            "value": node["degree"],
            # "symbol": "image://./1.png",
            "symbolSize": min(int(node["degree"]) * 10 + 10, 100),
            # "itemStyle": {"normal": {"color": color[random.randrange(0, len(color))]}},
            # "itemStyle": {"normal": {"color": "skyblue"}},
            "itemStyle": {'normal': {'color': get_color(int(node["degree"]))}},
            # "itemStyle": {"normal": {"color": "red", "border-color": "green"}},
            "label": {
                "normal": {
                    "show": True if int(node["degree"]) != 0 else False,
                    "position": 'inside',
                    "color": "black",
                    "fontSize": int(15 * min(int(node["degree"]) * 10 + 10, 100) / 100) 
                }
                }   
        }
        for node in nodes
]
    return nodes, edges
def get_formatter(params):
    if (params.data.type == 'node'):
        return params.data.total_name
    else:
        return 'value: ' + params.data.value.value + '<br>' + 'blocknumber: ' + params.data.value.blocknumber + '<br>' + 'tx_hash: ' + params.data.value.tx_hash 
def get_graph_json(nodes, edges):
    # js_code_str= '''
    #     function(params){
    #         if (params.data.type == 'node') {
    #             return params.data.total_name;
    #         } else {
    #             return 'value: ' + params.data.value.value + '<br>' + 'blocknumber: ' + params.data.value.blocknumber + '<br>' + 'tx_hash: ' + params.data.value.tx_hash;
    #         }
    #     }
    #     '''
    c = (
        Graph()
        .add(
            "",
            nodes,
            edges,
            repulsion=5000,
            symbol="circle",
            # text_opts=opts.TextStyleOpts(font_weight=700),
            # edge_symbol=["", "arrow"]
            label_opts=opts.LabelOpts(font_weight=700, color=""),
            # tooltip_opts=opts.TooltipOpts(formatter=),
        )
    )
    # print(c.dump_options())
    # return c.dump_options()
    json_content = json.loads(c.dump_options())
    json_content["animation"] = False
    json_content["series"][0]["force"]["layoutAnimation"] = False
    # print(json_content["series"][0]["tooltip"])
    return json_content
@check_method('POST')
def search_view(request):
    post = get_post_json(request=request)
    # print(post)
    label2Search = post["label"]
    blockNumberRangeMin, blockNumberRangeMax = 0, -1
    if post["blockNumberRange"][1] is None or post["blockNumberRange"][1] == '':
        blockNumberRangeMax = -1
    else:
        blockNumberRangeMax = post["blockNumberRange"][1]
    if post["blockNumberRange"][0] is None or post["blockNumberRange"][0] == '':
        blockNumberRangeMin = 0
    else:
        blockNumberRangeMin = post["blockNumberRange"][0]
    try:
        blockNumberRangeMin, blockNumberRangeMax = int(blockNumberRangeMin), int(blockNumberRangeMax)
    except:
        code, message = error.json_parse_error()
        return JsonResponse({
            'message': message
        }, status=code)       
    try:
        total_nodes, total_edges = get_all_data(label2Search, blockNumberRangeMin, blockNumberRangeMax)
        json_content = get_graph_json(total_nodes, total_edges)
    except:
        code, message = error.json_parse_error()
        return JsonResponse({
            'message': message
        }, status=code)
    # print(json_content)
    return JsonResponse({
        "message": 'ok',
        "json": json_content,
        "edges": [
            {
                "index": i + 1,
                "source": total_nodes[total_edges[i]["source"]]["total_name"],
                "target": total_nodes[total_edges[i]["target"]]["total_name"],
                "value": total_edges[i]["value"],
                "degrees": total_edges[i]["degrees"],
                "blocknumber": total_edges[i]["blocknumber"],
                "tx_hash": total_edges[i]["tx_hash"],
                "total_name": total_edges[i]["total_name"],
                "label": total_edges[i]["label"]
            } for i in range(len(total_edges))
        ]
    })
@check_method('GET')
def info_view(request):
    try:
        NodeNumber, EdgeNumber, labelNumber, label, blocknumberRange = get_info() 
        return JsonResponse({
            'message':"ok",
            # 'file_path':'static/brand/logo/',
            # 'file_name': "/media/upload_json/" + file_name,
            "NodeNumber": NodeNumber,
            "EdgeNumber": EdgeNumber,
            "labelNumber": labelNumber,
            "label": label,
            "blocknumberRange": {
                "max": blocknumberRange["max"],
                "min": blocknumberRange["min"]
            },
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        })
    except:
        code, message = error.json_parse_error()
        return JsonResponse({
            'message': message
        }, status=code)
@check_method('POST')
def upload_view(request):
    file = request.FILES.get("file")
    file_name = file.name
    base_url = os.path.join(settings.MEDIA_ROOT,'upload_json/')
    file_url = base_url + file_name
    with open(file_url,'wb') as f:
        # 因为图片是在内存中的
        f.write(file.file.read())
    # labelNumber, blocknumberRange = get_info()
    return JsonResponse({
        'message':"ok",
        # 'file_path':'static/brand/logo/',
        'file_name': "/media/upload_json/" + file_name,
    })
class Node:
    def __init__(self, address, jump):
        self.address = address
        self.jump = [jump]
    def add_jump(self, jump):
        if jump not in self.jump:
            self.jump.append(jump)
def get_timeline_data(type_name):
    file_name = "./data/new.txt"
    with open(file_name, encoding="utf-8") as f:
        data = f.read().split("\n")[:-1]
        # print(len(data))
        f.close()
    position = {}
    for i in range(len(data)):
        # print(data)
        info = data[i].split(":")[1].split(",")
        position[i] = {
            "x": float(info[0]),
            "y": float(info[1])
        }
    position_dic = {}
    position_index = 0
    with open("./data/edge.json", "r", encoding="utf-8") as f:
        total_edges = json.load(f)
        f.close()
    edges = []
    for edge in total_edges:
        if edge["label"] == type_name:
            edges.append(edge)
        if edge["from_account"] not in position_dic:
            info = data[position_index].split(":")[1].split(",")
            position_dic[edge["from_account"]] = { "x": float(info[0]), "y": float(info[1])}
            position_index += 1
        if edge["to_account"] not in position_dic:
            info = data[position_index].split(":")[1].split(",")
            position_dic[edge["to_account"]] = { "x": float(info[0]), "y": float(info[1])}
            position_index += 1
    Node_list = []
    dic4NodeList = {}
    max_jump = 0
    min_jump = 100
    if type_name != "Volcano-Model":
        for edge in edges:
            source = edge["from_account"]
            target = edge["to_account"]
            if source not in dic4NodeList:
                dic4NodeList[source] = len(Node_list)
                if target not in dic4NodeList:
                    Node_list.append(Node(source, 1))
                else:
                    jump = Node_list[dic4NodeList[target]].jump[-1] - 1
                    Node_list.append(Node(source, jump))
                    if jump < min_jump:
                        min_jump = jump
            node = Node_list[dic4NodeList[source]]
            edge["phase"] = node.jump[-1]
            if target not in dic4NodeList:
                dic4NodeList[target] = len(Node_list)
                Node_list.append(Node(target, edge["phase"] + 1))
                if edge["phase"] + 1 > max_jump:
                    max_jump = edge["phase"] + 1
        # print(min_jump)
        if min_jump < 1:
            for edge in edges:
                edge["phase"] += (1 - min_jump)
            max_jump += (1 - min_jump)
    # print(max_jump)
    # print([edge["phase"] for edge in edges])
    nodes = []
    dic4nodes = {}
    for edge in edges:
        if edge["from_account"] not in dic4nodes:
            nodes.append({"id": edge["from_account"], "degree": 1})
            dic4nodes[edge["from_account"]] = len(dic4nodes)
        else:
            nodes[dic4nodes[edge["from_account"]]]["degree"] += 1
        if edge["to_account"] not in dic4nodes:
            nodes.append({"id": edge["to_account"], "degree": 1})
            dic4nodes[edge["to_account"]] = len(dic4nodes)
        else:
            nodes[dic4nodes[edge["to_account"]]]["degree"] += 1
    dic4edges = {}
    for edge in edges:
        if edge["from_account"] not in dic4edges:
            dic4edges[edge["from_account"]] = {}
        if edge["to_account"] not in dic4edges[edge["from_account"]]:
            dic4edges[edge["from_account"]][edge["to_account"]] = 1
            edge["curve"] = 0.1
        else:
            dic4edges[edge["from_account"]][edge["to_account"]] += 1
            edge["curve"] = 0.1 * dic4edges[edge["from_account"]][edge["to_account"]]
    # color = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown"]
    edges = [
        {
        "type":"edge", 
        "source": dic4nodes[edge["from_account"]], 
        "target": dic4nodes[edge["to_account"]],
        "degrees": [nodes[dic4nodes[edge["from_account"]]]["degree"], nodes[dic4nodes[edge["to_account"]]]["degree"]],
        "value": edge["value"],
        "label": edge["label"],
        "total_name":[edge["from_account"], edge["to_account"]],
        "blocknumber": edge["blocknumber"],
        "tx_hash": edge["tx_hash"],
        "symbol": ["", "arrow"], 
        "phase": edge["phase"],
        "symbolSize": min(int(nodes[dic4nodes[edge["to_account"]]]["degree"]) + 6, 10), 
        "lineStyle": {"curveness": edge["curve"], "color": "#9FA1B8"}} for edge in edges
    ]

    nodes = [
        {
            "x": position_dic[node["id"]]["x"],
            "y": position_dic[node["id"]]["y"],
            "id": dic4nodes[node["id"]],
            "name": get_short_name(node["id"]),
            "total_name": node["id"],
            "type": "node",
            "value": node["degree"],
            # "opacity": 0.2,
            # "symbol": "image://./1.png",
            # "symbolSize": min(int(node["degree"]) * 10 + 10, 30),
            "symbolSize": (45 + int(node["degree"] / 6)) if (type_name == "laundering" or type_name == "type1") else (20 + int(node["degree"] / 6)),
            # "itemStyle": {"normal": {"color": color[random.randrange(0, len(color))]}},
            # "itemStyle": {"normal": {"color": "skyblue"}},
            "itemStyle": {'normal': {'color': get_color(int(node["degree"])), "opacity": 0.2}},
            # "itemStyle": {"normal": {"color": "red", "border-color": "green"}},
            "label": {
                "normal": {
                    "show": True if int(node["degree"]) != 0 else False,
                    "position": 'inside',
                    "color": "black",
                    "fontSize": int(15 * (20 + int(node["degree"] / 6)) / 50) if (type_name == "laundering" or type_name == "type1") else int(5 * (20 + int(node["degree"] / 6)) / 50)
                }
                }   
        }
        for node in nodes
]
    # for edge in edges:
    #     edge["lineStyle"]["opacity"],flag = get_opacity(phase, edge["phase"])
    #     if flag:
    #         nodes[edge["source"]]["itemStyle"]["normal"]["opacity"] = 1
    #         nodes[edge["target"]]["itemStyle"]["normal"]["opacity"] = 1ed
    # print(nodes)
    return nodes, edges
def get_opacity(phase, edgePhase):
    # if phase in phase_list:
    #     return "1"
    # else:
    #      return "0.4"
    if phase == edgePhase:
        return "0.3", True
    else:
        return "0", False
def get_timeline_json(type_name):
    max_jump = {
        # "type1": 2,
        # "type2": 1,
        # "type3": 2,
        # "type4": 2,
        # "null": 4,
        "Peel-Chain": 6,
        "Coin-Shuffle": 2,
        "Volcano-Model": 4
    }
    nodes, edges = get_timeline_data(type_name=type_name)
    # print(nodes)
    tl = Timeline()
    for i in range(max_jump[type_name]):
            # print(len(nodes), len(edges))
        select_nodes, select_edges = copy.copy(nodes), []
        select_list = []
        for edge in edges:
            if edge["phase"] == (i + 1):
                select_edges.append(edge)
                select_edges[-1]["lineStyle"]["opacity"] = 0.3
                # print(select_list)
                if edge["source"] not in select_list:
                    # select_nodes.append(nodes[edge["source"]])
                    # print(edge["source"])
                    select_list.append(edge["source"])
                    select_nodes[edge["source"]]["itemStyle"]["normal"]["opacity"] = 1
                if edge["target"] not in select_list:
                    # select_nodes.append(nodes[edge["target"]])
                    select_list.append(edge["target"])
                    select_nodes[edge["target"]]["itemStyle"]["normal"]["opacity"] = 1
        # print(len(select_edges), len(select_nodes))
        c = (
            Graph()
            .add(
                "",
                select_nodes,
                select_edges,
                repulsion=500,
                symbol="circle",
                # is_draggable=True,
                layout="none",
                is_roam=False,
                # text_opts=opts.TextStyleOpts(font_weight=700),
                # edge_symbol=["", "arrow"]
                # label_opts=opts.LabelOpts(font_weight=700, color=""),
                # tooltip_opts=opts.TooltipOpts(formatter=),
            )
                # .render("test.html")
            )
        tl.add(c, "第{}阶段".format(i + 1))
        # json_content = json.loads(c.dump_options())
        # json_content["animation"] = False
        # json_content["series"][0]["force"]["layoutAnimation"] = False
    tl.add_schema(is_auto_play=True, play_interval=3000)
    # tl.render("result.html")
    json_content = json.loads(tl.dump_options())
    json_content["baseOption"]["series"][0]["force"]["layoutAnimation"] = False
    for option in json_content["options"]:
        option["series"][0]["layoutAnimation"] = False
    return json_content
@check_method('GET')
def timeline_view(request):
    # try:
        type_name = request.GET.get("type")
        if type_name == '':
            type_name = "Peel-Chain"
        timeline_json = get_timeline_json(type_name=type_name)
        # total_nodes, total_edges = get_all_data('V', 0, -1)
        # timeline_json = get_graph_json(total_nodes, total_edges)
        return JsonResponse({
            "message": 'ok',
            "json": timeline_json
        })
    # except:
    #     code, message = error.json_parse_error()
    #     return JsonResponse({
    #         "message": message
    #     }, status=code)
@check_method('GET')
def overview_view(request):
    type_name = request.GET.get("type")
    filename = './data/' + type_name + '-overview.json'
    with open(filename, "r", encoding="utf-8") as f:
        edges = json.load(f)
        f.close()
    nodes = []
    dic4nodes = {}
    for edge in edges:
        if edge["from_account"] not in dic4nodes:
            nodes.append({"id": edge["from_account"], "degree": 1})
            dic4nodes[edge["from_account"]] = len(dic4nodes)
        else:
            nodes[dic4nodes[edge["from_account"]]]["degree"] += 1
        nodes[dic4nodes[edge["from_account"]]]["label"] = edge["from_account_type"]
        if edge["to_account"] not in dic4nodes:
            nodes.append({"id": edge["to_account"], "degree": 1})
            dic4nodes[edge["to_account"]] = len(dic4nodes)
        else:
            nodes[dic4nodes[edge["to_account"]]]["degree"] += 1
        nodes[dic4nodes[edge["to_account"]]]["label"] = edge["to_account_type"]
    dic4edges = {}
    for edge in edges:
        if edge["from_account"] not in dic4edges:
            dic4edges[edge["from_account"]] = {}
        if edge["to_account"] not in dic4edges[edge["from_account"]]:
            dic4edges[edge["from_account"]][edge["to_account"]] = 1
            edge["curve"] = 0.1
        else:
            dic4edges[edge["from_account"]][edge["to_account"]] += 1
            edge["curve"] = 0.1 * dic4edges[edge["from_account"]][edge["to_account"]]
    color = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown"]
    edges = [
        {
        "type":"edge", 
        "source": dic4nodes[edge["from_account"]], 
        "target": dic4nodes[edge["to_account"]],
        "degrees": [nodes[dic4nodes[edge["from_account"]]]["degree"], nodes[dic4nodes[edge["to_account"]]]["degree"]],
        "value": edge["value"],
        "label": edge["label"],
        "total_name":[edge["from_account"], edge["to_account"]],
        "blocknumber": edge["blocknumber"],
        "tx_hash": edge["tx_hash"],
        "symbol": ["", "arrow"], 
        "symbolSize": min(int(nodes[dic4nodes[edge["to_account"]]]["degree"]) + 6, 10), 
        "lineStyle": {"curve": edge["curve"],"color": "#9FA1B8", "opacity": 0.3}} for edge in edges
    ]

    nodes = [
        {
            # "x": node["x"],
            # "y": node["y"],
            "id": dic4nodes[node["id"]],
            "name": get_short_name(node["id"]),
            "total_name": node["id"],
            "type": "node",
            "value": node["degree"],
            # "symbol": "image://./1.png",
            "symbolSize": min(int(node["degree"]) * 10 + 10, 50),
            # "itemStyle": {"normal": {"color": color[random.randrange(0, len(color))]}},
            # "itemStyle": {"normal": {"color": "skyblue"}},
            "itemStyle": {'normal': {'color': "pink" if node["label"] != "normal" else "skyblue"}},
            # "itemStyle": {"normal": {"color": "red", "border-color": "green"}},
            "label": {
                "normal": {
                    "show": True if int(node["degree"]) != 0 else False,
                    "position": 'inside',
                    "color": "black",
                    "fontSize": int(7 * min(int(node["degree"]) * 10 + 10, 50) / 50) 
                }
                }   
        }
        for node in nodes
]
    c = (
        Graph()
        .add(
            "",
            nodes,
            edges,
            repulsion=1000,
            symbol="circle",
            # text_opts=opts.TextStyleOpts(font_weight=700),
            # edge_symbol=["", "arrow"]
            label_opts=opts.LabelOpts(font_weight=700, color=""),
            # tooltip_opts=opts.TooltipOpts(formatter=),
        )
    )
    # print(c.dump_options())
    # return c.dump_options()
    json_content = json.loads(c.dump_options())
    json_content["animation"] = False
    json_content["series"][0]["force"]["layoutAnimation"] = False
    return JsonResponse({
        'message': 'ok',
        'json': json_content
    })


@check_method('GET')
def aberration_view(request):
    # type_name = request.GET.get("type")
    with open('./data/edge.json', encoding="utf-8") as f:
        transactions = json.load(f)
        f.close()
    # print(type_name)
    aberration = {}
    for transaction in transactions:
        # print(transaction["label"])
        if transaction["label"] not in aberration and transaction["label"] != "null":
            aberration[transaction["label"]] = {"aberration_tx":[], "account": [], "value": 0}
            aberration[transaction["label"]]["aberration_tx"].append(transaction)
            if transaction["from_account"] not in aberration[transaction["label"]]["account"]:
                aberration[transaction["label"]]["account"].append(transaction["from_account"])
            if transaction["to_account"] not in aberration[transaction["label"]]["account"]:
                aberration[transaction["label"]]["account"].append(transaction["to_account"])
            aberration[transaction["label"]]["value"] += float(transaction["value"])
    # print(aberration_tx)
    result =  [{
            "source": aberration[label]["aberration_tx"][0]["from_account"],
            "account": len(aberration[label]["account"]),
            "value": aberration[label]["value"],
            "tx": len(aberration[label]["aberration_tx"]),
            "label": label
        } for label in aberration]
    for i in range(len(result)):
        result[i]["index"] = i
    return JsonResponse({
        "message": 'ok',
        "aberration": result
    }
    )