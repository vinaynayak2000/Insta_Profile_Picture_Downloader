import instaloader      #pip install instaloader

d = instaloader.Instaloader() 

profile_Name = 'virat.kohli'     #username of the profile whose profile picture is needed .
d.download_profile(profile_Name,profile_pic_only=True)
