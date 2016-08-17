import plotly.plotly as ply 
import pandas as pd 
import csv

ply.sign_in('rmm99', 'ko9rku5kqy')

country_death_rates_in = open("country_death_rates.csv", "rU")
stats_in = list(csv.reader(country_death_rates_in))
country_death_rates_2012={'Country':[],'Communicable & other Group I':[]}
for i in range(1,len(stats_in),2):
	country_death_rates_2012['Country'].append(stats_in[i][0])
	#country_death_rates_2012['All Causes'].append(float(stats_in[i][2]))
	country_death_rates_2012['Communicable & other Group I'].append(stats_in[i][3])
	# country_death_rates_2012['Noncommunicable diseases'].append(stats_in[i][4])
	# country_death_rates_2012['Injuries'].append(stats_in[i][5])
	# country_death_rates_2012['text'].append(stats_in[i][0] + "<br> Communicable & other Group I Diseases: " + stats_in[i][3] + "<br> Noncommunicable Diseases: " + stats_in[i][4] + "<br> Injuries: " + stats_in[i][5])

geo_deets = dict(
		scope = 'world',
		projection = dict(type='Mercator'),
		showlakes = False
		
	)


map_layout = dict(
	title = 'Incidents of Death By Communicable and other Group I Diseases Per Country in 2012',
	geo =  geo_deets
	)

violet_scale = [[0.0, 'pink'], [1.0, 'darkred']]

stuff_plotly_needs = [ dict(
		type='choropleth',
		colorscale= violet_scale,
		autocolorscale= False,
		locations = country_death_rates_2012['Country'],
		z = country_death_rates_2012['Communicable & other Group I'],
		locationmode= 'country names',
		text= country_death_rates_2012['Country'],
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

ply.plot(plotly_fig, filename='Deaths-by-communicable-diseases-map')

