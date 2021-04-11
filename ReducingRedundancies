# ReducingRedundancies.py
# Purpose: 
# Created: February 11, 2021
# Created by: Jessica Hobbins
# Created for: GEOM73

# Importing ArcPy module
import arcpy
from arcpy import env

######################################################################
# Requirement #1: Create a file geodatabase at the workspace level
workspace = input("Please input the full path to your folder: ")
arcpy.env.workspace = workspace
arcpy.env.overwriteOutput = True # Set to False is overwrite is not desired

out_folder_path = workspace # Setting folder path to workspace
out_name = "Reducing_Redundancy" # Setting geodatabase name
geodatabase = arcpy.management.CreateFileGDB(out_folder_path, out_name) # Executing geodatabase creation

######################################################################
# Requirement #2: Iterate through the folders two levels down from the workspace level
# The client swears the first level down will always just be a single folder called "Shapefiles" as in the above example

# Creating empty list to append objects in workspace
foldernames = []
folders = []

# Using walk function to access files in workspace
wswalk = arcpy.da.Walk(workspace)
for dirpath, dirnames, filenames in wswalk:
    for dir in dirnames:
        foldernames.append(dir) # Appending just file name to list
        folders.append("{}\{}\{}".format(workspace, "Shapefiles", dir)) # Adding workspace path and hardcoding in the first level down folder "Shapefiles"

foldernames.remove(foldernames[0])  # Removing newly created geodatabse
foldernames.remove(foldernames[0])  # Removing Shapefiles folder
folders.remove(folders[0])  # Removing newly created geodatabse
folders.remove(folders[0])  # Removing Shapefiles folder

######################################################################
# Requirement #3: For each folder, create a feature class in the file geodatabase with the following specifications:
    # The name should be the same as the folder name
    # You can assume each feature class is a POINT feature class
    # The spatial reference can be acquired from any of the shapefiles in that folder

# Getting spatial reference from existing shapefile in workspace
files = []  # Creating empty list to hold shapefiles
filewalk = arcpy.da.Walk(folders[0])  # Using walk function to access first folder in folders
for dirpath, dirnames, filenames in filewalk:
    for file in filenames:
        files.append(file)
shapefile_sr = ("{}/{}".format(folders[0], files[0])) # Appending file to variable
sr = arcpy.Describe(shapefile_sr).spatialReference  # Getting spatial reference of file and applying it to new variable

# Settings for feature class creation
out_path = geodatabase  # Setting out path to geodatabase
geometry = "POINT"  # Setting geometry type to point

# Creating new feature classes named after folders
shpfolder = "{}\{}".format(workspace, "Shapefiles")
walk = arcpy.da.Walk(shpfolder)
for dirpath, dirnames, filenames in walk:
    for dir in dirnames:
        out_path = geodatabase
        out_name = dir
        geometry_type = "POINT"  # These settings may be adjusted as needed
        template = ""
        has_m = "DISABLED"
        has_z = "DISABLED"
        spatial_ref = sr
        fc = arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template, has_m, has_z, spatial_ref)
######################################################################
# Requirement #4: Add a field called TYPECODE to this feature class of type SHORT, then set it as the subtype field for the feature class
        in_table = fc
        field_name = "TYPCODE" # These settings may be adjusted as needed
        field_type = "SHORT"
        arcpy.management.AddField(in_table, field_name, field_type)
        arcpy.management.SetSubtypeField(in_table, field_name)
######################################################################
# Requirement #5: Establish a counter variable, and then for each shapefile in the folder:
# Add a subtype to the previously created feature class, where the subtype code is the current value of the counter,
# and the subtype name corresponds to the shapefile name scrubbed of the extension and the folder name
    # e.g. the subtype created from MajorClientsAtlantic.shp should just be called Atlantic, scrubbed of the .shp extension and the MajorClients folder name
        shppath = "{}\{}".format(workspace, "Shapefiles", out_name)
        shapewalk = arcpy.da.Walk(shppath)
        for dirpath, dirnames, filenames in shapewalk:
            count = 0 # Initiating counter variable
            for file in filenames:
                count += 1 # Count increases as files are iterated through loop
                subtype = file
                subtype = subtype[:-4] # Stripping files of .shp extension
                if out_name in file:
                    subtype = subtype.replace(out_name, "") # Stripping files of folder names
                    subtype_code = count # These settings may be adjusted as needed
                    subtype_description = subtype
                    sub = arcpy.management.AddSubtype(in_table, subtype_code, subtype_description)
                    filepath = "{}\{}\{}".format(shppath, out_name, file)
                    arcpy.env.workspace = filepath
                    with arcpy.da.SearchCursor(filepath, ["SHAPE@XY"]) as scursor:
                        with arcpy.da.InsertCursor(fc, ["TYPCODE", "SHAPE@XY"]) as icursor:
                            for row in scursor:
                                point = (count, row[0])
                                icursor.insertRow(point)
