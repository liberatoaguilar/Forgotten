class rec:
    def __init__(self,item1,Torf,result):
        self.Torf = Torf
        if self.Torf:
            self.item1 = item1.split()[0]
            self.item2 = item1.split()[1]
        else:
            self.item1 = item1
        self.result = result
appsa = rec("Apple Water",True,"AppleSauce")
stick = rec("Wood",False,"Stick")
board = rec("Wood Wood",True,"Board")
boat = rec("Resin Board",True,"Boat")
axe = rec("Axehead Stick",True,"Axe")
numrec = 5
