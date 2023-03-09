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
    "0x12toapnwhlkqzddrz2wlsesignw9xkg5pamziuhb",
    "0xlg2kqu9f7htvh2ux2dmgbvk1tw3vzkbgzim16wv4",  
    "0xto5zrnn8qgits71gxmmdfl3bggfz8q40inywgs06", 
    "0xek1uci40xwi6y7aq9i2ghrs2uru0koepwvu8p32o"
]

hacker_list_no_icon = [
    "0xu1hdwc6cgr7cnv8xo8dvyvz6e2mwrp3rxtl7z9h5",
    "0xq9165xhiq9zc19syggqid8qorcd0hf4aqg9stbf7",
    "0xzrbay9r4h0ig96btyz421cxwwplwuye9hktgcei6", 
    "0x2imicclza5go3i5486ysxik00rubwft3x5qvdtbo",
    "0xco21vlgq2mtsc0qk64cpuvpbh2kmc074iwy8k7k9",
    "0xv2ki4alnx4yb2yenpbz29i1g4l5wdeksefgygnpi",
    "0x8epddqq2h4421ul1zhfovgg1gy5uamhryqd3dw0x",
    "0x84bz5s4f7ecde5z9rhw36mo9kytz3g2rg4db8wad",
    "0xcwy0z29i4ybxwkyu0c18xamyauvgmndh5hivkd6u",
    "0x6o5v6hnm6rb0v330mwowsvwxpssqw7ry8rrxvt27",
    "0xx2zfq2etghz5fk6nd9z23g2gdugmp02fhq2r3s1t", 
    "0xfgv113xtch13o0xxmf6cyyrck4s3znzmpt7vrhkw",
    "0xngbqzb1kqrlt2shlg2qf9kccpg9suxmp0wwg4q3l", 
    "0xtqc65crrf0kubu0srryz8p6ly53gueua4327xbyo",
    "0xas1mdflghu6bhp7aek82xgrlhpdecflcg3x8gg6c",
    "0xh5x5akaqcazn4d02co6h5rfi6fulbxgzc5wbokdg",
    "0x1um57pklnowgdecxlww522020baaxke9ov1u3aqh",
    "0xwrld11u6q93i36rxadpuurx5gd3iskolh67r7v8a",
    "0x5vrba0g63coa3wllpvspgvz1pz7h17lc55k8ooz2",
    "0xam1ehzm4pg5100pf7tztm0glhfmq569587dl86dr",
    "0xwxr5p5gz4x94p2m22hdx0k9kr252dkl0rzygzd67",
    "0xd2nsop1hhrl456w7nxl45eub3zr5cwnp2x1xokha",
    '0xlyyt62z2v3woth9w01fs8rmk8vrbt7uufo6sbgvp',
    "0xs3e2rdf1y2efpu2upzv8doqsfy146ytk9xny0kyw",
    "0xnr62pgzat5tqdn4kua0b8t9mayti979pn1ed605w",
    "0xp5mv6tktrnvgeawzgnr5yphlk0l43n5bu2l37zcv",
    "0x97nt6cf1b8e1rtgum2dsp8g6qqpbr4rl2n7t7h8c",
    "0xgposci88dokdpf8z2n665rw77nsk6z6ko91d3f5t",
    "0xiv2ewb87kgynqme25y3yc5l2ffq6amalhp6ddnds",
    "0x2s4we57yfga0z2uzpoq2e5i3fnsnsmep0bw2kfqb",
    "0xb7f68d5y61is14fcsdp5oah1gtaxb2atsdnri2ts",
    "0x64tyyubdfoi9o9u4fb86p265tuvruwobb25rtge4"
]
cash_list = [
    "0xv290h0knxrksy39vt3m78rnpvkbeu291wlm23zaq", 
    "0xf1r2wf53o45mqg6empwyy58mdlg559tvbbv969r1"]

compromised_account_list = [
    "0x78hnrbubw5688gyymwwnwuhamruq5b6t67utldpg"
]

compromised_account_list_no_label = [
    "0xgqkw5myorew58nmzg8syxi2n7ptdg92ye8y182di",
    "0xbvdywe6mgb2vdzth6612v0mc48sgdzypslxow4y9",
    "0xruewzunvdg5fu5ec6manwl9a9ygu96pgo1t8gh0w",
    "0xgnio6knh6g19n1kr2c0ghm0h4o2f5euxxgq7qsg2",
    "0x692emmr9v2h7mwxmx3crlgrmqgcvwyu7ox3edoy7",
    "0xu44g25s4vnqbuxnfsm0poiy31ind6za5gyww17ig",
    "0x6vfr6tofrkbst1l7i1v0idwagte8stz6t04vu1gh",
    "0x021cgduyftudedt7pyuftwmkrv697a7lb4wp75v4",
    "0xrdio71fas6lhdii52w5qsyoods7kpkbqo7oximgw",
    "0xnx12ao5hssauky5q0tdv8ga8giqz29acb6nzsshy",
    "0xdnyyriydkcvbpz7u8yc7vxizl8a2916vxa0e757r"
]

def get_label(node_id):
    if node_id in hacker_list:
        return True, "Hacker Wallet"
    if node_id in cash_list:
        return True, "Tornado.Cash"
    if node_id in compromised_account_list:
        return True, "Compromised Account"
    return False, ""

def get_color(node_id):
    return '#00BFFF'

def get_size(degree):
    default_node_size = 10
    if degree == 1:
        return default_node_size + 4 * int(degree)
    return default_node_size + 2 * int(degree)

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
        node["style"]  = {
            "fill": node["color"]
        }
        node["labelCfg"]={
            "style":{
              "fontSize": 10,
              "fontWeight": 800
            }
          }
        node["size"] = get_size(node["degree"])
        if node["id"] in hacker_list_no_icon:
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
            continue
        if node["id"] in compromised_account_list_no_label:
            node["icon"] = {
                "show": True,
                "img": "https://raw.githubusercontent.com/Liuyushiii/img/master/wallet4.png",
                "width": node["size"] * 0.8,
                "height": node["size"] * 0.8
            }
            continue    
        have_label, label = get_label(node["id"])
        if have_label:
            node["label"] = label
            # image
            if label == "Hacker Wallet":
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
            elif label == "Tornado.Cash":
                node["style"] = {
                    "fill": "#000000",
                    "lineWidth": 0
                }
                node["icon"] = {
                    "show": True,
                    "img": "https://raw.githubusercontent.com/Liuyushiii/img/master/inner_tornado.png",
                    "width": node["size"] * 0.8,
                    "height": node["size"] * 0.8
                }
            elif label == "Compromised Account":
                node["icon"] = {
                    "show": True,
                    "img": "https://raw.githubusercontent.com/Liuyushiii/img/master/wallet4.png",
                    "width": node["size"] * 0.8,
                    "height": node["size"] * 0.8
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
    # degree = {"1-5": 0, "6-10": 0, ">10" : 0}
    # for node in nodes:
    #     if node["degree"] <= 5:
    #         degree["1-5"] += 1
    #     elif node["degree"] <= 10:
    #         degree["6-10"] += 1
    #     else:
    #         degree[">10"] += 1
    # degree_list = [{"name": key, "value": degree[key]} for key in degree]
    degree_list = [
        {
            "name": "1-5",
            "value": 123
        },
        {
            "name": "6-10",
            "value": 94
        },
        {
            "name": ">10",
            "value": 49
        }
    ]
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
    