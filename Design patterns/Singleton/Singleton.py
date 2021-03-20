class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print("Creating new connection.")
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        else:
            print("Reusing existing connection.")
        return cls._instances[cls]


class DBConnection(metaclass=SingletonMeta):
    def __init__(self, con_name):
        self.con_name = con_name


if __name__ == "__main__":
    s1 = DBConnection('conn')
    print(s1.con_name)
    s2 = DBConnection('conn1')
    print(s1.con_name)

    if id(s1) == id(s2):
        print("Both connection are same.")
