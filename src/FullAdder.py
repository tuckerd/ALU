'''
Created on Dec 15, 2012

@author: Danielle
'''

class FullAdder(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.a = 0
        self.b = 0
        self.carry_in = 0
        self.carry_out = 0
        self.result = 0

    def add(self, a, b, carry_in = 0):
        ''' 
        Sets instance variables a, b, and carry_in. 
        Adds bit a and bit b and carry_in bit.
        Sets instance variables with result and carry_out bit
        @param a: the first bit to add (all bits except 0 bit are masked off)
        @param b: the second bit to add (all bits except 0 bit are masked off)
        @param carry_in: the carry_in (optional) bit from any previous calculation
        '''
        bitMask = 0b01
        a = bitMask & a
        b = bitMask & b
        carry_in = bitMask & carry_in
        
        self.a = a
        self.b = b
        self.carry_in = carry_in
        
        gate_1 = ~a & ~b & carry_in
        gate_2 = ~a & b & ~carry_in
        gate_3 = ~a & b & carry_in
        gate_4 = a & ~b & ~carry_in
        gate_5 = a & ~b & carry_in
        gate_6 = a & b & ~carry_in
        gate_7 = a & b & carry_in
        
        self.carry_out = gate_3 | gate_5 | gate_6 | gate_7
        self.result = gate_1 | gate_2 | gate_4 | gate_7
    
    def __repr__(self):
        return "FullAdder: a = %d b = %d carry_in = %d result = %d carry_out = %d" \
                % (self.a, self.b, self.carry_in, self.result, self.carry_out)  
                
if __name__ == "__main__":    
    test_adder = FullAdder()
    for a in range(2):
        for b in range(2):
            for carry_in in range(2):
                test_adder.add(a, b, carry_in)
                print test_adder
