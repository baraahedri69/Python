class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {'Yes' if self.is_rewards_member else 'No'}")
        print(f"Gold Card Points: {self.gold_card_points}")
        return self  

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print("User enrolled successfully.")
        return self  

    def spend_points(self, amount):
        if amount <= self.gold_card_points:
            self.gold_card_points -= amount
            print(f"{amount} points spent. Remaining points: {self.gold_card_points}")
        else:
            print("Insufficient points.")
        return self  

if __name__ == "__main__":
    user1 = User("John", "Doe", "john@gmail.com", 30).display_info().enroll().spend_points(50).display_info()

    user2 = User("Jane", "Smith", "jane@gmail.com", 25).enroll().spend_points(80).display_info()