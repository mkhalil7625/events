from eventloader.eventful_events import get_event
from eventloader.database import db_config

# import json
# Create your views here.

def searchResult(x):
    # query = None
    # if 'q' in request.GET:
    #     query = request.GET.get('q')
    #     print(query)
    r = get_event(x)
    print(x)
    events_data = []
    for event in r:
        if event.get('performers') is not None:
            events={'show_id':event['id'],
                    # 'show' : event['title'],
                'artist':event['performers']['performer']['name'],
                'venue': event['venue_name'],
                'city':event['city_name'],
                'state':event['region_abbr'],
                'date': event['start_time']}
                # 'image_url': event["image"],
        events_data.append(events)
        print(events_data)

        return events_data

def load_events():
    r=searchResult('first avenue')
    for event in r:
        artist = event.get('artist')
        venue_name = event.get('venue')
        city = event.get('city')
        state = event.get('state')
        show_id = event.get('show_id')
        date = event.get('date')
        db_config.add_record(artist,venue_name,city,state,show_id,date)


load_events()