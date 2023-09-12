import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
args = parser.parse_args()
main(args.url)

import logging
logging.debug('Debug the error')
logging.info('assignment2')
logging.warning('Warning')
logging.error('Something is wrong')
logging.critical('Critical error')

import datetime
birthday = datetime.date.birthday()
print(birthday)
print('ctime  :', birthday.ctime())
tt = birthday.timetuple()
print('tuple  : tm_year  =', tt.tm_year)
print('         tm_mon   =', tt.tm_mon)
print('         tm_mday  =', tt.tm_mday)
print('         tm_hour  =', tt.tm_hour)
print('         tm_min   =', tt.tm_min)
print('         tm_sec   =', tt.tm_sec)
print('         tm_wday  =', tt.tm_wday)
print('         tm_yday  =', tt.tm_yday)
print('         tm_isdst =', tt.tm_isdst)
print('ordinal:', birthday.toordinal())
print('Year   :', birthday.year)
print('Mon    :', birthday.month)
print('Day    :', birthday.day)

def downloadData(url):
    """Downloads the data"""
    import urllib.request

    url = 'https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'
    values = {'id': '2-101','personData': '2-101',
              'birthday': '2-101'}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()

    # return the data
    return response


def processData(downloadData):
    person_data = dict()

    for i, line in enumerate(file_content.split("\n")):
        if i == 0:
            # skip the header
            continue
        if len(line) == 0:
            # skip blank lines
            continue

        elements = line.split(",")
        id = int(elements[0])
        name = elements[1]
        try:
            birthday = datetime.datetime.strptime(elements[2], "%d/%m/%Y")
        except ValueError:
            logging.error(f"Error processing line #{i} for ID #{id}")
        person_data[id] = (name, birthday)
    return person_data


def displayPerson(id, personData):
    try:
        name, birthday = personData[id]
        print(f"Person #{id} is {name} with a birthday of {birthday:%Y-%m-%d}")
    except KeyError:
        print(f"No user found with that id")


def main(url):
    print(f"Running main with URL = {url}...")
    content = downloadData(url)
    personData = processData(content)
    while True:
        id = int(input("Enter an ID:"))
        if id < 0:
            break
        displayPerson(id, personData)


