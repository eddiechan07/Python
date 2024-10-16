if __name__=="__main__":
    user1 = User("John", "Doe", "john.doe@example.com", 30)
    user2 = User("Jane", "Smith", "jane.smith@example.com", 25)
    user3 = User("Bob", "Johnson", "bob.johnson@example.com", 40)
    user1.display_info()
    user1.enroll()
    user1.spend_points(50)
    user2.display_info()
    user2.spend_points(80)
    user3.display_info()
    user2.spend_points(40)

display_info(user1)