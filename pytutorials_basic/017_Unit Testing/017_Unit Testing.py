import unittest
import utestsupport


'''Basic Testing using unittest'''
class TestCalc(unittest.TestCase):

	def test_add(self):
		#ALL TESTS have to start with test. this is one test

		result = utestsupport.add(10,5)
		self.assertEqual(result,15)
		self.assertEqual(utestsupport.add(4, -2), 2)
		#.assertEqual() is a unittest method
		#tests whether adding using this function returns 15
		#adding extra checks does not increase the number of tests run

	def test_subtract(self):
		self.assertEqual(utestsupport.subtract(3,1), 2)
		#second test

	def test_divide(self):
		with self.assertRaises(ValueError):
			utestsupport.divide(10,0)
		#use context manager. checks for whether error is obtained


if __name__ == '__main__':
	unittest.main()
	#if module is run, run the code unittest.main()

#setUp and tearDown occurs before and after EACH test
#setUpClass and tearDownClass occurs before and after everything