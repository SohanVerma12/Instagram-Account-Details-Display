#So first o fall we install some package's

#importing libraries
from bs4 import BeautifulSoup
import requests

#instagram url
URL = "https://www.instagram.com/leomessi/"

#parse function
def parse_data(s):
    # creating a dictionary
    data = {}

    # splittting the conten
    # then taking the first part
    s = s.split("-")[0]

    # again splittting the content
    s = s.split(" ")

    #assigning the values
    data['Followers'] = s[0]
    data['Following'] = s[2]
    data['Posts'] = s[4]

    #returning the dictionary
    return  data

#scrape function
def scrape_data(username):
    #getting the requests from url
    r = requests.get(URL.format(username))

    #converting the text
    s = BeautifulSoup(r.text, "html.parser")
    
    #finding meta info
    meta = s.find("meta", property="og:description")#only og:description

    #calling parser method
    return parse_data(meta.attrs['content'])

#main_function
if __name__ == "__main__":
    #username
    username = "v_hamp_code"

    #calling scrape function
    data = scrape_data(username)

    #printing the info
    print(data)









