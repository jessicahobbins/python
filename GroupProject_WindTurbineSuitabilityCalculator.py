# WindTurbineSuitabilityCalculator.py
# Created for GEOM67 - Problem Solving & Programming
# Created by: Group 5 - Samir Imamovic, Dale Langford, Chelsea Penglington, Jessica Hobbins
# Documentation done by Chelsea Penlington
# Date created: November 30, 2020

# The purpose of this program is to determine whether site locations within the Peterborough Region are suitable for the 
# construction of wind energy turbines.
# The program assesses the site in relation to nearby obstacles (given obstacle hieght and turbine height), wind speed 
# (given tower height and surroudning vegetation), wind power and wind density.

# This program makes the following assumptions based on 2020 yearly data averages for the Peterborough area:
# Wind Speed: 13.9km/hr at 10m
# Wind Direction: West
# Humidity: 76%
# Temperature: 6 degrees celcius
# Pressure: 101.62 kPa
# Air Density: 0.12347 kg/m3
# Roughness lengths of surfaces.

# Import CSV to read in test values input by client/user
import csv
# Import math for use in CalcWindPower function (math.pi)
import math

####################### Programmer Defined Functions ############################

# Function to calculate suitability in relation to obstacle clearance
# Programmer defined function created by Samir Imamovic and Dale Langford
def CalcObstClearance(ObstHeight, ObstDirec, ObstProximity, BladeRadius, TurbineHeight):
    WindDirection = "W"                                     # Average wind direction for Ptb Region is west
    ObstDirec = ObstDirec.upper()                           # To ensure that the directional value input is upper case
    ObstClearance = (ObstHeight + BladeRadius + 10)         # Turbine height needs to be above obstacle height + 10 m + 
                                                            # blade radius for adequate obstacle clearance
    # If statement to ensure that the directional value input by user is N, NE, E, SE, S, SW, W or NW
    if ((str(ObstDirec) != "N") and (str(ObstDirec) != "NE") and (str(ObstDirec) != "E") and (str(ObstDirec) != "SE") and 
    (str(ObstDirec) != "S") and (str(ObstDirec) != "SW") and (str(ObstDirec) != "W") and (str(ObstDirec) != "NW")):
        MeetsReq = "Invalid Entry"                          # If direction does not equal one of the valif enties then the meets 
                                                            # requirments variable will return Invalid Entry message to the user.

    elif (ObstHeight <= 0):                                 # If statement to handle zero and negative numbers for obstacle 
                                                            # height input, obstacle height must be greater then zero.
        MeetsReq = "Invalid Entry"                          # If obstacle height is less then or equal to zero then meets 
                                                            # requirement variable will return Invalid Entry message to the user.

    elif (ObstProximity <= 0):                              # If statement to handle zero or negative numbers for obstacle 
                                                            # proximity input
        MeetsReq = "Invalid Entry"                          # If obstacle proximity is less then or equal to zero then meets 
                                                            # requirement varible will return Invalid Entry message to the user

    # Turbine height must be greater then obstacle height, proximity of obstable to turbine must be greater then then blade 
    # radius + 10 m, obstacle direction can not equal pervailing wind direction to meet the requirments for suitability of a 
    # wind turbine location.
    elif ((TurbineHeight > ObstClearance) and (ObstProximity > (BladeRadius + 10)) and (WindDirection != ObstDirec)):
        MeetsReq= "Yes"                                     # If values input by user meet obstacle clearance requirments for a 
                                                            # turbine location then variable returned to user will be assigned Yes

    else:                                                   # Else if values input do not meet requirments they will be assigned No  
        MeetsReq= "No"                                        
    return MeetsReq                                         # Return value of meets requirments variable back to program when called

# Function to calculate wind shear based on user inputs for roughness length and given values of wind speed and speed height 
# for Peterborough region.
# Programmer defined function created by Jessica Hobbins
def CalcWindShear(TurbineHeight, RoughnessLength):
    AvgWindSpeed = 13.9                                     # Average wind speed for Ptb Region in km/hr 
    AvgSpeedHeight = 10                                     # Height at which average speed was calculated for Ptb Region

    if (RoughnessLength != 0.0002) and (RoughnessLength != 0.0024) and (RoughnessLength != 0.03) and \
        (RoughnessLength != 0.055) and (RoughnessLength != 0.1) and (RoughnessLength != 0.2) and \
            (RoughnessLength != 0.4) and (RoughnessLength != 0.8) and (RoughnessLength != 1.6):
        Shear = "Invalid Entry"                             # If roughness length is not one of the valid entries wind 
                                                            # shear value will return invalid entry to user
    
    else:
        Shear = (AvgWindSpeed*(TurbineHeight/RoughnessLength))/(AvgSpeedHeight/RoughnessLength)     # Wind shear calculation, WindShear = AverageWindSpeed x (TurbineHeight / RoughnessLength) / (AverageWindSpeed / RoughnessLength)
        Shear = round(Shear,3)                                                                      # Round calculated wind shear value to three decimal places
    return Shear                                                                                    # Return value of wind shear back to program when called

# Function to calculate wind power density of turbine site location based on user input of blade radius and given values for air density and wind speed for the region
# Programmer defined function created by Chelsea Penlington
def CalcWindPower(Radius):
    AirDensity = 0.12347                                    # Average air density in kg/m3 for Ptb Region
    WindSpeed = 13.9                                        # Average wind speed in km/hr at 10m for Ptb Region
    
    PowerDensity = 0.5*((AirDensity)*((math.pi*Radius)**2) *(WindSpeed**3))     # Wind power density calculation, WindPowerDensity = 0.5 x AirDensity x (Pi x BladeRadius)^2 x WindSpeed^3
    PowerDensity = round(PowerDensity,3)                                        # Round wind power density value calculated to three decimal places
    return PowerDensity                                                         # Return value of wind power density value to program when called

########################## Main Program ###################################

# Try statement for exeption handlers, exceptions listed at the bottom of the program 
# Try statement and exceptions handlers created by Dale Langford
try:   
    # Main program function defined   
    # Content of main function where contributed to and edited by all group members
    def main():
        # Display purpose of the program to user 
        # Introductory print statments created by Chelsea Penlington
        print("This program will assess your site(s) in relation to nearbly obstacles, wind speed, wind power and wind density.")
        # Display the given values for calculations for the Peterborough region to the user including wind speed, 
        # wind direction, humidity, temperature, pressure and air density
        print ("The following assumptions are made based on 2020 yearly data averages for the Peterborough area:")
        print("Wind Speed: 13.9km/hr at 10m")
        print("Wind Direction: West")
        print("Humidity: 76%")
        print("Temperature: 6 degrees celsius")
        print("Pressure: 101.62 kPa")
        print("Air Density: 0.12347 kg/m3")
        print("Roughness lengths of surface areas.")
        print()
        print("*****************************************************************************************************************")
        print()
        # Display the requirements for the CSV file the user will input to the program including the site id, 
        # proximity of the nearest obstacle to turbine location, height of obstacle, direction of obstacle from wind turbine site, 
        # and roughness length of the turnbine site location
        print("In your csv file, please include the following:")
        print("Site ID")
        print("Proximity to nearby obstacle (m)")
        print("Height of nearby obstacle (m)")
        print("Direction of obstacle (N, W, S, E)")
        print("Roughness length of surface")
        print()
        print("*****************************************************************************************************************")
        print()
        # Creating empty list that will hold user data from CSV file
        # List code created by Jessica Hobbins
        input_ID = []                           # List to hold site IDs 
        input_ProxObst = []                     # List to hold proximity of nearest obstacle to turbine site values
        input_HeightObst = []                   # List to hold height of ostacle values
        input_DirectionObst = []                # List to hold direction of nearest obtacle from turbine
        input_RoughnessLength = []              # List to hold roughness length of the site location surface

        # Empty lists that will hold calculation data
        ClearanceReq = []                       # List to hold obstacle clearance requirments values
        WindShear = []                          # List to hold wind shear values
        WindPowerDensity = []                   # List to hold wind power density values
        SuitableLoc= []                         # List to hold suitable location values

        ######################## Program Inputs ###############################

        # Reading in CSV file data
        # Read in code created by Samir Imamovic
        doc = input("Please input the path of your csv file: ")     # Display message to user to input CSV file
        fo = open(doc, 'r')                                         # Function to open the CSV file, assign imported CSV file to variable, read only access type (r)
        freader = csv.reader(fo)                                    # Function to read the CSV file assigned to fo
        next(freader)                                               # Next function to skip header row, move on to read next row in file
        for line in freader:                                        # For loop to read lines of CSV file and append values into lists  
            input_ID.append(float(line[0]))                         # Append values from line one (position two) into input_ID list as float 
            input_ProxObst.append(float(line[1]))                   # Append values from line two (position three) into input_ProxObst list as float
            input_HeightObst.append(float(line[2]))                 # Append values from line three (position four) into input_HeightObst list as a float
            input_DirectionObst.append(str(line[3]))                # Append values from line four (position five) into input_DirectionObst
            input_RoughnessLength.append(float(line[4]))            # Append values from line five (position six) into input_RoughnessLength list as a float
        
        # Contents of while loop where contributed to and edied by all group members
        while True:
            # Input if/else statements created by Dale Langford
            TurbineHeight= float(input("What is the height of the turbine in metres: "))              # Display message for user to input turbine height in meters

            if TurbineHeight <= 0:                                                                    # If statement to handle zero or negative values input for turbine height, turbine height must be greater then zero
                print("Turbine height must be greater than zero.")                                    # If turbine height is less then or equal to zero then display message to user that turbine height must be greater then zero
                print()                                                                               
            else:                                                                                     # If turbine height is greater then zero program will continue to else statement  
                BladeRadius= float(input("What is the blade radius of the turbine in metres: "))      # Display message for user to input blade radius of the turbine in metres

                if BladeRadius <= 0:                                                                  # If statement to handle zero or negative values for blade radius input by user, blade radius must be greater then zero
                    print("Blade radius must be greater than zero.")                                  # If blade radius is less then or equal to zero then display message to user that blade radius must be greater then zero
                    print()
                else:                                                                                 # If blade radius input is greater then zero program will continue to else statement 
                    print()
                    print("*****************************************************************************************************************")
                    print()

                    # WHY IS IDnum COMMENTED OUT?
                    # For loop to assinged indexed values of lists to variables, call functions and input variable into function
                    # Index and calls to function created by Samir Imamovic
                    for index in range(len(input_ID)):   	                    # len to get length of list, range function so index will be 0, 1, 2, ...
                        # Create variables to contain the values of index
                        ProxObst = input_ProxObst[index]                        # Retrieve ProxObst in index position from input_ProxObst list
                        HeightObst= input_HeightObst[index]                     # Retrieve HeightObst in index position from input_HeightObst list 
                        DirectionObst= input_DirectionObst[index]               # Retrieve DirectionObst in index position from input_DirectionObst list 
                        RoughnessLength = input_RoughnessLength[index]          # Retrieve RoughnessLength in index position from input_RoughnessLength list

                        # Call to CalcObstClearance function
                        # Input the variables assigned with user input data to the function (HeightObst, DirectionObst, ProxObst, BladeRadius, TurbineHeight)
                        ProcessClearanceReq = CalcObstClearance(HeightObst, DirectionObst, ProxObst, BladeRadius, TurbineHeight)
                        ClearanceReq.append(ProcessClearanceReq)                            # Append ProcessClearanceReq variable value into ClearanceReq list

                        ProcessWindShear = CalcWindShear(TurbineHeight, RoughnessLength)    # Call to CalcWindShear function, pass in the variables assigned with user input data to the function (TurbineHeight, RoughnessLength)
                        WindShear.append(ProcessWindShear)                                  # Append ProcessClearanceReq variable value calculated in the CalcWindShear function into ClearanceReq list

                        ProcessWindPowerDensity = CalcWindPower(BladeRadius)                # Call to CalcWindPower function, pass in the variables assigned with user input data to the function (BladeRadius)
                        WindPowerDensity.append(ProcessWindPowerDensity)                    # Append ProcessWindPowerDensity variable value calculated in the CalcWindPower function into WindPowerDensity list 
                    
                    # For loop to assigned indexed 
                    # Suitablity code created by Jessica Hobbins
                    for index in range(len(input_ID)):                          # len to get length of list, range function so index will be 0, 1, 2, ...
                        # Create variables to contain the values of index
                        ClearanceSuitable = ClearanceReq[index]                 # Assign clearance requirement values to ClearanceSuitable variable, retrieve ClearanceSuitable variable in index position from ClearanceReq list
                        ShearSuitable = WindShear[index]                        # Assign wind shear values to ShearSuitable variable, retrieve ShearSuitable variable in index position from WindShear list
                        
                        # If/else statement to determine suitability of turbine and site location, 
                        # Obstacle clearance (ClearanceSuitable) must equal "Yes", wind shear (ShearSuitable) must be greater then or equal to 15 km/hr and less then or equal to 70 km/hr to be considered suitable
                        if ClearanceSuitable == "Yes" and ShearSuitable >= 15 and ShearSuitable <= 70:      
                            SuitableLocation= "Suitable"                        # If obstacle clearance and wind shear values fall within the if statement conditions then SiteLocation variable will be assigned a value of "Suitable"
                            SuitableLoc.append(SuitableLocation)                # SuitableLocation variable value will be appended into SuitableLoc list
                        else:
                            SuitableLocation= "Not Suitable"                    # Else if site does not meet the conditions then SuitableLocation variable will be assigned a value of "Not Suitable"
                            SuitableLoc.append(SuitableLocation)                # SuitableLocation variable value will be appended into SuitableLoc list

                    ############################ Program Outputs ############################

                    # Create, open and write results of program into output file
                    # Output table created by Chelsea Penlington
                    DocName = "Height" + str(TurbineHeight) + "Radius" + str(BladeRadius) + ".csv"          # Set name of output document, name shows user what turbine height and blade radius values in which the document pertains
                    file = open(DocName, 'w')                                                               # Open output CSV file using overwrite file access
                    
                    # Write data to new CSV file   
                    # Write table headers to file, formatted with spacing between columns                                                       
                    file.write('{}{:>25}{:>30}{:>30}{:>30}{:>30}{:>30}{:>30}{:>30}\n'.format('Site ID', 'Obstacle Proximity (m)', 'Height of Obstacle (m)', 'Direction of Obstacle', 'Roughness Length', 'Obstacle Clearance Met', 'Wind Shear', 'Wind Power', 'Suitable Location''\n'))
                    
                    # For loop to write all indexed values into output CSV file
                    # Write indexed values for each list created into output CSV file row by row, formatted with spacing in between columns
                    # Index used to specidy position of values in list
                    for index in range(len(input_ID)):
                        file.write('{:>5}{:>22}{:>25}{:>25}{:>35}{:>28}{:>40}{:>30}{:>30}\n'.format((str(input_ID[index])), str(input_ProxObst[index]), str(input_HeightObst[index]), str(input_DirectionObst[index]), str(input_RoughnessLength[index]), str(ClearanceReq[index]), str(WindShear[index]), str(WindPowerDensity[index]), str(SuitableLoc[index])))
                    # Function to close output file
                    file.close()    
                
                    end = input("Do you want to try again with different turbine height and blade radius values (Y/N)? ") # Display message to user asking if they would like to continue with the program and input more turbine height and blade radius values
                    print()
                    if  end.upper() == 'N' :                                                                              # If user inputs Y go back to beginning of while loop, if N then break out of loop, change end variable input value to upper case
                        break                                                                                             # Break out of if statement, continue with rest of program
            
        print()
        print("Done")               # Display "Done" message to the user once program is complete

    if __name__ == "__main__":      # Only execute when main function called in this module, not if this file is imported
        main()                      # Call main program function


# Exception handlers for main program  
# Exception handlers code created by Dale Langford     
except ValueError:                                                                                              # Exception handler for when an unexpected value occurs
    print("An error has occured with a number entered. Please review CSV and Turbine values and try again.")    # If error occurs display message to user that a value error has occured and to review their inputs
except ArithmeticError:                                                                                         # Exception handler for calculation erros
    print("An error has occured during calculations. Please review CSV values and try again.")                  # If error occurs display message to user that a calculation error has occured and to review their inputs
except SyntaxError:                                                                                             # Exception handler for typos
    print("A syntax error has occured. Please review and try again.")                                           # If error occurs display message to user that there is a typo and to review their inputs
except NameError:                                                                                               # Exception handler for variable or function name errors
    print("A variable you are using does not exist. Please review and try again.")                               # If error occurs display message to user to review variables used
except Exception as message:                                                                                    # General exception handler, not specific to one type of error
    print("Something unexpected has happened. Please review CSV values and try again.")                          # If another error occurs that was not listed above occurs display message to user to review all inputs 
