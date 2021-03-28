


class ResponseProducer:
	def __init__(self, response = "default response"):
		self.response = response


	def getResponse(self):
		return self.response


	def setResponse(self, response, train = False):
		self.response = response

		if train:
			trainModel()



	def trainModel():
		print("place holder for actual training")



