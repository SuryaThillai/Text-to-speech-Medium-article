from bs4 import BeautifulSoup
import requests
import pyttsx3

url = input("Copy and paste a url link of any medium article: ")

# Package to convert text to speech
engine = pyttsx3.init()

#  Getting the Html Structure of that particular page
response = requests.get(url=url)
content = response.text

#  Passing it into the beautiful Soup and finding the required tags.
soup = BeautifulSoup(content,"html.parser")

Ps = soup.find_all(name="p", class_="pw-post-body-paragraph ip iq hh ir b is it iu iv iw ix iy iz ja jb jc jd je jf jg jh ji jj jk jl jm ha bi")

data = []

#  Adding the text to list and converting into str
for p in Ps:
    data.append(p.text)
    read = ' '.join(data)
print(read)

# Make the module to read the text, until the text completes.
engine.say(read)
engine.runAndWait()


# ---------------------------------------------------------- Project Completed ----------------------------------------------------- #






