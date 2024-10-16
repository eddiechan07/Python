class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First Name:{self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Points: {self.gold_card_points}")
        return self
        
    def enroll(self):
        self.gold_card_points = 200
        if not self.is_rewards_member:
            print (f"{self.first_name} {self.last_name} is already a member.")
            return self
        else:
            return self

    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
        return self

if __name__=="__main__":
    user1 = User("John", "Doe", "john.doe@example.com", 30)
    user2 = User("Jane", "Smith", "jane.smith@example.com", 25)
    user3 = User("Bob", "Johnson", "bob.johnson@example.com", 40)
    user1.display_info().enroll().spend_points(50).display_info()
    user2.display_info().enroll().spend_points(50).display_info() 
    user3.display_info().enroll().spend_points(50).display_info()



