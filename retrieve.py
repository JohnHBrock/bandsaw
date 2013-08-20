import csv
import datetime
import requests


def get_data(user_id):
    url = 'https://app.mybasis.com/api/v1/chart/{0}.json?summary=true&interval=60&units=ms&start_date=2013-08-19&start_offset=-10800&end_offset=10800&heartrate=true&steps=true&calories=true&gsr=true&skin_temp=true&air_temp=true&bodystates=true'.format(user_id)
    return requests.get(url).json()


def output_to_csv(json):
    """Takes JSON and flattens into CSVs."""
    with open('data.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['timestamp', 'skin_temp', 'air_temp', 'heartrate', 'steps', 'gsr', 'calories'])
        for i in range((json['endtime'] - json['starttime']) / json['interval']):
            unix_time_utc = json['starttime'] + i*json['interval']
            
            skin_temp = json['metrics']['skin_temp']['values'][i]
            air_temp = json['metrics']['air_temp']['values'][i]
            heartrate = json['metrics']['heartrate']['values'][i]
            steps = json['metrics']['steps']['values'][i]
            gsr = json['metrics']['gsr']['values'][i]
            calories = json['metrics']['calories']['values'][i]

            timestamp = datetime.datetime.utcfromtimestamp(unix_time_utc)
            writer.writerow([timestamp, skin_temp, air_temp, heartrate, steps, gsr, calories])
