import sys
import unittest

from d1_ex2_more_function_testing import (
    SPEED_LIMIT, MAX_PENALTY_POINTS, KMH_PER_POINT,
    check_speed, LicenseSuspended,
)


class CheckSpeedTestCase(unittest.TestCase):
    def test_zero_speed(self):
        self.assertEqual(check_speed(0), 0)

    def test_negative_speed(self):
        # WARNING. TODO: this is probably bad
        self.assertEqual(check_speed(-1), 0)
    
    def test_max_legal_speed(self):
        self.assertEqual(check_speed(SPEED_LIMIT), 0)

    def test_slightly_over_max_legal_speed(self):
        self.assertEqual(check_speed(SPEED_LIMIT + 1), 0)

    def test_one_unit_over_max_legal_speed(self):
        self.assertEqual(check_speed(SPEED_LIMIT + KMH_PER_POINT), 1)

    def test_two_units_over_max_legal_speed(self):
        self.assertEqual(check_speed(SPEED_LIMIT + KMH_PER_POINT * 2), 2)

    def test_all_units_over_max_legal_speed(self):
        self.assertEqual(check_speed(SPEED_LIMIT + KMH_PER_POINT * MAX_PENALTY_POINTS),
                         MAX_PENALTY_POINTS)

    @unittest.skip("alternative implementation")
    def test_license_suspended(self):
        self.assertRaises(
            LicenseSuspended, # what it raises
            check_speed,      # the function
            SPEED_LIMIT + KMH_PER_POINT * (MAX_PENALTY_POINTS + 1)
        )

    def test_license_suspended_alt(self):
        with self.assertRaises(LicenseSuspended):
            check_speed(SPEED_LIMIT + KMH_PER_POINT * (MAX_PENALTY_POINTS + 1))

    @unittest.skipUnless(
            sys.platform == "very_special_platform",
            "demo for conditional skipping"
        )
    def test_that_does_nothing(self):
        pass