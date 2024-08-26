In this project I used Selenium to extract data about real estate in Nahariya & Beer Sheva for my seminar in management at Tel Aviv University.

I created this code because the Real estate database of the Israeli Tax Authority shows up to 50 results per search.
I needed to search for data between 2005-2008, which would lead to thousands of manual searching and downloading of csv files.

As Result, I found a website called "AD" that holds the real estate information in an html table that the Tax Authority publishes, but does not limit up to 50 results per search.
I took the HTML table and used selenium in order to extract all of the data I needed about each property (each row was a property), while expanding each row for additional information about each property and adding it to a pd dataframe.
At the end of each HTML table i exported the pd dataframe to csv and saved it on my pc. After that, the code automatically moves on to the next page and starts the whole extracting data into pd dataframe agan.
