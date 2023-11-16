import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()

#create graph 1
G.add_nodes_from([ 1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])
G.add_edges_from([ 
			(1,3), (3,2), (3,6), 
			(6,5), (5,4), (5,7), 
			(6,8), (11,10), (12,10), 
			(10,9), (9,13), (9,8), 
			(8,14), (14,15), (15,19), 
			(15,16), (16,17), (16,18), 
			(14,20), (20,21), (21,22),
			(21,23), (20,24), (24,25),
			(24,26), (26,27), (26,28) 
		])

print("Nodes: " +str(G.number_of_nodes()),"Edges:" + str(G.number_of_edges()))

nx.draw(G, with_labels=True, font_weight='bold', node_color='skyblue', edge_color='gray', node_size=400, font_size=10)
plt.show()
