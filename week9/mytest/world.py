# Testing reusable code.

def func3():
    print "Func3 - World"

def main():
    print "Main - World"

class MyClass(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def hello(self):
        print self.x, self.y, self.z

    def not_hello(self):
        print self.x + self.y, self.z

class ChildClass(MyClass):
    def hello(self):
        print self.x + self.y + self.z    

if __name__ == "__main__":
    main()

