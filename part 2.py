class BudgetCategory:
    def __init__(self, category, budget):
        self.__category = category
        self.__budget = budget
        self.__balance = budget

    # Getters and setters for category name and budget
    # ...
    def get_category(self):
        return self.__category
    
    def get_budget(self):
        return self.__budget
    
    def get_balance(self):
        return self.__balance
    
    def set_category(self,category):
        self.__category = category

    def set_budget(self, budget):
        if budget > 0:
            self.__budget = budget
            self.__balance = budget

        else:
            raise ValueError("Must be a positive number")


    def add_expense(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                raise ValueError("exceeds remaining balance")
        
        else:
            raise ValueError("must be a positve number")
        # Method to add an expense to the category
        

    def display_category_summary(self):
        print(f"category: {self.get_category()}")
        print(f"budget: {self.get_budget()}")
        print(f"remaining balance: {self.get_balance()}")
        # Method to display the budget category details
        

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()