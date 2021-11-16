import requests, re

groupid = input('Enter Group ID: ')

r = requests.get(f'https://groups.roblox.com/v1/groups/{groupid}').json()
group_name = r['name']
owner_name = r['owner']['username']
owner_id = r['owner']['userId']
members = r['memberCount']
entry = r['publicEntryAllowed']
created = r['shout']['created'].split('T')[0]
a = requests.get(f'https://games.roblox.com/v2/groups/{groupid}/games?accessFilter=All&sortOrder=Asc&limit=100').text
visits = re.findall('placeVisits":(.*?)},{', a)
game_amount = len(visits)
total = 0
for line in visits:
    total += int(line)
total = str(total)

print(f'Group Name: {group_name}')
print(f'Owner Name: {owner_name}')
print(f'Owner UserID: {owner_id}')
print(f'Members Amount: {members}')
print(f'Entry Allowed: {entry}')
print(f'Group Creation Date: {created}')
print(f'Total Games Amount: {game_amount}')
print(f'Total Visits: {total}')
