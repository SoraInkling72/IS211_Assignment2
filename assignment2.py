import argparse

import logging

import datetime
birthday = datetime.date.today()
print(today)
print('ctime  :', today.ctime())
tt = today.timetuple()
print('tuple  : tm_year  =', tt.tm_year)
print('         tm_mon   =', tt.tm_mon)
print('         tm_mday  =', tt.tm_mday)
print('         tm_hour  =', tt.tm_hour)
print('         tm_min   =', tt.tm_min)
print('         tm_sec   =', tt.tm_sec)
print('         tm_wday  =', tt.tm_wday)
print('         tm_yday  =', tt.tm_yday)
print('         tm_isdst =', tt.tm_isdst)
print('ordinal:', today.toordinal())
print('Year   :', today.year)
print('Mon    :', today.month)
print('Day    :', today.day)

def downloadData(url):
    """Downloads the data"""
    import urllib.request

    url = 'https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'
    values = {'id': 'Michael Foord',
              'name': 'Northampton',
              'birthday': 'Python'}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()

    # return the data
    return response


def processData(file_content):
pass


def displayPerson(id, personData):
pass

def main(url):
print(f"Running main with URL = {url}...")


if __name__ == "__main__":
"""Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
