identity =[]
name = input("What is your name: ")
clan = input("What is your clan: ").lower()
while clan not in ('stuart' or 'forbes' or 'gordon' or 'douglas'):
    clan = input("What is your clan: ").lower()

identity.append(name)
identity.append(clan)

print(identity)

