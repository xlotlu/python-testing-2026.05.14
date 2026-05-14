from d1_ex2_more_function_testing import (
    SPEED_LIMIT, MAX_PENALTY_POINTS, KMH_PER_POINT,
    check_speed, LicenseSuspended,
)

assert check_speed(0) == 0, \
    "test zero speed"

# WARNING. TODO: this is probably bad
assert check_speed(-1) == 0, \
    "test negative speed"

assert check_speed(SPEED_LIMIT) == 0, \
    "test max legal speed"

assert check_speed(SPEED_LIMIT + 1) == 0, \
    "test slightly over max legal speed"

assert check_speed(SPEED_LIMIT + KMH_PER_POINT) == 1, \
    "test one unit over max legal speed"

assert check_speed(SPEED_LIMIT + KMH_PER_POINT * 2) == 2, \
    "test two units over max legal speed"

assert check_speed(SPEED_LIMIT + KMH_PER_POINT * MAX_PENALTY_POINTS) == MAX_PENALTY_POINTS, \
    "test all units over max legal speed"

try:
    check_speed(SPEED_LIMIT + KMH_PER_POINT * (MAX_PENALTY_POINTS + 1))
    assert False, "test license suspended"
except LicenseSuspended:
    pass
