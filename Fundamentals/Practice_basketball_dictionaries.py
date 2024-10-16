class Player:
    # Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.
    def __init__(self, data):
        self.name = data.get("name", " ")
        self.age = data.get("age", 0)
        self.position = data.get("position", " ")
        self.team = data.get("team", " ")

    def __str__(self):
        return (f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Team: {self.team}")

    @classmethod
    # Creates a list of Player instances from a list of dictionaries.
    def get_team(cls, team_list):
        return [cls(data) for data in team_list]

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


# Make a new list of Player instances from a list of players
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

new_team = [(data) for data in players]
print(new_team)

team = Player.get_team(players)
for player in team:
    print(player)










