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
			(1,3, {'color':color_2}), (3,2,{'color':color_1}), (3,6,{'color':color_3}), 
			(6,5,{'color':color_2}), (5,4,{'color':color_1}), (5,7,{'color':color_3}), 
			(6,8,{'color':color_1}), (11,10,{'color':color_2}), (12,10,{'color':color_1}), 
			(10,9,{'color':color_3}), (9,13,{'color':color_1}), (9,8,{'color':color_2}), 
			(8,14,{'color':color_3}), (14,15,{'color':color_2}), (15,19,{'color':color_1}), 
			(15,16,{'color':color_3}), (16,17,{'color':color_2}), (16,18,{'color':color_1}), 
			(14,20,{'color':color_1}), (20,21,{'color':color_2}), (21,22,{'color':color_1}),
			(21,23,{'color':color_3}), (20,24,{'color':color_3}), (24,25,{'color':color_1}),
			(24,26,{'color':color_1}), (26,27,{'color':color_2}), (26,28,{'color':color_3}),

			#these are extra edges for testing the generality of my algorithm
			(12,11,{'color':color_1}),(13,10,{'color':color_1}), (8,7,{'color':color_1}),
			(8,20,{'color':color_1}),(21,8,{'color':color_1}), (16,24,{'color':color_1})
		])
colors=[]

#add degree values of each node
for node in G.nodes():
	G.nodes[node]["starting_degree"] = G.degree(node)
	G.nodes[node]["remaining_degree"] = G.degree(node)

# print(get_sorted_node_list_by_starting_degree(G))

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

for i,j,attributes in G.edges(data=True):
	colors.append(attributes['color'])

nx.draw_networkx(G, width=2, with_labels=True, font_weight='bold', node_color='skyblue', edge_color=colors, node_size=400, font_size=10)

plt.show()

