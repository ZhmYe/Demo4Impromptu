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
import requests
from . import FilterEngine
# global_path = {}
class Edge:
    def __init__(self, source, target, tx_hash, value):
        self.source = source
        self.target = target
        self.tx_hash = tx_hash
        self.value = value

    def to_json(self):
        return json.dumps(self.__dict__)
    
class Node:
    def __init__(self, id, degree):
        self.id = id
        self.degree = degree
        self.cluster = 0

    def to_json(self):
        return json.dumps(self.__dict__)

def get_color(node_id):
    return '#00BFFF'

def get_size(degree):
    default_node_size = 10
    if degree == 1:
        return default_node_size + 5 * int(degree)
    return default_node_size + 2 * int(degree)

    
def analyze(transactions, address, time_interval, valueDifference):
    filterEngine = FilterEngine.FilterEngine(time_interval=time_interval, value_difference=valueDifference)
    filterEngine.load_transactions(transactions)
    filterEngine.filter_by_address(address)              
    return filterEngine.abnormal
@check_method('POST')
def analyze_view(request):
    global global_path
    post = get_post_json(request)
    print(post)
    # post: json,参数如下：
        # address: [list, 所有账户]
        # khop: int, k跳
        # start_blk: int, start块
        # end_blk: int, end块
        # contracts: [list, 合约地址]
        # timeInterval: int, time Interval
        # valueDifference: int, value difference
    # url = "http://localhost:8000/data/overview/" # 这里把后面的Url补上包括端口，localhost:8010/路由/接口
    # 下面是requests的两种请求
        # response = requests.get(url, params=post) #这个是get请求，这里如果直接运行上面的Url,会有404因为我没有定义get接口（上面我封装了解释器check_method('POST'/'GET')），注意区分get和post
        # response = requests.post(url, data=post) # 这个是post请求
    #拿到response以后下面的内容按需保留修改，比如下面读取nodes和edges可能就不用了
    
    url = "http://localhost:8030/"
    response = requests.get(url, params=post)
    headers = response.headers # 响应头信息，是一个字典对象
    text = response.text # 响应体文本内容
    encoding = response.encoding # 响应体编码格式，如UTF-8、GBK等
    content = response.content # 响应体二进制数据，如图片、音频、视频等
    # print("headers: ", headers)
    print("text: ", text)
    # print("encoding: ", encoding)
    # print("content: ", content)
    
    # # 将字符串解析成JSON格式
    parsed_data = json.loads(text)
    print(parsed_data)
    # # 提取edges和nodes的数据
    edges = parsed_data['edges']
    nodes_dict = dict()
    nodes = list()
    for edge in edges:
        if nodes_dict.get(edge['source']) is None:
            nodes_dict[edge['source']] = 1
        else:
            nodes_dict[edge['source']] = nodes_dict[edge['source']] + 1
        if nodes_dict.get(edge['target']) is None:
            nodes_dict[edge['target']] = 1
        else:
            nodes_dict[edge['target']] = nodes_dict[edge['target']] + 1
    for (k,v) in nodes_dict.items():
        nodes.append(Node(k,v).__dict__)      
    # nodes = parsed_data['nodes']
    
    
    # with open('./data/position.json', encoding="utf-8") as f:
    #     node_position = json.load(f)
    # position_dic = {}
    # for node_info in node_position:
    #     position_dic[node_info["id"]] = {"x": node_info["x"], "y": node_info["y"]}
    # with open("./data/overview-nodes.json", encoding="utf-8") as f:
    #     nodes = json.load(f)
    #     f.close()
    # with open("./data/overview-edges.json", encoding="utf-8") as f:
    #     edges = json.load(f)
    #     f.close()
    degree = {"1-5": 0, "6-10": 0, ">10" : 0} 
    def get_size_overview(node_degree, base):
        if node_degree <= 10:
            return base * node_degree
        else:
            return base * 10 + get_size_overview(node_degree - 10, base/2) 
    for node in nodes:
        node["size"] = 10 + get_size_overview(node["degree"], 2)
        # node["x"] = position_dic[node["id"]]["x"]
        # node["y"] = position_dic[node["id"]]["y"]
        if node["degree"] <= 5:
            degree["1-5"] += 1
        elif node["degree"] <= 10:
            degree["6-10"] += 1
        else:
            degree[">10"] += 1
        
    degree_list = [{"name": key, "value": degree[key]} for key in degree]  

    overview_result = {
        "nodes": nodes,
        "edges": edges,
        "json": degree_list
    }  
    abnormal = []
    abnormal_tx_hash = []
    # analyze(edges, post.address[0])
    for address in post["address"]:
        temp_abnormal = analyze(edges, address, int(post["timeInterval"]), float(post["valueDifference"]) * 1e18)
        for transaction in temp_abnormal:
            if transaction["tx_hash"] not in abnormal_tx_hash:
                abnormal_tx_hash.append(transaction["tx_hash"])
                abnormal.append(transaction)
    # abnormal = list(set(abnormal))
    account_in_abnormal = []
    # 用于判断某个账户是否有转入交易（是否是某个树的根节点）
    account_flag = {}
    # 用于前端渲染边label(两个账户转账总额)
    value_dict = {"Previous Data": {}}
    for transaction in abnormal:
        account_flag[transaction["target"]] = True
        if transaction["source"] not in account_in_abnormal:
            account_in_abnormal.append(transaction["source"])
        if transaction["target"] not in account_in_abnormal:
            account_in_abnormal.append(transaction["target"])
        if transaction["source"] not in value_dict:
            value_dict[transaction["source"]] = {
                transaction["target"]: float(transaction["value"])
            }
        else:
            if transaction["target"] in value_dict[transaction["source"]]:
                value_dict[transaction["source"]][transaction["target"]] += float(transaction["value"])
            else:
                value_dict[transaction["source"]][transaction["target"]] = float(transaction["value"])
    
    for account in account_in_abnormal:
        value_dict["Previous Data"][account] = "Unknown"
    tree_data = []
    for account in account_in_abnormal:
        if account not in account_flag:
            result = get_tree_struct(account, abnormal, {})
            tree_data.append(get_tree_struct(account, abnormal, {}))
    # analyze_result = {
    #     "data": {
    #         "id": "Previous Data",
    #         "children": tree_data
    #     },
    #     "dict": value_dict
    # }
    analyze_node = []
    for account in account_in_abnormal:
        degree = 0
        for transaction in abnormal:
            if transaction["source"] == account or transaction["target"] == account:
                degree += 1
        analyze_node.append({"id": account, "degree": degree, "size": 10 + get_size_overview(degree, 2)})
    analyze_result = {
        "nodes": analyze_node,
        "edges": abnormal
    }
    # print(tree_data)
    global_path = {}
    return JsonResponse({
        'message': 'ok',
        "overview": overview_result,
        "analyze": analyze_result
    })
def get_tree_struct(address, transactions, global_path):
    # global global_path
    global_path[address] = True
    children = []
    children_dict = set()
    for transaction in transactions:
        if transaction["source"] == address:
            if transaction["target"] not in children_dict and transaction["target"] not in global_path:
                children.append(get_tree_struct(transaction["target"], transactions, global_path))
                children_dict.add(transaction["target"])
    if len(children) > 0:
        return {
            "id": address,
            "children": children
        }
    else:
        return {
            "id": address
        }