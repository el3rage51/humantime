import unittest

from humantime import format_duration, parse_duration


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


if __name__ == "__main__":
    unittest.main()
