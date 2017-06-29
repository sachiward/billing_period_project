#Sachi Ward June 2017
#days start at midnight end at 11:59PM

"""
Billing Period Object
"""
import datetime
import sys
import math
import calendar


class Billing_Period(object):

    '''
        Initialize function for the Billing_Period class.

        1) Initializes Billing Period class
        2) Sets self.start_time to the default of 00:00:00
        3) Sets self.end_time to the default of 23:59:59
        4) Creates an empty list of voided_days
        5) Sets the self.number_of_voided_days variable equal to 0

        Arguments:
            self

        Returns:
            none
    '''
    def __init__(self):
        super(Billing_Period, self).__init__()

        self.start_time = datetime.time(0, 0, 0, 0000)

        self.end_time = datetime.time(23, 59, 59, 9999)

        self.voided_days = []

        self.number_of_voided_days = 0


    ############################################################################
    '''
        Checks whether or not the inputted date is a valid date.

        1) Sets the boolean result equal to True.
        2) Tries to convert the string argument date_to_check into a datetime object.  (If it works, the result boolean stays True)
        3) If the argument is not in the correct format or is not a valid date, jumps to the except ValueError and changes the result to False.
        4) Returns the result boolean.

        Arguments:
            date_to_check       - (string) Sent as an argument. Should be in the YYYY-MM-DD format (if not the function will return as False)

        Returns:
            result              - (bool) Returns as a True if the date is in the correct YYYY-MM-DD format and is a valid date.
    '''
    def check_valid_date(self, date_to_check):

        result = True

        try:
            d = datetime.datetime.strptime(date_to_check, '%Y-%m-%d')

        except ValueError:
            result = False

        return result


    ############################################################################
    '''
        Checks whether or not the inputted date is within the billing period.

        1) Sets a boolean variable result to False
        2) Converts the date_to_check argument to a datetime object and stores that into a variable d.
        3) Checks if d is greater than self.start_date and less than self.end_date
            a) If this is true:
                i) Change the value of result to True
        3) Returns result

        Arguments:
            date_to_check       - (string) Sent as an argument. Must be in the YYYY-MM-DD format.

        Returns:
            result              - (boolean) Returns True if the date is within the billing period and False if the date is not within the billing period.
    '''
    def check_date_in_billing_period(self, date_to_check):
        result = False
        d = datetime.datetime.strptime(date_to_check, '%Y-%m-%d')

        if d >= self.start_date and d <= self.end_date:
            result = True

        return result


    ############################################################################
    '''
        Sets the start date for the billing period.

        1) Calls the check_valid_date with the start_date argument and sets the return of the check_valid_date equal to the validity boolean.
        2) Checks whether or not the input is valid:
            a) If the input is valid:
                i) Sets self.start_date equal to the string argument start_date
                ii) Combines the start_time and start_date to create a self.start_datetime object
            b) Else:
                i) Writes a standard error to the system
        3) Returns

        Arguments:
            start_date      - (string) The desired start date for the billing period.  Must be inputted in YYYY-MM-DD format.

        Returns:
            none
    '''
    def set_start_date(self, start_date):

        validity = check_valid_date(start_date)

        if validity == True:
            self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            self.start_datetime = datetime.datetime.combine(self.start_date, self.start_time)

        else:
            sys.stderr.write('Error: Start Date not allowed. Must be a valid date and in the YYYY-MM-DD format.')

        return


    ############################################################################
    '''
        Function that returns the set start date.

        1) Returns the datetime object format of self.start_date.

        Arguments:
            none

        Returns:
            self.start_date    - (datetime object) The set start_date for the billing period.
    '''
    def get_start_date(self):

        return datetime.strptime(self.start_date, '%Y-%m-%d')


    ############################################################################
    '''
        Sets the end date for the billing period.

        1) Checks for the validity of the entered date by calling the check_valid_date function with the end_date argument.
        2) Checks whether or not the input is valid:
            a) If the input is valid:
                i) Checks if the end date entered is after the start date for the billing period:
                    a) If the end date is after the start date:
                        i) Sets self.end_date equal to the string argument end_date
                        ii) Combines the end_date and end_time to create a self.end_datetime object
                    b) If the end date is before the start date:
                        i) Writes a standard error to the system
            b) If the input is invalid:
                i) Writes a standard error to the system
        3) Returns

        Arguments:
            end_date      - (string) The desired end date for the billing period.  Must be entered in the YYYY-MM-DD format, a valid date, and must be the same as the start date or after it.

        Returns:
            none
    '''
    def set_end_date(self, end_date):

        validity = check_valid_date(end_date)

        if validity == True:
            if end_date >= str(self.start_date):
                self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
                self.end_datetime = datetime.datetime.combine(self.end_date, self.end_time)

            elif end_date < str(self.start_date):
                sys.stderr.write('Error: End Date not allowed. Must be after %s' % str(start_date))

        else:
            sys.stderr.write('Error: End Date not allowed. Must be a valid date and in the YYYY-MM-DD format.')

        return


    ############################################################################
    '''
        Function that returns the set end date.

        1) Returns the datetime object format of self.end_date.

        Arguments:
            none

        Returns:
            self.end_date       - (datetime object) The set end date for the billing period.
    '''
    def get_end_date(self):

        return datetime.strptime(self.end_date, '%Y-%m-%d')


    ############################################################################
    '''
        Function that allows you to void days from the billing period.

        1) Sets a variable x equal to 0. (This will be used as an index)
        2) Begins a for-in loop to run through the days_to_void list argument and for every date:
            a) Calls the check_valid_date function to check the validity of the called date argument and sets it equal to a validity variable.
            b) Calls the check_date_in_billing_period function with the argument days_to_void and sets it equal to a dibp variable (date in billing period)
            c) Checks if the validity boolean is True and if the datetime object is within the billing period.
                i) If the validity boolean and the dibp boolean are True:
                    a) Sets a dt datetime object variable equal to the string at the x index in the days_to_void list.
                    b) Appends the datetime object d to the self.voided_days list.
                    c) Sets the self.number_of_voided_days variable equal to the length of the self.voided_days list.
                ii) If not:
                    a) Write a standard error to the system.
            d) Bumps up the x index by one.
        4) Returns

        Arguments:
            days_to_void         - (list of strings) Desired date(s) to void.  Must be in YYYY-MM-DD format and within the billing period.  Separate each date with a comma.

        Returns:
            none
    '''
    def void_days(self, days_to_void):

        x = 0
        for dates in days_to_void:
            validity = check_valid_date(days_to_void[x])
            dibp = check_date_in_billing_period(days_to_void[x])

            if validity and dibp:
                dt = datetime.datetime.strptime(days_to_void[x], '%Y-%m-%d')
                self.voided_days.append(dt)
                self.number_of_voided_days = len(self.voided_days)

            else:
                sys.stderr.write('Error: Date entered not allowed. Must be a valid date, within the billing period, and in the YYYY-MM-DD format.')

            x += 1

        return


    ############################################################################
    '''
        Function that returns the voided days for the billing period.

        1) Returns the list self.voided_days

        Arguments:
            none

        Returns:
            self.voided_days        - (list) The days in a billing period to be voided (and not billed for).
    '''
    def get_voided_days(self, day_to_void):

        return self.voided_days


    ############################################################################
    '''
        Function that returns the total number of days in a billing period based on the start date, end date, and whether or not you want to include the start/end days.

        1) Checks if there are any voided days for the billing period.
            a) If there are no voided days for the billing period:
                i) Sets duration (a timedelta object) equal to the absolute value of the self.end_date minus the self.start_date datetime objects and adds a day to account for the 23:59:59 end time of billing days.
            b) If there are voided days for the billing period:
                ii) Does the same calculation as in step 1ai) but accounts for the voided days by subtracting a timedelta object of days = self.number_of_voided_days.
            c) Returns duration

        Arguments:
            none

        Returns:
            duration            - (timedelta object) The length of the billing period.
    '''

    def duration_days(self):

        if self.number_of_voided_days == 0:
                duration = abs(self.end_date - self.start_date) + datetime.timedelta(days = 1)

        else:
            duration = abs(self.end_date - self.start_date) + datetime.timedelta(days = 1) - datetime.timedelta(days = self.number_of_voided_days)

        return duration


    ############################################################################
    '''
        Calculates the total number of hours in a billing period based on the start and end days.  Includes the last day.

        1) Sets x equal to self.end_datetime minus self.start_datetime.  (x is now a timedelta object)
        2) Uses the timedelta method total_seconds and sets seconds equal to x.total_seconds()
        3) Sets hours equal to the ceiling of seconds // 3600
        4) Sets minutes equal to the ceiling of (seconds % 3600) // 60
        5) Rounds seconds up using math.ceil(seconds % 60)
        6) Checks if there are any voided days in the billing period.
            a) If there are no voided days:
                i) Sets self.totalhours equal to the ceiling of the sum of hours and minutes // 60 and seconds // 60
            b) If there are voided days:
                i) Sets self.totalhours equal to the ceiling of the sum of hours and minutes // 60 and seconds // 60  and subtracts the self.number_of_voided_days variable multiplied by 24.
        7) Returns self.totalhours

        Arguments:
            none

        Returns:
            totalhours          - (timedelta object) The total number of hours in the billing period.  (Rounded up one second since days end at 23:59:59 and start at 00:00:00)
    '''
    def duration_hours(self):

        x = self.end_datetime - self.start_datetime

        seconds = x.total_seconds()
        hours = math.ceil(seconds // 3600)
        minutes = math.ceil((seconds % 3600) // 60)
        seconds = math.ceil(seconds % 60)

        if self.number_of_voided_days == 0:
            self.totalhours = math.ceil(hours + minutes // 60 + seconds // 60)

        else:
            self.totalhours = math.ceil(hours + minutes // 60 + seconds // 60) - self.number_of_voided_days * 24

        return self.totalhours


    ############################################################################
    '''
        Given a duration period in days and a start date, this function calculates the end date for that billing period.  Note: This function doesn't factor in voided days.dura

        1) Sets an interval variable equal to the timedelta object duration - one timedelta day (since the days end at 23:59:59, not midnight of the next day).
        2) Sets a local end_date variable equal to self.start_date plus the interval.
        3) Converts the end_date datetime local variable to a string format
        4) Calls the set_end_date function to set self.end_date and self.end_datetime equal to the local string_end_date variable.
        5) Returns self.end_date

        Arguments:
            duration             - (integer) Desired length of the billing period.

        Returns:
            self.end_date        - (datetime object) The end date of the billing period.
    '''
    def end_date_from_duration(self, duration):

        interval = datetime.timedelta(days = duration) - datetime.timedelta(days = 1)
        end_date = (self.start_date + interval)
        string_end_date = end_date.strftime('%Y-%m-%d')
        set_end_date(string_end_date)

        return self.end_date


    ############################################################################
    '''
        Finds the last day of the last billing period.

        1) Creates datetime object today and sets it equal to datetime.date.today().
        2) Checks if today's day is greater than 14 (the default end day of every billing period) and smaller than the last day of today's month:
            a) If the day is greater than 14 and less than or equal to the last day of the month:
                i) Set a datetime object last_billing_period with the same month and year as the today datetime object, but with a day of 14.
            b) Else if today is less than 14 and greater than 0:
                i) Check if the today's month is January:
                    a) If it isn't January, then set last_billing_period with the same year as today, with the day of 14, and one month earlier than today.
                    b) If it is January, set last_billing_period with a day of 14 and one month and one year earlier than today.
            c) If today's day is the 14th:
                i) set the last_billing_period equal to today.

        Arguments:
            none

        Returns:
            last_billing_period         - (datetime object) The last day of the last billing period.
    '''
    def find_end_of_last_billing_period(self):

        today = datetime.datetime.today()

        if today.day > 14 and today.day <= calendar.monthrange(today.year, today.month)[1]:
            last_billing_period = datetime.datetime(day = 14, month = today.month, year = today.year)

        elif today.day < 14 and today.day > 0:
            if today.month != 01:
                last_billing_period = datetime.datetime(day = 14, month = today.month - 1, year = today.year)

            else:
                last_billing_period = datetime.datetime(day = 14, month = today.month - 1, year = today.year - 1)

        if today.day == 14:
            last_billing_period = today

        return last_billing_period


    ############################################################################
    '''
        Calculates the number of days since the last billing period.  By default, the end date for the last billing period is the 14th of the month (or the previous month) at 11:59:59.
        Change the number 14 throughout the function if you want to change the end_date of the billing periods.

        1) Calls the find_end_of_last_billing_period function and inputs the return into the datetime object last_billing_period.
        2) Set a days_since variable equal to the absolute value of today's date minus the last_billing_period's date
        3) Return days_since.days

        Arguments:
            none

        Returns:
            days_since.days         - (int) The number of days since the last day of the billing period.  (Count includes today, but not the last day of the billing period)
    '''
    def get_days_since(self):

        last_billing_period = find_end_of_last_billing_period()

        days_since = abs(today - last_billing_period)

        return days_since.days


    ############################################################################
    '''
        Calculates the total number of hours since the last billing period.

        1) Creates datetime object today and sets it equal to datetime.date.today().
        2) Creates the datetime object beginning_of_today and sets the day to today.day, the year to today.year, and the month to today.month.
        3) Sets the hour and minute to 00:00
        4) Calls the find_end_of_last_billing_period function and inputs the return into the datetime object last_billing_period.
        5) Calculates the absolute value of beginning_of_today minus last_billing_period and inputs the difference into the timedelta object time_since.
        6) Creates an hours_since float variable and sets it equal to the ceiling of (time_since.total_seconds() // 3600) - 24.
        7) Returns the float variable hours_since.

        Arguments:
            none

        Returns:
            hours_since        - (float) The total number of hours since the last billing period.  Doesn't include the last day of the billing period since it ends at 23:59:59 or today (ends count at midnight of today).
    '''
    def get_hours_since(self):

        today = datetime.datetime.today()

        beginning_of_today = datetime.datetime(day = today.day, year = today.year, month = today.month)

        beginning_of_today = beginning_of_today.replace(hour = 00, minute = 00)

        last_billing_period = find_end_of_last_billing_period()

        time_since = abs(beginning_of_today - last_billing_period)

        hours_since = math.ceil(time_since.total_seconds() // 3600) - 24

        return hours_since


    ############################################################################
    '''
        Calculates the total number of billable days since the last billing period.  By default, the end date for the last billing period is the 14th of the month (or the previous month) at 11:59:59.
        Change the number 14 throughout the function if you want to change the end_date of the billing periods.

        1) Creates datetime object today and sets it equal to datetime.date.today().
        2) Calls the find_end_of_last_billing_period function and inputs the return into the datetime object last_billing_period.
        3) Set a days_since variable equal to the absolute value of today's date minus the last_billing_period's date.
        4) Return days_since.days.

        Arguments:
            none

        Returns:
            days_since.days         - (int) The number of days since the end of the last billing period that are billable (not voided). (Count includes today, but not the last day of the billing period)
    '''
    def get_billable_days_since(self):

        today = datetime.datetime.today()

        last_billing_period = find_end_of_last_billing_period()

        days_since = abs(today - last_billing_period)

        if self.number_of_voided_days > 0:
            days_since.days = days_since.days - datetime.timedelta(days = self.number_of_voided_days)

        return days_since.days


    ############################################################################
    '''
        Calculates the total number of hours since the last billing period.

        1) Creates datetime object today and sets it equal to datetime.date.today().
        2) Creates the datetime object beginning_of_today and sets the day to today.day, the year to today.year, and the month to today.month.
        3) Sets the hour and minute to 00:00
        4) Calls the find_end_of_last_billing_period function and inputs the return into the datetime object last_billing_period.
        5) Calculates the absolute value of beginning_of_today minus last_billing_period and inputs the difference into the timedelta object time_since.
        6) Creates an hours_since float variable and sets it equal to the ceiling of (time_since.total_seconds() // 3600) - 24.
        7) Checks if there are any voided_days:
            a) If there any voided days, sets the hours_since variable equal to itself minus the number of voided days multiplied by 24.
        8) Returns the float variable hours_since.

        Arguments:
            none

        Returns:
            hours_since        - (float) The total number of billable hours (non-voided days) since the last billing period.  Doesn't include the last day of the billing period since it ends at 23:59:59, today (ends count at midnight of today), or any voided days.
    '''
    def get_billable_hours_since(self):

        today = datetime.datetime.today()

        beginning_of_today = datetime.datetime(day = today.day, year = today.year, month = today.month)

        beginning_of_today = beginning_of_today.replace(hour = 00, minute = 00)

        last_billing_period = find_end_of_last_billing_period()

        time_since = abs(beginning_of_today - last_billing_period)

        hours_since = math.ceil(time_since.total_seconds() // 3600) - 24

        if self.number_of_voided_days > 0:
            hours_since = hours_since - (24 * self.number_of_voided_days)

        return hours_since


    ############################################################################
