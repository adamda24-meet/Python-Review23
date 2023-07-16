def create_youtube_video(title,description):
	newvid={"title":title,"description":description,"likes":0,"dislikes":0,"comments":{"username":""}}
	return newvid
def like(newvid):
	if "likes" in newvid:
		newvid["likes"]+=1
	return newvid
def dislike(newvid):
	if "dislikes" in newvid:
		newvid["dislikes"]+=1
	return newvid
def add_comment(youtubevideo,username,comment_text):
	youtubevideo["comments"][username]=comment_text
	return youtubevideo

create_youtube_video("lol","double lol")
like(exa)
dislike(exa)
add_comment(exa,"h","h")
for i in range(495)
like(exa)


