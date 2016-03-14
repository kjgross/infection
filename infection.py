import unittest

def find_connections(head_uid, users_connections):
	connected = []
	for row in users_connections:
		if row['c_uid'] == head_uid:
			connected.append(row['s_uid'])
		if row['s_uid'] == head_uid:
			connected.append(row['c_uid'])
	if len(connected) > 0:
		connected.insert(0, head_uid)
	return connected


def find_network(head_uid, network, checknext, goal, users_connections):
	connected = find_connections(head_uid, users_connections)
	for i in connected:
		# if we have not yet already checked this user
		if i not in network:
			network.append(i)
			# and we have not yet noted to check this user in the future 
			if i not in checknext:
				checknext.append(i)
	# we have hit our limit so return
	if goal and len(network) >= goal:
		return network
	# keep checking connection's connections
	else:
		if len(checknext) > 1:
			find_network(checknext[0], network, checknext[1:], goal, users_connections)
		elif len(checknext) == 1:
			find_network(checknext[0], network, [], goal, users_connections)
		return network


def total_infection(head_uid, new_version, users_connections, users_version):
	network = []
	checknext = []
	usr_network = find_network(head_uid, network, checknext, None, users_connections)
	for i in usr_network:
		users_version[i] = new_version
	return users_version


def limited_infection(head_uid, new_version, goal, users_connections, users_version):
	network = []
	checknext = []
	if goal == 0:
		usr_network = []
	else:
		usr_network = find_network(head_uid, network, checknext, goal, users_connections)
	for i in usr_network:
		users_version[i] = new_version
	return users_version
