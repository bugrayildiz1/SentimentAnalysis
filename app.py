import json
import requests
import pprint


api_key = '6be098ce1f644d6abe8d914f420af088'

TRANSCRIPT_ENDPOINT = 'https://api.assemblyai.com/v2/transcript/rutxp2wyod-e574-4d82-921a-dc9994f3254b'

response = requests.get(
      TRANSCRIPT_ENDPOINT,
      headers={'authorization': api_key},
      json={
    	'audio_url': '-your-audio-url-',
        'sentiment_analysis': True
      },
)
  
response_json = response.json()
print(pprint.pprint(response_json))
