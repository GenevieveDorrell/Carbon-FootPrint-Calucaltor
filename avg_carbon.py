#Graphs the user's carbon against a baseline average
import matplotlib.pyplot as plt

AVG_CARBON = 5000

def avg_carbon(usr_carbon):

    plt.figure(figsize=(2,4))
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
    
    path = "figures/avg_carbon"
    plt.savefig(path, bbox_inches='tight')
    plt.show()
    


if __name__ == '__main__':
    # Unit test
    avg_carbon(3000)
