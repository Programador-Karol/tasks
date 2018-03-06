import unittest

from egnyte import EgnyteTasks


class TestEgnyteTasks(unittest.TestCase):
    def setUp(self):
        self.tasks = EgnyteTasks()

    def test_difference_calculation(self):
        self.assertEqual(self.tasks._EgnyteTasks__difference(10, 6), 4,
                         'difference should be substraction'
        )
        self.assertEqual(self.tasks._EgnyteTasks__difference(6, 10), 4,
                         'difference should be absolute substraction'
        )
        self.assertEqual(self.tasks._EgnyteTasks__difference('10', '6'), 4,
                         'difference should work with strings'
        )
        self.assertEqual(self.tasks._EgnyteTasks__difference(1, 1), 0,
                         'difference should be 0 for equal arguments'
        )
        self.assertEqual(self.tasks._EgnyteTasks__difference(-3, -1), 2,
                         'difference should work with negative numbers'
        )
        self.assertEqual(self.tasks._EgnyteTasks__difference(-3, 1), 4,
                         'difference should work with various signs numbers'
        )

    def test_new_min(self):
        self.assertEqual(self.tasks._EgnyteTasks__new_min(None, 1), True,
                         'new_min should be True when old is None'
        )
        self.assertEqual(self.tasks._EgnyteTasks__new_min(6, 10), False,
                         'new_min should be False for larger new number'
        )
        self.assertEqual(self.tasks._EgnyteTasks__new_min(10, 6), True,
                         'new_min should be True for smaller new number'
        )

    def test_weather_matching(self):
        self.assertIsNone(self.tasks._EgnyteTasks__weather_match(''),
                         'weather_match should be None for empty string'
        )
        legend_line = ('  Dy MxT   MnT   AvT   HDDay  AvDP 1HrP TPcpn WxType '
                       + 'PDir AvSp Dir MxS SkyC MxR MnR AvSLP'
        )
        self.assertIsNone(self.tasks._EgnyteTasks__weather_match(legend_line),
                         'weather_match should be None for legend line'
        )
        valid_line = ('   1  88    59    74          53.8       0.00 F'
                      + '       280  9.6 270  17  1.6  93 23 1004.5'
        )
        self.assertIsNotNone(
            self.tasks._EgnyteTasks__weather_match(valid_line),
            'weather_match should not be None for valid line'
        )
        short_line = '   1  88    59    74 '
        self.assertIsNotNone(
            self.tasks._EgnyteTasks__weather_match(short_line),
            'weather_match should not be None for short line'
        )
        line_with_stars = '   1  88*   59*   74 '
        self.assertIsNotNone(
            self.tasks._EgnyteTasks__weather_match(line_with_stars),
            'weather_match should not be None for line with stars'
        )

    def test_team_matching(self):
        self.assertIsNone(self.tasks._EgnyteTasks__team_match(''),
                         'team_match should be None for empty string'
        )
        legend_line = ('       Team            P     W    L   D    '
                       +'F      A     Pts'
        )
        self.assertIsNone(self.tasks._EgnyteTasks__team_match(legend_line),
                         'team_match should be None for legend line'
        )
        valid_line = ('    1. Arsenal         38    26   9   3    '
                      +'79  -  36    87'
        )
        self.assertIsNotNone(
            self.tasks._EgnyteTasks__team_match(valid_line),
            'team_match should not be None for valid line'
        )
        short_line = '    1. Arsenal   79  -  36 '
        self.assertIsNotNone(
            self.tasks._EgnyteTasks__team_match(short_line),
            'team_match should not be None for short line'
        )
        

    def test_default_weather_file(self):
        self.assertEqual(self.tasks.smallest_temperature_spread(), 14,
                        'wrong day from default file'
        )

    def test_default_football_file(self):
        self.assertEqual(self.tasks.smallest_goals_difference(), 
                         'Aston_Villa', 'wrong team from default file'
        )


if __name__ == "__main__":
    unittest.main()