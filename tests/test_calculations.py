import unittest

from pcb_calculator import trace_width_mm, via_barrel_area_mm2


class CalculationTests(unittest.TestCase):
    def test_trace_reference_case(self):
        self.assertAlmostEqual(trace_width_mm(2, 1, 10), 0.781, places=3)

    def test_more_current_requires_wider_trace(self):
        self.assertGreater(trace_width_mm(3), trace_width_mm(1))

    def test_thicker_copper_reduces_width(self):
        self.assertLess(trace_width_mm(2, 2), trace_width_mm(2, 1))

    def test_via_area_is_positive(self):
        self.assertAlmostEqual(via_barrel_area_mm2(.3, 25), 0.02553, places=5)

    def test_rejects_invalid_input(self):
        with self.assertRaises(ValueError):
            trace_width_mm(0)


if __name__ == "__main__":
    unittest.main()
