# How much carbon is used for one online delivery with slow and fast delivery options
ONLINE_PKG = 0.37
ONLINE_PKG_ONE_DAY = 0.9
# The amount of carbon generated per 1 clothing item per 1 month
NEW_CLOTHING = 20.875
USED_CLOTHING = 8.625

# Calculate how much carbon is generated based on online shopping habits
"""
pkgs_n:
    number of online packages ordered in a MONTH, NOT INCLUDING CLOTHING
    integer >=0
fast_delivery:
    flag denoting if the user usually uses one or two day delivery options, True or False
used_clothing (amount of wardrobe that is second-hand):
    'all' (100%)
    'most' (80%)
    'half' (50%)
    'some' (35%)
    'none' (~0%)
clothing_n:
    number clothing items purchased per month
    integer >= 0
"""

def consumer_footprt_percent(clothing_n, used_clothing, pkgs_n,fast_delivery = False):
    carbon = 0
    if fast_delivery:
        # Multiply number of monthly packages by carbon per package by number of months
        carbon = ONLINE_PKG_ONE_DAY * pkgs_n * 12
    else:
        carbon = ONLINE_PKG * pkgs_n * 12

    clothing_carbon = (clothing_n * used_clothing * USED_CLOTHING
                    + clothing_n * (1 - used_clothing) * NEW_CLOTHING)

    carbon += clothing_carbon * 12

    return round(carbon, 2)

def consumer_footprt(clothing_n, used_clothing, pkgs_n,fast_delivery = False):
    carbon = 0
    used_clothing_perc = {"all":1, "most":0.8, "half":0.5, "some":0.35, "none":0}
    if fast_delivery:
        # Multiply number of monthly packages by carbon per package by number of months
        carbon = ONLINE_PKG_ONE_DAY * pkgs_n * 12
    else:
        carbon = ONLINE_PKG * pkgs_n * 12

    clothing_carbon = (clothing_n * used_clothing_perc[used_clothing] * USED_CLOTHING
                    + clothing_n * (1 - used_clothing_perc[used_clothing]) * NEW_CLOTHING)

    carbon += clothing_carbon * 12

    return round(carbon, 2)


if __name__ == '__main__':
    # Unit tests
    carbon_s = consumer_footprt(5, "all", 10)
    print("5 recycled garmets and 10 online packages per month with slow deliver: "
            + str(carbon_s) + "lbs. of CO2/yr.")

    carbon_fs = consumer_footprt(5, "all", 10, fast_delivery = True)
    print("5 recycled garmets and 10 online packages per month with fast deliver: "
            + str(carbon_fs) + "lbs. of CO2/yr.")

    carbon_c = consumer_footprt(5, "most", 10, fast_delivery = True)
    print("5 mostly recycled garmets and 10 online packages per month with fast delivery: "
        + str(carbon_c) + "lbs. of CO2/yr.")

    carbon_f = consumer_footprt(5, "none", 10, fast_delivery = True)
    print("5 new garmets and 10 online packages per month with fast delivery: "
        + str(carbon_f) + "lbs. of CO2/yr.")
