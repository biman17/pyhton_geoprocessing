import arcpy
arcpy.env.overwriteOutput = True
try:
    #get the input parameteres
    inpath = arcpy.GetParameterAsText(0)
    outpath = arcpy.GetParameterAsText(1)
    buff_dist = arcpy.GetParameterAsText(2)

    #run the buuffer function
    arcpy.Buffer_analysis(inpath, outpath, buff_dist)

    arcpy.AddMessage("Buffer created successfully")

except:
    #error message
    arcpy.AddError("Error!!!")

    #report error message the buffer tool generated
    arpy.AddMessage(arcpy.GetMessage())
