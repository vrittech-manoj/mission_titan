import random
 
 
class comets:
    def __init__(self,velocity,size,destruction,position_x,position_y):
        self.velocity=velocity
        self.size=size
        self.destruction=destruction
        self.position_x=position_x
        self.position_y=position_y

    def destruction(self,destruction):
        self.destruction-=destruction
        if self.destruction<=0:
            self.destruction=random.randint(0,200)
            return self.destruction
 
    def size(self,size):
        self.size=size
        self.size=random.randint(20,62)
        return self.size
 
    def velocity(self,velocity):
        self.velocity=velocity
        self.velocity=random.randint(22000,45000)
        return self.velocity
   
 
    def x_position(self,position_x):
        self.position_x=position_x
        self.position_x=random.randint()----------
        return self.position_x
   
    def y_position(self,position_y):
        self.position_y=position_y
        self.position_y=random.randint(height of the screen)----------
        return self.position_y
   
    def random_value(velocity,size,destruction,position_x,position_y):
        return random.randint(velocity,size,destruction,position_x,position_y)
   
   
   
class aestroids:
    def __init__(self,velocity,size,destruction,position_x,position_y):
        self.velocity=velocity
        self.size=size
        self.destruction=destruction
        self.position_x=position_x
        self.position_y=position_y
 
    def destruction(self,destruction):
        self.destruction-=destruction
        if self.destruction<=0:
            self.destruction=random.randint(0,200)
            return self.destruction
 
    def size(self,size):
        self.size=size
        self.size=random.randint(20,62)
        return self.size
 
    def velocity(self,velocity):
        self.velocity=velocity
        self.velocity=random.randint(22000,45000)
        return self.velocity
   
 
    def x_position(self,position_x):
        self.position_x=position_x
        self.position_x=random.randint(width of the screen)----------
        return self.position_x
   
    def x_position(self,position_y):
        self.position_y=position_y
        self.position_y=random.randint(height of the screen)----------
        return self.position_y
 
 
    def random_value(velocity,size,destruction,position_x,position_y):
        return random.randint(velocity,size,destruction,position_x,position_y)