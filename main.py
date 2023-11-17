import networkx as nx
import matplotlib.pyplot as plt

color_1 = 'red'
color_2 = 'blue'
color_3 = 'yellow'

G = nx.Graph()

#create graph 1
G.add_nodes_from([ 1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])
G.add_edges_from([ 
			(1,3, {'color':color_2}), (3,2,{'color':color_1}), (3,6,{'color':color_3}), 
			(6,5,{'color':color_2}), (5,4,{'color':color_1}), (5,7,{'color':color_3}), 
			(6,8,{'color':color_1}), (11,10,{'color':color_2}), (12,10,{'color':color_1}), 
			(10,9,{'color':color_3}), (9,13,{'color':color_1}), (9,8,{'color':color_2}), 
			(8,14,{'color':color_3}), (14,15,{'color':color_2}), (15,19,{'color':color_1}), 
			(15,16,{'color':color_3}), (16,17,{'color':color_2}), (16,18,{'color':color_1}), 
			(14,20,{'color':color_1}), (20,21,{'color':color_2}), (21,22,{'color':color_1}),
			(21,23,{'color':'yellow'}), (20,24,{'color':'yellow'}), (24,25,{'color':'red'}),
			(24,26,{'color':'blue'}), (26,27,{'color':'red'}), (26,28,{'color':'yellow'}) 
		])
colors=[]
for i,j,attributes in G.edges(data=True):
	colors.append(attributes['color'])
print(colors)
print("Nodes: " +str(G.number_of_nodes()),"Edges:" + str(G.number_of_edges()))

nx.draw_networkx(G, width=2, with_labels=True, font_weight='bold', node_color='skyblue', edge_color=colors, node_size=400, font_size=10)
plt.show()
