import csv
import wikipedia
from bs4 import BeautifulSoup

footballer_names = []
footballer_data = []

with open('/Users/jackmorgan/Desktop/FOOTBALL/footballers.csv', 'rb') as f:
    reader = csv.reader(f)
    counter = 0
    for row in reader:
      if counter > 0:
        footballer_names.append(row[0])
      counter += 1

for footballer_name in footballer_names:
  html_ver = wikipedia.page(footballer_name, None, True, True, True).html()

  soup = BeautifulSoup(html_ver, 'html.parser')

  array = []
  found = False
  ignore_next = False

  for tr in soup.find("table", {"class":"infobox vcard"}).findChildren('tr'):

    if tr.text.find("Senior career*") > -1:
      found = True
      ignore_next = True
    elif tr.text.find("National team") > -1:
      found = False
      break

    if found == True and ignore_next == False:
      array.append(tr.text)
    elif ignore_next == True:
      ignore_next = False

  # remove the header
  array.remove(array[0])

  footballer_data.append(array)

  print (footballer_name + " played for: " + ', '.join(array))

# with open('/Users/Max/Desktop/footballer_clubs.csv', 'w') as fp:
#     a = csv.writer(fp, delimiter=',')
#     column_names = ['name', 'club', 'start_year', 'end_year']
#     a.writerows(column_names)
#     a.writerows(footballer_data)

