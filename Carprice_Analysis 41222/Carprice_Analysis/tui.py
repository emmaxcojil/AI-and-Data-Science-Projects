LINE_WIDTH = 85


def started(msg=""):
    output = f"Operation started: {msg}..."
    dashes = "-" * LINE_WIDTH
    print(f"{dashes}\n{output}\n")


def completed(msg=""):
    dashes = "-" * LINE_WIDTH
    print(f"\nOperation completed. {msg}\n{dashes}\n")


def error(msg):
    msg = msg.upper()
    print("-"*LINE_WIDTH)
    print(f"| ERROR! {msg}!!! |\n")
    print("-"*LINE_WIDTH)


def menu():
    print(f"""Please select one of the following options:
    {"[load_file]":<10} To specify file path to load csv into memory
    {"[carbyid]":<10} To retrieve a car by a given ID
    {"[cylindernumber]":<10} To retrieve a car by cylindernumber
    {"[team]":<10} Tally up medals for each team
    {"[exit]":<10} Exit the program
    """)
    selection = input("Your selection: ")
    return selection.strip().lower()

def display_car(car, column_to_index_map):
    for column in column_to_index_map:
        print(f"{column}: ".upper(), car[column_to_index_map[column]])

def display_cars(cars, column_to_index_map):
    for car in cars:
        print("#"*20)
        display_car(car, column_to_index_map)
    
def display_medal_tally(tally):
    print(f"| {'Gold':<10} | {tally['Gold']:<10} |")
    print(f"| {'Silver':<10} | {tally['Silver']:<10} |")
    print(f"| {'Bronze':<10} | {tally['Bronze']:<10} |")


def display_team_medal_tally(team_tally):
    for team, tally in team_tally.items():
        print(team)
        print(f"\tGold:{tally['Gold']}, Silver:{tally['Silver']}, Bronze:{tally['Bronze']}")


def display_years(years):
    sorted_years = sorted(years, reverse=True)
    for year in sorted_years:
        print(year)