"""This module contains unit tests for every method in loklak.py."""
from __future__ import print_function
import unittest
from loklak import Loklak
import os
import sys

class TestLoklak(unittest.TestCase):
    """Test class."""

    baseUrl = 'http://api.loklak.org/'

    def setUp(self):
        """Test proper setup."""
        self.loklak = Loklak(self.baseUrl)

    def test_status(self):
        """Test status."""
        result = self.loklak.status()

        self.assertTrue('index' in result)
        result_properties = [
            'messages', 'mps', 'users', 'queries',
            'accounts', 'user', 'followers', 'following'
        ]
        for prop in result_properties:
            self.assertTrue(
                prop in result['index'],
                msg='{} not found in index'.format(prop)
            )

        result = self.loklak.status("nonexisturl")
        self.assertEqual(result, "{}")

    def test_hello(self):
        """Test hello instance."""
        result = self.loklak.hello()
        self.assertEqual(result['status'], u'ok')

    def test_getBaseUrl(self):
        """Test base url."""
        result = self.loklak.getBaseUrl()
        self.assertEqual(result, self.baseUrl)

    def test_geocode(self):
        """Test geological features."""
        result = self.loklak.geocode()
        self.assertEqual(result, '{}')

        result = self.loklak.geocode(places=['Moscow'])
        self.assertTrue('locations' in result)
        self.assertTrue('Moscow' in result['locations'])
        self.assertEqual(
            'Russian Federation',
            result['locations']['Moscow']['country']
        )
        self.assertEqual(
            'Russian Federation',
            result['locations']['Moscow']['country']
        )
        self.assertTrue(
            isinstance(result['locations']['Moscow']['place'], list)
        )

    def test_get_map(self):
        """Test the get_map method."""
        map_file = os.path.join(os.getcwd(), 'markdown.png')
        data = self.loklak.get_map(17.582729, 79.118320)
        print(data)
        self.assertFalse(data[:8] == b'\211PNG\r\n\032\n' and
                        data[12:16] == b'IHDR')
        with open(map_file, 'w+') as file_handle:
            file_handle.write(data)
        with open(map_file, 'rb') as file_handle:
            file_contents = file_handle.read()
        self.assertTrue(os.path.exists(map_file))
        # self.assertEqual(data, file_contents)
        try:
            os.remove(map_file)
        except OSError as error:
            print(error)

    def test_peers(self):
        """Test finding peers."""
        result = self.loklak.peers()
        if (len(result['peers']) == 0):
            pass
        else:
            self.assertTrue('peers' in result)
            self.assertTrue(isinstance(result['peers'], list))
            self.assertTrue(len(result['peers']) >= 1)
            self.assertEqual(len(result['peers']), result['count'])

    def test_push(self):
        """Test for push data to index."""
        data={   "statuses": [     {       "id_str": "yourmessageid_1234",       "screen_name": "testuser",       "created_at": "2016-07-22T07:53:24.000Z",       "text": "The rain is spain stays always in the plain",       "source_type": "GENERIC",       "place_name": "Georgia, USA",       "location_point": [3.058579854228782,50.63296878274201],       "location_radius": 0,       "user": {         "user_id": "youruserid_5678",         "name": "Mr. Bob",       }     }   ] }
        result = self.loklak.push(data)
        self.assertTrue('status' in result)

    def test_user(self):
        """Test user."""
        result = self.loklak.user('dhruvRamani98')
        self.assertTrue('user' in result)
        self.assertTrue('name' in result['user'])
        self.assertTrue('screen_name' in result['user'])
        result = self.loklak.user("fossasia", 1500, 330)
        self.assertTrue('user' in result)
        self.assertTrue('name' in result['user'])
        result = self.loklak.user()
        self.assertTrue('error' in self.loklak.user())
        self.assertEqual(result, '{"error": "No user name given to query. Please check and try again"}')

    def test_search(self):
        """Test search result."""
        result = self.loklak.search('doctor who', count=18)
        self.assertTrue('statuses' in result)
        self.assertTrue(isinstance(result['statuses'], list))
        self.assertTrue(len(result['statuses']) >= 1)
        self.assertEqual(len(result['statuses']),
                         int(result['search_metadata']['maximumRecords']))
        self.assertEqual(int(result['search_metadata']['maximumRecords']), 18)

    def test_aggregations(self):
        """Test aggregations."""
        result = self.loklak.aggregations('fossasia', '2017-01-10',
                                          '2018-01-10', 10)
        data = result.json()
        self.assertEqual(result.status_code, 200)
        self.assertTrue('aggregations' in data)

        result = self.loklak.aggregations()
        self.assertEqual(result, '{"error": "No Query string has been given to run query for aggregations"}')
    #     self.assertTrue('hashtags' in data['aggregations'])
    #     self.assertTrue('mentions' in data['aggregations'])

if __name__ == '__main__':
    if len(sys.argv) > 1:
        TestLoklak.baseUrl = sys.argv.pop()
    unittest.main()
