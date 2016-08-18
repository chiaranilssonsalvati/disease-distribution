import plotly.plotly as ply
import pandas as pd 
import csv 

def country_choropleth():
	ply.sign_in('rmm99', 'ko9rku5kqy')

	'''
	country_death_rates= pd.read_csv("country_death_rates.csv")
	country_death_rates_2012= []

	for col in country_death_rates.columns:
		country_death_rates[col]= country_death_rates[col].astype(str)
		if country_death_rates
	'''
	country_death_rates_in = open("country_death_rates.csv", "rU")
	stats_in = list(csv.reader(country_death_rates_in))
	country_death_rates_2012={'Country':[],'All Causes':[],'Communicable & other Group I':[],'Noncommunicable diseases':[],'Injuries':[],'text':[]}
	for i in range(1,len(stats_in),2):
		country_death_rates_2012['Country'].append(stats_in[i][0])
		country_death_rates_2012['All Causes'].append(float(stats_in[i][2]))
		country_death_rates_2012['Communicable & other Group I'].append(stats_in[i][3])
		country_death_rates_2012['Noncommunicable diseases'].append(stats_in[i][4])
		country_death_rates_2012['Injuries'].append(stats_in[i][5])
		country_death_rates_2012['text'].append(stats_in[i][0] + "<br> Communicable & other Group I Diseases: " + stats_in[i][3] + "<br> Noncommunicable Diseases: " + stats_in[i][4] + "<br> Injuries: " + stats_in[i][5])

	geo_deets = dict(
			scope = 'world',
			projection = dict(type='Mercator'),
			showlakes = False
			
		)


	map_layout = dict(
		title = 'Incidents of Death By All Causes Per Country in 2012',
		geo =  geo_deets
		)

	violet_scale = [[0.0, 'lavender'], [1.0, 'indigo']]

	#country_death_rates_2012['text'] = country_death_rates_2012['Country'] + "<br> Communicable & other Group I Diseases: " + country_death_rates_2012['Communicable & other Group I'] + "<br> Noncommunicable Diseases: " + country_death_rates_2012['Noncommunicable diseases'] + "<br> Injuries: " + country_death_rates_2012['Injuries']

	'''
	for value in country_death_rates['Year']:
		if value == 2012:
			country_death_rates['text'] 
		#else:
			#print('error')
	'''

	stuff_plotly_needs = [ dict(
			type='choropleth',
			colorscale= violet_scale,
			autocolorscale= False,
			locations = country_death_rates_2012['Country'],
			z = country_death_rates_2012['All Causes'],
			locationmode= 'country names',
			text= country_death_rates_2012['text'],
			marker = dict(
				line = dict(
					color='black',
					width= 1
					)
				),
			colorbar= dict(
				title= 'Age-standardized mortality rate (per 100,000 population)'
				)
		)
	]
	plotly_fig = dict(
			data= stuff_plotly_needs,
			layout= map_layout
		)

	ply.plot(plotly_fig, filename='Deaths-by-countries-map')

