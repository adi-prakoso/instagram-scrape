from instascrape import Profile, scrape_posts
import pandas as pd
import matplotlib.pyplot as plt

# Scraping bookstore's profile
SESSIONID = '7529360293%3A29uTMTXShXULBe%3A18'
headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57",
           "cookie": f"sessionid={SESSIONID};"}
bookstore = ["bukuakik", "berdikaribook", "jualbukusastra",
             "demabuku", "paperplanebookstore", "akalbuku", "aebookstore"]
profiles = [Profile(username) for username in bookstore]
for prof in profiles:
    prof.scrape(headers=headers)

data = [prof.to_dict() for prof in profiles]
df = pd.DataFrame(data)

# Plot username vs followers
# plt.style.use("seaborn-darkgrid")
ax = plt.subplot()
ax.bar(df["username"], df["followers"])
plt.xticks(rotation=30, ha='right', fontsize=10)
plt.ylabel('followers')
plt.tight_layout()
plt.show()
# plt.savefig('bookstore_vs_followers.png')

# Plot recent posts engagements
# for prof in profiles:
# posts = prof.get_recent_posts()     #gets the 12 most recent posts
#posts_data = [post.to_dict() for post in posts]
#post_df = pd.DataFrame(posts_data)
#plt.plot(post_df.upload_date, post_df.likes, label=prof.username)
