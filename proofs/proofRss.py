


# %% RSS
import feedparser
import urllib
url = "https://www.reddit.com/user/m-xames/m/uk_politics/search.rss?"
search_terms = {
    "q": "is_self:0 NOT site:(500px.com OR abload.de OR deviantart.com OR deviantart.net OR fav.me OR fbcdn.net OR flickr.com OR forgifs.com OR giphy.com OR gfycat.com OR gifsoup.com OR gyazo.com OR imageshack.us OR imgclean.com OR imgur.com OR instagr.am OR instagram.com OR mediacru.sh OR media.tumblr.com OR min.us OR minus.com OR myimghost.com OR photobucket.com OR picsarus.com OR puu.sh OR i.redd.it OR staticflickr.com OR tinypic.com OR twitpic.com)",
    "sort": "hot",
    "restrict_sr":1,
    "is_multi":1
}
query = url + urllib.parse.urlencode(search_terms)
UkPoliticsFeed = feedparser.parse(query)
for entry in UkPoliticsFeed.entries:
    print(entry["title"], "\n")

# %%
entry.keys()
# %%
