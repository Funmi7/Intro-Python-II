# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None, items=[]):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items
    
    def __str__(self):
        return f"{self.name} {self.description}"
    
    def get_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
            else:
                return self.items
        
    def display_item(self):
        for i in self.items:
            print(f"This is {i.name} which is {i.description}")
    
    def add_item(self, item):
        self.items.append(item)

    # def __str__(self):
    #     if self.items == None:
    #         return f" No items available in {self.name}"
    #     else:
    #         output = f"current Room: {self.name} {self.description}"
    #         for i in self.items:
    #              output += f"Available items: [{i}]"