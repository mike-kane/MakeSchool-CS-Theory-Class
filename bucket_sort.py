import unittest


def bucket(list):
    """Assume list contains only integers in range [0, 10] """
    result = []
    #  create buckets
    #  assign list items to each bucket
    buckets = [[] for x in range(0,11)]
    for number in list:
        buckets[number].append(number)
    for bucket in buckets:
        result.extend(bucket)

    return result



class TestSorting(unittest.TestCase):
    def test_bucket_sort(self):
        list = [1,5,4,7, 6, 8, 4, 2, 9, 1, 5, 4, 6, 8]
        expected_result = sorted(list)
        bucket_sorted = bucket(list)
        print('original list: ', list)
        print('sorted list: ', bucket_sorted)
        self.assertEqual(bucket_sorted, expected_result)

if __name__ == '__main__':
    unittest.main()
