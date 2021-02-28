import unittest

class TestS3(unittest.TestCase):
    def test_bucket_name_value(self):
        bucket = 'snetcloudnative'

        self.assertEqual(bucket, 'snetcloudnative')

    def test_region_value(self):
        region = 'us-west-1'

        self.assertEqual(region, 'us-west-1')

    def test_bucket_name_is_string(self):
        bucket = 'snetcloudnative'

        self.assertTrue(type(bucket), str)

    def test_region_is_string(self):
        region = 'us-west-1'

        self.assertTrue(type(region), str)

if __name__ == '__main__':
    unittest.main()