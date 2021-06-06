from .keys import weatherKey, postCode


class Settings():
    ORCHESTRATOR = {
        "refresh": "second" # ["second", "minute"]
    }

    LOGGER = {
        "level": "INFO",
        "format": "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        "filename": "./logs/main.log"
    }

    BINS = {
        "baseUrl": "https://www.ealing.gov.uk/site/custom_scripts/waste_collection/waste_collection.aspx",
        "postCode": postCode,
        "binsOfInterest": ["BLUE RECYCLING WHEELIE BIN", "FOOD BOX", "BLACK RUBBISH WHEELIE BIN"]
    }

    CLOCK = {
        "dateFormat": "%Y-%m-%d",
        "timeFormat": "%H:%M:%S"
    }

    FOOTBALL = {
        "baseUrl": "https://www.espn.co.uk/football/fixtures",
        "league": "eng.2",
        "teamsOfInterest": "BRN"
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

    WEATHER = {
        "apiKey": weatherKey,
        "baseUrl": "https://api.openweathermap.org/data/2.5/onecall?",
        "lat": "51.5149",
        "lon": "0.3019",
        "exclude": "minutely,hourly",
        "units": "metric",
        "desiredFields": ["dt", "feels_like", "weather"],
        "imgUrl": "http://openweathermap.org/img/w/{imgCode}.png"
    }