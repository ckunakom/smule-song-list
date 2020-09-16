# Smule: Songs List

Get a list of songs (and more) you recorded together with your favorite Smulean~

![all_songs](Images/all_songs_table.PNG)
<em>Don't worry, you will get the date😂 I consider date a PII!</em>


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

IF after you run the first loop and you get an error in the 2nd loop (the chance is really high unfortunately):
  1. Wait about half an hour and run the 2nd loop 
  1. Export the csv of the first loop and rerun the notebook next time and export another csv. Append two csv, sort by date (if you want) and reset the index...
  
  <em>Yeah, I haven't figured out any way around that yet or why. I tried adding `time.sleep(2)` and to no avail😅 Smule doesn't spawn a way to do API request either😫</em>



Note: I am sure many hard-core programmers already figured this out (and didn't share since I couldn't find one😔), but I created this as a 3-month-old programming toddler; hence, the OMG-excitement🤩

Oh! Crediting my [buddy](https://github.com/Dorfnox) for helped looking for the workable url and for walking through my `while` syntax with me🙌