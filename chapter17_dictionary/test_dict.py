import unittest
from unittest import TestCase
from dictionary import *

class TestDictionary(TestCase):
	def test_set(self):
		states = Dictionary()

		states.set('Oregon', 'OR')
		states.set('Florida', 'FL')
		states.set('California', 'CA')
		states.set('New York', 'NY')
		states.set('Michigan', 'MI')

		self.assertEqual(states.get('Oregon'), 'OR')
		self.assertEqual(states.get('Florida'), 'FL')
		self.assertEqual(states.get('California'), 'CA')
		self.assertEqual(states.get('New York'), 'NY')
		self.assertEqual(states.get('Michigan'), 'MI')

	def test_get(self):
		cities = Dictionary()

		cities.set('CA', 'San Francisco')
		cities.set('MI', 'Detroit')
		cities.set('FL', 'Jacksonville')
		cities.set('NY', 'New York')
		cities.set('OR', 'Portland')

		self.assertEqual(cities.get('MI'), 'Detroit')
		self.assertIsNone(cities.get('N/A'))

	def test_delete(self):
		cities = Dictionary()

		cities.set('CA', 'San Francisco')

		cities.delete('CA')

		self.assertIsNone(cities.get('CA'))


	def test_get_bucket(self):
		pass

	def test_get_slot(self):
		pass

	def test_hash_key(self):
		pass

	def test_list(self):
		pass


if __name__ == '__main__':
	unittest.main()