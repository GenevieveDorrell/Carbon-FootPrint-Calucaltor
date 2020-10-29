# Average CO2 produced per mile from different modes of transportation per person
CAR = 0.89
BUS = 0.28 # Assumes half full bus on average
# Calculate how much carbon is generated based on commuting and travel costs
"""
mode:
    the primary type of travel (car, bike, plane, bus)
distance:
    the usual distance traveled to get to campus every day
"""

def travel_footprt(mode, distance):
    carbon = 0
    if mode == "car":
        carbon = CAR * distance * 10 # Assumes going to campus 5 times a week
    elif mode == "bike":
        carbon = 0
    elif mode == "walk":
        carbon = 0
    elif mode == "bus":
        carbon = BUS * distance * 10

    # Assumes going to campus every week
    carbon *= 52
    return carbon

if __name__ == '__main__':
    # Unit tests
    carbon_c = travel_footprt("car", 1)
    print("Driving 1 mile to and from campus: " + str(carbon_c) + "lbs. of CO2/yr.")

    carbon_b = travel_footprt("bus", 1)
    print("Busing 1 mile to and from campus: " + str(carbon_b) + "lbs. of CO2/yr.")

    carbon_w = travel_footprt("walk", 1)
    print("Walking 1 mile to and from campus: " + str(carbon_w) + "lbs. of CO2/yr.")

    carbon_bi = travel_footprt("bike", 1)
    print("Biking 1 mile to and from campus: " + str(carbon_bi) + "lbs. of CO2/yr.")
