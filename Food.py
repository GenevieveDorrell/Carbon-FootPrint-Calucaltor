# Calculate how much carbon is generated based on food consumption
"""
diet_type:
    vegan
    vegetarian
    white_meat_only
    med_meat
    high_meat
"""

def food_footprt(diet_type):
    carbon = 0
    if diet_type == "vegan":
        carbon = 1.5 * 2000
    elif diet_type == "vegetarian":
        carbon = 1.7 * 2000
    elif diet_type == "white_meat_only":
        carbon = 1.9 * 2000
    elif diet_type == "med_meat":
        carbon = 2.5 * 2000
    elif diet_type == "high_meat":
        carbon = 3.3 * 2000

    return carbon

if __name__ == '__main__':
    # Unit tests
    carbon_v = food_footprt("vegan")
    print("vegan diet: " + str(carbon_v) + "lbs. of CO2/yr.")

    carbon_w = food_footprt("white_meat_only")
    print("vegan diet: " + str(carbon_w) + "lbs. of CO2/yr.")

    carbon_h = food_footprt("high_meat")
    print("vegan diet: " + str(carbon_h) + "lbs. of CO2/yr.")
