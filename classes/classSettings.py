from .keys import weatherKey, postCode


class Settings():
    WEATHER = {
        "api_key": weatherKey,
        "base_url": "https://api.openweathermap.org/data/2.5/onecall?",
        "lat": "51.5149",
        "lon": "0.3019",
        "exclude": "minutely,hourly",
        "units": "metric",
        "desired_fields": ["dt", "feels_like", "weather"]
    }

    CLOCK = {
        "dateFormat": "%Y-%m-%d",
        "timeFormat": "%H:%M:%S"
    }

    BINS = {
        "baseUrl": "https://www.ealing.gov.uk/site/custom_scripts/waste_collection/waste_collection.aspx",
        "postCode": postCode,
        "binsOfInterest": ["BLUE RECYCLING WHEELIE BIN", "FOOD BOX", "BLACK RUBBISH WHEELIE BIN"]
    }

    RSS = {
        "baseUrl": "https://www.reddit.com/user/m-xames/m/uk_politics/search.rss?",
        "searchTerms": {
            "q": "is_self:0 NOT site:(500px.com OR abload.de OR deviantart.com OR deviantart.net OR fav.me OR fbcdn.net OR flickr.com OR forgifs.com OR giphy.com OR gfycat.com OR gifsoup.com OR gyazo.com OR imageshack.us OR imgclean.com OR imgur.com OR instagr.am OR instagram.com OR mediacru.sh OR media.tumblr.com OR min.us OR minus.com OR myimghost.com OR photobucket.com OR picsarus.com OR puu.sh OR i.redd.it OR staticflickr.com OR tinypic.com OR twitpic.com)",
            "sort": "hot",
            "restrict_sr":1,
            "is_multi":1},
        "displayNumberOfItems": 3
    }