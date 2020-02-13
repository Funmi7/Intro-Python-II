# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, items=[]):
        self.name = name
        self.room = room
        self.items = items
    
    def __str__(self):
        return f"{self.name} is in {self.room}"
    
    def get_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
            else:
                return None


    def add_item(self, item):
        self.items.append(item)
