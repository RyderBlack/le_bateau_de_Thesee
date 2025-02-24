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
        self.history = [] 
        
    def display_state(self):
        if not self.__parts:
            print(f"\nNo parts have been added to {self.ship_name} yet.")
            return
        
        print(f"\nCurrent state of {self.ship_name}:")
        for part_name, part in self.__parts.items():
            print(f"Part '{part_name}': {part}")
            
            
    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            self.__parts[part_name] = new_part
            
    def change_part(self, part_name, new_material):
        if part_name in self.__parts:
            self.__parts[part_name].change_material(new_material)
            
    def add_part(self, part_name, part):
        self.__parts[part_name] = part
        self.history.append(f"Added new part: {part_name}")
  
    def display_history(self):
        if not self.history: 
            print("\nNo modifications have been made yet.Please come back later!")
            return
            
        print("\nModification History:")
        for i, event in enumerate(self.history, 1):
            print(f"{i}. {event}")

class RacingShip(Ship):
    def __init__(self, ship_name, max_speed):
        super().__init__(ship_name)
        self.max_speed = max_speed
        
    def display_speed(self):
        print(f"The maximum speed of {self.ship_name} is {self.max_speed} knots")
 
def interactive_menu(ship):
    while True:
        print("\n*===* Ship Management Menu *===*")
        print("1. Add new part")
        print("2. Replace part")
        print("3. Change part material")
        print("4. Display ship state")
        print("5. Display modification history")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        match choice:
            case "1":
                name = input("Enter part name: ")
                material = input("Enter part material: ")
                new_part = Part(name, material)
                ship.add_part(name.lower(), new_part)
                print("Part added successfully!")

            case "2":
                part_name = input("Enter part name to replace: ").lower()
                new_name = input("Enter new part name: ")
                new_material = input("Enter new part material: ")
                new_part = Part(new_name, new_material)
                ship.replace_part(part_name, new_part)
                print("Part replaced successfully!")

            case "3":
                part_name = input("Enter part name: ").lower()
                new_material = input("Enter new material: ")
                ship.change_part(part_name, new_material)
                print("Material changed successfully!")

            case "4":
                ship.display_state()

            case "5":
                ship.display_history()

            case "6":
                print("Exiting program...")
                break

            case _:
                print("Invalid choice! Please try again.")
            
            
            
            
# ship_01 = Ship("Titanic")
# part_001 = Part("Mast", "Wood")
# ship_01._Ship__parts["mast"] = part_001 

# print(part_001) 
# ship_01.change_part("mast", "Steel")
# print("\nWe have changed the part's material:")
# print(part_001)  

racing_ship = RacingShip("SpeedBoat", 50)
print("\nRacing Speed:")
racing_ship.display_speed()


if __name__ == "__main__":
    ship_type = input("Enter ship type (normal/racing): ").lower()
    ship_name = input("Enter ship name: ")
    
    if ship_type == "racing":
        max_speed = float(input("Enter maximum speed (in knots): "))
        ship = RacingShip(ship_name, max_speed)
    else:
        ship = Ship(ship_name)

    interactive_menu(ship)