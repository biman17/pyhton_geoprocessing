import arcpy

shp = "L:\\3rd_Sem\\GIS_Cust_Dev\\Data\\mydb.gdb\\DELHI_POI_font_point"

rows = arcpy.SearchCursor(shp)
row = rows.next()

while row:
	print row.NAME, row.ID
	row = rows.next()