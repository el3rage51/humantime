import unittest

from humantime import add_durations, format_duration, gap, has_unit, longer_than, longest, parse_duration, same_duration, shorter_than, shortest, unit_count


class HumantimeTest(unittest.TestCase):
    def test_parse_and_format(self) -> None:
        self.assertEqual(parse_duration("1h30m2s"), 5402)
        self.assertEqual(format_duration(5402), "1h30m2s")
        self.assertEqual(format_duration(0), "0s")

    def test_reject(self) -> None:
        with self.assertRaises(ValueError):
            parse_duration("1h1h")
        with self.assertRaises(ValueError):
            format_duration(-1)

    def test_shorter(self) -> None:
        self.assertTrue(shorter_than("30m", "1h"))
        self.assertFalse(shorter_than("1h", "30m"))
        self.assertFalse(shorter_than("1h", "1h"))
        self.assertTrue(same_duration("1h", "60m"))
        self.assertFalse(same_duration("1h", "61m"))
        self.assertEqual(shortest("2h", "30m", "45s"), "45s")

    def test_add(self) -> None:
        self.assertEqual(add_durations("1h", "30m"), "1h30m")
        self.assertEqual(gap("1h", "30m"), "30m")
        self.assertTrue(longer_than("1h", "30m"))
        self.assertFalse(longer_than("30m", "1h"))
        self.assertEqual(unit_count("1h30m2s"), 3)
        self.assertEqual(unit_count("0s"), 1)
        self.assertTrue(has_unit("1h30m", "h"))
        self.assertFalse(has_unit("1h30m", "s"))
        self.assertEqual(longest("30m", "2h", "45s"), "2h")
        with self.assertRaises(ValueError):
            add_durations()


if __name__ == "__main__":
    unittest.main()
