import unittest


class Test_element(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(element1([1,2,3,4,5,6,7,8,9,10,11,12]),[2,4,6,8,10,12])
    def testcase_2(self):
        self.assertEqual(element2([1,2,3,4,5,6,7,8,9,10,11,12]),[1,3,5,7,9,11])                   

def element1(k):
    j = []
    for i in k:
        if (i%2==0):
            j.append(i)
    return(j)

def element2(k):
    p = []
    for i in k:
        if (i%2!=0):
            p.append(i)
    return(p)
        
if __name__=="__main__":
    unittest.main()

