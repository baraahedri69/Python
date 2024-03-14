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

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print("User enrolled successfully.")
            return True

    def spend_points(self, amount):
        if amount <= self.gold_card_points:
            self.gold_card_points -= amount
            print(f"{amount} points spent. Remaining points: {self.gold_card_points}")
        else:
            print("Insufficient points.")

#Testin User Class#
if __name__ == "__main__":
    user1 = User("John", "Doe", "john@gmail.com", 30)
    user1.display_info()

#Calling the enroll method#
    print("\nEnrolling user1...")
    user1.enroll()
    user1.display_info()

#Creating 2 more instances#
    user2 = User("Jane", "Smith", "jane@gmail.com", 25)
    user3 = User("Alice", "Johnson", "alice@gmail.com", 35)

#Have the first user spend 50 points#
    print("\nSpending points for user1...")
    user1.spend_points(50)
    user1.display_info()

#Enrolling the second user#
    print("\nEnrolling user2...")
    user2.enroll()
    user2.display_info()

#Have the second user spend 80 points#
    print("\nSpending points for user2...")
    user2.spend_points(80)
    user2.display_info()

#Call the display_info method on each of the users#
    print("\nDisplaying info for all users...")
    user1.display_info()
    user2.display_info()
    user3.display_info()

#Bonus: Try to re-enroll the first user#
    print("\nTrying to re-enroll user1...")
    user1.enroll()

#Prevent over-spending for the third user#
    print("\nSpending points for user3...")
    user3.spend_points(40)
    user3.display_info()