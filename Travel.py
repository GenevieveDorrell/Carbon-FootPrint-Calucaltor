# Average CO2 produced per mile from different modes of transportation per person
GCAR = 0.83
HCAR = 0.42
ECAR = 0.27
BUS = 0.28 # Assumes half full bus on average
# Calculate how much carbon is generated based on commuting and travel costs
"""
mode:
    'GCAR' (conventional)
    'HCAR' (hybrid)
    'ECAR' (electric)
    'non_motor'
    'bus'
distance:
    the usual distance traveled to get to campus every day
    integer >=0
"""

def travel_footprt(mode, distance):
    carbon = 0
    # Conventional gas car
    if mode == "gcar":
        carbon = GCAR * distance * 10 # Assumes going to campus 5 times a week
    # Hybrid car
    elif mode == "hcar":
        carbon = HCAR * distance * 10
    # Hybrid car
    elif mode == "ecar":
        carbon = ECAR * distance * 10
    # Includes walking and biking
    elif mode == "non_motor":
        carbon = 0
    elif mode == "bus":
        carbon = BUS * distance * 10

    # Assumes going to campus every week
    carbon *= 52
    return round(carbon, 2)

if __name__ == '__main__':
    # Unit tests
    carbon_c = travel_footprt("hcar", 1)
    print("Driving 1 mile to and from campus with a hybrid: " + str(carbon_c) + "lbs. of CO2/yr.")

    carbon_b = travel_footprt("bus", 1)
    print("Busing 1 mile to and from campus: " + str(carbon_b) + "lbs. of CO2/yr.")

    carbon_w = travel_footprt("walk", 1)
    print("Walking 1 mile to and from campus: " + str(carbon_w) + "lbs. of CO2/yr.")

    carbon_bi = travel_footprt("bike", 1)
    print("Biking 1 mile to and from campus: " + str(carbon_bi) + "lbs. of CO2/yr.")
