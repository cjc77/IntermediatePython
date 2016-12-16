#! usr/bin/env python3

# *args turn all input into a list

blog_1 = "Heynong man."
blog_2 = "Nong-Hey man."
blog_3 = "Hey, man."

site_title = "Comedy Blog Blog"

def blog_posts(title, *args):
    print("Title:", title, sep=" ")
    print("Posts:")
    for post in args:
        print(post)


# All arguments can be thrown in and put into a "list"
blog_posts(site_title, blog_1, blog_2, blog_3)
    

