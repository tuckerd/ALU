'''
Created on Dec 16, 2012

@author: Danielle
'''
import unittest
import RippleCarryAdder


class Test(unittest.TestCase):


    def setUp(self):
        self.rca = RippleCarryAdder.RippleCarryAdder()

    def testAddNO(self):
        '''
        Test of adding with negative and overflow result
        '''
        self.rca.add(0x70b0, 0x41aa)
        self.assertEqual(0xb25a, self.rca.result)
        self.assertEqual(0x9, self.rca.flags)
    
    def testAddCO(self):
        '''
        Test of adding with carry out bit and overflow
        '''
        self.rca.add(0xa123, 0x8001)
        self.assertEqual(0x2124, self.rca.result)
        self.assertEqual(0x03, self.rca.flags)
        
    def testAdd(self):
        '''
        Test of adding with no flags set
        '''
        self.rca.add(0x2, 0x1)
        self.assertEqual(0x03, self.rca.result)
        self.assertEqual(0x0, self.rca.flags)
        
    def testAddZ(self):
        '''
        Test of adding with zero flag set
        '''
        self.rca.add(0x02, 0xfffe)
        self.assertEqual(0x0, self.rca.result)
        self.assertEqual(0x6, self.rca.flags)
    
    def testBitErrors(self):
        self.assertRaises(ValueError, RippleCarryAdder.getBitAt, 0x0, 30)
        self.assertRaises(ValueError, RippleCarryAdder.setBitAt, 0x0, 3, 5)
        self.assertRaises(ValueError, RippleCarryAdder.setBitAt, 0x0, 1, 30)
        
    '''
    test_ripple.add(0x70b0, 0x41aa)
    print test_ripple

    test_ripple.add(0x0a123, 0x8001)
    print test_ripple

    test_ripple.add(0xa123, 0x7001)
    print test_ripple

    test_ripple.add(0x0, 0x0)
    print test_ripple 
    
    test_ripple.add(0xfffc, 0x001)
    print test_ripple   
    '''


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()