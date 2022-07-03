import re
import collections
import csv


def parse_syslog(filename):
    result = []
    count = collections.Counter()
    header = ['Datetime', 'Count']
    file = open(filename, 'r')
    fr = file.readlines()
    file.close()

    write_csv = open('/tmp/parse_count.csv', 'w', encoding='UTF8')
    writer = csv.writer(write_csv)

    for line in fr:
        match = re.search(r'^(.*? \d+:\d+)', line)
        log = match.group()
        result.append(log)

    for x in result:
        count[x] += 1

    writer.writerow(header)
    writer.writerow(count)

    return count
    # match = re.match(r'^(.*? \d+ \d+\d+).*', line).group()
    # print(match)


print(parse_syslog('/var/log/system.log'))
