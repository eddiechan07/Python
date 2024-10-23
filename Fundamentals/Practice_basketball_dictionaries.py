class Player:
    # Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.
    def __init__(self, dictionary):
        self.name = dictionary["name"]
        self.age = dictionary["age"]
        self.position = dictionary["position"]
        self.team = dictionary["team"]

    def __str__(self):
        return (f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Team: {self.team}")

    @classmethod
    # Creates a list of Player instances from a list of dictionaries.
    def get_team(cls, team_list):
        return [cls(element) for element in team_list]    # returns a new list of Player objects

# Create instances using individual player dictionaries.
kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
}
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

# Make a list of Player instances from a list of dictionaries
players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
}
]
new_team = []
# player = [Player(each_player) for each_player in players]
for each_dictionary in players:             # iterate through the players dictionaries
    player = Player(each_dictionary)        # create a list of Player instances from the players dictionaries
    new_team.append(player)                   # put the list of Player instances into a new list called new_team[]


[print(team)for team in new_team]
# for team in new_team:                   # interate through the new_team[] list 
#     print(team)                         # print out each element in the new_team[] list 

team = Player.get_team(players)
[print(player) for player in team]
# for player in team:
#     print(player)










