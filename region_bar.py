import csv
import numpy as np 
import matplotlib.pyplot as plt 

def make_hist(region, diseases=['HIV/AIDS', 'Malaria', 'Tuberculosis', 'Stroke', 'Diabetes mellitus', 'Malignant neoplasms'], ages=[' All ages (total) years', '5-14 years', '15-29  years', '30-49 years', '50-59  years', '60-69  years', '70+  years']):
	if region == 'Eastern mediterranean':
		f = open('emed.csv', 'r')
	elif region == 'Europe':
		f = open('europe.csv', 'r')
	elif region == 'Americas':
		f = open('americas.csv', 'r')
	elif region == 'Africa':
		f = open('africa.csv', 'r')
	elif region == 'Southeast Asia':
		f = open('seasia.csv', 'r')
	elif region == 'Western pacific':
		f = open('wpacific.csv', 'r')
	#else:
		#error/go back to menu (menu should probably have a checking function first though)
	read = list(csv.reader(f))
	headers = read[0]

	for d in diseases:
		x = False
		for row in read:
			if row[0]==' '+d:
				x = True
		if x == False:
			print('Sorry, we have no information on the disease '+d+' and will remove it from your query.')
			diseases.remove(d)

	causes = [' Communicable &amp; other Group I', ' Noncommunicable diseases', ' Injuries']
	labels = ['Communicable diseases', 'Noncommunicable diseases', 'Injuries']
	for d in diseases:
		causes.append(' '+d)
		labels.append(d)
	
	y_vals_overall = {}
	x_vals = range(25, 80*len(labels)+25, 80)
	print(ages)
	for a in ages:
		y_vals_overall[a]=[]
		for c in causes:
			for row in read:
				if row[0] == c:
					print(c)
					y_vals_overall[a].append(float(row[headers.index(a)]))



	colors=['red', 'orange', 'yellow', 'green', 'blue', 'lavender', 'indigo']
	x = 0
	for a, c in zip(ages, colors):
		plt.bar([y+x for y in x_vals], y_vals_overall[a], align='center', width=10, label=a, color=c, edgecolor='none')
		x +=10
	
	plt.xticks([y+(10*len(ages))/4 for y in x_vals], labels, rotation='vertical')
	plt.xlabel('Causes of Death')
	plt.title('Frequency of Causes of Death in 2012 in the WHO '+region+' Region')
	plt.ylabel('Number of Deaths per 100000 Population')
	# plt.margins(.2)
	plt.subplots_adjust(bottom=0.4)
	plt.legend()
	plt.show()





# make_hist(raw_input('region pls: ').lower().capitalize())

make_hist('Americas', ['Asthma', 'Sunstroke', 'Tuberculosis', 'Syphilis'], ['15-29  years', '30-49 years', ' All ages (total) years'])

# all 'Injuries', all 'Communicable &amp; other Group 1', 'Noncommunicable diseases'