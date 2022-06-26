import re
from re import match


def extract_names(filename):
    """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
    # +++your code here+++
    # Extract the year and print it
    file = open(filename, 'r')
    fr = file.read()
    file.close()

    match = re.search(r'\d\d\d\d', filename)
    year = match.group()
    print(year)

    nr_match = re.findall(r'<td>(.*?)</td>', fr, re.M | re.I | re.S)
    print(nr_match)
 
    print(nr_rank)


extract_names('baby1990.html')
