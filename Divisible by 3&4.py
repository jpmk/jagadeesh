import unittest

class Test_divisible(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(divis(100),"yes")
    def testcase_2(self):
        self.assertEqual(divis(50),"yes")

def divis(n):
    for i in range(n):
      if i % 3 == 0 and i % 4 == 0:
        return "yes"
      else:
        return "No"

if __name__=="__main__":
    unittest.main()
