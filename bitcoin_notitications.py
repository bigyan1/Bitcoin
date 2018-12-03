import requests
import time
from datetime import datetime

BITCOIN_API_URL = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"
IFTTT_WEBHOOKS_URL = "https://maker.ifttt.com/trigger/test_event/with/key/di2S3nOFhqWctR4Iu7EKA1"

def get_latest_bitcoin_price():
	response = requests.get(BITCOIN_API_URL)
	response_json = response.json()
	return float(response_json[0]['price_usd'])
def post_ifttt_webhook(event, value):
	data = {'Value1' : value}
	ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)
	requests.post(ifttt_event_url, json = data)
def main():
	pass

if __name__ == '__main__':
	main()
