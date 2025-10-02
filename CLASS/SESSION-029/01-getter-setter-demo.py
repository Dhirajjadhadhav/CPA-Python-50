class Date:
    def __init__(self, init_day, init_month, init_year):
        self.day = init_day
        self.month = init_month
        self.year = init_year

    def get_day(self):
        return self.day

    def set_day(self, new_day):
        self.day = new_day

D = Date(30, 9, 2025)
d = D.get_day()
print('d:', d)
D.set_day(25)
d = D.get_day()
print('d:', d)
