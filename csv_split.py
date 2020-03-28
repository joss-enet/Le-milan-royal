import pandas as pd
import os
from datetime import datetime, date

data = pd.read_csv("ks-projects-201801.csv")

#Remove the messed up lines
print("Data cleaning... ", end='')
toRemove = data[(data.country == "N,0\"")].index
data.drop(toRemove, inplace=True)


#Fix launched date format
for row in data.itertuples():
        dateValue = datetime.fromisoformat(row.launched)
        data.at[row.Index, 'launched'] = str(date(dateValue.year, dateValue.month, dateValue.day))

print("Done.")

#Create target directory
dirName = "sql_scripts"
if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("Directory " , dirName ,  " created.")
else:    
    print("Directory " , dirName ,  " already exists.")


#Create Category table
print("Creating Category table generation script... ", end='')
categoryFile = open("sql_scripts/categoryTable.sql", "w")
categoryFile.write("CREATE TABLE Category(idCategory INT, nameCategory VARCHAR(50), PRIMARY KEY (idCategory));\n")

id = 1
categoriesMap = {}
categories = data.category.unique()
for category in categories:
        categoryFile.write("REPLACE INTO Category VALUES (" + str(id) + ", \"" + category + "\");\n")
        categoriesMap[category] = id
        id = id+1

categoryFile.close()
print("Done.")


#Create MainCategory table
print("Creating MainCategory table generation script... ", end='')
mainCategoryFile = open("sql_scripts/mainCategoryTable.sql", "w")
mainCategoryFile.write("CREATE TABLE MainCategory(idMainCategory INT, nameMainCategory VARCHAR(50), PRIMARY KEY (idMainCategory));\n")

id = 1
mainCategoriesMap = {}
mainCategories = data.main_category.unique()
for mainCategory in mainCategories:
        mainCategoryFile.write("REPLACE INTO MainCategory VALUES (" + str(id) + ", \"" + mainCategory + "\");\n")
        mainCategoriesMap[mainCategory] = id
        id = id+1

mainCategoryFile.close()
print("Done.")


#Create Currency table
print("Creating Currency table generation script... ", end='')
currencyFile = open("sql_scripts/currencyTable.sql", "w")
currencyFile.write("CREATE TABLE Currency(idCurrency INTEGER, code VARCHAR(3), nameCurrency VARCHAR(25), changeRate FLOAT, PRIMARY KEY (idCurrency));\n")

id = 1
currenciesMap = {}
currencyInfoMap = {
        "GBP" : {"name" : "Great British Pound", "changeRate" : 1.23},
        "USD" : {"name" : "US Dollar", "changeRate" : 1.00},
        "CAD" : {"name" : "Canadian Dollar", "changeRate" : 0.72},
        "AUD" : {"name" : "Australian Dollar", "changeRate" : 0.61},
        "NOK" : {"name" : "Norwegian Krone", "changeRate" : 0.10},
        "EUR" : {"name" : "Euro", "changeRate" : 1.11},
        "MXN" : {"name" : "Mexican Peso", "changeRate" : 0.04},
        "SEK" : {"name" : "Swedish Krona", "changeRate" : 0.10},
        "NZD" : {"name" : "New Zealand Dollar", "changeRate" : 0.61},
        "CHF" : {"name" : "Swiss Franc", "changeRate" : 1.06},
        "DKK" : {"name" : "Danish Krone", "changeRate" : 0.15},
        "HKD" : {"name" : "Hong Kong Dollar", "changeRate" : 0.13},
        "SGD" : {"name" : "Singapore Dollar", "changeRate" : 0.70},
        "JPY" : {"name" : "Japanese Yen", "changeRate" : 0.0095}
        }
currencies = data.currency.unique()
for currency in currencies:
        currencyFile.write("REPLACE INTO Currency VALUES (" + str(id) + ", \"" + currency + "\", \"" + currencyInfoMap[currency]["name"] + "\", " + str(currencyInfoMap[currency]["changeRate"]) + ");\n")
        currenciesMap[currency] = id
        id = id+1

currencyFile.close()
print("Done.")


#Create Country table
print("Creating Country table generation script... ", end='')
countryFile = open("sql_scripts/countryTable.sql", "w")
countryFile.write("CREATE TABLE Country(idCountry INT, code VARCHAR(2), nameCountry VARCHAR(25), population INT, PRIMARY KEY (idCountry));\n")

id = 1
countriesMap = {}
countryNameData = pd.read_csv("country_name.csv")
countryPopulationData = pd.read_csv("country_population.csv")
countries = data.country.unique()
for country in countries:
        countryName = countryNameData[countryNameData.Alpha2 == country].iloc[0]["Country"]
        countryAlpha3 = countryNameData[countryNameData.Alpha2 == country].iloc[0]["Alpha3"]
        population = int(countryPopulationData[countryPopulationData["Country Code"] == countryAlpha3].iloc[0]["2018"])
        countryFile.write("REPLACE INTO Country VALUES (" + str(id) + ", \"" + country + "\", \"" + countryName + "\", " + str(population) + ");\n")
        countriesMap[country] = id
        id = id+1

countryFile.close()
print("Done.")


#Create DateTime table
print("Creating DateTime table generation script... ", end='')
dateTimeFile = open("sql_scripts/dateTimeTable.sql", "w")
dateTimeFile.write("CREATE TABLE DateTime(idDateTime INT, year INT, month INT, day INT, PRIMARY KEY (idDateTime));\n")

id = 1
dateTimesMap = {}
dateTimes = data.launched.append(data.deadline).unique()
for dateTime in dateTimes:
        current = datetime.fromisoformat(dateTime)
        dateTimeFile.write("REPLACE INTO DateTime VALUES (" + str(id) + ", " + str(current.year) + ", " + str(current.month) + ", " + str(current.day) + ");\n")
        dateTimesMap[dateTime] = id
        id = id+1

dateTimeFile.close()
print("Done.")


#Create Facts table
print("Creating Facts table generation script... ", end='')
factsFile = open("sql_scripts/factsTable.sql", "w")
factsFile.write("CREATE TABLE Facts(idProject INT, nameProject VARCHAR(200), state ENUM('failed', 'successful', 'canceled', 'live', 'undefined', 'suspended'), backers INT, pledged FLOAT, goal FLOAT, usd_pledged FLOAT, usd_goal FLOAT, financingRate FLOAT, duration INT, averageDonation FLOAT, " +
        "idCountry INT, CONSTRAINT fk_idCountry FOREIGN KEY (idCountry) REFERENCES Country(idCountry) ON DELETE CASCADE ON UPDATE CASCADE, " +
        "idCurrency INT, CONSTRAINT fk_idCurrency FOREIGN KEY (idCurrency) REFERENCES Currency(idCurrency) ON DELETE CASCADE ON UPDATE CASCADE, " +
        "idCategory INT, CONSTRAINT fk_idCategory FOREIGN KEY (idCategory) REFERENCES Category(idCategory) ON DELETE CASCADE ON UPDATE CASCADE, " +
        "idMainCategory INT,  CONSTRAINT fk_idMainCategory FOREIGN KEY (idMainCategory) REFERENCES MainCategory(idMainCategory) ON DELETE CASCADE ON UPDATE CASCADE, " +
        "idDateTimeLaunch INT, CONSTRAINT fk_idDateTimeLaunch FOREIGN KEY (idDateTimeLaunch) REFERENCES DateTime(idDateTime) ON DELETE CASCADE ON UPDATE CASCADE, " +
        "idDateTimeDeadline INT, CONSTRAINT fk_idDateTimeDeadline FOREIGN KEY (idDateTimeDeadline) REFERENCES DateTime(idDateTime) ON DELETE CASCADE ON UPDATE CASCADE, " +
        "PRIMARY KEY (idProject));\n")

for fact in data.itertuples():
        financingRate = (fact.pledged/fact.goal)
        duration = date.fromisoformat(fact.deadline) - date.fromisoformat(fact.launched)
        if (fact.backers == 0):
                avgDonation = 0
        else:
                avgDonation = (fact.usd_pledged_real/fact.backers)
        idCountry = countriesMap[fact.country]
        idCurrency = currenciesMap[fact.currency]
        idCategory = categoriesMap[fact.category]
        idMainCategory = mainCategoriesMap[fact.main_category]
        idDateTimeLaunch = dateTimesMap[fact.launched]
        idDateTimeDeadline = dateTimesMap[fact.deadline]
        factsFile.write("REPLACE INTO Facts VALUES (" + str(fact.ID) + ", \"" + str(fact.name).replace("\"","\'") + "\", \"" + str(fact.state) + "\", " + str(fact.backers) + ", " + str(fact.pledged) + ", " + str(financingRate) + ", " + str(duration.days) +  ", " + str(avgDonation) +
        ", " + str(fact.goal) + ", " + str(fact.usd_pledged_real) + ", " + str(fact.usd_goal_real) + ", " + str(idCountry) + ", " + str(idCurrency) + ", " + str(idCategory) + 
        ", " + str(idMainCategory) + ", " + str(idDateTimeLaunch) + ", " + str(idDateTimeDeadline) + ");\n")

factsFile.close()
print("Done.")


#Create database generation script
print("Creating database generation script... ", end='')
absPath = os.path.dirname(os.path.abspath(__file__))
dbFile = open("sql_scripts/dbScript.sql", "w")
dbFile.write("source " + absPath + "/sql_scripts/categoryTable.sql;\n")
dbFile.write("source " + absPath + "/sql_scripts/mainCategoryTable.sql;\n")
dbFile.write("source " + absPath + "/sql_scripts/countryTable.sql;\n")
dbFile.write("source " + absPath + "/sql_scripts/currencyTable.sql;\n")
dbFile.write("source " + absPath + "/sql_scripts/dateTimeTable.sql;\n")
dbFile.write("source " + absPath + "/sql_scripts/factsTable.sql;")
dbFile.close()
print("Done.")