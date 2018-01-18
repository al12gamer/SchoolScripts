1. Go into /audio-scraper-master
2. In Terminal: pip install audioscrape (if you don't have it)
3. Navigate back into FINAL folder
4. Audioscrape for whatever songs you want and wait about five minutes (you
shouldn't have to wait longer than that- if you do, just ctrl+c)
	Audioscrape usage: audioscrape "mysong"
5. After the audioscraper runs, run ScraperSort.py and most
music-player-readable audiofiles should be collected into a "sounds" folder

NOTE: MY SCRIPT WAS ONLY TESTED TO WORK ON CENTOS 64 BIT AND 64BIT ARCH LINUX
I originally had a longer, 30-line bit of code to handle this, but scrapped
it once I found out about shutil and os utilities in python.
If this doesn't work, please email me about it at seibenab@mail.uc.edu
