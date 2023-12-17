import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()


for i in range (1,28): 
	G.add_node(i,is_engaged=False)

G.add_edges_from([ 
			(1,3, {'weight':3.0, 'color':'purple'}), (3,2,{'weight':4.1, 'color':'yellow'}), (3,6,{'weight':8.0, 'color':'green'}), 
			(6,5,{'weight':1.0, 'color':'green'}), (5,4,{'weight':7.0, 'color':'green'}), (5,7,{'weight':4.0, 'color':'yellow'}), 
			(6,8,{'weight':3.2, 'color':'purple'}), (11,10,{'weight':4.4, 'color':'green'}), (12,10,{'weight':1.0, 'color':'green'}), 
			(10,9,{'weight':8.0, 'color':'green'}), (9,13,{'weight':5.0, 'color':'green'}), (9,8,{'weight':2.4, 'color':'orange'}), 
			(8,14,{'weight':9.0, 'color':'green'}), (14,15,{'weight':3.2, 'color':'purple'}), (15,19,{'weight':2.1, 'color':'yellow'}), 
			(15,16,{'weight':8.0, 'color':'green'}), (16,17,{'weight':4.5, 'color':'orange'}), (16,18,{'weight':3.6, 'color':'green'}), 
			(14,20,{'weight':7.0, 'color':'green'}), (20,21,{'weight':7.0, 'color':'orange'}), (21,22,{'weight':9.0, 'color':'green'}),
			(21,23,{'weight':1.2, 'color':'purple'}), (20,24,{'weight':7.0, 'color':'purple'}), (24,25,{'weight':4.2, 'color':'yellow'}),
			(24,26,{'weight':9.0, 'color':'green'}), (26,27,{'weight':4.4, 'color':'orange'}), (26,28,{'weight':5.0, 'color':'purple'}),
            
            (18,11,{'weight':6.0, 'color':'orange'}), (15,13,{'weight':1.1, 'color':'orange'}), (17,19,{'weight':5.2, 'color':'green'}), 
			(19,16,{'weight':4.1, 'color':'orange'}), (19,22,{'weight':4.0, 'color':'purple'}), (23,24,{'weight':7.0, 'color':'orange'}), 
            (24,3,{'weight':2.4, 'color':'blue'}), (1,26,{'weight':9.0, 'color':'green'}), (25,28,{'weight':3.7, 'color':'green'}), 
			
            (4,12,{'weight':6.6, 'color':'orange'}), (3,7,{'weight':6.3, 'color':'orange'}), (10,5,{'weight':5.1, 'color':'purple'}), 
			(10,6,{'weight':7.1, 'color':'orange'}), (14,13,{'weight':3.0, 'color':'purple'}), (20,8,{'weight':6.1, 'color':'yellow'}),
            (20,8,{'weight':6.1, 'color':'yellow'}),  

		])

colors=[]

for i,j, attributes in G.edges(data=True):
    colors.append(attributes['color'])

pos=nx.spring_layout(G)
nx.draw_networkx(G, pos, width=2,font_weight='bold', edge_color=colors, node_size=400, font_size=10)
edge_labels = nx.get_edge_attributes(G, 'weight')

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)
plt.show()