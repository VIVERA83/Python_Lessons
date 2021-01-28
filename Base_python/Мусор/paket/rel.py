class Pupok:

    def __init__(self):
        self.y = 5

    def decorator(self, function):
        x = self.y
        def wropper(*args):
            nonlocal x
            x += 1
            if x < 5:
                return function(*args)
            else:
                print(x)
            if x > 7:
                x = 0
        return wropper

    @decorator.
    def privet(self, st):
        print(st)
        return st


p = Pupok()
for i in range(11):
    print(p.privet('что делать'))
