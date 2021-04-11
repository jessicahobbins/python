# PresidentsVacation.py 
# Purpose: The purpose of this program is to take an input folder of geotagged photos and add them to a geodatabase as a point feature class.
         # The input folder for the photos is the same as the workspace and is entered by the user.
         # A geodatabase is created and named by the user and the points, also named by the user, are then added into the geodatabase.
         # Only the geotagged images are imported, as attachments.
# Created: January 30, 2021
# Created by: Jessica Hobbins
# Created for: GEOM73

# Importing ArcPy module
import arcpy

#####################################################
# Requirement #1: Use the folder containing the photos as its workspace
# Setting workplace environment
# Set workplace environment to folder you would like to take an inventory of
workspace = input("PLease input the full path to your folder: ")
arcpy.env.workspace = workspace

#####################################################
# Requirement #2: Create a new file geodatabase in that workspace using the Create File GDB tool
# Setting folder path to workspace
out_folder_path = workspace
# Requesting user to input geodatabase name
out_name = input("Enter a name for your geodatabase: ")
# Executing geodatabase creation
geodatabase = arcpy.management.CreateFileGDB(out_folder_path, out_name)

#####################################################
# Requirement #3: Call the GeoTagged Photos To Points tool with the following settings:
# The input folder should be the same as the workspace
# The output feature class should be created in the geodatabase created earlier
# The script should not import photos that aren't geotagged
# The script should add imported photos as attachments
# None of the sample pictures should be hardcoded into the script

# Setting input folder as workspace
Input_Folder = workspace
# Allowing user to name points
PointName = input("Enter a name for the points: ")
# Locating points feature class into previously made geodatabase
Output_Feature_Class = str(geodatabase) + str("/") + str(PointName)
# Editing tool parameters, importing only geotagged photos and importing as attachments
Invalid_Photos_Table = ""
Include_Non_GeoTagged_Photos = "ONLY_GEOTAGGED"
Add_Photos_As_Attachments = "ADD_ATTACHMENTS"

# Executing GeoTagged Photos to Points tool
arcpy.management.GeoTaggedPhotosToPoints(Input_Folder, Output_Feature_Class, Invalid_Photos_Table, Include_Non_GeoTagged_Photos, Add_Photos_As_Attachments)