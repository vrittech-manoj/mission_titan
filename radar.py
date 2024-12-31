import random

command =input("Enter the Command[Auto/Manual]")
if command =="Auto":
    
        class Radar_auto:

            def __init__(self): 
                self.found = random.randint(1,3)        

            #check the condition for identify the object            
            def object_detection(self):
                if self.found == 1:
                    return("Object Found!!!") 
                elif self.found ==2:
                    return("Astroid Found!!!")
                elif self.found==3:
                    return("Commit Found!!!")         
            
            #Display object_detection Result
            def object_display(self): 
                print(self.object_detection())
            

        class Measure(Radar_auto):
        
            def __init__(self):
                self.distance =random.randint(1,1000)
                self.side =random.randint(10,13)
                Radar_auto.__init__(self)  
                
        
            
            def direction(self):
                if self.side==10:
                    return(f"The Direction Right and Distance is: {self.distance} Miter")
                
                elif self.side==11:
                    return (f"The Direction Left and Distance is: {self.distance} Miter")
                    
                elif self.side==12:
                    return(f"The Direction top and Distance is: {self.distance} Miter")
                
                elif self.side==13:
                    return(f"The Direction bottom and Distance is: {self.distance} Miter")
                
            
            #display direction result   
            def display(self): 
                self.object_display()
                print(self.direction())
        
        m =Measure()
        m.display()
    
else:
    print("!!!Wrong Command!!!")

