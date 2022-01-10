class Freight_train():
    def __init__(self, locomotive_make, locomotive_model, locomotive_count, cargo_type):
        self.set_locomotive_make(locomotive_make)
        self.set_locomotive_model(locomotive_model)
        self.set_locomotive_count(locomotive_count)
        self.set_cargo_type(cargo_type)
    
    def move(self, place):
        print(f"Freight train moves to {place}")
    
    def stop(self):
        print("Freight train stopped")

    def get_locomotive_make(self):
        return self.__locomotive_make
    
    def get_locomotive_model(self):
        return self.__locomotive_model
    
    def get_locomotive_count(self):
        return self.__locomotive_count
    
    def get_cargo_type(self):
        return self.__cargo_type
    
    def set_locomotive_make(self, locomotive_make):
        self.__locomotive_make = locomotive_make
    
    def set_locomotive_model(self, locomotive_model):
        self.__locomotive_model = locomotive_model
    
    def set_locomotive_count(self, locomotive_count):
        self.__locomotive_count = locomotive_count
    
    def set_cargo_type(self, cargo_type):
        self.__cargo_type = cargo_type
        
    locomotive_make = property(get_locomotive_make, set_locomotive_make)
    locomotive_model = property(get_locomotive_model, set_locomotive_model)
    locomotive_count = property(get_locomotive_count, set_locomotive_count)
    cargo_type = property(get_cargo_type, set_cargo_type)

f_tr1 = Freight_train("НЭВЗ", "ВЛ80", 5, "petrol")
print(f_tr1.locomotive_make, f_tr1.locomotive_model, f_tr1.locomotive_count, f_tr1.cargo_type)
f_tr1.move("Novosibirsk")
f_tr1.stop()