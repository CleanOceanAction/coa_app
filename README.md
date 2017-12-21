Web Analytics Dashboard For Clean Ocean Action
======

## Introduction

- Clean Ocean Action: [http://www.cleanoceanaction.org](http://www.cleanoceanaction.org)
- Bloomberg Philanthropy: [http://www.cleanoceanaction.org](http://www.bloomberg.org)

Bloomberg partnered with Clean Ocean Action (COA), an organization Bloomberg already had an extensive relationship with, to solve its data challenge. We performed these tasks in order to streamline its data collection process for Beach Sweeps.

1. Schema Architecture
2. Historical Data Clenup
3. Web Application
4. Data Analysis

As a result, this project was selected to present during these conferences below.

- [Strata + Hadoop World - Conferences](http://conferences.oreilly.com/strata/big-data-conference-ny-2015)
- [Data for Good Exchange - Bloomberg L.P.](http://www.bloomberg.com/company/d4gx/)
- [Debris Free Sea Conference - Clean Ocean Action](http://www.cleanoceanaction.org/index.php?id=830)

## Tasks

### 1. Schema Architecture
The first task of introducing the new data governance system was to thoroughly review the current data retrieval process in order to fully understand the data flow from beginning to end, as data could be deteriorated at any point of the process. To begin, we interviewed the COA and American Littoral Society staff as well as internal Bloomberg employees who participated in the COA beach clean-ups to identify the steps volunteers take to report the collected trash items from beaches and the procedures the COA staff follow to compile the data. Based on the observations and analysis of the 1993-2014 datasets, database schemas were developed in MySQL, for both its reputation and significant presence in the data science community.

### 2. Historical Data Clenup
After designing the schemas, data munging was required. Due to the data volume and inconsistency, this process demanded a significant amount of time. Each year contained two Excel files with multiple sheets of detailed data collected by COA. Furthermore, there was little format consistency between files and the classified categories had changed overtime. Thus, there was no way to programmatically process these files and manual examination of each category and file was needed. Utilizing volunteer time at Bloomberg, the most recent years of the data were standardized and successfully transferred to the database. The remaining files will undergo a similar process during an upcoming “Bloomberg Datathon” event. After the schema design and significant data munging, a new data entry framework was needed for volunteers and COA to update collected items into the database. To solve this, we created a custom web application based solely on open source solutions so that COA could invest the resources for its core operations. For readability and future maintenance purposes, Python was our language choice and we utilized a micro web framework, Flask, as the backend. The front end was built on top of a popular open source solution, Bootstrap, so the site could be optimized for desktop computers and smartphones. This application will not only solve data entry and integrity problems but will function as a real time data analytics dashboard as well. As of September 2015, the application was successfully deployed from an internal Bloomberg web server to Amazon Web Services, more precisely, Amazon Relational Database Service and Elastic Beanstalk. 

### 3. Web Application
After the schema design and significant data munging, a new data entry framework was needed for volunteers and COA to update collected items into the database. To solve this, we created a custom web application based solely on open source solutions so that COA could invest the resources for its core operations. For readability and future maintenance purposes, Python was our language choice and we utilized a micro web framework, Flask, as the backend. The front end was built on top of a popular open source solution, Bootstrap, so the site could be optimized for desktop computers and smartphones. This application will not only solve data entry and integrity problems but will function as a real time data analytics dashboard as well. As of September 2015, the application was successfully deployed from an internal Bloomberg web server to Amazon Web Services, more precisely, Amazon Relational Database Service and Elastic Beanstalk.

### 4. Data Analysis Methods
Using the semi-annual (Fall and Spring) trash data provided by COA, we analyzed the volume of trash collected against: macro indicators including GDP, unemployment rate, and New Jersey population; related industry indicators including aggregated inventory, sales, and revenue data; and finally, related company information such as Pepsi and Coca-Cola revenue and sales data from the US market. We performed Granger causality test on the data series containing strong correlation, setting our constraints to t<0.05 as statistically significant and r2 to 0.8.

## Conclusion
The development and implementation of the web application, as mentioned above, will serve four purposes. The first will allow our Bloomberg team to standardize the remaining historical years of data. Second, the application will allow volunteers and COA to standardize the data they are collecting and directly load this data into the database. As a result, future data will no longer need to undergo the time intensive process that was necessary for the historical data we received. Third, we see the application serving as a tool to increase volunteer engagement. Analytics on the web application are updated real time and allow an individual or team leader to visualize the impact they are making. Lastly, the analytics made available to the organization via the web application will allow COA to plan more efficiently from an operations standpoint. We see this application being used to properly allocate resources at the various beach sites and also to allow the organization to reflect on prior Beach Sweeps and strategies that may or may not have worked.


## Getting Started
1. To run this app, make sure you have python 2 and pip installed. Note that you may need to update your PATH environment variable to include the python and pip paths. This can be downloaded here: https://www.python.org/downloads/

2. Once this repository is cloned, cd into the directory and install dependencies:
`pip -r requirements.txt`

3. Then, run application locally:
`python application.py`

4. The application can be viewed at: http://localhost:8080/impact/
