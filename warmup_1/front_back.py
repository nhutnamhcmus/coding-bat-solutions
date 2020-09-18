"""
Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""

import unittest


##########################
def front_back(str):
  return str[len(str)] + str[1:] + str[0]


############# TESTING CLASS ############# 
class Test(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()