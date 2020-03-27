from random import randrange

class DNA:
    def __init__(self, parent=""):
        #   двигаться вправо - 0
        #   двигаться прямо  - 1
        #   двигаться влево - 2
        #   двигаться назад - 3

        #   атаковать - 4
        #   кушать - 5
        #   стоять - 6
        #   отпочковаться - 7

        if parent == "":
            self.pain = [] * 4

            for direction in range(0, 4):
                self.pain[direction] = []

                self.pain[direction]["none"] = randrange(0, 6)
                self.pain[direction]["food"] = randrange(0, 6)
                self.pain[direction]["meat"] = randrange(0, 6)
                self.pain[direction]["cell"] = randrange(0, 6)
                self.pain[direction]["devide"] = randrange(0, 6)

            self.action = [] * 5

            for action in range(0, 5):
                self.action[action] = []

                self.action[action]["none"] = randrange(0, 6)
                self.action[action]["food"] = randrange(0, 6)
                self.action[action]["meat"] = randrange(0, 6)
                self.action[action]["cell"] = randrange(0, 6)
                self.action[action]["devide"] = randrange(0, 6)