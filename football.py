import csv
import wikipedia
from bs4 import BeautifulSoup

with open("playerhistory.csv", "w") as fp:
    a = csv.writer(fp)
    a.writerow("")
    
footballer_names = []
footballer_data = []

#Open player name CSV file
with open('footballers.csv', 'rt') as f:
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

#'infobox card' is the class name of the table that Wiki uses for the player information    
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
  print(array)
  array.insert(0, footballer_name)
#   datafooty = footballer_name + " played for: " + ', '.join(array)
#   datafooty = datafooty.encode('ascii', 'replace')
#   print (datafooty)
  with open("playerhistory.csv", "a") as fp:
    a = csv.writer(fp)
    a.writerow(array)

#a.close()


