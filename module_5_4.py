class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        house_name = args[0]
        cls.houses_history.append(house_name)
        instance = super(House, cls).__new__(cls)
        return instance

    def __init__(self, name, second=None, third=None):
        self.name = name
        self.second = second
        self.third = third

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

if __name__ == "__main__":
    house1 = House("ЖК Ключи", second=25, third=3.14)
    print(House.houses_history)
    house2 = House("ЖК Березовый", second=30, third=2.71)
    print(House.houses_history)
    house3 = House("ЖК Малиновка", second=15, third=1.41)
    print(House.houses_history)

    del house2
    del house3

    print(House.houses_history)