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
			(1,3, {'color':color_2}), (3,2,{'color':color_1}), (3,6,{'color':color_3}), 
			(6,5,{'color':color_2}), (5,4,{'color':color_1}), (5,7,{'color':color_3}), 
			(6,8,{'color':color_1}), (11,10,{'color':color_2}), (12,10,{'color':color_1}), 
			(10,9,{'color':color_3}), (9,13,{'color':color_1}), (9,8,{'color':color_2}), 
			(8,14,{'color':color_3}), (14,15,{'color':color_2}), (15,19,{'color':color_1}), 
			(15,16,{'color':color_3}), (16,17,{'color':color_2}), (16,18,{'color':color_1}), 
			(14,20,{'color':color_1}), (20,21,{'color':color_2}), (21,22,{'color':color_1}),
			(21,23,{'color':color_3}), (20,24,{'color':color_3}), (24,25,{'color':color_1}),
			(24,26,{'color':color_2}), (26,27,{'color':color_1}), (26,28,{'color':color_3}) 
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

nx.draw_networkx(G, width=2, with_labels=True, font_weight='bold', node_color='skyblue', edge_color=colors, node_size=400, font_size=10)

plt.show()

