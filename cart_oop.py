my_list = ShoppingList = (["apples", "beer", "grapes", "peaches", "milk", "bread", "beer", "deoderant", "kiwi","beer"])
class Shopping_cart:
    def __init__(self, items):
        # Checks if a value is a string or a list.
        if isinstance(items, str):       # isinstance checks if a value is a string or a list ## STR makes sure everything is a string
            items = [items]              # puts items in a list
            self._needed = set(items)    # set handles multi inputs of the same type
            self._purchased = set()      # set handles multi inputs of the same type in empty list
        # Adds new items to the list.
    def add_new_items(self, items):
        if isinstance(items,str):
            items = [items]
        self._needed.update(items)          # updates the item list
        # Provides the names of the items to mark as purchased.
    def purchased_items(self, items):
        if isinstance(items, str):          # str makes sure all things are a string
            items = [items]                 # puts items in a list
        self._purchased.update(set(items) and self._needed)        # this marks items as purchased on the list
        self._needed.difference_update(self._purchased)      # removes purchased items from the unpurchased item list
    def list_purchased_items(self):            # return a sorted list of items I purchased
        return sorted(self._purchased)
    def list_unpurchased_items(self):          # return a list of items that are not purchased
        return sorted(self._needed)

#main()      # O.K it returns nothing......I broke it!!!!!.......I dont like OOP!!!!!!......Going to bed!!!!!!






            
           
               
