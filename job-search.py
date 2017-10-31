import requests
from bs4 import BeautifulSoup

url = "http://jobs.jobvite.com/forgerock/job"
fr = requests.get(url)
 BeautifulSoup([your markup], "lxml")
soup = BeautifulSoup(fr.text)
