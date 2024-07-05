#Multi-level inheritance

class GrandFather:
    def music(self):
        print("Ability to sing")

class Father(GrandFather):
    def dance(self):
        print("Ability to dance")

class Son(Father):
    def act(self):
        print("Ability to act")

son = Son()
son.music()
son.dance()
son.act()