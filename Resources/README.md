# Steps & Notes

Create python env and run `pip install` for `pandas` and `requests`. Maybe `json` as well.

Run `main.py`: You will be asked to enter username of the data you want to grab.

### Note about `offset`:
This was the case back in 2021. I think you can only have 100ish recordings total in your favorite folder. So you should be able to complete the full run and this note probably wouldn't apply. Leaving it just in case:
- You will need to change the `offset` if the while-loop doesn't finish in the next block. 
- Get the last `next_offset` from the print message before the request becomes unsuccessful.
