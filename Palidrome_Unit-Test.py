import unittest

class jagadeesh(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(palindrome("malayalam"),True)
    def testcase_2(self):
        self.assertEqual(palindrome("malay"),False)
    def testcase_3(self):
        self.assertEqual(palindrome("2332"),True)
    def testcase_4(self):
        self.assertEqual(palindrome("jagadeesh"),False)

def palindrome(str1):
    rev=""
    for i in str1:
        rev=i+rev
    if str1==rev:
        return True
    else:
        return False

if __name__=="__main__":
    unittest.main()
