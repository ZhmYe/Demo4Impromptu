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
from web3 import Web3
import requests
import csv
import random
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


def random_string16(randomlength=16):
  """
  生成一个指定长度的随机字符串
  """
  random_str ='0x'
  base_str ='abcdefghigklmnopqrstuvwxyz0123456789'
  length =len(base_str) -1
  for i in range(randomlength):
    random_str +=base_str[random.randint(0, length)]
  return random_str

def get_port_dict(file_path='/home/z/yzm_demo_graph/demo_http/Demo4Impromptu/backend/data/port'):
    data_dict = {}
    with open(file_path, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile, fieldnames=['contract', 'port', 'type'])
        next(csv_reader)  # Skip the first row/header.

        # Iterate through the CSV data and convert it into a dictionary.
        for row in csv_reader:
            # Convert the 'port' value to an integer (if needed).
            # row['port'] = row['port']
            # Add the data to the dictionary, using the 'contract' as the key and 'port' as the value.
            data_dict[row['contract']] = {
                "port": row['port'],
                "type": row["type"]
            }
    return data_dict

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


# 过滤掉交易中涉及合约地址的部分
def run_ignore_contract_address(edges):
    check_list = dict()
    ans = []
    w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
    for edge in edges:
        # print(edge)
        source = edge['source']
        target = edge['target']
        if source == '' or target == '':
            continue
        flag_1 = False
        flag_2 = False
        if check_list.get(source) is None:
            code = w3.eth.getCode(w3.to_checksum_address(source))
            flag_1 = code != b''
            check_list[source] = flag_1
        else:
            flag_1 = check_list[source]
        if check_list.get(target) is None:
            code = w3.eth.getCode(w3.to_checksum_address(target))
            flag_2 = code != b''
            check_list[target] = flag_2
        else:
            flag_2 = check_list[target]
        # if flag_1:
        #     print(source , 'is a contract address')
        # if flag_2:
        #     print(target , 'is a contract address')
        if flag_1 == False and flag_2 == False:
            ans.append(edge)
    return ans
def get_struct_edges(edges):
    struct_edges = []
    from_to_dict = {}
    for edge in edges:
        if edge["source"] not in from_to_dict:
            from_to_dict[edge["source"]] = {}
        if edge["target"] not in from_to_dict[edge["source"]]:
            from_to_dict[edge["source"]][edge["target"]] = {
                "value": edge["value"],
                "blockNumber": [edge["blockNumber"]],
                "contract": [edge["contract"]],
                "tx_hash": [edge["tx_hash"]]
            } 
        else:
            from_to_dict[edge["source"]][edge["target"]]["value"] += edge["value"]
            if edge["blockNumber"] not in from_to_dict[edge["source"]][edge["target"]]["blockNumber"]:
                from_to_dict[edge["source"]][edge["target"]]["blockNumber"].append(edge["blockNumber"])
            if edge["contract"] not in from_to_dict[edge["source"]][edge["target"]]["contract"]:
                from_to_dict[edge["source"]][edge["target"]]["contract"].append(edge["contract"])
            # 现在随机生成的tx_hash还是有可能重合的（逻辑上）
            if edge["tx_hash"] not in from_to_dict[edge["source"]][edge["target"]]["tx_hash"]:
                from_to_dict[edge["source"]][edge["target"]]["tx_hash"].append(edge["tx_hash"])
    # print(from_to_dict)
    for source in from_to_dict:
        for target in from_to_dict[source]:
            # print(target)
            struct_edges.append(
                {
                    "source": source, 
                    "target": target, 
                    "blockNumber": from_to_dict[source][target]["blockNumber"],
                    "contract": from_to_dict[source][target]["contract"],
                    "tx_hash": from_to_dict[source][target]["tx_hash"],
                    "value": from_to_dict[source][target]["value"],
                    "coin_type": edges[0]["coin_type"]
                }
                )
    # print(struct_edges)
    return struct_edges
# todo
# 2023/8/1 ZhmYe
# 这里原本overview_view和analyze_view是分开来的，因为之前两个之前其实没啥关系都是定死的
# 现在两个有关系了所以我在前后端都改成了一起
@check_method('POST')
def analyze_view(request):
    # ignore_contract_address = True
    total_nodes = []
    total_edges = []
    global global_path
    post = get_post_json(request)
    print(post)
    abnormal = []
    abnormal_tx_hash = []
    # post: json,参数如下：
        # address: [list, 所有账户]
        # khop: int, k跳
        # start_blk: int, start块
        # end_blk: int, end块
        # contracts: [list, 合约地址]
        # timeInterval: int, time Interval
        # valueDifference: int, value difference
        # ignore: bool, 是否过滤checkbox
        # eth: bool, eth checkbox
    # url = "http://localhost:8000/data/overview/" # 这里把后面的Url补上包括端口，localhost:8010/路由/接口
    # 下面是requests的两种请求
        # response = requests.get(url, params=post) #这个是get请求，这里如果直接运行上面的Url,会有404因为我没有定义get接口（上面我封装了解释器check_method('POST'/'GET')），注意区分get和post
        # response = requests.post(url, data=post) # 这个是post请求
    #拿到response以后下面的内容按需保留修改，比如下面读取nodes和edges可能就不用了
    

    # 这里我们要先考虑request中的address和contracts，都是list
        # 针对不同的contracts, address是否有局部性（？就是一个地址为0x123456的账户是否只出现在某个合约里，不同合约里的0x123456是否是同一个账户？）
        # 这里我先简单的针对不同的contracts也就是不同的数据库后端“端口”，全部发送所有address去查询
    # 那么首先先遍历contracts
    ignore_contract_address = post["ignore"]
    port_dict = get_port_dict()
    # 将eth加入合约列表中
    if post["eth"]:
        post["contracts"].append('eth')
    elapsed_time = 0.0
    # 逐合约查询
    for contract in post["contracts"]:
        # 这里我重新构造一下post，因为contracts没必要全部发过去
            # 但是不知道现在的数据库在处理contracts时是按什么处理的
                # 我姑且先把contracts参数还是作为list
        each_query_params = {
            "address": post["address"],
            "khop": post["khop"],
            "start_blk": post["start_blk"],
            "end_blk": post["end_blk"],
            "contracts": [ contract ], # 如果只要一个不需要list就把[]删了
            "timeInterval": post["timeInterval"],
            "valueDifference": post["valueDifference"]
        }
        def get_url_by_contracts(contract):
            if port_dict.get(contract) is None:
                return ""
            return "http://localhost:" + port_dict.get(contract)["port"]+ "/"
        url = get_url_by_contracts(contract)
        if url == "":
            print(contract, 'is not supported')
            continue
        text = ""
        try:
            response = requests.get(url, params=each_query_params)
            text = response.text # 响应体文本内容
        except:
            print(contract, 'is not supported')
            continue
        # headers = response.headers # 响应头信息，是一个字典对象
        # encoding = response.encoding # 响应体编码格式，如UTF-8、GBK等
        # content = response.content # 响应体二进制数据，如图片、音频、视频等
    
        # # # 将字符串解析成JSON格式
        parsed_data = json.loads(text)
        # # 提取edges和nodes的数据
        edges = parsed_data['edges']

        # 这是最早的定死的写法
        # with open('./data/position.json', encoding="utf-8") as f:
        #     node_position = json.load(f)
        # position_dic = {}
        # for node_info in node_position:
        #     position_dic[node_info["id"]] = {"x": node_info["x"], "y": node_info["y"]}
        # with open("./data/overview-edges.json", encoding="utf-8") as f:
        #     edges = json.load(f)
        #     f.close() 
        # 将字符串解析成JSON格式
        parsed_data = json.loads(text)
        
        # 计算查询时间
        for queryResult in parsed_data["queryResults"]:
            elapsed_time += float(queryResult["elapsed_time"])
            
        # 提取edges和nodes的数据
        edges = parsed_data['edges'] if not ignore_contract_address else run_ignore_contract_address(parsed_data['edges'])
        # print(edges)
        
        # 这里加上contract属性 
        for edge in edges:
            edge["contract"] = contract
            # db里没有存tx_hash，这边随机生成一下
            edge["tx_hash"] = random_string16(64)
            edge["coin_type"] = port_dict.get(contract)["type"]
            
        # print(edges)
        # 先注释一下
        for address in post["address"]:
            temp_abnormal = analyze(edges, address, int(post["timeInterval"]), float(post["valueDifference"]) * 1e18)
            for transaction in temp_abnormal:
                if transaction["tx_hash"] not in abnormal_tx_hash:
                    abnormal_tx_hash.append(transaction["tx_hash"])
                    abnormal.append(transaction)
                    
                    
                    
        total_edges.extend(edges)
    # 到此所有的交易和异常交易得到完毕
        # 因为不同合约得到的交易tx_hash不可能一致，不需要进行去重合并(？)

    print('elapsed_time: ', round(elapsed_time, 2), 'ms')
    nodes_dict = dict()
    nodes = list()
    
    # 判断是否忽略合约地址相关的交易
    if ignore_contract_address:
        total_edges = run_ignore_contract_address(total_edges)
        
    # 统一计算节点度数
    for edge in total_edges:
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
    # print(total_edges)
    overview_result = {
        "nodes": nodes,
        "edges": get_struct_edges(total_edges),
        "json": degree_list
    }  
    
    
    
    
    # 统一获取异常账户 
    account_in_abnormal = []
    for transaction in abnormal:
        if transaction["source"] not in account_in_abnormal:
            account_in_abnormal.append(transaction["source"])
        if transaction["target"] not in account_in_abnormal:
            account_in_abnormal.append(transaction["target"])
    analyze_node = []
    for account in account_in_abnormal:
        degree = 0
        for transaction in abnormal:
            if transaction["source"] == account or transaction["target"] == account:
                degree += 1
        analyze_node.append({"id": account, "degree": degree, "size": 50})
    # abnormal = list(set(abnormal))
    analyze_result = {
        "nodes": analyze_node,
        "edges": get_struct_edges(abnormal)
    }       
    # print(abnormal)           
    return JsonResponse({
        'message': 'ok',
        "overview": overview_result,
        "analyze": analyze_result
    })
    
