# Artemio Guerrero,
# complete,
# Ocean Levels
# Assuming the ocean’s level is currently rising at about 1.8 millimeters per year, 
# create an application that displays the number of millimeters that the ocean will have risen each year for the next 25
# years
# Year Rise (in millimeters)
# ------------------------------------------

# the ocean’s level is currently rising at about 1.8 millimeters per year
rise = 1.8

# our ocean level will start at zero becouse it will be a total acumlator
ocean_level = 0

year_start = 1
year_end = 26

print('Year             Rise (in millimeters)')
print('--------------------------------------')
for year in range(year_start,year_end):
    # here we use the accumulate to add the results of the loop
    ocean_level += rise

    # displays the number of millimeters that the ocean will have risen each year for the next 25
# years
    print(year,"\t","\t","%.2f"%ocean_level)

