import pandas as pd
import os
from datetime import datetime, date

data = pd.read_csv("ks-projects-201801.csv")


#Remove the messed up lines
toRemove = data[(data.country == "N,0\"")].index
data.drop(toRemove, inplace=True)


#Create target directory
dirName = "sql_scripts"
if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ")
else:    
    print("Directory " , dirName ,  " already exists")


#Create Category table
categoryFile = open("sql_scripts/categoryTable.sql", "w")
categoryFile.write("CREATE TABLE Category(idCategory INT, name VARCHAR(50), PRIMARY KEY (idCategory));\n")

id = 1
categoriesMap = {}
categories = data.category.unique()
for category in categories:
        categoryFile.write("INSERT OR REPLACE INTO Category VALUES (" + str(id) + ", \"" + category + "\");\n")
        categoriesMap[category] = id
        id = id+1

categoryFile.close()


#Create MainCategory table
mainCategoryFile = open("sql_scripts/mainCategoryTable.sql", "w")
mainCategoryFile.write("CREATE TABLE MainCategory(idMainCategory INT, name VARCHAR(50), PRIMARY KEY (idMainCategory));\n")

id = 1
mainCategoriesMap = {}
mainCategories = data.main_category.unique()
for mainCategory in mainCategories:
        mainCategoryFile.write("INSERT OR REPLACE INTO MainCategory VALUES (" + str(id) + ", \"" + mainCategory + "\");\n")
        mainCategoriesMap[mainCategory] = id
        id = id+1

mainCategoryFile.close()


#Create Currency table
currencyFile = open("sql_scripts/currencyTable.sql", "w")
currencyFile.write("CREATE TABLE Currency(idCurrency INTEGER, code VARCHAR(3), name VARCHAR(25), changeRate FLOAT, PRIMARY KEY (idCurrency));\n")

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
        currencyFile.write("INSERT OR REPLACE INTO Currency VALUES (" + str(id) + ", \"" + currency + "\", \"" + currencyInfoMap[currency]["name"] + "\", " + str(currencyInfoMap[currency]["changeRate"]) + ");\n")
        currenciesMap[currency] = id
        id = id+1

currencyFile.close()


#Create Country table
countryFile = open("sql_scripts/countryTable.sql", "w")
countryFile.write("CREATE TABLE Country(idCountry INT, code VARCHAR(2), name VARCHAR(25), PRIMARY KEY (idCountry));\n")

id = 1
countriesMap = {}
countryNameData = pd.read_csv("country_name.csv")
countries = data.country.unique()
for country in countries:
        countryName = countryNameData[countryNameData.Code == country].iloc[0]["Name"]
        countryFile.write("INSERT OR REPLACE INTO Country VALUES (" + str(id) + ", \"" + country + "\", \"" + countryName + "\");\n")
        countriesMap[country] = id
        id = id+1

countryFile.close()


#Create DateTime table
dateTimeFile = open("sql_scripts/dateTimeTable.sql", "w")
dateTimeFile.write("CREATE TABLE DateTime(idDateTime INT, year INT, month INT, day INT, hour INT, minute INT, second INT, PRIMARY KEY (idDateTime));\n")

id = 1
dateTimesMap = {}
countryNameData = pd.read_csv("country_name.csv")
dateTimesLaunch = data.launched.unique()
dateTimesDeadline = data.deadline.unique()
for dateTime in dateTimesLaunch:
        current = datetime.fromisoformat(dateTime)
        dateTimeFile.write("INSERT OR REPLACE INTO DateTime VALUES (" + str(id) + ", " + str(current.year) + ", " + str(current.month) + ", " + str(current.day) + ", " + str(current.hour) + 
        ", " + str(current.minute) + ", " + str(current.second) + ");\n")
        dateTimesMap[dateTime] = id
        id = id+1

for dateTime in dateTimesDeadline:
        current = date.fromisoformat(dateTime)
        dateTimeFile.write("INSERT OR REPLACE INTO DateTime VALUES (" + str(id) + ", " + str(current.year) + ", " + str(current.month) + ", " + str(current.day) + ", " + str(0) + 
        ", " + str(0) + ", " + str(0) + ");\n")
        dateTimesMap[dateTime] = id
        id = id+1

dateTimeFile.close()


#Create Facts table
factsFile = open("sql_scripts/factsTable.sql", "w")
factsFile.write("CREATE TABLE Facts(idProject INT, nameProject VARCHAR(200), state ENUM('failed', 'successful', 'canceled', 'live', 'undefined', 'suspended'), backers INT, pledged FLOAT, goal FLOAT, usd_pledged FLOAT, usd_goal FLOAT, " +
        "idCountry INT, CONSTRAINT fk_idCountry FOREIGN KEY (idCountry) REFERENCES Country(idCountry) ON DELETE CASCADE ON UPDATE CASCADE, " +
        "idCurrency INT, CONSTRAINT fk_idCurrency FOREIGN KEY (idCurrency) REFERENCES Currency(idCurrency) ON DELETE CASCADE ON UPDATE CASCADE, " +
        "idCategory INT, CONSTRAINT fk_idCategory FOREIGN KEY (idCategory) REFERENCES Category(idCategory) ON DELETE CASCADE ON UPDATE CASCADE, " +
        "idMainCategory INT,  CONSTRAINT fk_idMainCategory FOREIGN KEY (idMainCategory) REFERENCES MainCategory(idMainCategory) ON DELETE CASCADE ON UPDATE CASCADE, " +
        "idDateTimeLaunch INT, CONSTRAINT fk_idDateTimeLaunch FOREIGN KEY (idDateTimeLaunch) REFERENCES DateTime(idDateTime) ON DELETE CASCADE ON UPDATE CASCADE, " +
        "idDateTimeDeadline INT, CONSTRAINT fk_idDateTimeDeadline FOREIGN KEY (idDateTimeDeadline) REFERENCES DateTime(idDateTime) ON DELETE CASCADE ON UPDATE CASCADE, " +
        "PRIMARY KEY (idProject));\n")

for fact in data.head(10).itertuples():
        idCountry = countriesMap[fact.country]
        idCurrency = currenciesMap[fact.currency]
        idCategory = categoriesMap[fact.category]
        idMainCategory = mainCategoriesMap[fact.main_category]
        idDateTimeLaunch = dateTimesMap[fact.launched]
        idDateTimeDeadline = dateTimesMap[fact.deadline]
        factsFile.write("INSERT OR REPLACE INTO Facts VALUES (" + str(fact.ID) + ", \"" + fact.name + "\", \"" + fact.state + "\", " + str(fact.backers) + ", " + str(fact.pledged) + 
        ", " + str(fact.goal) + ", " + str(fact.usd_pledged_real) + ", " + str(fact.usd_goal_real) + ", " + str(idCountry) + ", " + str(idCurrency) + ", " + str(idCategory) + 
        ", " + str(idMainCategory) + ", " + str(idDateTimeLaunch) + ", " + str(idDateTimeDeadline) + ");\n")

factsFile.close()