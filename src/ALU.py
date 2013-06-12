'''
Created on Dec 16, 2012

@author: Danielle Tucker
@version: 2012 December
'''
import RippleCarryAdder

class ALU(RippleCarryAdder.RippleCarryAdder):
    '''
    classdocs
    '''

    def notALU(self, a):
        '''
        Takes a 16 bit integer (rest bitmasked off), sets instance variable a, b=0
        Determines the bitwise logical NOT of a and sets instance value of Result and Flags
        @param a: the value to perform the logical NOT on
        '''
        self.a = a & 0x0ffff
        self.b = 0
        self.result = ~self.a & 0x0ffff
        self.setFlags()
        #Ensure that only N and Z flag are set as Carry and overflow don't make sense in this context
        self.flags &= 0b01100  
        
    def andALU(self, a, b):
        '''
        Takes 2 16-bit integers (rest bitmasked off), sets the instance variables,
        performs a bitwise logical AND, sets the result and flag instance variables.
        @param a: 16 bit integer to AND
        @param b: 16 bit integer to AND
        '''
        bitmask = 0x0ffff
        self.a = a & bitmask
        self.b = b & bitmask
        self.result = self.a & self.a
        self.setFlags()
        #Ensure that only N and Z flag are set as Carry and overflow don't make sense in this context
        self.flags &= 0b01100  
        
    def orALU(self, a, b):
        '''
        Takes 2 16-bit integers (rest bitmasked off), sets the instance variables,
        performs a bitwise logical OR, sets the result and flag instance variables.
        @param A: 16 bit integer to OR
        @param B: 16 bit integer to OR
        '''
        bitmask = 0x0ffff
        self.a = a & bitmask
        self.b = b & bitmask
        self.result = self.a | self.b
        self.setFlags()
        #Ensure that only N and Z flag are set as Carry and overflow don't make sense in this context
        self.flags &= 0b01100  
        
    def negate(self, a):
        '''
        Takes a 16 bit integer (rest bitmasked off), sets instance variable a, b=0
        Determines the negation of a (-a) and sets instance value of Result and Flags
        @param a: the value to perform the negation on 
        '''
        self.a = a & 0x0ffff
        self.b = 0
        self.notALU(self.a)
        self.add(self.result, 1)
        #Don't need to explicitly set flags as add will do that
        #Ensure that only N and Z flag are set as Carry and overflow don't make sense in this context
        self.flags &= 0b01100
        
    def subtract(self, a, b):
        '''
        Takes 2 16-bit integers (rest bitmasked off), sets the instance variables,
        performs a - b, sets the result and flag instance variables.
        @param a: 16 bit integer value
        @param b: 16 bit integer to subtract from a
        '''
        bitmask = 0x0ffff
        self.b = b & bitmask
        self.negate(self.b)
        #self.a is overwritten in the negate function so need to define self.a afterwards!
        self.a = a & bitmask
        self.add(self.a, self.result)
        #Don't need to explicitly set flags because add will do that!
