#! usr/bin/env python3


site_title = "Comedy Blog Blog"

def blog_posts(title, **kwargs):
    print("Title:", title, sep=" ")
    print("Posts:")
    for p_title, post in kwargs.items():
        print(p_title, post, sep=" --- ")


# All arguments can be thrown in and put into a "dictionary"
blog_posts(site_title, 
           blog_1 = "Heynong man.",
           blog_2 = "Nong-Hey man.",
           blog_3 = "Hey, man.")
    

