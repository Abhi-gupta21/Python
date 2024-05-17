class animal:
    def __init__(self):
        self.eyes = 2

    def breath(self):
        print("inhale, exhale")


class fish(animal):

    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water")

    def breath(self):
        super().breath()
        print("doing this underwater")

nemo = fish()

nemo.swim()
nemo.breath()
print(nemo.eyes)