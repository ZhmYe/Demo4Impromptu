import json
import os



def write_json(json_list, output):
    f = open(output, 'w+')
    f.write('[')
    for i in range(len(json_list)):
        if i < len(json_list)-1:
            f.write('\n    '+json.dumps(json_list[i])+',')
        else:
            f.write('\n    '+json.dumps(json_list[i]))
    f.write('\n]')
    
# 计算度
def calculate_degree(edges):
    degrees = dict()
    for edge in edges:
        if degrees.get(edge["source"]) is None:
            degrees[edge["source"]] = 1
        else:
            degrees[edge["source"]] += 1
        if degrees.get(edge["target"]) is None:
            degrees[edge["target"]] = 1
        else:
            degrees[edge["target"]] += 1
    return degrees
    
    
if __name__ == '__main__':
    target = '0x278a8453ecf2f477a5ab3cd9b0ea410b7b2c4182'
    edges = json.load(open('backend/data/overview-edges.json'))
    nodes = json.load(open('backend/data/overview-nodes.json'))
    # print(nodes)
    print('number of edges: ',str(len(edges)),'number of nodes: ',str(len(nodes)))
    new_edges = []
    new_nodes = []
    for edge in edges:
        if edge["source"] == target or edge["target"] == target:
            continue
        new_edges.append(edge)
    degrees = calculate_degree(new_edges)
    for node in nodes:
        if node["id"] == target:
            continue
        if degrees.get(node["id"]) is None:
            continue
        new_nodes.append(node)
    
    write_json(new_edges, 'backend/data/overview-edges.json')
    write_json(new_nodes, 'backend/data/overview-nodes.json')
    print('number of edges: ',str(len(new_edges)),'number of nodes: ',str(len(new_nodes)))