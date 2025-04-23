class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting value (0 = full, 10 = very hungry)
        self.energy = 5  # Starting value (0 = tired, 10 = fully rested)
        self.happiness = 5  # Starting value (0-10)
        self.tricks = []  # List to store learned tricks
    
    def eat(self):
        """Reduces hunger by 3 points (minimum 0) and increases happiness by 1"""
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food. Yum!")
    
    def sleep(self):
        """Increases energy by 5 points (maximum 10)"""
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a good nap and feels refreshed!")
    
    def play(self):
        """Decreases energy by 2, increases happiness by 2, and increases hunger by 1"""
        if self.energy < 2:
            print(f"{self.name} is too tired to play right now!")
            return
        
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} had a great time playing!")
    
    def get_status(self):
        """Prints the current state of the pet"""
        print(f"\n--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10 {'🍽️' * self.hunger}")
        print(f"Energy: {self.energy}/10 {'⚡' * self.energy}")
        print(f"Happiness: {self.happiness}/10 {'😊' * self.happiness}")
        
        # Provide some feedback based on status
        if self.hunger > 7:
            print(f"{self.name} is very hungry!")
        if self.energy < 3:
            print(f"{self.name} is getting tired.")
        if self.happiness < 3:
            print(f"{self.name} looks sad.")
    
    def train(self, trick):
        """Teaches the pet a new trick"""
        if trick in self.tricks:
            print(f"{self.name} already knows how to {trick}!")
            return
            
        if self.energy < 3:
            print(f"{self.name} is too tired to learn new tricks right now.")
            return
            
        self.tricks.append(trick)
        self.energy = max(0, self.energy - 1)
        self.happiness = min(10, self.happiness + 1)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} learned how to {trick}!")
    
    def show_tricks(self):
        """Displays all tricks the pet has learned"""
        if not self.tricks:
            print(f"{self.name} doesn't know any tricks yet.")
        else:
            print(f"\n--- {self.name}'s Tricks ---")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")                # Create a new pet
                my_pet = Pet("Sissy")
                
                # Test all the features
                my_pet.get_status()
                my_pet.eat()
                my_pet.play()
                my_pet.sleep()
                my_pet.train("roll over")
                my_pet.train("sit")
                my_pet.show_tricks()
                my_pet.get_status()