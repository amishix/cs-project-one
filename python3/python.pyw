import matplotlib.pyplot as plt
from PIL import Image

# Sample Formula One race calendar data
calendar_data = [
    {
        'race_name': 'Australian Grand Prix',
        'date': '2023-03-20',
        'logo_path': 'logos/australia.png'
    },
    {
        'race_name': 'Monaco Grand Prix',
        'date': '2023-05-28',
        'logo_path': 'logos/monaco.png'
    },
    {
        'race_name': 'British Grand Prix',
        'date': '2023-07-16',
        'logo_path': 'logos/britain.png'
    },
    # Add more races and logos here
]

# Function to display the Formula One calendar
def display_formula_one_calendar(data):
    fig, ax = plt.subplots(figsize=(10, 6))

    for event in data:
        race_date = event['date']
        race_name = event['race_name']
        logo_path = event['logo_path']

        # Load and display the team logo
        logo = Image.open(logo_path)
        ax.imshow(logo, extent=(race_date, race_date, 0, 1), aspect='auto')

        # Add the race name as a label
        ax.annotate(race_name, (race_date, 0.5), fontsize=10, ha='center')

    ax.set_xlabel('Date')
    ax.set_ylabel('Races')
    ax.set_title('Formula One Calendar 2023')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Display the Formula One calendar
display_formula_one_calendar(calendar_data)




