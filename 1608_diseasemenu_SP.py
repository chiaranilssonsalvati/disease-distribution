import csv 
import wikipedia as w
b = open('CountryTotal2012.csv', 'rU')
data = list(csv.reader(b))

def shouldquit(user_letter):
	if(user_letter.lower() == 'quit'):
		choice = 'quit'
		disease_info_goodbye()

column_headers = data[0]
number_index = column_headers.index('AllCauses')
country_index = column_headers.index('Country')

countries = []
for row in data[1:]:
	countries.append(row[country_index])


def disease_info(disease):
	info=(raw_input('This many total people (Age-standardized mortality rate by cause is per 100,000 population) die from all causes in the year 2012:  '+data[int(disease)][number_index]+' . Type "m" to go back to country selection.')).lower()
	while info != 'quit':
		if info == 'm':
			menu()
		else:
			info=(raw_input('You did not type a valid character. Type "quit" to exit the program. '))
		
		shouldquit(info)
		return "QUIT" 

def information():
	country=raw_input('Type in the disease or country that you want to access more information on. Or, type "quit" to quit. ')
	if country.lower()!="quit":
		print(w.summary(country, sentences=5))
	else:
  		shouldquit(country)
			
def menu():
	print ('There are many causes of death around the world. Use this program to more learn about them.')
	choice = raw_input ('Type in the country you want to access more information on, type "w" for more information, or "QUIT" to quit. ')
	while choice.lower() != 'quit':
		if choice == 'w':
  			information()
	  	else:
	  		choice = disease_info(countries.index(choice)+1)
		shouldquit(choice)
  		

def disease_info_goodbye():
	print('Thank you for using the program. Goodbye!')
	quit()

menu()