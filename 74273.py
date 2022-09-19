
class HC74273:

    CLK = Undefined
    OE = Undefined
    IN = Undefined
    OUT = Undefined

    def setDIN(self,data,clk):
        if clk == RAISE:
            self.data = data 

    def setDOU(self,oe):
        self.OE = oe 
        if self.OE == LOW:
            self.OUT = self.IN
