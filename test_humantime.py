import unittest

from humantime import add_durations, format_duration, parse_duration, shorter_than


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

    def test_add(self) -> None:
        self.assertEqual(add_durations("1h", "30m"), "1h30m")
        with self.assertRaises(ValueError):
            add_durations()


if __name__ == "__main__":
    unittest.main()
