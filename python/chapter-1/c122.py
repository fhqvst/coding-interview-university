import unittest

def dot_product(a, b):
    if len(a) is not len(b):
        raise ValueError('dimension mismatch')

    c = []
    for i in range(len(a)):
        c.append(a[i] * b[i])
    
    return c

class Test(unittest.TestCase):

    def test_works(self):
        self.assertEqual(dot_product([1, 2, 3], [4, 5, 6]), [4, 10, 18])

    def test_invalid_dimension(self):
        self.assertRaises(ValueError)


unittest.main()
