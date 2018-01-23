import json
import sys
import os


def load_from_json(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(bar_data):
    biggest_bar = max(bar_data['features'], key=lambda x:
                      x['properties']['Attributes']['SeatsCount'])
    biggest_bar_seats = biggest_bar['properties']['Attributes']['SeatsCount']
    biggest_bar_data = [biggest_bar['properties']['Attributes']['Name'],
                        biggest_bar['properties']['Attributes']['Address'],
                        'Мест:' + str(biggest_bar_seats)]
    return biggest_bar_data


def get_smallest_bar(bar_data):
    smallest_bar = min(bar_data['features'], key=lambda x:
                       x['properties']['Attributes']['SeatsCount'])
    smallest_bar_seats = smallest_bar['properties']['Attributes']['SeatsCount']
    smallest_bar_data = [smallest_bar['properties']['Attributes']['Name'],
                         smallest_bar['properties']['Attributes']['Address'],
                         'Мест:'+str(smallest_bar_seats)]
    return smallest_bar_data


def get_closest_bar(bar_data, longitude, latitude):
    closest_bar = min(bar_data['features'], key=lambda x:
                      (x['geometry']['coordinates'][0] - longitude)**2 +
                      (x['geometry']['coordinates'][1] - latitude)**2)
    closest_bar_seats = closest_bar['properties']['Attributes']['SeatsCount']
    closest_bar_data = [closest_bar['properties']['Attributes']['Name'],
                        closest_bar['properties']['Attributes']['Address'],
                        'Мест:'+str(closest_bar_seats)]
    return closest_bar_data

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Error: define file path')
        print('Usage example: python pprint_json.py <path to file>')
    else:
        if os.path.isfile(sys.argv[1]):
            bar_data = load_from_json(sys.argv[1])
            longitude = float(input('Your longitude: '))
            latitude = float(input('Your latitude: '))
            biggest_bar = get_biggest_bar(bar_data)
            smallest_bar = get_smallest_bar(bar_data)
            closest_bar = get_closest_bar(bar_data, longitude, latitude)
            print('Biggest bar: \n' + '\n'.join(biggest_bar) + '\n')
            print('Smallest bar: \n' + '\n'.join(smallest_bar) + '\n')
            print('Closest bar: \n' + '\n'.join(closest_bar))

        else:
            print('Error: No such file in directory')
