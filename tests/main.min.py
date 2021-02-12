_D=' (Number only)'
_C=' Options: \n'
_B='Press any key to exit...'
_A=True
import os,sys
os.system('cls'if os.name=='nt'else'clear')
api_id=3367796
api_hash='caa1bff56bb93387d2496fc6024256c1'
def print_msg_time(message):print('['+Fore.CYAN+f"{datetime.now().strftime('%H:%M:%S')}"+Fore.RESET+f"] {message}")
def get_response(url,method='GET'):response=requests.request(method,url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'},timeout=15);text_response=response.text;status_code=response.status_code;return[status_code,text_response]
def number_check():
	if len(sys.argv)<2:print('Usage: python main.py phone_number');print('-> Input number in international format (example: +639162995600)\n');e=input(_B);exit(1)
number_check()
from modules import *
color_ama(autoreset=_A)
print(Fore.MAGENTA+'\t\t__      _____ _    ___ ___  __  __ ___ ')
print(Fore.MAGENTA+'\t\t\\ \\    / / __| |  / __/ _ \\|  \\/  | __|')
print(Fore.MAGENTA+'\t\t \\ \\/\\/ /| _|| |_| (_| (_) | |\\/| | _| ')
print(Fore.MAGENTA+'\t\t  \\_/\\_/ |___|____\\___\\___/|_|  |_|___|\n'+Fore.RESET)
print(Fore.RED+'   -                   Click Bot Monster v1.0                -'+Fore.RESET)
print('')
print(Fore.YELLOW+'   -               Git :'+Fore.RED+' https://github.com/toutpuissantged/'+Fore.WHITE+''+Fore.YELLOW+'             -')
print('\n\t\t Earn money using telegram bot.\n')
print(_C)
option=['Dogecoin_click_bot','Litecoin_click_bot','BCH_clickbot','Zcash_click_bot','Bitcoinclick_bot']
for (number,letter) in enumerate(option):print('\t',number,letter)
ask=int(input('\t\n\tWhich bot do you want to run?'+Fore.RED+_D+Fore.RESET+':'))
answer=option[ask]
url_channel=answer
async def main():
	I='You earned';H='/visit';G='Sending /visit command';F='Sorry, there are no new ads available\n';E='no new ads available';D='Current account:';C='session/';B=' performed';A='session';print(Fore.GREEN+url_channel+Fore.RESET+' selected.\n');print('\t\tDogeClick Bot Channel Actions Menu.\n');print(_C);action=['Visit','Message','Join']
	for (number,letter) in enumerate(action):print('\t',number,letter)
	ask_action=int(input("\t\n\tWhat bot's action do you want to perform?"+Fore.RED+_D+Fore.RESET+':'));answer=action[ask_action];bot_action=answer
	if answer==action[0]:
		print(action[0]+B);phone_number=sys.argv[1]
		if not os.path.exists(A):os.mkdir(A)
		client=TelegramClient(C+phone_number,api_id,api_hash);await client.start(phone_number);me=await client.get_me();print(D+Fore.CYAN+f"{me.first_name}({me.username})\n"+Fore.RESET);print_msg_time(Fore.YELLOW+G+Fore.RESET);await client.send_message(url_channel,H)
		@client.on(events.NewMessage(chats=url_channel,incoming=_A))
		async def visit_ads(event):
			A=None;original_update=event.original_update
			if type(original_update)is not UpdateShortMessage:
				if hasattr(original_update.message,'reply_markup')and type(original_update.message.reply_markup)is ReplyInlineMarkup:
					url=event.original_update.message.reply_markup.rows[0].buttons[0].url
					if url is not A:
						print_msg_time('Visiting website...');status_code,text_response=get_response(url);parse_data=BeautifulSoup(text_response,'html.parser');captcha=parse_data.find('div',{'class':'g-recaptcha'})
						if captcha is not A:print_msg_time(Fore.RED+'Captcha detected!'+Fore.RED+' Skipping ads...\n');await client(GetBotCallbackAnswerRequest(peer=url_channel,msg_id=event.message.id,data=event.message.reply_markup.rows[1].buttons[1].data))
		@client.on(events.NewMessage(chats=url_channel,incoming=_A))
		async def wait_hours(event):
			message=event.raw_text
			if I in message:print_msg_time(Fore.GREEN+f"{message}"+Fore.RESET)
		@client.on(events.NewMessage(chats=url_channel,incoming=_A))
		async def manual_skip(event):
			message=event.raw_text
			if'Skipping task...'in message:print_msg_time(Fore.YELLOW+f"{message}"+Fore.RESET)
		@client.on(events.NewMessage(chats=url_channel,incoming=_A))
		async def no_valid(event):
			message=event.raw_text
			if'Sorry, that task is no longer valid'in message:print_msg_time(Fore.RED+'Sorry, that task is no longer valid.'+Fore.RESET);print_msg_time(Fore.YELLOW+G+Fore.RESET);await client.send_message(url_channel,H)
		@client.on(events.NewMessage(chats=url_channel,incoming=_A))
		async def no_ads(event):
			message=event.raw_text
			if E in message:print_msg_time(Fore.RED+F+Fore.RESET);e=input(_B);exit(1)
	elif answer==action[1]:
		print(action[1]+B);phone_number=sys.argv[1]
		if not os.path.exists(A):os.mkdir(A)
		client=TelegramClient(C+phone_number,api_id,api_hash);await client.start(phone_number);me=await client.get_me();print(D+Fore.CYAN+f"{me.first_name}({me.username})\n"+Fore.RESET);print_msg_time('Sending /bots command');await client.send_message(url_channel,'/bots')
		@client.on(events.NewMessage(chats=url_channel,incoming=_A))
		async def join_start(event):
			A='?';message=event.raw_text
			if'Forward a message to'in message:
				channel_msg=event.original_update.message.reply_markup.rows[0].buttons[0].url;print_msg_time(f"URL @{channel_msg}")
				if A in channel_msg:channel_name=re.search('t.me\\/(.*?)\\?',channel_msg).group(1)
				elif A not in channel_msg:channel_name=re.search('t.me\\/(.*?)',channel_msg).group(1)
				print_msg_time(f"Messaging @{channel_name}...");await client.send_message(channel_name,'/start')
				@client.on(events.NewMessage(chats=channel_name,incoming=_A))
				async def earned_amount(event):msg_id=event.message.id,;await client.forward_messages(url_channel,msg_id,channel_name)
		@client.on(events.NewMessage(chats=url_channel,incoming=_A))
		async def earned_amount(event):
			message=event.raw_text
			if I in message:print_msg_time(Fore.GREEN+event.raw_text+'\n'+Fore.RESET)
		@client.on(events.NewMessage(chats=url_channel,incoming=_A))
		async def no_ads(event):
			message=event.raw_text
			if E in message:print_msg_time(Fore.RED+F+Fore.RESET);e=input(_B);exit(1)
	elif answer==action[2]:
		print(action[2]+B);phone_number=sys.argv[1]
		if not os.path.exists(A):os.mkdir(A)
		client=TelegramClient(C+phone_number,api_id,api_hash);await client.start(phone_number);me=await client.get_me();print(D+Fore.CYAN+f"{me.first_name}({me.username})\n"+Fore.RESET);print_msg_time('Sending /join command');await client.send_message(url_channel,'/join')
		@client.on(events.NewMessage(chats=url_channel,incoming=_A))
		async def join_start(event):
			message=event.raw_text
			if'You must join'in message:channel_name=re.search('You must join @(.*?) to earn',message).group(1);print_msg_time(f"Joining @{channel_name}...");await client(JoinChannelRequest(channel_name));print_msg_time(f"Verifying...");await client(GetBotCallbackAnswerRequest(peer=url_channel,msg_id=event.message.id,data=event.message.reply_markup.rows[0].buttons[1].data))
		@client.on(events.NewMessage(chats=url_channel,incoming=_A))
		async def wait_hours(event):
			message=event.raw_text
			if'You must stay'in message:waiting_hours=re.search('at least (.*?) to earn',message).group(1);print_msg_time(Fore.GREEN+f"Success! Please wait {waiting_hours} to earn reward\n"+Fore.RESET)
		@client.on(events.NewMessage(chats=url_channel,incoming=_A))
		async def no_ads(event):
			message=event.raw_text
			if E in message:print_msg_time(Fore.RED+F+Fore.RESET);e=input(_B);exit(1)
	else:print('You insert nothing which me no action. Exit..');exit
	await client.run_until_disconnected()
asyncio.get_event_loop().run_until_complete(main())