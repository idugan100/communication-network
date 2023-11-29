import networkx as nx
import matplotlib.pyplot as plt

def get_max_degree_of_graph(Graph):
	return max(G.degree[node] for node in G.nodes())

def get_sorted_node_list_by_starting_degree(Graph):
	nodes_by_degree = []
	graph_degree = get_max_degree_of_graph(Graph)
	
	for i in range (graph_degree, -1, -1):
		for node in G.nodes():
			if (G.nodes[node]["starting_degree"]==i):
				nodes_by_degree.append(node)
	return nodes_by_degree

def get_sorted_node_list_by_remaining_degree(Graph):
	nodes_by_degree = []
	graph_degree = get_max_degree_of_graph(Graph)

	for i in range (graph_degree, -1, -1):
		for node in G.nodes():
			if(G.nodes[node]["remaining_degree"]==i):
				nodes_by_degree.append(node)
	return nodes_by_degree	
	
def clear_node_engagements(Graph):
	for node in Graph.nodes():
		Graph.nodes[node]["is_engaged"]=False
	return None

def get_node_to_transfer_with(Graph, starting_node,num):
	edges=list(Graph.edges(starting_node, data=True))
	valid_edges=edges.copy()
	print("all edges from node"+str(starting_node)+" "+str(edges))
	print(len(edges))
	for (i, j, attributes) in edges:
		print(i,j)
		if (attributes["completed"]==True):
			valid_edges.remove( (i,j,Graph[i][j]) )
		elif(Graph.nodes[j]["is_engaged"]==True):
			valid_edges.remove( (i,j,Graph[i][j]) )
	print("remaining edges"+str(edges))
	max_val=0
	max_node=-1
	for i,j,attributes in valid_edges:
		if(Graph.nodes[j]["remaining_degree"]>=max_val):
			max_val=Graph.nodes[j]["remaining_degree"]
			max_node=j
	return max_node

color_1 = 'pink'
color_2 = 'pink'
color_3 = 'pink'
color_list=['red','blue','yellow','green','orange','brown','pink']
G = nx.Graph()

#create graph 1
for i in range (1,29): 
	G.add_node(i,is_engaged=False)

G.add_edges_from([ 
			(1,3), (3,2), (3,6), (6,5), (5,4), (5,7), (6,8), (11,10), (12,10), (10,9), (9,13), (9,8), 
			(8,14), (14,15), (15,19), (15,16), (16,17), (16,18), (14,20), (20,21), (21,22),
			(21,23), (20,24), (24,25), (24,26), (26,27), (26,28), 
		])

#add degree values of each node
for node in G.nodes():
	G.nodes[node]["starting_degree"] = G.degree(node)
	G.nodes[node]["remaining_degree"] = G.degree(node)


for i,j,attributes in G.edges(data=True):
	attributes["completed"]=False

#logic for optimization algorithm
for i in range(get_max_degree_of_graph(G)):
	for node in get_sorted_node_list_by_remaining_degree(G):
		if(G.nodes[node]["is_engaged"]==False):
			destination_node = get_node_to_transfer_with(G,node,i)
			if(destination_node == -1):
				continue
			else:
				G.nodes[destination_node]["is_engaged"]=True
				G.nodes[node]["is_engaged"]=True	
				G.nodes[destination_node]["remaining_degree"]-=1				
				G.nodes[node]["remaining_degree"]-=1

				G[node][destination_node]["completed"]=True
				G[node][destination_node]["color"]=color_list[i] 	
				
				print("completed", node, destination_node, G[node][destination_node])

	clear_node_engagements(G)	

colors=[]
for i,j,attributes in G.edges(data=True):
	colors.append(attributes['color'])

nx.draw_networkx(G, width=2, with_labels=True, font_weight='bold', node_color='skyblue', edge_color=colors, node_size=400, font_size=10)
plt.savefig("a.png")
plt.show()

