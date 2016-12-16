#! usr/bin/env python3

first = "Joke"
second = "Fake"
third = "Normal"


site_title = "Comedy Blog Blog"

def blog_posts(title, *args, **kwargs):
    count = 0
    print("Title:", title, sep=" ")
    print("Posts:")
    for p_title, post in kwargs.items():
        print(p_title, post, args[count], sep=" --- ")
        count += 1


blog_posts(site_title, first, second, third,
           blog_1 = "Heynong man.",
           blog_2 = "Nong-Hey man.",
           blog_3 = "Hey, man.")
    
