'''
Created on Dec 16, 2012

@author: Danielle
'''
import unittest
from ALU import ALU


class Test(unittest.TestCase):
    '''[nzco]'''

    def setUp(self):
        self.ALU = ALU()

    def testAnd(self):
        self.ALU.andALU(0x1111, 0x0000)
        self.assertEqual(0x1111, self.ALU.result)
        self.assertEqual(0x00, self.ALU.flags)
    
    def testOr(self):
        self.ALU.orALU(0xfff1, 0x0002)
        self.assertEqual(0xfff3, self.ALU.result)
        self.assertEqual(0x8, self.ALU.flags)
        
    def testNot(self):
        self.ALU.notALU(0xffff)
        self.assertEqual(0x0, self.ALU.result)
        self.assertEqual(0x4, self.ALU.flags)

    def testNegate(self):
        self.ALU.negate(0xffff)
        self.assertEqual(0x01, self.ALU.result)
        self.assertEqual(0x0, self.ALU.flags)
        
    def testSubtract(self):
        self.ALU.subtract(0x07, 0x02)
        self.assertEqual(5, self.ALU.result)
        self.assertEqual(0x02, self.ALU.flags)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()