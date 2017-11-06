coordlist = []

for row in csvReader:
	lat = row[latIndex]
	lon = row[lonIndex]
	coordlist.append([lat],[lon])