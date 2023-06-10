# Steps & Notes

Create python env and run `pip install` for `pandas` and `requests`. Maybe `json` as well.

Run `main.py`: You will be asked to enter username of the data you want to grab.

### Note about `offset`:
This was the case back in 2021. I think you can only have 100 recordings total in your favorite folder. So this note probably won't apply but will leave it just in case.
- You will need to change the `offset` if the while-loop doesn't finish in the next block. 
- Get the last `next_offset` from the print message before the request becomes unsuccessful.

### Note about `main.ipynb`: 
Old, OG file. This was created to grab data from two different users back in 2021. It will look different and might have a lot of 'overly excited comments'. Use it as a playground or for testing if needed. Otherwise, feel free to ignore it.