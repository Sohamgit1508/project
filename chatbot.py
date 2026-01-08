print("What's your name?:")
name = input()
print(f'hello,{name!} welcome to the Soham Chatbot!')
print("How was your day? good/bad")
mood = input()
if mood == "good":
    print("That's great!! hope your day shines as bright as the sun!!")
elif mood == "bad":
    print("i am sorry to hear that😔,hope your day gets better:)")
else:
    print("It's ok, if you don't want to share it with me!!")