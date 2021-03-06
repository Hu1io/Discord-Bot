import feedparser
from bs4 import BeautifulSoup


def GetArticle():
    NewsFeed = feedparser.parse("https://www.theguardian.com/world/coronavirus-outbreak/rss")
    print('Number of RSS posts :', len(NewsFeed.entries))

    entry = NewsFeed.entries[3]  # Grabs Correct Title and Body

    # Removes HTML from the text so it is easily readable
    soup = BeautifulSoup(entry.summary)
    text = soup.get_text()

    print('Post Title :', entry.title, '\n----------\n', text, '\n----News Link----\n', entry.link)

    FinRssFeed = "**__" + entry.title + "__**\n\n" + text + '\n\n----News Link----\n' + entry.link


    return FinRssFeed