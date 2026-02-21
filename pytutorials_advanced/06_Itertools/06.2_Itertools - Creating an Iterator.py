#example: iterate through a sentence in which the values returned will be the words in that sentence


'''Solving through Class'''
def example1():

	class Sentence:

		def __init__(self, sentence):
			self.sentence = sentence
			#class variables
			self.index = 0
			self.words = self.sentence.split()

		def __iter__(self):
			return self

		def __next__(self):
			if self.index >= len(self.words):
				raise StopIteration

			index = self.index
			self.index += 1
			#self.index incremented after it is assigned to index, so index still retains the value before it is incremented
			return self.words[index]

	test_sentence = Sentence('test sentence for class Sentence')
	#basically casts the instance into a list (iterable). however this object is also an iterator since it has dunder next.

	# print(next(test_sentence))
	# print(next(test_sentence))
	# print(next(test_sentence))
	# print(next(test_sentence))
	# print(next(test_sentence)) 		#or

	for word in test_sentence:
		print(word)

#example1()


'''Solving through Generator Functions (more common)'''
def example2():

	def Sentence(string):

		words = string.split()
		index = 0

		while index < len(words):
			yield words[index]
			index += 1

		'''
		for word in string.split():
			print(word)
		'''


	test_sentence = 'test sentence for class Sentence'
	x = Sentence(test_sentence)

	# print(next(x))
	# print(next(x))
	# print(next(x))
	# print(next(x))
	# print(next(x)) 		#or

	for i in x:
		print(i)

example2()