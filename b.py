import networkx as nx
import matplotlib.pyplot as plt

color_1 = 'red'
color_2 = 'blue'
color_3 = 'yellow'

G = nx.Graph()

#create graph 1
for i in range (1,28): 
	G.add_node(i,in_engaged=[False,False,False])

G.add_edges_from([ 
			(1,3, {'color':color_2,'weight':3.0}), (3,2,{'color':color_1,'weight':4.1}), (3,6,{'color':color_3,'weight':8.0}), 
			(6,5,{'color':color_2,'weight':1.0}), (5,4,{'color':color_1, 'weight':7.0}), (5,7,{'color':color_3,'weight':4.0}), 
			(6,8,{'color':color_1,'weight':3.2}), (11,10,{'color':color_2,'weight':4.4}), (12,10,{'color':color_1,'weight':1.0}), 
			(10,9,{'color':color_3,'weight':8.0}), (9,13,{'color':color_1,'weight':5.0}), (9,8,{'color':color_2,'weight':2.4}), 
			(8,14,{'color':color_3,'weight':9.0}), (14,15,{'color':color_2,'weight':3.2}), (15,19,{'color':color_1,'weight':2.1}), 
			(15,16,{'color':color_3,'weight':8.0}), (16,17,{'color':color_2,'weight':4.5}), (16,18,{'color':color_1,'weight':3.6}), 
			(14,20,{'color':color_1,'weight':7.0}), (20,21,{'color':color_2,'weight':7.0}), (21,22,{'color':color_1,'weight':9.0}),
			(21,23,{'color':color_3,'weight':1.2}), (20,24,{'color':color_3,'weight':7.0}), (24,25,{'color':color_1,'weight':4.2}),
			(24,26,{'color':color_2,'weight':9.0}), (26,27,{'color':color_1,'weight':4.4}), (26,28,{'color':color_3,'weight':5.0}) 
		])
colors=[]
for i,j,attributes in G.edges(data=True):
	colors.append(attributes['color'])

print("Nodes: " +str(G.number_of_nodes()),"Edges:" + str(G.number_of_edges()))
print("Highest Degree of Any Node:"  + str(len(nx.degree_histogram(G))-1))

#logic for optimization algorithm
#for i in the highest node degree
	#for each node in G (must be sorted so highest degree nodes (remaining?) go first)
		#if node is not engaged
			#get all edges from the node that are not completed and do not go to an engaged node
			#of these eligible edges select the one that goes to the node with the highest (remaining?) degree
			# set the edge to be completed with the corresponding color
			# set the node to be engaged
		#else continue to next node interation
	#clear all node engagements for next round	
pos=nx.kamada_kawai_layout(G)
nx.draw_networkx(G, pos, width=2, with_labels=True, min_source_margin=2,font_weight='bold', node_color='skyblue', edge_color=colors, node_size=400, font_size=10)

edge_labels = nx.get_edge_attributes(G, 'weight')

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()

