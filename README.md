# Smule: Songs List

Get a list of songs (and more) you recorded together with your favorite Smulean~

![all_songs](Images/all_songs_table.PNG)
<em><h5>Don't worry, you will get the date😂 I consider date a PII!</h5></em>

### PURPOSE

Do you have a favorite singing Smulean(s)? Well... I do! Smule doesn't have a good way to show you a list of songs you sang, and I have been wondering how many songs in total I have sung together with my favorite Smuleans!  Never would have thought that my first project outside my coding bootcamp would be for this -and it's already worth all the sweat & tears of going through the bootcamp😭

This entire project is dedicated to getting a list of songs that you sang with your favorite person in the app since the age of time🎤 <em>C'on... it can't just be me who is obsessed with this curiosity</em>🙄

Because there's a limit on the request you can make, you will not have access to Smule web for -I think- 30mins-ish? after you run the code. So, please be advised!

### TOOLS

Everything you need is in the `Resources` folder👍

- Add the username in the `config.py file` (or if you want, you can add the username directly within the code too)

- Run the code in the jupyter notebook
  - Note all the library that you should have before you run the code.

- Get a beautiful dataframe which you can export to csv -Done!🎉

### LIMITATIONS
IF after you run the first loop and you get an error in the 2nd loop (the chance is really high unfortunately):
  1. Wait about half an hour and run the 2nd loop and the rest of the code.
  1. If it still doesn't work, use the `alt.ipynb`: Make sure to not run all the code in one-go since we need that 30 min between each request. Once the 1st run and 2nd run are complete, you should have 2 csv files. Run the `alt_clean-up.ipynb` to clean-up, load & append two csv as one dataframe.
  
  <em>Yeah, I haven't figured out any way around that request limitation or why it is such a pain in the 🦄🌈...</em> 
  
  I tried adding `time.sleep(2)` and to no avail. Smule doesn't spawn a way to do a proper API request either... because no one cares! 😫😭</em>

### FINAL NOTE
I am sure many hard-core programmers already figured this out (and didn't share since I couldn't find one😔), but I created this as a 3-month-old programming toddler; hence, the OMG-excitement🤩

Oh! Crediting my [buddy](https://github.com/Dorfnox) for helped looking for the workable url and for walking through my `while` syntax with me🙌

### Update 7-MAR-2021:
- Previously, the hardcoding `offset += 25` will skip some of the records when making requests. This is fixed by having the `offset` takes the values from the data , `next_offset`.
- Updated the request and the loop code to update the user with print statement and to handle different response codes.  

### Untracked History & Update for 16-SEP-2020:
I had to trash my repo and re-created it. Previous revision history is not available, but please note the following: 
- The table has been updated to include "Invite Spawner" column.
- This update also included adding the alternative route for obtaining the table of songs if the `main.ipynb` fails to run due to request limits have been attained.