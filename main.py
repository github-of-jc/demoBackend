
from stream_chat import StreamChat 
from time import time, sleep
import datetime
from response import ResponseProducer

 
# instantiate your stream client using the API key and secret 
# the secret is only used server side and gives you full access to the API 


def lastMsgIsFromUser(resp, user_id):
	respId = resp['messages'][-1]['user']['id']
	print("resp: user: %s: %s" % (respId, user_id))
	if respId == user_id:
		return True
	else:
		return False

user_id = 'Jiayichen321'
user_id2 = 'Jiayichen2'
bot_userId = 'iamrobot'

client = StreamChat(api_key="<key>", api_secret="<secret>") 
user_token = client.create_token(user_id) 
bot_token = client.create_token(bot_userId) 

# next, hand this token to the client in your in your login or registration response 


print("token: %s" % user_token) 


updateUsersRes = client.update_users([{"id": user_id, "role": "admin", "mycustomfield": "123"}])
updateUsersRes = client.update_users([{"id": user_id2, "role": "admin", "mycustomfield": "123"}])
updateUsersRes = client.update_users([{"id": bot_userId, "role": "admin", "mycustomfield": "123"}])



print("updateUsersRes: %s" % updateUsersRes)

getChannelRes = client.query_channels(None)

print("getChannelRes: %s" % getChannelRes)
for item in getChannelRes:
	print("=== \n %s" % item)
	for a in getChannelRes[item]:
		print("====== \n %s" % a)


print("creating a channel")

channel = client.channel("messaging", "kung-fu")
print("update the channel name to kfchannel")
channel.update({"name": "kfchannel", "image": "image url", "mycustomfield": "123"})

# response is produced here
responseProducer = ResponseProducer()

print("channel: %s" % channel)


res = channel.add_members(['Jiayichen321', "Jiayichen2", "iamrobot"])

print("after adding members: %s" % res)

message = { 
    "text": ' I told them I was pesca-pescatarian. Which is one who eats solely fish who eat other fish.', 
    "attachments": [{ 
        "type": 'image', 
        "asset_url": 'https://bit.ly/2K74TaG', 
        "thumb_url": 'https://bit.ly/2Uumxti', 
        "myCustomField": 123 
    }], 
   "anotherCustomField": 234, 
} 

# channel.send_message(message, user_id)

# channel.send_message(message, user_id2)




last_message_at = '2000-03-27T23:55:19.240795Z'
# date_time_str2 = '2021-03-27T23:56:19.240795Z'
# date_time_str3 = '2021-03-27T23:54:19.240795Z'


date_time_obj = datetime.datetime.strptime(last_message_at, "%Y-%m-%dT%H:%M:%S.%fZ")
# date_time_obj2 = datetime.datetime.strptime(date_time_str2, "%Y-%m-%dT%H:%M:%S.%fZ")
# date_time_obj3 = datetime.datetime.strptime(date_time_str3, "%Y-%m-%dT%H:%M:%S.%fZ")


# print('Date:', date_time_obj.date())
# print('Time:', date_time_obj.time())
# print('Date-time:', date_time_obj)
# print("  ")
# print(date_time_obj > date_time_obj2)
# print(date_time_obj2 > date_time_obj3)
# print(date_time_obj > date_time_obj3)


response = ""

while True:
	sleep(5)
	# thing to run
	print("\nquerying")
	# query in most recent order
	resp = channel.query()
	new_last_message_at = resp['channel']['last_message_at']
	new_date_time_obj = datetime.datetime.strptime(new_last_message_at, "%Y-%m-%dT%H:%M:%S.%fZ")
	# print("\n\nres from querying")
	if new_date_time_obj > date_time_obj and not lastMsgIsFromUser(resp, bot_userId):
		print("got new msg")
		date_time_obj = new_date_time_obj
		print("new time: %s" % new_date_time_obj)
		print(resp['messages'][-1]['html'])
		print("send a response to the sender:")
		responseText = responseProducer.getResponse()
		respMessage = { 
			"text": responseText, 
			"attachments": [{ 
				"type": 'image', 
				"asset_url": 'https://bit.ly/2K74TaG', 
				"thumb_url": 'https://bit.ly/2Uumxti', 
				"myCustomField": 123 
				}], 
			"anotherCustomField": 234, 
		} 
		print("response: %s" % respMessage)
		resp = channel.send_message(respMessage, bot_userId)
		print("after sending response: %s" % resp)
	else:
		print("no news")







# import asyncio
# from stream_chat import StreamChatAsync


# async def main():

# 	user_id = 'Jiayichen321'
# 	user_name = 'Jiayichen321_uname'
# 	async with StreamChatAsync(api_key="d9uqr3rqmy4k", api_secret="d8cz5d9hvck37nazxypdb42b8qk9c8hgghb4zwvg6y97342jrdxsnaxvn3pkdmw7") as chat:

# 		print("chat:")
# 		print(chat)
# 		# add a user
# 		await chat.update_user({"id": user_id, "name": user_name})
# 		print("chat: ")


# 		# create a channel about kung-fu
# 		channel = chat.channel("messaging", "kung-fu")
# 		print(channel)
# 		await channel.create(user_id)

# 		# add a first message to the channel
# 		await channel.send_message({"text": "AMA about kung-fu"}, user_id)


# if __name__ == '__main__':
# 	loop = asyncio.get_event_loop()
# 	try:
# 		loop.run_until_complete(main())
# 	finally:
# 		loop.run_until_complete(loop.shutdown_asyncgens())
