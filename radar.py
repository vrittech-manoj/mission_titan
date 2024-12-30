import random

class Radar:
    # it check is object ,astroid ,commet 
    def __init__(self,found):
        self.found = found
        pass
    
        #check the condition for identify the objects
        if self.found == "1":
            self.check_object()
        elif self.found =="2":
            self.check_astroid()
        elif self.found=="3":
            self.check_commit()

    def check_object(self):
        print("Object Functions Call")
        pass
    
    def check_astroid(self):
        print("Astroid Functions call")
        pass
    
    def check_commit(self):
        print("Commit Functions call")
        pass
    
    
found =random.randint(1,3) #random number ge
rd =Radar(str(found)) #create a object of Radar Class

