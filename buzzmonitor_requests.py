import requests
import json
from dotenv import load_dotenv
from datetime import datetime
import os
import boto3

def get_mentions_fb_ig():
    s3 = boto3.client('s3')
    load_dotenv()
    list_payloads = [
        "FACEBOOK_WALL_PAYLOAD",
        "FACEBOOK_INBOX_PAYLOAD",
        "YOUTUBE_WALL_PAYLOAD",
        "INSTAGRAM_WALL_PAYLOAD",
        "FB_IG_PAYLOAD"
        ]

    for payload in list_payloads:


        first_call = requests.post(
            url = os.getenv("URL_SCROLL"),
            data = os.getenv(payload)
        ).json()

        scroll_id = first_call['scroll_id']
        dataset = first_call['data']
        number_file = 0

        while dataset:
            string_payload = os.getenv(payload)
            payload_with_scroll_id = json.loads(string_payload)
            payload_with_scroll_id['scroll_id'] = scroll_id

            scroll_call = requests.post(
                url = os.getenv("URL_SCROLL"),
                data = json.dumps(payload_with_scroll_id)
            ).json()

            s3.put_object(
                Body=str(json.dumps(scroll_call)),
                Bucket='data-lake-brandtest',
                Key='landing/social/buzzmonitor_mentions/FACEBOOK_PAGES_WALL_DATETODAY_{}_NFILE_{}.json'.format(
                    datetime.today().strftime('%Y%m%d%H%M%S'), 
                    number_file
                    )
                )
                
            number_file = number_file + 1
            scroll_id = scroll_call['scroll_id']
            dataset = scroll_call['data']

get_mentions_fb_ig()