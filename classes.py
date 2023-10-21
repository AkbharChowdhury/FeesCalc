class Workout:
    def __init__(self):
        self.__course_fees = dict(home=9250, international=13_000)

    def process(self, selection, courses):
        return self.__course_fees['home'] * courses if selection == 1 else self.__course_fees['international'] * courses

    def get_course_fees(self, course):
        return self.__course_fees[course]