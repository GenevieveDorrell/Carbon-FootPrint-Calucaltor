# How much carbon is used for one online delivery with slow and fast delivery options
ONLINE_PKG = 0.37
ONLINE_PKG_ONE_DAY = 0.9
# Calculate how much carbon is generated based on online shopping habits
"""
pkgs_n:
    number of online packages ordered in a MONTH, integer >=0
fast_delivery:
    flag denoting if the user usually uses one or two day delivery options, True or False
"""
def consumer_footprt(pkgs_n, fast_delivery = False):
    carbon = 0
    if fast_delivery:
        # Multiply number of monthly packages by carbon per package by number of months
        carbon = ONLINE_PKG_ONE_DAY * pkgs_n * 12
    else:
        carbon = ONLINE_PKG * pkgs_n * 12
    return round(carbon, 2)

if __name__ == '__main__':
    # Unit tests
    carbon_s = consumer_footprt(10)
    print("10 packages per month with slow delivery: " + str(carbon_s) + "lbs. of CO2/yr.")

    carbon_f = consumer_footprt(10, fast_delivery = True)
    print("10 packages per month with fast delivery: " + str(carbon_f) + "lbs. of CO2/yr.")
