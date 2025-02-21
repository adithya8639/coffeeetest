Yahoo finance website automation with selenium python

overview:
This scripts automates beloww listed tasks of yahoo finance website by using webdriver
1. open yahoo finance website
2. verify title
3. search for TSLA stock in search bar
4. verify auto suggestion
5. click on first search result
6. check if TSLA stock price is greater than 200
7. prints previous close and volume of the TSLA stock

pre requisites:
python, browser(chrome), chromedriver, packages(selenium, time...)

installation:
1.install selenium - pip install selenium

usage:
save the script with appropriate name
run the script using sh

Exp output:
verifies the title
searches for TSLA and verifies the suggestion
if stock price is > 200, it will proceed and retrive it
