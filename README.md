# Sales Enquiry App

Sales Enquiry is a multiplatform kivy app designed to work in Smartphone, Tablet, computer. People with marketing would make use of this application effectively to generate sales enquiries, store them quick and effectively. The application contains text fields that are required generally in enquiry generation. User has to open the app and enter the details. On clicking 'submit' the enquiry data would be stored in database. 

![appscreenshot](https://i.imgur.com/FgGWjMp.png)

## Prerequisite

There are few pre-requisites for the app to work properly. 

1. Mysql database with following table description

![db desc](https://i.imgur.com/t2UUMG0.png)

### Create mysql table 

```
CREATE TABLE IF NOT EXISTS enquiry(
        _id INT AUTO_INCREMENT PRIMARY KEY, 
        agentName VARCHAR(40),
        customerName VARCHAR(40),
        companyName VARCHAR(50),
        address VARCHAR(250),
        contactNumber VARCHAR(15),
        emailId VARCHAR(50),
        requirement VARCHAR(500)
        );
```

2. pymysql module to be installed 

```
pip3 install pymysql
``` 

## App design

`main.py` is the actual python file with app design layouts. `dbconnection.py` file has the database connectivity functions. 

If you don't have the database configured properly the enquiry data would be stored in a text file like the below. All the enquiries would append to the text file. 

Error we get when database is not configured properly
![Error DB](https://i.imgur.com/Cyx8GMd.png)

Append the data to text file like below

![Text file](https://i.imgur.com/OyPuiQq.png)

If the database connectivity is configured and working properly the enquiry details would be saved in the database like the below screenshot.

![Database](https://i.imgur.com/6AEDtYx.png)


**Note: ** In our `dbconnection.py` the password was stored as a plain text. This is not recommended thing to do in production. It's worth to look at the repo [vaultpass](https://github.com/sundararajan93/vaultpass) to add password vault mechanism to your code.