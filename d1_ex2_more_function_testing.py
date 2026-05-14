# 1.
# Write a function that checks whether the speed limit
# has been passed, and if so
# a) returns a number of penalty points,
# or b) after a certain limit,
#       raises an exception.
#
# The meaning of the exception is that
# the driving license will be suspended.


SPEED_LIMIT = 50 
KMH_PER_POINT = 5 # every 5 km/h --> 1 penalty point
MAX_PENALTY_POINTS = 12


class LicenseSuspended(Exception):
    pass

def check_speed(speed):
    # If speed is within the legal limit, 
    # return 0 penalty points
    if speed <= SPEED_LIMIT:
        return 0

    # Calculate the number of penalty points.
    penalty_points = (speed - SPEED_LIMIT) // KMH_PER_POINT

    # Raise exception if the number 
    # of penalty points exceeds the maximum allowed.
    if penalty_points > MAX_PENALTY_POINTS:
        raise LicenseSuspended("Driving license suspended")

    return penalty_points


# 2.
# Write assertion tests for it.

assert check_speed(110) == 12
check_speed(120) # error
check_speed(12)

