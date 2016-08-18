import csv 
import wikipedia as w
import communicable_choropleth as comm
import country_choropleth as count 
import region_bar as reg 
import injuries_choropleth as inj 
import line_graph as lg 
import noncommunicable_choropleth  as nc 

def shouldquit(user_letter):
	if(user_letter.lower() == 'quit'):
		choice = 'quit'
		goodbye()

def information():
	country=raw_input('Type in the disease or country that you want to access more information on. Or, type "quit" to quit. ')
	if country.lower()!="quit":
		print(w.summary(country, sentences=5))
	else:
  		shouldquit(country)

def country():
	b = open('CountryTotal2012.csv', 'rU')
	data = list(csv.reader(b))
	column_headers = data[0]
	number_index = column_headers.index('AllCauses')
	country_index = column_headers.index('Country')

	countries = []
	for row in data[1:]:
		countries.append(row[country_index])
	country = raw_input ('Type in the country you want to access more information on or "QUIT" to quit. ').lower().capitalize()
	if country == 'Quit':
	  	goodbye()
	else:
		info=(raw_input('This many people (per 100,000 population) died from all causes in the country '+country+' in the year 2012:  '+data[int(countries.index(country)+1)][number_index]+'. Type "m" to go back to country selection or type "quit" to quit. ')).lower()
		if info == 'quit':
			goodbye()
		elif info == 'm':
			choices()
		else:
			error()
		
	shouldquit(info)
	return "QUIT" 
	b.close()

def welcome():
	print ('There are many causes of death around the world. Use this program to more learn about them.')
	choices()

def choices():
	print('''You have several options:
		1. View a map that depicts the death rates in different countries across the world in 2012.
		2. View a graph that compares causes of death by age group.
		3. Choose a specific country to access information about its death rates.
		4. Learn more information about specific diseases or countries.
		
		Type 'QUIT' to quit.


		''')
	menu()
		
def menu():
	choice = raw_input("Choose 1, 2, 3, or 4, or type 'QUIT' to quit. ")
	# 
	if choice.lower() != 'quit':
		if choice == '1':
			choro_menu()
  		elif choice == '2':
  			bar_menu()
  		elif choice == '3':
  			country()
  		elif choice == '4':
  			wiki()
	  	else:
	  		error()

		# shouldquit(choice)
	else:
		goodbye()

def wiki():
	thing=raw_input('Type in the disease or country that you want to access more information on. Or, type "quit" to quit. ')
	if thing.lower() != 'quit':
		print(w.summary(thing, sentences=5))
		choices()
	else:
		goodbye()

def choro_menu():
	print('''
		Choose 1 to see the occurrence of death by all causes by country, 2 to see occurrence of death by communicable disease, 3 to see occurrence of death by noncommunicable illness, or 4 to see occurrence of death by injury. 

		Type 'm' to return to the main menu, or type 'quit' to quit.
		''')
	chor = raw_input('Type your choice: ')
	if chor == '1':
		count.country_choropleth()
	elif chor == '2':
		comm.comm_choropleth()
	elif chor == '3':
		nc.noncomm_choropleth()
	elif chor == '4':
		inj.injuries_choropleth()
	elif chor.lower() == 'm':
		choices()
	elif chor.lower() == 'quit':
		goodbye()
	else:
		error()

def bar_menu():
	region = raw_input('''Select a WHO region you would like to learn about.
		Type 1 for the Americas, 2 for Africa, 3 for Europe, 4 for the Eastern Mediterranean, 5 for Southeast Asia, or 6 for the Western Pacific.
		Type 'm' to go back to the main menu, or type 'quit' to quit. ''').lower()
	if region == 'm':
		choices()
	elif region == 'quit':
		goodbye()
	elif region != '1' and region != '2' and region != '3' and region != '4' and region != '5' and region != '6':
		error()
	y_or_n = raw_input('Would you like to input your own diseases to compare? (y or n) ').lower()
	if y_or_n == 'y':
		diseases = []
		x = 0
		while x == 0:
			d = raw_input("Input a disease you would like to view information on.  If your list is complete, type 'end'. ").lower().capitalize()
			if d != 'End':
				diseases.append(d)
			else:
				x += 1
	elif y_or_n != 'n':
		error()
	else:
		diseases=['HIV/AIDS', 'Malaria', 'Tuberculosis', 'Stroke', 'Diabetes mellitus', 'Malignant neoplasms']

	ages = raw_input('Would you like to input your own ages to compare? (y or n) ').lower()
	if ages == 'y':
		ages = []
		x = 0
		while x == 0:
			a = raw_input("Type 1 to add 'All ages' to your graph; type 2 for '5-14 years'; type 3 for '15-29 years'; type 4 for '30-49 years'; type 5 for '50-59 years'; type 6 for '60-69 years'; type 7 for '70+ years'.  When your list is complete, type 'end'. ").lower()
			if a == 'end':
				x += 1
			elif a == '1':
				ages.append(' All ages (total) years')
			elif a == '2':
				ages.append('5-14 years')
			elif a == '3':
				ages.append('15-29  years')
			elif a == '4':
				ages.append('30-49 years')
			elif a == '5':
				ages.append('50-59  years')
			elif a == '6':
				ages.append('60-69  years')
			elif a == '7':
				ages.append('70+  years')
			else:
				error()
	elif ages != 'n':
		error()
	else:
		ages=[' All ages (total) years', '5-14 years', '15-29  years', '30-49 years', '50-59  years', '60-69  years', '70+  years']

	reg.reg_bar(region, diseases=diseases, ages=ages)
	after_bar()

def after_bar():
	c = raw_input("Type 'b' to make another bar graph; type 'm' for the main menu; or type 'quit' to quit. ").lower()
	if c == 'b':
		bar_menu()
	elif c == 'm':
		choices()
	elif c == 'quit':
		goodbye()
	else:
		error()

def error():
	print("Sorry, I didn't understand.  Please input a valid choice.")
	choices()

def goodbye():
	print('Thank you for using the program. Goodbye!')
	quit()

welcome()