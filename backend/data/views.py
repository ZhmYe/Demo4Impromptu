from django.http.response import JsonResponse
# from pydantic import Json
from backend import error
from backend.function import check_login, check_method, generate_token, \
    get_username_by_token, get_post_json
import json
from django.conf import settings
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
# 颜色和label

hacker_list = [
    "0xc611952d81e4ecbd17c8f963123dec5d7bce1c27",
    "0xbfa93e1067ebabdc6b648ff7bdc45602fd37b61a",
    "0xpzbn6l6oymcw155mxgrr6wuioyvu5koig1it59s0",
    "0xa16f139337836df3458652cce7776a4994dba719",
    "0x15cc46e874d7d8b9c1535f0f7e5f719b63f22d54",
    "0xlldgwd2y1glpv8x0vq7vlad63grqnbbqbt649z25",
    "0x9b8dda29d117d794fb7c5efe25bf764a022d40d2",
    "0x8epddqq2h4421ul1zhfovgg1gy5uamhryqd3dw0x",
    "0xv2ki4alnx4yb2yenpbz29i1g4l5wdeksefgygnpi",
    "0xd90e2f925da726b50c4ed8d0fb90ad053324f31b",
    "0xc55d12edf3502ed4847f1328e1d66b0e3f6b492f",
    "0xa16f139337836Df3458652CcE7776a4994dba719",
    "0xg48y58ocz4o00qzat8ugqywqr7v6ghxrsfxyzo7o",
    "0x1e76cpsd57tgo2nfqr3osko0c88rh29zm0ffl4fq",
    "0x13Ebe7F59E87fE12850c26eAf27812736104d3F9"
]

hacker_list_label = [
    "0xc611952d81e4ecbd17c8f963123dec5d7bce1c27",
    "0x9b8dda29d117d794fb7c5efe25bf764a022d40d2"
]

compromised_account_list = [
    "0x8bc90377daf1b4e71686d025c88b2178089cf3e8",
    "0x1a26db1b2baf0b23f18e19375e8fdc159feb707e",
    "0x43da6d2db9651b7042e31ffb2607a7cfa4d5d03b",
    "0x47537db3dfec13e9f20fb4f4cd0cf26e2cc37fdd",
    "0xe5c04c954c5494f6975f63e3f19957a380648f82",
    "0x795d8f8b2bf1bb23e99e165c8e4fa067d96cb00a",
    "0x1e29e2cefd3395d892678add3eb791ed74114f3b",
    "0x75cd2467f8dd731a5acb927bd79c4cb361210db6",
    "0xbdf4cf8269c3883dd88975e1978a6aa9d3877f2e",
    "0x4842336fdaf0405e12c7e968dc1998856672a4d7",
    "0x6e8b6af9d8b402d89d1f5d8c1cf535850dc28b98",
    "0xa789d472cfef01e09674e4a6c03b35c72e0bfdb0",
    "0x74de5d4fcbf63e00296fd95d33236b9794016631",
    "0x72433e5b7a34b7c3235c9fbaef1ef1ae9f0c9f5a",
    "0x8yplfwimnnygisxb07zpqw7ht3wgimg32h2hsdcp",
    "0xo8rzggrfguipne1xk98zb4s30qrd3bdm8yuehel2",
    "0xco21vlgq2mtsc0qk64cpuvpbh2kmc074iwy8k7k9",
    "0x8b3468d420fc59034e4e84afa8ef847d3c9b2932",
    "0xg2p5nrshiyrwgl8w27hvp282gk07a5yfm8ltq28p"
]

usdt_list = [
    "0x8cc6df6fbd4f9fcce78261decea12614df3017646e53167173fe894ba726341f",
    "0x123c0b2f9073460aa25d6a878ac64addc753eeb055ff164933873d2b0399f8d60",
    "0xb13d10c552402b5c9db2a44ccd35277431d84b7bd1a9513ec75f9ac2ab1d3ecc",
    "0xeb2d1da9a194cc627a56e8fc9e386c8d2fa64733e382b397a7ce36f59debdfd9"
]

def get_label(node_id):
    # if node_id in hacker_list_with_label:
    #     return True, "Hacker Wallet"
    # if node_id in cash_list:
    #     return True, "Tornado.Cash"
    return False, ""

def get_color(node_id):
    return '#00BFFF'

def get_size(degree):
    default_node_size = 10
    if degree == 1:
        return default_node_size + 5 * int(degree)
    return default_node_size + 2 * int(degree)

def get_suffix(tx_hash):
    if tx_hash in usdt_list:
        return 'USDT'
    else:
        return "ETH"
    
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
        # 配置label
        edge["label"] = edge["value"] + ' ' + get_suffix(edge["tx_hash"])
        edge["labelCfg"] = {
            "refY": 5,
            "style" : {
                "fontSize" : 6,
                "fontWeight" : 700
            }
        }
        # edge["style"] = {
        #     "endArrow": {
        #         "path": "G6.Arrow.triangle(10, 20, 25)",
        #         "d": 25
        #     }
        # }
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
        node["style"]  = {
            "fill": node["color"],
        }
        node["labelCfg"]={
            "style":{
              "fontSize": 10,
              "fontWeight": 800
            }
          }
        node["size"] = get_size(node["degree"])
        if node["id"] in hacker_list:
            node["style"] = {
                "fill": "#D40202",
                "lineWidth": 0
            }
            node["icon"] = {
                "show": True,
                "img": "https://raw.githubusercontent.com/Liuyushiii/img/master/inner_warning.png",
                "width": node["size"] * 0.8,
                "height": node["size"] * 0.8
            }
        if node["id"] in compromised_account_list:
            node["icon"] = {
                "show": True,
                "img": "https://raw.githubusercontent.com/Liuyushiii/img/master/wallet4.png",
                "width": node["size"] * 0.8,
                "height": node["size"] * 0.8
            }
        if node["id"] in hacker_list_label:
            id = node["id"]
            firstChars = id[:5]
            lastChars = id[-3:]
            node["label"] = firstChars + '...' + lastChars
            node["labelCfg"] = {
                "position": "bottom",
                "offset": 5,
                "style" : {
                    "fontSize": 10,
                    "fontWeight": 700
                }
            }                
    return JsonResponse({
        'message': 'ok',
        "nodes": nodes,
        "edges": edges
    })
@check_method('POST')
def overview_view(request):
    with open("./data/overview-nodes.json", encoding="utf-8") as f:
        nodes = json.load(f)
        f.close()
    with open("./data/overview-edges.json", encoding="utf-8") as f:
        edges = json.load(f)
        f.close()
    degree = {"1-5": 0, "6-10": 0, ">10" : 0}
    
    
    
    def get_size_overview(node_degree, base):
        if node_degree <= 10:
            return base * node_degree
        else:
            return base * 10 + get_size_overview(node_degree - 10, base/2)

    
    for node in nodes:
        node["size"] = 10 + get_size_overview(node["degree"], 2)
        if node["degree"] <= 5:
            degree["1-5"] += 1
        elif node["degree"] <= 10:
            degree["6-10"] += 1
        else:
            degree[">10"] += 1
        
    degree_list = [{"name": key, "value": degree[key]} for key in degree]
    

    # degree_list = [
    #     {
    #         "name": "1-5",
    #         "value": 123
    #     },
    #     {
    #         "name": "6-10",
    #         "value": 94
    #     },
    #     {
    #         "name": ">10",
    #         "value": 49
    #     }
    # ]
    # c = (
    #     Pie()
    #     .add(
    #         "",
    #         degree_list,
    #         radius=["40%", "75%"],
    #     )
    #     .set_global_opts(
    #         title_opts=opts.TitleOpts(title="Degree Distribution"),
    #         legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
    #     )
    #     .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    #     # .render("pie_radius.html")
    # )
    # json_content = json.loads(c.dump_options())
    # json_content["legend"]["left"] = "5%"
    return JsonResponse({
        'message': 'ok',
        "nodes": nodes,
        "edges": edges,
        "json": degree_list
    })
    