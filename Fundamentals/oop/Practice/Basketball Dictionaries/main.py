class Player:
    def __init__(self, player_info):
        self.name = player_info.get("name")
        self.age = player_info.get("age")
        self.position = player_info.get("position")
        self.team = player_info.get("team")

    @classmethod
    def get_team(cls, team_list):
        return [cls(player_info) for player_info in team_list]

    def __repr__(self):
        return f"Player(name={self.name}, age={self.age}, position={self.position}, team={self.team})"


kevin = {
    "name": "Kevin Durant", 
    "age": 34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age": 24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age": 32, 
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

print("Individual Player Instances:")
print(player_kevin)
print(player_jason)
print(player_kyrie)

players = [
    {
        "name": "Kevin Durant", 
        "age": 34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age": 24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age": 32, 
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age": 33, 
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age": 32, 
        "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age": 16, 
        "position": "P", 
        "team": "en"
    }
]

new_team = []

# Populate the new_team list with Player objects
for player_info in players:
    new_team.append(Player(player_info))

# Print the new team list
print("\nNew Team List:")
for player in new_team:
    print(player)

# Test the get_team class method
team = Player.get_team(players)

# Print the team created by get_team method
print("\nTeam from get_team method:")
for player in team:
    print(player)