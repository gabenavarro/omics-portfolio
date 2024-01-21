import json

# Opening JSON file
with open('/app/assets/gcp-settings.json') as json_file:
    PORTFOLIO_JSON = json.load(json_file)

BQ_CONFIG = PORTFOLIO_JSON['bigquery']
TAG_KEY = PORTFOLIO_JSON['blog_tag']
QUERY_TAG_KEY = PORTFOLIO_JSON['query_tags']