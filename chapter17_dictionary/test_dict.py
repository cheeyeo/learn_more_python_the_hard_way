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
		tmp = Dictionary()
		key = tmp.hash_key('test')
		self.assertEqual(tmp.get_bucket('test'), tmp.map.get(key))
		self.assertIsInstance(tmp.get_bucket('test'), DoubleLinkedList)

	def test_get_slot(self):
		d = Dictionary(num_buckets=1)
		b, s = d.get_slot('test')
		self.assertEqual(b, d.map.get(d.hash_key('test')))
		self.assertIsNone(s)

		d.set('test', 1)

		b, s = d.get_slot('test')
		self.assertEqual(b, d.map.get(d.hash_key('test')))
		self.assertEqual(s, b.begin)
		self.assertEqual(s.value[0], 'test')
		self.assertEqual(s.value[1], 1)

	# TODO: Fix the test below to mock hash()
	def test_hash_key(self):
		d = Dictionary(num_buckets=2)
		k = d.hash_key('test')
		self.assertEqual(k, 1)
		k = d.hash_key('test2')
		self.assertEqual(k, 1)


if __name__ == '__main__':
	unittest.main()