


class ResponseProducer:
	def __init__(self, response = "Sorry I don't understand"):
		self.response = response


	def getResponse(self, lastMsg = ""):
		return self.response


	def setResponse(self, lastMsg, train = False):
		print("1self.response:")
		print(self.response)
		if train:
			self.trainModel(lastMsg)
		else:
			self.response = "Sorry I don't understand"
		print("after training:")
		print("2self.response:")
		print(self.response)


	def trainModel(self, lastMsg):
		print("place holder for actual training")
		lastMsg = lastMsg.lower().strip()
		print("lastMsg: ")
		print(lastMsg)
		if lastMsg == "<p>hi</p>":
			self.response = "hi"
		elif lastMsg == "<p>yo</p>":
			self.response = "yo"
		elif lastMsg == "<p>bye</p>":
			self.response = "bye"
		else:
			print("no match at all")
			self.response = "Sorry I don't understand"
		print("3self.response:")
		print(self.response)

