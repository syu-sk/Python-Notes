#1A
def digit_product(n):
	result = 1
	for i in str(n):
		result *= int(i)
	return result
#print(digit_product(1234))

#1B
def max_digit_product(n, k):
	biggest = 0
	for index in range(len(str(n)) - k + 1):	#find start
		product = 1
		for i in range(k):
			product *= int(str(n)[index + i])	#find product of consecutive numbers
		if product > biggest:
			biggest = product 
	return biggest
#print(max_digit_product(189113451, 2))

#2A
def parse_data(file):
	parsed = []
	with open(file, 'r') as f:
		for line in f:
			elements = line.split(',')[:-1] + [line.split(',')[-1][:-1]]
			parsed.append(elements)
	return parsed 
#print(parse_data('employment.csv'))

#2B
def compute_employment_rate(filename, university, degree, start_year, end_year):
	data = parse_data(filename)
	emprates = []
	for line in data:
		try:
			if int(line[0]) <= end_year and int(line[0]) >= start_year and line[1] == university and line[3] == degree and line[4] == 'employment_rate_overall':
				emprates.append(int(line[5]))
		except:
			continue
	return sum(emprates) / len(emprates)
#print(compute_employment_rate("employment.csv",'National University of Singapore',"Bachelor of Computing (Computer Science)",2014,2018))

#3
class Weapon:

    def __init__(self, name, dmg):
        self.name = name
        self.dmg = dmg

    def get_weapon_damage(self):
        return self.dmg

    def get_weapon_name(self):
        return self.name


class Soldier:

	def __init__(self, name, *weapons):
		self.name = name 
		self.weapons = []
		self.health = 100
		self.alive = True
		self.army = None

		for i in weapons:				#validate input data
			if isinstance(i, Weapon):
				self.weapons.append(i)

	def weaponlist(self):				#learning point: method cannot have overlapping names with attribute
		if not self.weapons:
			return f'{self.name} is unarmed!'
		else:
			return [i.name for i in self.weapons]

	def is_alive(self):					#predicate -- can be used rather than not self.alive. receive_damage can also be polished better using more readable if statements
		return self.alive

	def receive_damage(self, dmg):
		if self.alive == False:
			return f'{self.name} is already dead!'
		elif self.health - dmg <= 0:
			self.alive = False
			self.health = 0
			self.removefromarmy()
			return f'{self.name} received {dmg} damage and died!'
		else:
			self.health -= dmg 
			return f'{self.name} received {dmg} damage -- {self.health} health left!'

	def attack(self, enemy):			#assuming type(enemy) is always Soldier, no input errors
		weapon_damage = [i.dmg for i in self.weapons]
		if enemy == self:
			return f'{self.name} cannot attack itself!'
		elif not self.alive:
			return f'{self.name} is already dead!'
		elif not enemy.alive:
			return f'{enemy.name} is already dead!'
		else:
			imm_damage = max(weapon_damage)
			enemy.receive_damage(imm_damage)
			return f'{enemy.name} received {imm_damage} damage!'

	def add_weapon(self, new_wep):		#assuming type(new_wep) is always Weapon
		if not self.alive:
			return f'{self.name} is already dead!'
		elif new_wep in self.weapons:
			return f'{new_wep.name} is already equipped!'
		else:
			self.weapons.append(new_wep)
			return f'{self.name} obtained {new_wep.name}'

	def drop_weapon(self):
		if not self.alive:
			return f'{self.name} is already dead!'
		elif not self.weapons:
			return f'{self.name} has no weapon!'
		else:							#after error catching, initiate operation
			weapons, weapondmg = [i for i in self.weapons], [i.dmg for i in self.weapons]
			dropped_weapon = weapons[weapondmg.index(min(weapondmg))]		#nature of .index finds the earliest weapon, fulfilling requirement automatically
			self.weapons.remove(dropped_weapon)
			return f'{self.name} has dropped {dropped_weapon.name}!'

	def removefromarmy(self):			#two way input
		self.army.soldiers.remove(self)
		self.army = None



class Army:

	def __init__(self, soldiers, name):
		self.name = name 
		self.soldiers = []

		for i in soldiers:
			if isinstance(i, Soldier):
				self.soldiers.append(i)
				i.army = self
		print(self.soldiers)

	def is_wiped_out(self):
		return not self.soldiers
 
	def fight_army(self, enemy):		#assuming type(enemy) is always Army
		if not self.soldiers:
			return f'{self.name} has already been wiped out!'
		elif not enemy.soldiers:
			return f'{enemy.name} has already been wiped out!'
		else:							#after error catching, initiate operation
			if len(self.soldiers) <= len(enemy.soldiers):		#find smaller army to deny excess soldiers
				smaller_army = self.soldiers					#alternatively, try fighting till index error but fk that
			else:
				smaller_army = enemy.soldiers
			for i in range(len(smaller_army)):	#uniform index to fight other army
				self.soldiers[i].attack(enemy.soldiers[i])
			if enemy.is_wiped_out():
				return f'{enemy.name} has been wiped out!'
			else:
				return f'{enemy.name} was attacked by {self.name}, but survives...'

spear_30 = Weapon("Spear", 30)
sword_25 = Weapon("Sword", 25)
yu_guan = Soldier("Yu Guan", spear_30)
bei_liu = Soldier("Bei Liu")
print(yu_guan.weaponlist())				#class method here is named weaponlist rather than weapons, since it already has an attribute weapons with a conflicting name

print(yu_guan.is_alive())
print(yu_guan.receive_damage(5))
print(yu_guan.add_weapon(sword_25))
print(yu_guan.attack(bei_liu))
print(bei_liu.drop_weapon())
print(yu_guan.drop_weapon())
print(yu_guan.weaponlist())

quan_sun = Soldier("Quan Sun", Weapon("Halberd", 30))
liang_sun = Soldier("Liang Sun", Weapon("Halberd", 25))
xiu_sun = Soldier("Xiu Sun", Weapon("Halberd", 20))
army1 = Army([quan_sun, liang_sun, xiu_sun], "army1")
army2 = Army([yu_guan, bei_liu], "army2")
print(army1.fight_army(army2))
print(army1.fight_army(army2))
print(army1.fight_army(army2))
print(army1.fight_army(army2))
print(army1.fight_army(army2))
print(yu_guan.is_alive())
print(yu_guan.drop_weapon())
print(yu_guan.add_weapon(sword_25))
print(yu_guan.attack(quan_sun))
print(quan_sun.attack(yu_guan))
print(quan_sun.attack(quan_sun))