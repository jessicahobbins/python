# SpatialRealtors.py
# Purpose: The purpose of this program is to take an input workspace and create a file geodatabase in that workspace, a new feature dataset within that geodatabase,
         # point feature classes within that feature dataset, and then read in text files of coordinates and add the point geometries to those feature classes.
# Created: February 11, 2021
# Created by: Jessica Hobbins
# Created for: GEOM73

# Importing ArcPy module
import arcpy
from arcpy import env

######################################################################
# Requirement #1: Take an input folder as a workspace.
workspace = input("Please input the full path to your folder: ")
arcpy.env.workspace = workspace
arcpy.env.overwriteOutput = True

######################################################################
# Requirement #2: Create a new file geodatabase called Realtor_Tracks
# Setting folder path to workspace
out_folder_path = workspace
# Setting geodatabase name
out_name = "Realtor_Tracks"
# Executing geodatabase creation
geodatabase = arcpy.management.CreateFileGDB(out_folder_path, out_name)

######################################################################
# Requirement #3: Create a new feature dataset within the file geodatabase called Realtors
# Dataset should have NAD83 UTM Zone 12 projection, same as the GPS devices

# Assigning spatial reference
wkt = "PROJCS['NAD_1983_UTM_Zone_12N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-123.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]];-5120900 -9998100 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision"
sr = arcpy.SpatialReference()
sr.loadFromString(wkt)
# Assinging feature dataset parameters
out_dataset_path = geodatabase
out_name = "Realtors"
spatial_reference = sr
# Executing CreateFeatureDataset tool
realtorsfd = arcpy.CreateFeatureDataset_management(out_dataset_path, out_name, sr)

######################################################################
# Requirement #4: For every text file in the workspace, it should:
# Create a feature class inside the feature dataset with the same name as the text file
# Read the coordinates from the file and insert them as points into the new FC

# Getting text files in workspace and assigning to variable txt
txt = arcpy.ListFiles("*.txt")
# Removing file extensions from txt file names
txtfiles = [x[:-4] for x in txt]
out_path = "{}/{}".format(geodatabase, "Realtors") # Setting outpath to Realtors feature dataset
geometry = "POINT" # Setting geometry type to point
import fileinput

for file in txt:
    out_name = file[:-4]
    fc = arcpy.CreateFeatureclass_management(out_path, out_name, geometry)  # Executing create feature class
    infile = "{}/{}".format(workspace, file)    # Setting infile as txt file
    f = fileinput.input(infile)
    next(f) # Skipping header row
    with arcpy.da.InsertCursor(fc, ["SHAPE@XY"]) as cursor: # Creating cursor on fc and shape field
        array = arcpy.Array()   # Creating empty array
        point = arcpy.Point()   # Creating empty point object
    for line in f:
        point.ID, point.X, point.Y = line.split()   # Split lines and assign to point variables
        point.ID, point.X, point.Y = float(point.ID), float(point.X), float(point.Y)    # Convert point variables from strings to floats
        array.add(point)    # Appending points to array
        pointgeometry = arcpy.PointGeometry(point)
        cursor.insertRow([pointgeometry])
    f.close()
    del cursor