import pytest

from d1_ex2_more_function_testing import (
    SPEED_LIMIT, MAX_PENALTY_POINTS, KMH_PER_POINT,
    check_speed, LicenseSuspended,
)

@pytest.mark.parametrize(
        "speed", [
            0, 1, 10, 20, SPEED_LIMIT - 1, SPEED_LIMIT
        ]
)
def test_valid_speeds(speed):
    assert check_speed(speed) == 0

@pytest.mark.parametrize(
        "speed, points", [
            (55, 1),
            (78, 5),
            (110, 12),
        ]
)
def test_penalty_points(speed, points):
    assert check_speed(speed) == points