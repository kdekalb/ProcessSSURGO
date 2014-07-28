#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:      Remove Null values to -99
#
# Author:      kundan dhakal
#
# Created:     23/07/2014
# Copyright:   (c) kundan 2014
# Licence:     <105BKCR_469AGH>
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy
fc = r'D:\SSURGO Database\SSURGO\ssurgo dump\Pool\SDM_State_OK.gdb\OK_Raster'




# Create a list of string fields
fields = arcpy.ListFields(fc, "", "Double")


rows = arcpy.UpdateCursor(fc)


for row in rows:
    for field in fields:
        if row.TEST == None:
            row.TEST = -99
            cursor.updateRow(row)

print "Processing complete"

del row