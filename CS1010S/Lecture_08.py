'''Lecture 8'''

'''
Introduction to Data Structures:
- 2 players
- Game has multiple piles of coins
- Players take turns removing any number of coins from a single pile
- Player who take the last coin wins
'''

#Game state: to keep track of number of coins in each pile.

'''Functions required'''
#Assuming we have make_game_state function, memorising each pile
#size_of_pile(game_state, p), p being the pile index
#remove_coins_from_pile(game_state, n, p), n being number of coins to remove
#notice below that when crafting complex mutual recursive functions (such as when making games like these), it is better to make the skeleton, then code the subfunctions out
#see below on play(). there are many unknown functions at first, but those can be made again later. obtain the big picture first.

'''
Undo function:
Requires complex use of data structures.
The data structure used here will be one known as 'Stack'
- Works on a Last in, First Out principle.
- Items are removed in the reverse order in which they were added. This way the most recent turn can be cancelled with one action.

Functions required:
1. make_stack(), a constructor for the data structure
2. push(s, item), adds item to a stack s
3. pop(s), which removes the most recently added item (as with the principle)
4. is_empty(s), a predicator, which returns a boolean on whether stack is empty.

*comments indicated on operations pertaining to this function
'''

#starting with the game,
def play(game_stack, game_state, player):	#stack is to be manually keyed into play, i.e selecting a save file.
	display_game_state(game_state) 	#external function to display game status for human readability
	if is_game_over(game_state):
		announce_winner(player)
	elif player == "human":
		play(game_stack, human_move(game_stack, game_state), "computer")
	elif player == "computer":
		play(game_stack, computer_move(game_state), "human")	#play function requires game_stack even though computer_move does not use it
	else: 	#catch errors
		print("player wasn't human or computer:", player)

#display menu
def display_game_state(game_state):
	print('-----------------------')
	print(f'Pile 1: {str(size_of_pile(game_state, 1))}')
	print(f'Pile 2: {str(size_of_pile(game_state, 2))}')
	print('-----------------------')

#other game states - game end, winner message, player move
def is_game_over(game_state):
	return size_of_pile(game_state, 1) + size_of_pile(game_state, 2) == 0

def announce_winner(player):
	if player == 'human':
		print('You Lose')
	else:
		print('You Win!!')
	#logic is reversed because function is called before start of the turn.

def human_move(game_stack, game_state):
	p = input('Enter pile to remove from: ')
	if int(p) == 0:		#data structure, undo function
		return handle_undo(game_stack, game_state)

	n = input('Enter number of coins to remove: ')
	try:				#error catching
		test = int(p) + int(n)
	except:
		print('Please enter an integer.')
		return human_move(game_stack, game_state)
	push(game_stack, game_state) 		#data structure, pushing previous turn ONLY if pile != 0.
	return remove_coins_from_pile(game_state, int(p), int(n)) 		#note the game state for this turn is NOT saved, waits till next turn to save if p != 0.
	#input required to run through REPL

#how computer moves
def computer_move(game_state):
	pile = 1 if size_of_pile(game_state, 1) > 0 else 2
	print("Computer removes 1 coin from pile " + str(pile))
	#remove 1 coin at all times, prioritising pile 1
	#realistically this strategy is a sure lose
	return remove_coins_from_pile(game_state, pile, 1)

def remove_coins_from_pile(game_state, pile, n):
	if pile == 1:
		return make_game_state(size_of_pile(game_state, 1) - n, size_of_pile(game_state, 2))
	else:
		return make_game_state(size_of_pile(game_state, 1), size_of_pile(game_state, 2) - n)

#backend game statuses
def make_game_state(pile1, pile2):
	return [pile1, pile2]

def size_of_pile(game_state, pile):
	return game_state[pile - 1]

#undo function
def handle_undo(game_stack, game_state):
	old_state = gpop(game_stack, game_state)
	if old_state: 		#i.e if old_state == True, that is if old_state is not None.
		print('Move undone')
		display_game_state(old_state) 		#as usual, proceed as with play()
		return human_move(game_stack, old_state)
	else:
		print('No previous moves')
		return human_move(game_stack, game_state) 		#error catching

def push(s, game_state):
	return s.append(game_state)

def gpop(s, game_state):
	return s.pop()		#why does pop do the job? because the last game_state is the previous turn. current game state is not yet saved.
						#thats why pop, which isolates the last value, will return the previous game state.
def make_stack():
	return []

stack33 = make_stack()		#acts as a save file
game33 = make_game_state(3, 3)
#play(stack33, game33, 'human')

'''
Concepts of data structure:
- Overview of data structure (type)
- State assumptions, contracts, guarantees. i.e fill in 'ghost' functions, then write them out later.
- Give examples

Operations:
- Constructors (make_game_state, make_stack)
- Selectors (gpop, size_of_pile)
- Predicates (is_empty)
- Printers (display_game_state)
'''



#Moving on to the next part about Sets.
'''
A set is an unordered collection of objects WITHOUT duplicates.
- Denoted by curly brackets {}
- Unordered: {1,2,3} == {3,2,1}
- No duplicates: {1,2,2,3} computes to {1,2,3}

Specs (i.e operations):
- Constructors: make_set, adjoin_set, union_set, intersection_set
- Selectors: [ ]
- Predicates: is_element_of_set, is_empty_set
- Printers: print_set
'''

#question of the day
def make_set():		#constructor as provided
	return []

def intersection_set(s1, s2):
	for i in s1:
		if i not in s2:
			s1.remove(i)
	return s1

'''Tutorial 7'''
#1
def accumulate(op, init, seq):	#given -- general accumulate function
	if not seq:		#if seq is empty
		return init
	else:
		return op(seq[0], accumulate (op, init, seq[1:]))

def accumulate_n(op, init, sequences):
	if not sequences[0]:		#base case -- if sequence no longer has any more elements, return []. adding [] to a list does nothing, usable as a terminator.
		return []
	else:
		return [accumulate(op, init, [i[0] for i in sequences])] + accumulate_n(op, init, [i[1:] for i in sequences]) #no brackets around recursive function
		#higher order function than accumulate. isolates the first element of each list, combining them into a list which can then be summed using accumulate().
		#using list comprehensions, the untouched part of each list is then made into another list itself where accumulate_n is recursively used.

s = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
#print(accumulate_n(lambda x, y: x + y, 0, s))

#2
def transpose(m):
	transposed = []
	for i in range(0, len(m[0])):
		newcol = []
		for lst in m:
			newcol.append(lst[i])
		transposed.append(newcol)
	return transposed

def col_sum(m):
	return accumulate_n(lambda x, y: x + y, 0, m)

def row_sum(m):
	return accumulate_n(lambda x, y: x + y, 0, transpose(m))

#3a
def count_sentence(s):
	words = 0
	letters = 0
	for word in s:
		words += 1
		for letter in word:
			letters += 1
	return [words, letters]

#print(count_sentence([[ 'P', 'y', 't', 'h', 'o', 'n'] , ['i', 's'] , ['c', 'o', 'o', 'l']]))

#3b
def letter_count(s):
	return [[i[0], len(i)] for i in s]
	#time - O(n), space - O(n)

#print(letter_count ([[ 's', 'h', 'e'] , ['l', 'i', 'k', 'e', 's'] ,['p', 'i', 'e', 's']]))
	
#3c
def level(lst):
	if lst == []:
		return []
	elif type(lst) != list:
		return [lst] 		#similarly, nest only single outputs
	else:
		return level(lst[0]) + level(lst[1:])		#nesting [0] returns same output, nesting each individual word
													#nesting [1:] nests the entire back portion recursively.

def most_frequent_letters(lst):
	levelled = level(lst)
	if not levelled:
		return []									#return empty list if lst is empty
	highfreq = 0
	for i in levelled:
		if levelled.count(i) > highfreq:
			highfreq = levelled.count(i)			#to find highest frequency for appearance of letters
	result = []
	for i in levelled:
		if levelled.count(i) == highfreq and i not in result:
			result.append(i)						#filter out letters with that highest frequency, without duplicates
	return result

#print(most_frequent_letters([[ 's', 'h', 'e'] , ['l', 'i', 'k', 'e', 's'] ,['p', 'i', 'e', 's']]))
#time - O(n), since loops are not nested. space - O(n) ?

#4
def make_queue():
	return []										#mutable

def enqueue(q, item):
	return q.append(item)

def dequeue(q):
	return q.pop(0)

def size(q):
	return len(q)

q = make_queue()
enqueue(q, 1)
enqueue(q, 5)
#print(size(q))
#print(dequeue(q))
#print(q)

#5
def who_wins(m, lst):
	players = make_queue()
	for i in lst:
		enqueue(players, i)
	timer = m
	while len(players) >= m:
		if timer == 0:
			dequeue(players)
			timer = m
			enqueue(players, dequeue(players))
		else:
			enqueue(players, dequeue(players))
		timer -= 1
	return players

#print(who_wins(3 , ['val ', 'hel ', 'jam ', 'jin ', 'tze ', 'eli ', 'zha ', 'lic ']))
#print(who_wins (2 , ['poo ', 'ste ', 'sim ', 'nic ', 'luo ', 'ibr ', 'sie ', 'zhu ']))
