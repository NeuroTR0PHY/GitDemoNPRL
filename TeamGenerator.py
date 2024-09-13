##making changes

###making

import random

def assign_teams(names, team_size):
    # Shuffle the list of names
    random.shuffle(names)
    
    # Calculate the number of full teams
    num_full_teams = len(names) // team_size
    
    # Create full teams
    teams = [names[i:i+team_size] for i in range(0, num_full_teams * team_size, team_size)]
    
    # Add any remaining members to the last team
    if len(names) % team_size != 0:
        teams.append(names[num_full_teams * team_size:])
    
    return teams

def main():
    # Get input from user
    names =  ["Nathan", "Yasmine", "Camille", "Iran", "Aryaman", "Jasmine", "Catie", "Andrew", "Emily"] #input("Enter names separated by commas: ").split(',')
    names = [name.strip() for name in names]  # Remove any whitespace
    
    team_size = int(input("Enter the desired team size: "))
    
    # Assign teams
    teams = assign_teams(names, team_size)
    
    # Report results
    print("\nTeam Assignments:")
    for i, team in enumerate(teams, 1):
        print(f"Team {i}: {', '.join(team)}")

if __name__ == "__main__":
    main()