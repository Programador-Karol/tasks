import urllib.request
import re


class EgnyteTasks():
    """Class resolving recruitment tasks for Egnyte."""
    def __init__(self):
        self.day_group = 'day'
        self.max_group = 'max'
        self.min_group = 'min'
        weather_regex_string = (r'^\s+(?P<day>\d+)'
                              + r'\s+(?P<max>\d+)\*?\s+'
                              + r'(?P<min>\d+)\*?\s+').format(
                               day = self.day_group, max = self.max_group, 
                               min = self.min_group
                               )
        self.weather_regex = re.compile(weather_regex_string)
        self.team_group = 'team'
        self.f_group = 'f'
        self.a_group = 'a'
        team_regex_string = (r'\s+\d+\.\s(?P<team>\w+)'
                       + r'.+\s+(?P<f>\d+)\s+-\s+(?P<a>\d+)\s+').format(
                       team = self.team_group, f = self.f_group, 
                       a = self.a_group
                       )
        self.team_regex = re.compile(team_regex_string)
        
    def smallest_temperature_spread(self, 
        file_path='http://codekata.com/data/04/weather.dat'
        ):
        """Find the day with smallest temperature spread"""
        data = urllib.request.urlopen(file_path)
        min_spread = None
        day_with_min_spread = None
        for line in data:
            m = self.__weather_match(line.decode())
            if m:
                spread = self.__difference(m.group(self.max_group),
                         m.group(self.min_group)
                         )
                if self.__new_min(min_spread, spread):
                    min_spread = spread
                    day_with_min_spread = int(m.group(self.day_group))
        return day_with_min_spread

    def __weather_match(self, line):
        return self.__match(self.weather_regex, line)

    def smallest_goals_difference(self, 
        file_path='http://codekata.com/data/04/football.dat'
        ):
        """Find the team with smallest goals difference."""
        data = urllib.request.urlopen(file_path)
        min_diff = None
        team_with_min_diff = None
        for line in data:
            m = self.__team_match(line.decode())
            if m:
                diff = self.__difference(m.group(self.f_group),
                         m.group(self.a_group)
                         )
                if self.__new_min(min_diff, diff):
                    min_diff = diff
                    team_with_min_diff = m.group(self.team_group)
        return team_with_min_diff

    def __team_match(self, line):
        return self.__match(self.team_regex, line)

    def __match(self, regex, line):
        return regex.match(line)

    def __new_min(self, current, new):
        return current is None or current > new

    def __difference(self, max, min):
        return abs(int(max) - int(min))


if __name__ == "__main__":
    tasks = EgnyteTasks()
    day = tasks.smallest_temperature_spread()
    if day is None:
        print('There is no day with temperatures in a file')
    else:
        print('The smallest temperature spread was on day {}.'.format(day))
    team = tasks.smallest_goals_difference()
    if team is None:
        print('There is no team in a file')
    else:
        print('The smallest goals difference has {} team.'.format(team))