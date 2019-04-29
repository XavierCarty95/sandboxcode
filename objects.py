class Program(): 
    
    def __init__(self,*args, **kwargs):
        
        self.lang = input('What language:')
        self.version = float(input("Version?"))
        self.skill = input("What skill level")
        
    def upgrade(self):
        new_version = input('What version?:')
        print("We have update the version for",self.lang)
        self.version 
        
p1 = Program() 
p2 = Program() 