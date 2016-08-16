import csv
import sqlite3 as sq 

africa = open('africa.csv', 'w')
africa_write = csv.writer(africa)
americas = open('americas.csv', 'w')
am_write = csv.writer(americas)
emed = open('emed.csv', 'w')
med_write = csv.writer(emed)
europe = open('europe.csv', 'w')
eur_write = csv.writer(europe)
seasia = open('seasia.csv', 'w')
asia_write = csv.writer(seasia)
pacific = open('wpacific.csv', 'w')
pac_write = csv.writer(pacific)
conn = sq.connect('diseases.db')
c = conn.cursor()

files = [africa_write, am_write, med_write, eur_write, asia_write, pac_write]
tables = ['Africa', 'Americas', 'Medit', 'Europe', 'Asia', 'Pacific']

for f, t in zip(files, tables):
	c.execute('UPDATE '+t+' SET B=B+I')
	c.execute('UPDATE '+t+' SET C=C+J')
	c.execute('UPDATE '+t+' SET D=D+K')
	c.execute('UPDATE '+t+' SET E=E+L')
	c.execute('UPDATE '+t+' SET F=F+M')
	c.execute('UPDATE '+t+' SET G=G+N')

	c.execute('SELECT Diseases, A, B, C, D, E, F, G FROM '+t)
	rows = c.fetchall()
	for r in rows:
		f.writerow(r)






conn.commit()
conn.close()
africa.close()
americas.close()
emed.close()
europe.close()
seasia.close()
pacific.close()