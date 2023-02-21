import unittest

class Test_Alternate(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(Average([20,30,40,50,10]),30)
    def testcase_2(self):
        self.assertEqual(Average([5,10,30]),15)

def Average (k):
 sum = 0
 for i in k:
    sum=sum+i
 return (sum/len(k))


if __name__=="__main__":
    unittest.main()
