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
fields = ['db_0_10','db_11_20','db_21-30','db_31_60','db_61_90','db_91_120','db_121_150','db_151_180','om_0_10','om_11_20','om_21-30','om_31_60','om_61_90','om_91_120','om_121_150','om_151_180','cec_0_10','cec_11_20','cec_21-30','cec_31_60','cec_61_90','cec_91_120','cec_121_150','cec_151_180','ksat_0_10','ksat_11_20','ksat_21-30','ksat_31_60','ksat_61_90','ksat_91_120','ksat_121_150','ksat_151_180','clay_0_10','clay_11_20','clay_21-30','clay_31_60','clay_61_90','clay_91_120','clay_121_150','clay_151_180','silt_0_10','silt_11_20','silt_21-30','silt_31_60','silt_61_90','silt_91_120','silt_121_150','silt_151_180','sand_0_10','sand_11_20','sand_21-30','sand_31_60','sand_61_90','sand_91_120','sand_121_150','sand_151_180','pH_0_10','pH_11_20','pH_21-30','pH_31_60','pH_61_90','pH_91_120','pH_121_150','pH_151_180'
]

rows = arcpy.UpdateCursor(fc)

for row in rows:
    for FIELD in fields:
        if row.TEST == None:
            row.TEST = -99
            cursor.updateRow(row)

print "Processing complete"

del row