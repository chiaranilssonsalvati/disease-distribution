import plotly.plotly as ply
import pandas as pd 

ply.sign_in('rmm99', 'ko9rku5kqy')


country_death_rates= pd.readcsv('/Users/rebeccamuratore/Documents/BridgeUp/DataViz/disease-distribution/country_death_rates.csv')


for col in country_death_rates.columns:
	country_death_rates[col]= country_death_rates[col].astype(str)

geo_deets = dict(
		scope = 'world',
		projection = dict(type='Mercator'),
		showlakes = True,
		lakecolor = 'turquoise'
	)


map_layout = dict(
	title = 'Incidents of Death By All Causes By Country',
	geo =  geo_deets
	)

blue_scale = [[0.0, 'white'], [1.0, 'blue']]

country_death_rates['text'] = country_death_rates['']


stuff_plotly_needs = [ dict(
		type='choropleth',
		colorscale= blue_scale,
		autocolorscale= False,
		locations = country_death_rates['country'],
		z = country_death_rates['All Causes'].astype(float),
		locationmode= 'world-countries',
		text= country_death_rates['text'],
		marker = dict(
			line = dict(
				color='white',
				width= 2
				)
			),
		colorbar= dict(
			title= 'Age-standerdized mortality rate by cause (per 100,000 population'
			)
	)
]
plotly_fig = dict(
		data= stuff_plotly_needs,
		layout= map_layout
	)

ply.plot(plotly_fig, filename='awesome-sauce-map')

