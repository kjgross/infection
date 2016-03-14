import networkx as nx
import matplotlib.pyplot as plt
from infection import *


users_connections =  [{"s_uid":1,"c_uid":3}
	, {"s_uid":4,"c_uid":4}
	, {"s_uid":2,"c_uid":3}
	, {"s_uid":2,"c_uid":6}
	, {"s_uid":3,"c_uid":4}
	, {"s_uid":5,"c_uid":6}
	, {"s_uid":7,"c_uid":8}
	]

users_version = {1:'a', 2:'a', 3:'a', 4:'a', 5:'a', 6:'a', 7:'a', 8:'a'}

def infect():
	head_user_id = input('Which user would you like to infect first? ')
	goal = input('If you want to run total_infection, type None, otherwise, tell me your upper bound for the number of users you want to infect. ')
	if not goal:
		return total_infection(head_user_id, 'b', users_connections, users_version)
	else:
		return limited_infection(head_user_id, 'b', goal, users_connections, users_version)


def viz(users_connections, users_version):
	G=nx.Graph()
	G.add_nodes_from(users_version)

	colors = []
	for n in G.nodes():
		if users_version[n] == 'a':
			colors.append('g')
		else:
			colors.append('b')

	edges_to_add = []
	for i in users_connections:
		edges_to_add.append((i["s_uid"], i["c_uid"]))
	G.add_edges_from(edges_to_add)

	nx.draw(G, node_color = colors, with_labels=True, )
	plt.show()

def main():
	viz(users_connections, users_version)
	new_users_versions = infect()
	viz(users_connections, new_users_versions)



main()
