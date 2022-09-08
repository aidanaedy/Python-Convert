class Getter():
    
    
    def __init__(self, name):
        self.name = name
      
    x = 10
    
    
    def xget(self, x):
        return (x)
        
    def xset(self, x):
        self.x=(x+1)
        print(f"inside xset method = {x}")
        
""" class names start with a capital letter and are camel case        
such as MethodOne or MainClass etc. """      
class Animal():
    def speak(self):
        return "growl"
        
class Dog():
    def speak(self):
        return "bark"


def main():
    print(f"main method {getx.x}")
    menu()


def menu():
    print ("menu method")
    print(f"calling manually and specifying a number {getx.xset(15)}")


getx = Getter("Aidan")
getx2 = Getter("Pauline")
getx3 = Getter("Eleanor")
getx4 = Getter("Harriet")

aspeak = Animal()
dspeak = Dog()


# this is the first calling of the class getx using the getter.x value (10) 
print(f"printing manually calling the variable getter.x {getx.xset(Getter.x)}")

# we then set the value with the setter method to 25 & 45. 
# The setter method prints the new value and increments by 1
getx.xset(25)
getx.xset(45)

# the main method prints the new incremented value of x and then calls the menu method
# the menu method prints "menu method and then ca"
main()
print(f"is it 10 again?{getx.xget(Getter.x)}")
print(f"last {getx.x}")
# getx.xset(getx.x+1)
print(40 * "_")

# doggie == animal.speak

print(f"animal says {aspeak.speak()}")
print(getx.name, "= name1, ", getx2.name, "= name2, ", getx3.name, "= , ", getx4.name, "= name4")
print(f"dog says {dspeak.speak()}")
doggie= dspeak.speak()
print(f"{doggie} says the dog")


