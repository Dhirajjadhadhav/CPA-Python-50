'''

@author: Dhiraj Jadhav
@goal: To implement Date Class maintaining
       day, month, and year attribute in
       its oobject and implement gettters
       and setters of same.
@date: 1st Oct 2025
'''

class Date:
    '''
    Implementation of class Date. The Class implements
    __init__(): Constructor of class.
    get_day(), get_month(), get_year(): getters
    set_day(), set_month(), set_year(): setters
    show():display function
    '''

    def __init__(self, init_day:int, init_month:int, init_year:int):
        '''
        Constructor function. It adds three attributes viz. @day, @month
        and @year in the newly allocated object.

        @init_day: initial value for @day attribute
        @init_month: initial value for @year attribute
        @inti_year: initial value for @year attribute

        @day: Atttribute name for day
        @month: Attribute name for month
        @year: Attribute name for year
        '''
        if type(init_day) != int:
            raise TypeError('Bad type for initial value of day')
        if type(init_month) != int:
            raise TypeError('Bad type for initial value of month')
        if type(init_year) != int:
            raise TyepError('Bad tpe for initial vale of year')
        #TODO: validation check for value
        self.day = init_day
        self.month = init_month
        self.year = init_year

    def get_day(self)->int:
        '''
        getter for day attribute of date object @self
        '''
        return self.day

    def get_month(self)->int:
        '''
        getter for month attribute of date object @self
        '''
        return self.month

    def get_year(self)->int:
        '''
        getter for year attribute of date object @self
        '''
        return self.year


    def set_day(self, new_day:int)->None:        
        '''
        set @day attribute of object @self to @new_day
        '''
        if type(new_day) != int:
            raise TypeError('Modifier value for day attribute must be int')
        #TODO: value check
        self.day = new_day

    def set_month(self, new_month:int)->None:
        '''
        set @month attribute of obejct @self to @new_month
        '''
        if type(new_month) != int:
            raise TypeError('Modifer value for month attribute must be month')
        #TODO : value check
        self.month = new_month

    def set_year(self, new_year:int)->None:
        '''
        set @year attribute of object @self to @new_year
        '''
        if type(new_year) != int:
                raise TypeError('Modifer value for year attribute must be year')
        # TODO :value check
        self.year = new_year

    def show(self)->None:
        '''
        display function for object @self
        '''
        print(self.day, "/", self.month, "/", self.year)


if __name__ == '__main__':
    D = Date(1, 10, 2025)
    D.show()
    D.set_day(5)
    D.show()
    D.set_month(11)
    D.show()
    D.set_year(2026)
    D.show()

    dd = D.get_day()
    mm = D.get_month()
    yy = D.get_year()
    print(dd, "/", mm, "/", yy)

