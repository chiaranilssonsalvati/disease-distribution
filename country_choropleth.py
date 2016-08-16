import plotly.plotly as ply
import pandas as pd 

ply.sign_in('rmm99', 'ko9rku5kqy')


country_death_rates= pd.read_csv('/Users/rebeccamuratore/Documents/BridgeUp/DataViz/disease-distribution/country_death_rates.csv')


for col in country_death_rates.columns:
	country_death_rates[col]= country_death_rates[col].astype(str)

geo_deets = dict(
		scope = 'world',
		projection = dict(type='Mercator'),
		showlakes = True,
		lakecolor = 'turquoise'
	)


map_layout = dict(
	title = 'Incidents of Death By All Causes Per Country in 2012',
	geo =  geo_deets
	)

blue_scale = [[0.0, 'white'], [1.0, 'blue']]

country_death_rates['text'] = country_death_rates['Country'] + "<br> Communicable & other Group I Diseases: " + country_death_rates['Communicable & other Group I'] + "<br> Noncommunicable Diseases: " + country_death_rates['Noncommunicable diseases'] + "<br> Injuries: " + country_death_rates['Injuries']

for value in country_death_rates['Year']:
	if value == 2012:
		country_death_rates['text'] 
	#else:
		#print('error')

stuff_plotly_needs = [ dict(
		type='choropleth',
		colorscale= blue_scale,
		autocolorscale= False,
		locations = country_death_rates['Country'],
		z = country_death_rates['All Causes'].astype(float),
		locationmode= 'country names',
		text= country_death_rates['text'],
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

