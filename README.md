# impact-hackathon-2018

The steps to reproduce the full Hackathon which was done at Coveo Impact 2018.

## Indexing

We indexed a Sitemap and a Youtube source.

### Web site/Sitemap

* Create a new source, using a Sitemap connector: [Website](https://retail-static.coveodemo.com/sitemap.xml).
* Add fields:
    * mybrand, String, Facet
    * mycategory, String, Facet
    * myprice, Decimal
    * myrating, Int 32
    * allmetadatavalues, String (NO FACET, used for debugging metadata values)
* Add Mappings (on your source), these are coming from META header tags from the page:
    * myprice: %[productlistprice]
    * mybrand: %[productbrandname]
* Add Extension script to only index '/Shop/' items, called: OnlyShop.
    * Use [OnlyShop.py](Indexing/OnlyShop.py) as source
* Add Extension script to debug metadata values, called: Trace.
    * Use [Trace.py](Indexing/Trace.py) as source
* Add Extension script to get Category, called: GetCategoryAndOthers.
    * Use [GetCategoryAndOthers.py](Indexing/GetCategoryAndOthers.py) as source
* Assign the Extension script OnlyShop as a pre-conversion script to your source.
* Assign the Extension script Trace as a post-conversion script to your source.
* Assign the Extension script GetCategoryAndOthers as a post-conversion script to your source.

The configuration of the Sitemap should be: [Sitemap.json](Indexing/Sitemap.json).
Full configuration: [SitemapComplete.json](Indexing/SitemapComplete.json).

### Youtube
* Create a new source, using a Youtube connector: [Youtube](https://www.youtube.com/channel/UCrX0lGAJ3Q-fHiFsOb9hvHw).
* Disable the Refresh Schedule.

Full configuration: [YoutubeComplete.json](Indexing/YoutubeComplete.json).

## UI

Create a search page.
Insert the [HTML](UI/search.html) into it.

## Chatbot
Restore the [ChatBot](ChatBot/Agent.zip) in your Chatbot agent. That will contain all Intents and Entities.
The Fullfillment must be manually imported.

### Important
* Make sure to use a proper Google account (some google accounts are restricted).
* Make sure to link a Billing Profile to your Agent (because we are calling external services).

### Fullfillment
Enable Inline Editor for the Fullfillment. 
Insert into [package.json](ChatBot/package.json).
Insert into [index.js](ChatBot/index.js).

To make it work, first make sure to change the proper URL and insert your API KEY in index.js.
```javascript
const SEARCH_ENDPOINT = 'https://platform.cloud.coveo.com/rest/search/v2/';
const API_KEY = 'APIKEY'
```

In the bottom of the index.js file there is the definition of the intents:
```javascript
app.intent('Get Latest Products', specsHelper);
app.intent('Get products in stock', specsHelper);
app.intent('Get high rated products', specsHelper);
app.intent('Get products from brand', specsHelper);
app.intent('Get products from brand - in stock', specsHelper);
app.intent('Get products from brand - rated', specsHelper);
app.intent('Get products from brand - price', specsHelper);
app.intent('SpecsHelper - videos', specsHelper);
```

## Authors

* Jerome Devost (jdevost@coveo.com)
* Wim Nijmeijer (wnijmeijer@coveo.com)
