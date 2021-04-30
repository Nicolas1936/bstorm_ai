class Person:
    name = 'Adam'

    def __repr__(self):
        return repr('Hello ' + self.name )

p = Person()

print(p.__dict__)