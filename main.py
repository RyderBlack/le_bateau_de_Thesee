class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material
        
    def change_material(self, new_material):
        self.material = new_material
        return self.material
    
    def __str__(self):
        return f"Here is the {self.name} with a {self.material} material."
    
    
class Ship:
    def __init__(self, ship_name):
        self.ship_name = ship_name
        self.__parts = {}
        
    def display_state(self):
        for part_name, part in self.__parts.items():
            print(f"Part '{part_name}': {part}")
            
    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            self.__parts[part_name] = new_part
            
    def change_part(self, part_name, new_material):
        if part_name in self.__parts:
            self.__parts[part_name].change_material(new_material)
  

class RacingShip(Ship):
    def __init__(self, ship_name, max_speed):
        super().__init__(ship_name)
        self.max_speed = max_speed
        
    def display_speed(self):
        print(f"The maximum speed of {self.ship_name} is {self.max_speed} knots")
 
            
ship_01 = Ship("Titanic")
part_001 = Part("Mast", "Wood")
ship_01._Ship__parts["mast"] = part_001 

print(part_001) 
ship_01.change_part("mast", "Steel")
print("\nWe have changed the part's material:")
print(part_001)  

racing_ship = RacingShip("SpeedBoat", 50)
print("\nRacing Speed:")
racing_ship.display_speed()