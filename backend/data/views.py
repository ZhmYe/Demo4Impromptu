from django.http.response import JsonResponse
# from pydantic import Json
from backend import error
from backend.function import check_login, check_method, generate_token, \
    get_username_by_token, get_post_json
import json
from django.conf import settings

# 颜色和label
hacker_list = ["0xngbqzb1kqrlt2shlg2qf9kccpg9suxmp0wwg4q3l", "0xx2zfq2etghz5fk6nd9z23g2gdugmp02fhq2r3s1t", "0xfgv113xtch13o0xxmf6cyyrck4s3znzmpt7vrhkw", "0x6o5v6hnm6rb0v330mwowsvwxpssqw7ry8rrxvt27",
"0xq9165xhiq9zc19syggqid8qorcd0hf4aqg9stbf7", "0xcwy0z29i4ybxwkyu0c18xamyauvgmndh5hivkd6u", "0xu1hdwc6cgr7cnv8xo8dvyvz6e2mwrp3rxtl7z9h5", "0x12toapnwhlkqzddrz2wlsesignw9xkg5pamziuhb",
"0xlg2kqu9f7htvh2ux2dmgbvk1tw3vzkbgzim16wv4", "0x8epddqq2h4421ul1zhfovgg1gy5uamhryqd3dw0x", "0xv2ki4alnx4yb2yenpbz29i1g4l5wdeksefgygnpi",
"0x2imicclza5go3i5486ysxik00rubwft3x5qvdtbo", "0xzrbay9r4h0ig96btyz421cxwwplwuye9hktgcei6", "0x84bz5s4f7ecde5z9rhw36mo9kytz3g2rg4db8wad",
"0xco21vlgq2mtsc0qk64cpuvpbh2kmc074iwy8k7k9", "0xto5zrnn8qgits71gxmmdfl3bggfz8q40inywgs06"
]
cash_list = ["0xv290h0knxrksy39vt3m78rnpvkbeu291wlm23zaq", "0xf1r2wf53o45mqg6empwyy58mdlg559tvbbv969r1"]
def get_label(node_id):
    if node_id in hacker_list:
        return True, "Solana Walker Hacker"
    if node_id in cash_list:
        return True, "Tornado.Cash"
    return False, ""

def get_color(node_id):
    return '#DA5914'

@check_method('POST')
def analyze_view(request):
    with open("./data/position.txt", encoding="utf-8") as f:
        position = f.read().split("\n")
        f.close()
    position_dic = {}
    for line in position:
        info = line.split(" ")
        position_dic[info[0]] = {"x": info[1], "y": info[2]}
    # nodes id
    with open('./data/node.txt', encoding='utf-8') as f:
        nodes = f.read().split("\n")
        f.close()
    # edges
    with open("./data/edge.json") as f:
        edges = json.load(f)
        f.close()
    # 获取度数
    degree_dic = {}
    for edge in edges:
        if edge["source"] not in degree_dic:
            degree_dic[edge["source"]] = 1
        else:
            degree_dic[edge["source"]] += 1
        if edge["target"] not in degree_dic:
            degree_dic[edge["target"]] = 1
        else:
            degree_dic[edge["target"]] += 1
    # 得到nodes
    nodes = [{
                "id": node, 'color': get_color(node), 
                'degree': degree_dic[node],
                'label': 'null', 
                "x": position_dic[node]["x"], 
                "y": position_dic[node]["y"]
            } for node in nodes]
    # 判断是否需要有label，是否需要换图标 具体函数自定义
    for node in nodes:
        have_label, label = get_label(node["id"])
        if have_label:
            node["label"] = label
            # image
            if label == "Solana Walker Hacker":
                node["type"] = "image"
                node["img"] = "https://raw.githubusercontent.com/Liuyushiii/img/master/warning.png"
                node["clipCfg"] = {
                "show": 'true',
                "type": 'circle',
                }
            elif label == "Tornado.Cash":
                node["type"] = "image"
                node["img"] = "https://raw.githubusercontent.com/Liuyushiii/img/master/tornado.png"
                node["clipCfg"] = {
                "show": 'true',
                "type": 'circle',
                }
    return JsonResponse({
        'message': 'ok',
        "nodes": nodes,
        "edges": edges
    })
    