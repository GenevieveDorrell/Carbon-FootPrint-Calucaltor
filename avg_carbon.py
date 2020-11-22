#Graphs the user's carbon against a baseline average
AVG_CARBON = 6370.09
DAILY_AVG = 17.45

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def avg_carbon(usr_carbon, userID):
    dcarbon = []; dates = []
    for c in usr_carbon:
        dcarbon.append(c[0])
        date = datetime.strptime(c[1], '%Y-%m-%d')
        dates.append(date)

    ax = plt.gca()
    formatter = mdates.DateFormatter("%Y-%m-%d")
    ax.xaxis.set_major_formatter(formatter)
    locator = mdates.DayLocator()
    ax.xaxis.set_major_locator(locator)
    if (len(dates) > 1):
        plt.plot(dates, dcarbon, linewidth=2, label="Your carbon")
    else:
        ax.axhline(dcarbon[0], linewidth=2, label="Your carbon (projected)")
    ax.axhline(DAILY_AVG, linewidth=2, linestyle='--', color = 'r', label="Average carbon")
    plt.title("Your carbon vs. the average college student in a dorm")
    plt.ylabel("lbs. of CO2 per day")
    plt.xlabel("Date")
    plt.legend(facecolor='inherit')
    path = "static/figures/"+ userID +"_avg_carbon"#added username to create folders for user for syconicity
    #plt.savefig(path, bbox_inches='tight', transparent=True)
    #plt.show()

def avg_carbon_str(usr_carbon):
    diff = round(AVG_CARBON - usr_carbon, 2)
    comp = " the average college student living in a dorm"
    if diff == 0:
        return "You use the same amount of carbon as" + comp
    elif diff < 0:
        return "You use " +str(abs(diff))+ " more lbs of CO2/yr. than" + comp
    else:
        return "You use " +str(abs(diff))+ " less lbs of CO2/yr. than" + comp

if __name__ == '__main__':
    # Unit test
    avg_carbon([[18.81, '2020-11-20'], [18.71, '2020-11-21']], "-1")
    print(avg_carbon_str(5000))
    print(avg_carbon_str(500))
    print(avg_carbon_str(5001))
