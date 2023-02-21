import unittest


class Test_element(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(element([1,2,3,4]),"present")

def element(k):
    if 2 in k:
        return "present"
    else:
        return "not present"
        
if __name__=="__main__":
    unittest.main()

