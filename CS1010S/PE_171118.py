#1A - iterative
def floyd_row(n):
	num = 0
	result = []
	for i in range(1, n):
		num += i
	for i in range(n):
		num += 1
		result.append(num)
	return tuple(i for i in result)

#print(floyd_row(5))

#1B
def floyd_sum(n):
	last_num = floyd_row(n)[-1]
	result = 0
	for i in range(1, last_num + 1):
		result += i
	return result
#print(floyd_sum(5))

def fundamental_sum(seq):
	if len(seq) == 1:
		return seq[0]	#seq[0] as (x,) is still considered a tuple term and cannot be added to an integer
	return seq[0] + fundamental_sum(seq[1:])
#print(fundamental_sum((1,2,3)))

#2A
def regional_sales(f, platform, year):

	lines = []
	sales = [0, 0, 0, 0, 0]

	with open(f,'r') as f:
		for line in f:
			columns = line.split(',')					#split into cell value, categorise into lists
			lines.append(columns)						#save each list into 'lines'
		for lst in lines:
			if lst[1] == platform and lst[2] == str(year):			#match criteria first
				toadd = lst[5:9] + [lst[-1][:-1]]				#save the sales part of each entry into 'sales'. but last term has a \n which needs to be parsed out
				toadd = [float(i) for i in toadd]				#cast into integer
				sales = map(sum, zip(sales, toadd))				#zip sales, toadd to form a tuple for every corresponding term. then apply (map) the function sum over that list.

	sales = list(sales)		#recall map returns an iterable, has to be casted into a list to read
	return [round(i, 2) for i in sales]	

print(regional_sales('vgsales.csv', 'X360', 2016))
print(regional_sales('vgsales.csv', '3DS', 2012))
#import csv, instead of manually parsing the file.
#filter(lambda x: x[2] == str(year) and x[1] == platform, lines)

#2B
def trending_genre(f, platform):

	lines = []
	years = []
	genres = []
	result = dict()

	with open(f, 'r') as file:
		for line in file:
			columns = line.split(',')
			lines.append(columns)						#parse lines

		#find all years for that platform
		for line in lines:
			if line[1] == platform and line[2] not in years:
				try:
					x = int(line[2])					#error catching, if 'N/A' or other values (eg. if name had a comma, thus messing up the format)
					years.append(line[2])				
				except:
					continue

		#find all genres for that platform
		for line in lines:
			if line[1] == platform and line[3] not in genres:
				genres.append(line[3])

		#find greatest percentage increases for each year -- to be put into result
		for i in range(1, len(years)):
			increases = dict()
			#increases will have to be a dictionary as we still have to locate the genre
			#this dictionary contains the percentage increase for each genre for that year

			for genre in genres:
				current_sales = 0						#total sales for that genre in that year.
				for line in lines:
					if line[1] == platform and line[2] == years[i] and line[3] == genre:	#for that platform, year, and genre, add TOTAL sales to the counter
						current_sales += float(line[-1][:-1])
				current_sales = round(current_sales, 2)	#round due to integer leak

				prev_sales = 0 							#copy for previous year sales
				for line in lines:
					if line[1] == platform and line[2] == years[i - 1] and line[3] == genre:
						prev_sales += float(line[-1][:-1])
				prev_sales = round(prev_sales, 2)
				
				try:
					increase = round((current_sales - prev_sales) / prev_sales * 100, 2)	#bare formula for percentage increase
				except ZeroDivisionError:				#ignore if previous year was 0
					continue
				except:
					print('error noooo')
				increases[genre] = increase
			
			#fragment the list, extract the maximum percentage increase value, find the corresponding genre, then enter it into the main result dictionary.
			#is there a better way? yes. use .get method, which can be input as a key parameter in max()
			genre_list = list(increases.keys())			
			increase_list = list(increases.values())
			result[years[i]] = genre_list[increase_list.index(max(increase_list))]

		return result

print(trending_genre('vgsales.csv', 'PC'))
print(trending_genre('vgsales.csv', 'PSP'))

#3
class Stone():

	def __init__(self, name, *powers):
		self.name = name 
		self.powers = list(powers)		#powers currently imbued, mutable. if already exists, cannot imbue
		self.destroyed = False			#not destroyed by default
		self.attached = None			#attached to nothing by default -- interaction with Artefact class

	def imbue(self, power):
		if self.destroyed == True:
			return f'{self.name} is already destroyed'
		elif power not in self.powers:
			self.powers.append(power)	#add power
			return f'{self.name} is now imbued with power: {power}'
		elif power in self.powers:
			return f'{self.name} is already imbued with power: {power}'

	def disarm(self, power):
		if self.destroyed == True:
			return f'{self.name} is already destroyed'
		elif power in self.powers:
			self.powers.remove(power)	#remove power
			return f'{self.name} is no longer imbued with power: {power}'
		elif power not in self.powers:
			return f'{self.name} is not imbued with power: {power}'

	def destroy(self):
		if self.destroyed == True:
			return f'{self.name} is already destroyed'
		else:
			self.destroyed = True
			self.powers = []
			self.attached.stones.remove(self)
			self.attached = None 		#two way tagging. but remove from artefact side first before deleting from self.
			return f'{self.name} has been destroyed'

	def list_powers(self):
		if self.destroyed == True:
			return ()
		else:
			return self.powers


class Artefact():

	def __init__(self, name, *stones):
		self.name = name 
		self.stones = []
		self.combined = [self]

		#validate input data -- this is good practice
		for i in list(stones):
			if isinstance(i, Stone):
				self.stones.append(i)
				i.attached = self

	def add_stone(self, stone):
		#input error catching
		if isinstance(stone, Stone):
			#contextual error catching
			if stone.destroyed == True:
				return f'{stone.name} has already been destroyed'
			elif stone.attached != None:
				return f'{stone.name} is already part of {stone.attached.name}'
			elif stone in self.stones:
				return f'{self.name} already has {stone.name}'
			elif stone not in self.stones:
				self.stones.append(stone)	#stone attached to artefact
				stone.attached = self  	#artefact name attached to the stone -- two way tagging
				return f'{stone.name} has been added to {self.name}'
		else:
			return 'Stone object not recognised'

	def remove_stone(self, stone):
		if isinstance(stone, Stone):
			if stone not in self.stones:
				return f'{self.name} does not contain {stone.name}'
			elif stone in self.stones:
				self.stones.remove(stone)
				stone.attached = None
				return f'{stone.name} has been removed from {self.name}'
		else:
			return 'Stone object not recognised'

	def combine(self, artefact):		#combining here is a network, i.e A & C both connecting to B means A and C are also connected
		if isinstance(artefact, Artefact):
			if artefact is self:
				return 'Cannot combine with itself'
			elif artefact in self.combined:
				return f'{self.name} is already combined with {artefact.name}'
			else:
				self.combined = self.combined + artefact.combined
				artefact.combined = artefact.combined + self.combined
				return f'{self.name} combines with {artefact.name}'
		else:
			return 'Artefact object not recognised'	

	def invoke(self):
		result = set()
		for artefact in self.combined:
			for stone in artefact.stones:
				for power in stone.powers:
					result.add(power)
		return tuple(result)

#important -- instances can also be added to lists, though it is not readable. matter of fact technically everything in Python is an instance
power_stone = Stone("Power Stone", "Attack", "Defense")
mind_stone = Stone("Mind Stone", "Brainwash")
time_stone = Stone("Time Stone")
reality_stone = Stone("Reality Stone", "Illusion")

print(power_stone.imbue("Attack"))
print(power_stone.imbue("Strength"))
print(power_stone.list_powers())
print(time_stone.imbue("Repeat"))
print(time_stone.imbue("Undo"))

vision = Artefact("Vision", mind_stone)
gauntlet = Artefact("Gauntlet", power_stone)
eye_of_agamotto = Artefact("Eye of Agamoto")

print(vision.add_stone(mind_stone))
print(vision.remove_stone(power_stone))
print(vision.remove_stone(mind_stone))
print(vision.add_stone(mind_stone))
print(vision.invoke())
print(vision.add_stone(power_stone))

print(mind_stone.disarm("AI"))
print(mind_stone.destroy())
print(mind_stone.disarm("Brainwash"))

print(vision.remove_stone(mind_stone))
print(eye_of_agamotto.add_stone(time_stone))
print(vision.combine(eye_of_agamotto))
print(eye_of_agamotto.combine(vision))

mind_stone_remade = Stone("Mind Stone", "Brainwash", "Illusion")

print(gauntlet.add_stone(mind_stone))
print(gauntlet.add_stone(mind_stone_remade))
print(gauntlet.invoke())
print(gauntlet.add_stone(reality_stone))
print(gauntlet.invoke())
print(gauntlet.combine(eye_of_agamotto))
print(gauntlet.combine(vision))
print(gauntlet.invoke())