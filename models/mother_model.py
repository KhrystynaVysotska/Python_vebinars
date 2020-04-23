from abc import ABC, abstractmethod


class AbstractParent(ABC):

    @abstractmethod
    def hello_friend(self):
        raise NotImplementedError

    @abstractmethod
    def cook(self):
        raise NotImplementedError


class Mother(AbstractParent):
    def __init__(self, age):
        self.age = age
        print("Mother constructor")

    def do_work(self):
        print("I`m working")

    def do_house_work(self):
        print("listening to music")

    def cook(self):
        print("Supper is ready!")


class Father(AbstractParent):
    def __init__(self):
        print("Father constructor")

    def play_guitar(self):
        print("play guitar")

    def do_house_work(self):
        print("sitting on the sofa and drink beer")


class Daughter(Father, Mother):
    def __init__(self, age=0):
        Mother.__init__(self, age=age)
        Father.__init__(self)

    def do_work(self):
        print("I`m working like a horse")

    def play_guitar(self):
        print("daughter plays")

    def hello_friend(self):
        pass


class Friend:
    pass


def greet_mother(mother: Mother):
    print("hello mother!!!!!")
    mother.do_work()


def greet_father(father: Father):
    print("time for beer!")
    father.play_guitar()


if __name__ == "__main__":
    daughter = Daughter()
    # mother.do_work()

    # change parents
    # daughter.__class__ = Father, Mother
    greet_mother(daughter)
    greet_father(daughter)
    daughter.hello_friend()
    daughter.do_house_work()

    for x in [daughter]:
        x.do_house_work()
    # list
    my_list = ["mathan_2", "programming_2", "superprise"]

    # tuple
    vasian = ("11 years", 12, 3.14, daughter)

    # set
    my_set = {23, 11, 10, 10, 10, 10, "call"}
    print(my_set)

    # frozen set
    another_set = frozenset(["di_", "mi", "do"])

    # dictionary
    my_dict = {1: "first", "2": 123, (1, 2, 3): "tuple_as_a_key"}
