class Graph:
    def __init__(self,graph_dic=None):
        if graph_dic == None:
            graph_dic = {}
        self.__graph_dic   = graph_dic
        
    def verticies(self):
        return self.__graph_dic.keys()
    
    '''def Edges(self):
        return self.__graph_dic.values()
    '''
    def Edges(self):
        edges = []
        for node in self.__graph_dic:
            for neig in self.__graph_dic[node]:
                edges.append((node,neig))
        
        return edges        
    
    
    
    
def main():
    gd = {"a":["c"],"b":["c","e"],"c":["a","b","d","e"],"d":["c"],"e":["b","c"],"f":[]}
    graph = Graph(gd)
    print(graph.verticies())
    print(graph.Edges())
    
    
    
main()
    
    
        
        
            
            
        
        