def singleton(cls):    
    instance = [None]
    def wrapper(*args, **kwargs):
        if instance[0] is None:
            print("Creating new connection.")
            instance[0] = cls(*args, **kwargs)
        else:
            print("Reusing existing connection.")
        return instance[0]

    return wrapper


@singleton
class DBConnection():
    def __init__(self, con_name):
        self.con_name = con_name

instance1 = DBConnection('conn') 
print(instance1.con_name)
instance2 = DBConnection('conn1')
print(instance2.con_name) 