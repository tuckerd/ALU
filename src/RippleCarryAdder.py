'''
Created on Dec 15, 2012

@author: Danielle
'''
import FullAdder

class RippleCarryAdder(object):
    '''
    classdocs
    '''
    REGISTER_BIT_SIZE = 16
    FLAG_O = 0x1
    FLAG_C = 0x2
    FLAG_Z = 0x4
    FLAG_N = 0x8


    def __init__(self):
        '''
        Constructor
        '''
        self.adders = []
        for _i in range(self.REGISTER_BIT_SIZE):
            self.adders.append(FullAdder.FullAdder())
        self.a = 0b0
        self.b = 0b0
        self.result = 0b0
        self.flags = 0b0
    
    def add(self, A, B):
        '''
        Takes 2 16-bit integers (rest bitmasked off), sets the instance variables,
        adds them, sets the result and flag instance variables.
        @param A: 16 bit integer to add
        @param B: 16 bit integer to add
        '''
        bitmask = 0x0ffff
        A = A & bitmask
        B = B & bitmask
        self.a = A
        self.b = B
        
        self.adders[0].add(getBitAt(A, 0), getBitAt(B, 0))
        for index in range(1,self.REGISTER_BIT_SIZE):
            self.adders[index].add(getBitAt(A, index), getBitAt(B, index), self.adders[index - 1].carry_out)
            
        self.result = 0b0
        for index in range(self.REGISTER_BIT_SIZE):
            if self.adders[index].result == 1:
                self.result = setBitAt(self.result, self.adders[index].result, index)
                    
        self.setFlags()
        
    def setFlags(self):
        self.flags = 0
        
        #Check for overflow - Overflow if neg + neg = pos OR pos + pos = neg
        sign_a = getBitAt(self.a, self.REGISTER_BIT_SIZE-1)
        sign_b = getBitAt(self.b, self.REGISTER_BIT_SIZE-1)
        sign_result = getBitAt(self.result, self.REGISTER_BIT_SIZE-1)
        if sign_a != sign_result and sign_b != sign_result:
            self.flags |= self.FLAG_O
        
        #Check for carry_out - last adder has a carry out bit
        if self.adders[self.REGISTER_BIT_SIZE-1].carry_out == 1:
            self.flags |= self.FLAG_C
            
        #Check for negative result
        if sign_result == 1:
            self.flags |= self.FLAG_N
        
        #Check for zero result
        result = 0
        for adder in self.adders:
            result |= adder.result
        if self.result == 0:
            self.flags |= self.FLAG_Z 
    
    def __repr__(self):
        return "0x{:04x} + 0x{:04x} = 0x{:04x} Flags = {:04b}".format(self.a, self.b, self.result, self.flags)
            
    def flagKey(self):
        '''
        @return: Returns a string describing how to understand the flag notation
        '''
        return "Key to Flags [NZCO]: Negative Flag = 1000, Zero Flag = 0100, " + \
                "Carry Out Flag = 0010, Overflow Flag = 0001\n"

    
def getBitAt(value, bit_number):
    '''
    Check if bit is turned on in a value
    @param value: the value to check
    @param bit_number: the bit to check (uses convention right-most bit is 0)
    @return: 1 if bit is on and 0 if bit is off
    '''
    if bit_number >= 16 or bit_number < 0:
        raise ValueError, "Invalid bit number"

    mask = 0b001 << bit_number
    if (value & mask) > 0:
        return 1
    else:
        return 0
            
def setBitAt(value_in, bit_value, bit_number):
    '''
    Sets a bit in a value to the given 1 or
    @param value_in: the value to modify
    @param bit_value: the value (1 or 0) to change the bit to
    @param bit_number: the bit to modify (uses convention right-most bit is 0)
    @return: the value_in changed with bit_number set to value.  If invalid value or bit given returns "ERROR"
    '''
    if bit_value not in (0, 1):
        raise ValueError, "Value %d is not a 0 or 1" % bit_value
    if bit_number >= 16 or bit_number < 0:
        raise ValueError, "Invalid bit number"
    
    return value_in | (bit_value << bit_number)
