from itertools import islice
from youtube_comment_downloader import *
downloader = YoutubeCommentDownloader()
comments = downloader.get_comments_from_url('https://www.youtube.com/watch?v=13qTDXm12EE', sort_by=SORT_BY_POPULAR)
print(comments)
for comment in islice(comments, 5):
    print(comment)