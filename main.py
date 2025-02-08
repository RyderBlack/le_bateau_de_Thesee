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
            print(part)
            
    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            self.__parts[part_name] = new_part