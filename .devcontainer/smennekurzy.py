import requests

URL = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/"
exchange_rates = []
table_line = []

data = requests.get(URL)

lines = data.text.splitlines()
counter = 1
for line in lines:

    line = line.strip()

    if not line.startswith("<td"):
        continue
    line = line.replace("<td>", "")
    line = line.replace("</td>", "")
    line = line.replace('<td align="right">', "")
    line = line.replace('<td align="center">', "")

    if counter == 6:
        print(table_line[0] + ": " + table_line[2] + " " + table_line[3] + " = " + table_line[4] + " CZK")
        table_line.clear()
        counter = 1
    
    table_line.append(line)
    counter = counter + 1
    if line.startswith("</tbody>"):
        break