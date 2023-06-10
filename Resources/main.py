# ### Setting up
import json
import pandas as pd
import requests

# Enter the username to get data of that user
username = input('Enter the username you wish to grab data for: ')

###### Setting up data request ######
# Building url
data_url = f'https://www.smule.com/s/profile/performance/{username}/sing?offset='

# Counter for while loop
n = 0

# Starting page for request
offset = 0 

# Create an empty list to store all the json data output
mining_list = []

# Print out what's going on..
print('Requesting and grabbing data begins...')

# Infinite loop until the list is empty (offset ran out)
while True:
    response = requests.get(f'{data_url}{offset}')
    print(f'response code: {response.status_code}')
    
    # Get out of the loop if request is unsuccessful
    if response.status_code != 200:
        print('Unsuccessful Request T^T')
        break
    
    # Continue to data request
    response_json = response.json()
    json_stuff = response_json['list']
    n += 1
    print(f'Request #{n}: Success!')
    print(f"next offset: {response_json['next_offset']}")
    
    # If the list is empty in the json data
    if not json_stuff:
        break
    
    for x in range(0,len(json_stuff)):
        mining_list.append(json_stuff[x])
        print(f'Processing record index #{offset + x}: {offset}, #{x}')

    offset = response_json['next_offset']
    
    # Get out of the while loop since there is no more data to request
    if offset == -1:
        print(f'No more records to be processed. Total Loops: {n}')
        break

print('Commencing data cleaning...')

##### Data Cleaning #####
# Mapped all the wanted field from the data + rename field
def create_song_list(track):
    key = track['key']
    title = track['title']
    artist = track['artist']
    date = track['created_at']
    inviter = track['performed_by']
    recording_base_url = 'https://www.smule.com'
    recording_url = recording_base_url + track['web_url']
    
    return {
        'key': key,
        'title': title,
        'artist': artist,
        'date_created': date,
        'username': inviter,
        'url': recording_url
    }
    
# Use map to give a list iterator
song_list_iterator = map(create_song_list, mining_list)
# Turn iterator into a list
data_list = list(song_list_iterator)

# To dataframe and transform date string
data_df = pd.DataFrame(data_list)
data_df['date_created'] = data_df['date_created'].str.split('T').str[0]

# Get a count of all the rows
record_num = len(data_df)
print(f'{username} has a total of {record_num} records.')

# Save cleaned to csv
data_df.to_csv('data.csv', encoding='utf_8_sig', index=False)
print('Data has been exported as csv file.')




