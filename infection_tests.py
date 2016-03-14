import unittest
from ka_interview_q import *

class TestUM(unittest.TestCase):

	def setUp(self):
		self.users_connections =[{"s_uid":1,"c_uid":3}
			, {"s_uid":4,"c_uid":4}
			, {"s_uid":2,"c_uid":3}
			, {"s_uid":2,"c_uid":6}
			, {"s_uid":3,"c_uid":4}
			, {"s_uid":5,"c_uid":6}
			, {"s_uid":7,"c_uid":8}
			]

		self.users_version = {1:'a', 2:'a', 3:'a', 4:'a', 5:'a', 6:'a', 7:'a', 8:'a'}

	def tearDown(self):
		self.users_connections = None
		self.users_version = None


### TESTS ON FIND_CONNECTIONS ####

	# Find_connections: Connection from student to coach.
	def test_find_connections_1(self):
		self.assertEqual( find_connections(1, self.users_connections), [1,3])

	# Find_connections: Connection from coach to student.
	def test_find_connections_8(self):
		self.assertEqual( find_connections(8, self.users_connections), [8,7])

	# Find_connections: Connection in both directions.
	def test_find_connections_3(self):
		self.assertEqual( find_connections(3, self.users_connections), [3,1,2,4])

	# Find_connections: Connected with self 
	def test_find_connections_4(self):
		self.assertEqual( find_connections(4, self.users_connections), [4,4,4,3])

	# Find_connections: Not in Users  
	def test_find_connections_9(self):
		self.assertFalse( find_connections(9, self.users_connections))


### TESTS ON TOTAL_INFECTION ####

	# Total: One level of infection occur.
	def test_total_7(self):
		self.assertEqual( total_infection(7, 'b', self.users_connections, self.users_version)
			, {1:'a', 2:'a', 3:'a', 4:'a', 5:'a', 6:'a', 7:'b', 8:'b'})

	# Total: Two levels of infection occur.
	def test_total_3(self):
		self.assertEqual( total_infection(3, 'b', self.users_connections, self.users_version)
			, {1:'b', 2:'b', 3:'b', 4:'b', 5:'b', 6:'b', 7:'a', 8:'a'})

	# Total: Three levels of infection occur.
	def test_total_1(self):
		self.assertEqual( total_infection(1, 'b', self.users_connections, self.users_version)
			, {1:'b', 2:'b', 3:'b', 4:'b', 5:'b', 6:'b', 7:'a', 8:'a'})

	# Total: Head not in users so change nothing.
	def test_total_9(self):
		self.assertEqual( total_infection(9, 'b', self.users_connections, self.users_version)
			, {1:'a', 2:'a', 3:'a', 4:'a', 5:'a', 6:'a', 7:'a', 8:'a'})

	# Total: Pass in bad head_uid.
	def test_total_x(self):
		self.assertEqual( total_infection('x', 'b', self.users_connections, self.users_version)
			, {1:'a', 2:'a', 3:'a', 4:'a', 5:'a', 6:'a', 7:'a', 8:'a'})

	# Total: Pass in bad head_uid.
	def test_total_str7(self):
		self.assertEqual( total_infection('7', 'b', self.users_connections, self.users_version)
			, {1:'a', 2:'a', 3:'a', 4:'a', 5:'a', 6:'a', 7:'a', 8:'a'})


### TESTS ON LIMITED_INFECTION ###

	# Limited: Goal is none, so nothing should change.
	def test_limited_3_0(self):
		self.assertEqual( limited_infection(3, 'c', 0, self.users_connections, self.users_version)
			, {1:'a', 2:'a', 3:'a', 4:'a', 5:'a', 6:'a', 7:'a', 8:'a'})

	# Limited: Two levels of infection could occur, but only one does.
	def test_limited_3_3(self):
		self.assertEqual( limited_infection(3, 'c', 3, self.users_connections, self.users_version)
			, {1:'c', 2:'c', 3:'c', 4:'c', 5:'a', 6:'a', 7:'a', 8:'a'})

	# Limited: Two levels of infection occur.
	def test_limited_3_6(self):
		self.assertEqual( limited_infection(3, 'c', 6, self.users_connections, self.users_version)
			, {1:'c', 2:'c', 3:'c', 4:'c', 5:'c', 6:'c', 7:'a', 8:'a'})

	# Limited: Three levels of infection could occur, but only two do. Ultimate num-of-changes is greater than goal.
	def test_limited_1_3(self):
		self.assertEqual( limited_infection(1, 'c', 3, self.users_connections, self.users_version)
			, {1:'c', 2:'c', 3:'c', 4:'c', 5:'a', 6:'a', 7:'a', 8:'a'})

	# Limited: Three levels of infection could occur, but only two do. Ultimate num-of-changes is equal to goal.
	def test_limited_1_4(self):
		self.assertEqual( limited_infection(1, 'c', 4, self.users_connections, self.users_version)
			, {1:'c', 2:'c', 3:'c', 4:'c', 5:'a', 6:'a', 7:'a', 8:'a'})

	# Limited: Three levels of infection occur.
	def test_limited_1_100(self):
		self.assertEqual( limited_infection(1, 'c', 100, self.users_connections, self.users_version)
			, {1:'c', 2:'c', 3:'c', 4:'c', 5:'c', 6:'c', 7:'a', 8:'a'})



if __name__ == '__main__':
	unittest.main()


