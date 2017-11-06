def createPoints(coordinates, featureClass):
	import arcpy 
	with arcpy.da.InsertCursor(featureClass, ("SHApe@",)) as rowInserter:
		for coordinate in coordinateList:
			point = arcpy.Point(coordinate[0], coordinate[1])
			rowInserter.inserrtRow((point,))
