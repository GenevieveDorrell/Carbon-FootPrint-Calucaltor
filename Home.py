# Some constant average energy values per year
# Yearly laptop energy use
LAPTOP = 0.05 * 365
# Monthly dorm, house, and energy use
DORM = (505.74 / 12) * (4 / 3) * 2
HOUSE = 1000
APARTMENT = 600

# Calculate how much carbon is generated based on home energy usage in a year
# Making assumptions on room/house size and heating type, since many college students don't know this
"""
home_type:
    dorm
    off_apartment
    off_house
room_n:
    number of BEDROOMS integer >=0
roommate_n:
    number of people they reside with integer >=0
"""
def home_footprt(home_type, room_n, roommate_n):
    carbon = 0
    # Energy in kWh
    energy = 0

    # students use just over 5kWh of enerergy per week
    # avg dorm room size 180 sq ft
    if home_type == "dorm":
        # Takes the average dorm room energy, divided by number of roommates
        energy += ((DORM * room_n) / (roommate_n + 1))
        # Addds in additional significant source of energy that increases with roomates
        energy *= 12
        energy += LAPTOP * roommate_n

    #Avg home size - 2325 sq ft
    #Avg house bedroom size - 250 sq ft
    elif home_type == "off_house":
        energy = 919
        # Avg home size assuming ~250 sq ft beddrooms
        # which correspond to ~100kWh increase in energy consumption
        if room_n == 1:
            energy = HOUSE
        if room_n > 1:
            energy = HOUSE + 120 * (room_n - 1)
        # Yearly energy
        energy *= 12
        energy /= (roommate_n + 1)
        energy += LAPTOP * roommate_n

    #Avg apartment size - 892 sq ft
    #Avg apartment bedroom size - 132 sq ft
    if home_type == "off_apartment":
        # Daily energy useage in kWh
        energy = 20
        if room_n > 0:
            energy = APARTMENT + (150 * (room_n ))

        energy *= 12
        energy /= (roommate_n + 1)
        energy += LAPTOP * roommate_n

    # Pounds CO2 per average kWh generated
    carbon = 0.99 * energy
    return carbon

if __name__ == '__main__':
    # Unit tests
    carbon_h = home_footprt("off_house", 2, 1)
    print("2bd. 2pr. house:" + str(carbon_h) + "lbs. of CO2/yr.")

    carbon_a = home_footprt("off_apartment", 2, 1)
    print("2bd. 2pr. apartment:" + str(carbon_a) + "lbs. of CO2/yr.")

    carbon_d = home_footprt("dorm", 1, 2)
    print("1bd. 2pr. dorm: " + str(carbon_d) + "lbs. of CO2/yr.")
