#Graphs the user's carbon against a baseline average
AVG_CARBON = 5000
import matplotlib.pyplot as plt

def avg_carbon(usr_carbon, userID):

    plt.figure(figsize=(4,6))
    plt.axhline(y = AVG_CARBON, color = 'r', linestyle='--', linewidth=2)
    plt.axhline(y = usr_carbon, color = 'b', linestyle='-', linewidth=3)

    plt.tick_params(
        axis='x',
        which='both',
        bottom=False,
        top=False,
        labelbottom=False
    )
    #plt.title("How you compare against the average college student")
    plt.ylabel("lbs. of CO2 per year")

    path = "static/figures/"+userID+"_avg_carbon"#added username to create folders for user for syconicity
    plt.savefig(path, bbox_inches='tight', transparent=True)
    #plt.show()

def avg_carbon_str(usr_carbon):
    diff = AVG_CARBON - usr_carbon
    comp = " the average college student"
    if diff == 0:
        return "You use the same amount of carbon as" + comp
    elif diff < 0:
        return "You use " +str(abs(diff))+ " more lbs of co2 per year than" + comp
    else:
        return "You use " +str(abs(diff))+ " less lbs of co2 per year than" + comp

if __name__ == '__main__':
    # Unit test
    print(avg_carbon_str(5000))
    print(avg_carbon_str(500))
    print(avg_carbon_str(5001))
