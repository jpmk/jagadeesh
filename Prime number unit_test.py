import unittest


class Test_prime(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(variable([1,2,3,4,5,6,7,8,9,10,11,12]),(12,11))

def variable(k):
    j = []
    p = []
    for i in k:
        if (i%2==0):
            j.append(i)
        else:
            p.append(i)
    j.sort()
    p.sort()
    a=j[-1]
    b=p[-1]
    return(a,b)
   
if __name__=="__main__":
    unittest.main()
