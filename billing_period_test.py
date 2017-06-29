import unittest
import datetime
import sys
import math
import calendar

class TestStringMethods(unittest.TestCase):

    def test_check_valid_date(self):

        date_to_check = '2015-02-20'

        result = True

        try:

            d = datetime.datetime.strptime(date_to_check, '%Y-%m-%d')

        except ValueError:

            result = False

        self.assertEqual(result, True)

        return result

    def test_check_date_in_billing_period(self):

        end_date = '2017-06-14'
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        start_date = '2017-05-15'
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        date_to_check = '2017-05-26'

        d = datetime.datetime.strptime(date_to_check, '%Y-%m-%d')

        if d >= start_date and d <= end_date:

            print 'Yes!'

        else:

            print 'No :('

        return


    def test_set_start_date(self):

        start_date = '2015-01-01'
        validity = True
        start_time = datetime.time(0, 0, 0, 0000)

        if validity == True:

            start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            start_datetime = datetime.datetime.combine(start_date, start_time)

        else:

            sys.stderr.write('Error: Start Date not allowed. Must be a valid date and in the YYYY-MM-DD format.')

        self.assertTrue(start_date, '2015-01-01')

        self.assertTrue(start_datetime, '2015-01-01 00:00:00')

    def test_get_start_date(self):

        start_date = '2015-01-01'

        sd = datetime.datetime.strptime(start_date, '%Y-%m-%d')

        self.assertTrue(sd, '2015-01-01')

    def test_set_end_date(self):

        start_date = '2015-01-01'

        end_date = '2016-01-01'

        end_time = datetime.time(23, 59, 59, 9999)

        validity = True

        if validity == True:

            if end_date >= str(start_date):

                end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')

                end_datetime = datetime.datetime.combine(end_date, end_time)

            elif end_date < str(start_date):

                sys.stderr.write('Error: End Date not allowed. Must be after %s' % str(start_date))

                x = 'Error: End Date not allowed. Must be after %s' % str(start_date)

                return x

        else:

            sys.stderr.write('Error: End Date not allowed. Must be a valid date and in the YYYY-MM-DD format.')

            x = 'Error: End Date not allowed. Must be a valid date and in the YYYY-MM-DD format.'

            return x


        self.assertTrue(end_date, '2016-01-01')

        self.assertTrue(end_datetime, '2016-01-01 23:59:59')

        self.assertEqual(validity, True)

    def test_get_end_date(self):

        end_date = '2016-01-01'

        ed = datetime.datetime.strptime(end_date, '%Y-%m-%d')

        self.assertTrue(ed, '2016-01-01')
        
    def test_void_days(self):

        validity = True
        days_to_void = ['2017-06-10', '2017-06-11', '2017-06-12']
        start_date = '2017-05-15'
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = '2017-06-14'
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        voided_days = []

        x = 0
        for dates in days_to_void:
            dibp = True

            if validity and dibp:
                dt = datetime.datetime.strptime(days_to_void[x], '%Y-%m-%d')
                voided_days.append(dt)
                number_of_voided_days = len(voided_days)

            else:
                sys.stderr.write('Error: Date entered (%s) not allowed. Must be a valid date, within the billing period, and in the YYYY-MM-DD format.' % days_to_void[x])

            x += 1

        print voided_days, number_of_voided_days
        print type(voided_days), type(number_of_voided_days)

        return
    
    
    def test_get_voided_days(self):
        voided_days = []
        voided_days.append('2017-05-19')
        print voided_days
        print type(voided_days)


    def test_duration_days(self):

        end_date = '2017-06-14'
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        start_date = '2017-05-15'
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')

        number_of_voided_days = 0

        if number_of_voided_days == 0:

                duration = abs(end_date - start_date) + datetime.timedelta(days = 1)

        else:

            duration = abs(end_date - start_date) + datetime.timedelta(days = 1) - datetime.timedelta(days = number_of_voided_days)

        print duration

        return duration

    def test_duration_hours(self):
        end_time = datetime.time(23, 59, 59, 9999)
        end_date = '2017-06-14'
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        end_datetime = datetime.datetime.combine(end_date, end_time)
        start_time = datetime.time(0, 0, 0, 0000)
        start_date = '2017-05-15'
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        start_datetime = datetime.datetime.combine(start_date, start_time)

        x = end_datetime - start_datetime

        seconds = x.total_seconds()

        hours = math.ceil(seconds // 3600)

        minutes = math.ceil((seconds % 3600) // 60)

        seconds = math.ceil(seconds % 60)

        # totalhours = math.ceil(hours + minutes // 60 + seconds // 60)

        number_of_voided_days = 3

        totalhours = math.ceil(hours + minutes // 60 + seconds // 60) - number_of_voided_days * 24

        print totalhours

        return totalhours

    def test_end_date_from_duration(self):

        start_date = '2017-05-15'
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        duration = 31

        interval = datetime.timedelta(days = duration) - datetime.timedelta(days = 1)

        end_date = (start_date + interval)

        string_end_date = end_date.strftime('%Y-%m-%d')


        #set_end_date function below
        final_end_date = datetime.datetime.strptime(string_end_date, '%Y-%m-%d')

        print final_end_date

    def test_find_end_of_last_billing_period(self):

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

        #print type(last_billing_period)

        return last_billing_period

    def test_get_days_since(self):

        last_billing_period = '2017-06-14'
        end_time = datetime.time(23, 59, 59, 9999)
        last_billing_period = datetime.datetime.strptime(last_billing_period, '%Y-%m-%d')

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

        days_since = abs(today - last_billing_period)

        #print days_since.days

        return days_since.days


    def test_get_hours_since(self):

        today = datetime.datetime.today()
        beginning_of_today = datetime.datetime(day = today.day, year = today.year, month = today.month)
        beginning_of_today = beginning_of_today.replace(hour = 00, minute = 00)

        if today.day > 14 and today.day <= calendar.monthrange(today.year, today.month)[1]:
            last_billing_period = datetime.datetime(day = 14, month = today.month, year = today.year)
        elif today.day < 14 and today.day > 0:
            if today.month != 01:
                last_billing_period = datetime.datetime(day = 14, month = today.month - 1, year = today.year)
            else:
                last_billing_period = datetime.datetime(day = 14, month = today.month - 1, year = today.year - 1)

        time_since = abs(beginning_of_today - last_billing_period)

        hours_since = math.ceil(time_since.total_seconds() // 3600) - 24

        print type(hours_since)

        print hours_since
        print 'get_hours_since function'


    def test_get_billable_days_since(self):

        last_billing_period = '2017-06-14'
        end_time = datetime.time(23, 59, 59, 9999)
        last_billing_period = datetime.datetime.strptime(last_billing_period, '%Y-%m-%d')
        number_of_voided_days = 0

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

        days_since = abs(today - last_billing_period)

        if number_of_voided_days > 0:

            days_since = days_since - datetime.timedelta(days = number_of_voided_days)

        #print days_since.days
        #print type(days_since.days)
        #return days_since.days

    def test_get_billable_hours_since(self):

        today = datetime.datetime.today()
        beginning_of_today = datetime.datetime(day = today.day, year = today.year, month = today.month)
        beginning_of_today = beginning_of_today.replace(hour = 00, minute = 00)

        if today.day > 14 and today.day <= calendar.monthrange(today.year, today.month)[1]:
            last_billing_period = datetime.datetime(day = 14, month = today.month, year = today.year)
        elif today.day < 14 and today.day > 0:
            if today.month != 01:
                last_billing_period = datetime.datetime(day = 14, month = today.month - 1, year = today.year)
            else:
                last_billing_period = datetime.datetime(day = 14, month = today.month - 1, year = today.year - 1)

        time_since = abs(beginning_of_today - last_billing_period)

        hours_since = math.ceil(time_since.total_seconds() // 3600) - 24
        number_of_voided_days = 0

        if number_of_voided_days > 0:

            hours_since = hours_since - (24 * number_of_voided_days)

        print type(time_since)

        print type(hours_since)

        print hours_since
        print 'get_hours_since function 2'

    if __name__ == '__main__':
        unittest.main()
