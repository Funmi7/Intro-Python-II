
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return f"{self.name} is {self.description}"

    def on_take(self):
        print(f"You have taken {self.name}")
    
    def on_drop(self):
        print(f"You have dropped {self.name}")
