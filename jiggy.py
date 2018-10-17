import random
import string
import names
import csv

myfile = open("output.csv", "w", newline='')

def generatedot(email): 
	if len(email) <= 1:
		yield email 
	else:
		head, tail = email[0], email[1:] 
		for item in generatedot(tail): 
			yield head + item 
			yield head + '.' + item
			
email = str(input("Enter a gmail or catchall email: ")).lower()
while "@" not in email:
	email = str(input("Please enter a valid gmail or catchall email: ")).lower()
	
useraddy = str(input("Enter your address 1: "))
while useraddy == "":
	useraddy = str(input("Please enter your address 1: "))
	
city = input("Enter your city: ")
while city == "":
	city = input("Please enter your city: ")

state = input("Enter your state abbreviation (ex. NY): ").upper()
while state == "" or len(state) != 2:
	state = input("Please enter a valid state abbreviation (ex. NY): ").upper()

zipcode = str(input("Enter your zip code: "))
while zipcode == "":
	zipcode = str(input("Please enter your zip code: "))

country = input("Enter your country abbreviation (ex. US): ").upper()
while country == "" or len(country) != 2:
	country = input("Please enter your correct country abbreviation (ex. US): ").upper()
	
userarea = str(input("Enter your area code: "))
while userarea == "":
	userarea = str(input("Please enter your area code: "))
	
amount = str(input("Enter how many tasks you want generated: "))
while amount == "0" or amount == "":
	amount = str(input("Please enter more than 0: "))
amount = int(amount)

gmail = False
catchall = ""

if "gmail" in email:
	gmail = True
	email2 = email.split('@')[0]
	emaillist = list(generatedot(email2))
else:
	catchall = "@" + email.split('@')[1]

output_writer = csv.writer(myfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

defaultlist = ['First Name', 'Last Name', 'Address 1', 'Address 2', 'City', 'State', 'Zipcode', 'Country', 'Phone', 'Full Name', 'Email', 'Credit Card Number', 'Expiry Month', 'Expiry Year', 'CVV']
output_writer.writerow(defaultlist)

    
while amount > 0:
  firstname = names.get_first_name()
  lastname = names.get_last_name()
  addy1 = random.choice(string.ascii_letters[0:4]).upper() + random.choice(string.ascii_letters[0:26]).upper() + random.choice(string.ascii_letters[0:26]).upper() + random.choice(string.ascii_letters[0:26]).upper() + " " + useraddy
  addy2 = "Apt " + str(random.randint(100, 999))
  phone = userarea + str(random.randint(1000000, 9999999))
  
  if gmail:
	  if len(emaillist) > 0:
		  jigged = random.choice(emaillist)
		  jigemail = jigged + "@gmail.com"
		  emaillist.remove(jigged)
	  else:
		  jigemail = email
  else:
	  jigemail = firstname + lastname + str(random.randint(10000, 999999)) + catchall
  
  newlist = []
  newlist.append(firstname)
  newlist.append(lastname)  
  newlist.append(addy1)  
  newlist.append(addy2)  
  newlist.append(city)  
  newlist.append(state)  
  newlist.append(zipcode)  
  newlist.append(country)  
  newlist.append(phone)    
  newlist.append(firstname + " " + lastname)
  newlist.append(jigemail)
  
  output_writer.writerow(newlist)
    
  amount -= 1
    
myfile.close()
