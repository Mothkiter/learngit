class Person:

    bio = "human"

    def __init__(self,name,gender,sex,age,color,bio):
        self.name = name
        self.gendr = gender
        self.sex = sex
        self.age = age
        self.color = color
        self.b = bio
    
    def ruSWM(self):
        if self.gendr == 'male' and self.sex == 'male' and self.color=="white":
            print("U r a fucking straight white man")
        else:
            print("bro")