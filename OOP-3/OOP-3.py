class Phone:
    def __init__(self, manufacturer, is_on_line, has_technical_issues):
        self.__manufacturer = manufacturer
        self.__is_on_line = is_on_line
        self.__has_technical_issues = has_technical_issues

    def fix_technical_issues(self):
        self.__has_technical_issues = True
        self.__is_on_line = True

    def turn_off(self):
        self.__is_on_line = False

    def turn_on(self):
        self.__is_on_line = True


class Smartphone(Phone):
    def __init__(self, m, ol, ti, os, screen_type, sim, memory_left):
        super().__init__(m, ol, ti)
        self.__os = os
        self.__screen_type = screen_type
        self.__sim = sim
        self.__memory_left = memory_left

    def pull_sim_out(self):
        self.__sim = None
        self.__is_on_line = False
        self.__has_technical_issues = True

    def take_photo(self, photo_size):
        self.__memory_left -= photo_size

    def battery_state(self, left_percents):
        if left_percents < 0:
            self.__is_on_line = False


class WiredPhone(Phone):
    def __init__(self, m, ol, ti, cable_length, numbers_keyboard_type):
        super().__init__(m, ol, ti)
        self.__cable_length = cable_length
        self.__numbers_keyboard_type = numbers_keyboard_type

    def cut_cable(self):
        self.__cable_length = None
        self.__has_technical_issues = True
        self.__is_on_line = False

    def fix_cable(self, cable_length):
        self.__cable_length = cable_length
        self.__is_on_line = True

