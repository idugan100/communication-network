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

def get_sorted_node_list_by_remaining_degree_then_max_edge_weight(Graph):
	nodes_by_degree = []
	graph_degree = get_max_degree_of_graph(Graph)

	for i in range (graph_degree, -1, -1):
		node_degree_class=[]
		for node in G.nodes():
			if(G.nodes[node]["remaining_degree"]==i):
				node_degree_class.append(node)
		for j in range(len(node_degree_class)):
			all_edges_under_consideration=[]
			#add all edges to list
			all_edges_under_consideration=list(Graph.edges(node_degree_class))
			#remove completed nodes
			edges=all_edges_under_consideration.copy()
			for (i, j) in edges:
				if (Graph[i][j]["completed"]==True):
					all_edges_under_consideration.remove( (i,j) )
			#find the highest weight edge
			max_i=-1
			max_j=-1
			max_weight=-1
			for (i,j) in all_edges_under_consideration:
				if(Graph[i][j]["weight"]>max_weight):
					max_i=i
					max_j=j 
					max_weight=Graph[i][j]["weight"]
			# print(max_i,max_j,node_degree_class, all_edges_under_consideration)
			# print("\n")
			# add the node it is from to the nodes_by_degree final results array
			#remove added node from the nodes_degree_class so it's edge wont get picked again 
			if max_i in node_degree_class:
				nodes_by_degree.append(max_i)
				node_degree_class.remove(max_i)
			elif max_j in node_degree_class:
				nodes_by_degree.append(max_j)
				node_degree_class.remove(max_j)
	# print(nodes_by_degree)
	return nodes_by_degree	
	
def clear_node_engagements(Graph):
	for node in Graph.nodes():
		Graph.nodes[node]["is_engaged"]=False
	return None

def get_node_to_transfer_with(Graph, starting_node,num):
	edges=list(Graph.edges(starting_node, data=True))
	valid_edges=edges.copy()
	# print("all edges from node"+str(starting_node)+" "+str(edges))
	# print(len(edges))
	for (i, j, attributes) in edges:
		if (attributes["completed"]==True):
			valid_edges.remove( (i,j,Graph[i][j]) )
		elif(Graph.nodes[j]["is_engaged"]==True):
			valid_edges.remove( (i,j,Graph[i][j]) )
	# print("remaining edges"+str(edges))
	max_val=0
	max_node=-1
	for i,j,attributes in valid_edges:
		if(Graph.nodes[j]["remaining_degree"]>=max_val):
			max_val=Graph.nodes[j]["remaining_degree"]
			max_node=j
	if(max_node==-1):
		return -1
	node_sort_results=[]
	for i,j,attributes in valid_edges:
		if(Graph.nodes[j]["remaining_degree"]==max_val):
			node_sort_results.append((i,j,attributes))
	max_edge_weight=0
	result_i=0
	result_j=0
	for i,j,attributes in node_sort_results:
		if(Graph[i][j]["weight"]>=max_edge_weight):
			max_edge_weight=Graph[i][j]["weight"]
			result_i=i
			result_j=j	
	return result_i if result_i != starting_node else result_j

color_list=['red','blue','yellow','green','orange','brown','pink']

G = nx.Graph()

#create graph 1
for i in range (1,29): 
	G.add_node(i,is_engaged=False)

G.add_edges_from([ 
			(1,3, {'weight':3.0}), (3,2,{'weight':4.1}), (3,6,{'weight':8.0}), 
			(6,5,{'weight':1.0}), (5,4,{'weight':7.0}), (5,7,{'weight':4.0}), 
			(6,8,{'weight':3.2}), (11,10,{'weight':4.4}), (12,10,{'weight':1.0}), 
			(10,9,{'weight':8.0}), (9,13,{'weight':5.0}), (9,8,{'weight':2.4}), 
			(8,14,{'weight':9.0}), (14,15,{'weight':3.2}), (15,19,{'weight':2.1}), 
			(15,16,{'weight':8.0}), (16,17,{'weight':4.5}), (16,18,{'weight':3.6}), 
			(14,20,{'weight':7.0}), (20,21,{'weight':7.0}), (21,22,{'weight':9.0}),
			(21,23,{'weight':1.2}), (20,24,{'weight':7.0}), (24,25,{'weight':4.2}),
			(24,26,{'weight':9.0}), (26,27,{'weight':4.4}), (26,28,{'weight':5.0}) 
		])

#add degree values of each node
for node in G.nodes():
	G.nodes[node]["starting_degree"] = G.degree(node)
	G.nodes[node]["remaining_degree"] = G.degree(node)


for i,j,attributes in G.edges(data=True):
	attributes["completed"]=False

#logic for optimization algorithm
for i in range(get_max_degree_of_graph(G)):
	for node in get_sorted_node_list_by_remaining_degree_then_max_edge_weight(G):
		if(G.nodes[node]["is_engaged"]==False):
			destination_node = get_node_to_transfer_with(G,node,i)
			if(destination_node == -1):
				continue
			else:
				G.nodes[destination_node]["is_engaged"]=True
				G.nodes[node]["is_engaged"]=True	
				G.nodes[destination_node]["remaining_degree"]-=1				
				G.nodes[node]["remaining_degree"]-=1
				print("edge completed round " + color_list[i] + " " + str(node) + " " + str(destination_node) + " time taken: " + str(G[node][destination_node]["weight"]))
				G[node][destination_node]["completed"]=True
				G[node][destination_node]["color"]=color_list[i] 	
				
				# print("completed", node, destination_node, G[node][destination_node])

	clear_node_engagements(G)

colors=[]
for i,j,attributes in G.edges(data=True):
	colors.append(attributes['color'])

print("Nodes: " +str(G.number_of_nodes()),"Edges:" + str(G.number_of_edges()))
print("Highest Degree of Any Node:"  + str(len(nx.degree_histogram(G))-1))

pos=nx.spring_layout(G)
nx.draw_networkx(G, pos, width=2, with_labels=True, min_source_margin=2,font_weight='bold', node_color='skyblue', edge_color=colors, node_size=400, font_size=10)
edge_labels = nx.get_edge_attributes(G, 'weight')

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)
plt.savefig("b.png")
plt.show()