class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Other(object):

    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()    

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD BEFORE PARENT altered()"
        self.other.altered()
        print "CHILD, AFTER Other altered()"

# dad = Parent()
son = Child()

# dad.implicit()
son.implicit()

# dad.override()
son.override()

# dad.altered()
son.altered()
