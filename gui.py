from swampy.Gui import *

g = Gui()
g.title('PLP Routing')

listOfClubs = ['Liverpool','Man United', 'Tottenham', 'Man City', 'Everton', 'Arsenal', 'West Ham', 'Sunderland', 'Stoke', 'Crystal Palace', 'Southampton', 'Burnley', 'Hull', 'Watford', 'West Brom', 'Leicester', 'Chelsea','Bournemouth','Swansea','Middlesbrough']

listOfClubs.sort()

for each in listOfClubs:
    button = g.bu(text=each)

g.mainloop()