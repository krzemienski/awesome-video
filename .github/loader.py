
from twisted.python.util import println
import json


def add_to_contents():
    with open('data.txt') as json_file:
        data = json.load(json_file)
        for p in data['people']:
            print('Name: ' + p['name'])
            print('Website: ' + p['website'])
            print('From: ' + p['from'])
            print('')

def main():
    # First, we load the current README into memory as an array of lines
    with open('resources-1214.txt', 'r') as resources_file:
        resources = resources_file.readlines()
        resources_dict = []

        for line in resources:
            resource_nice = {}
            try:
                split_line = line.split(']')
                resource_description = split_line[0]
                resource_link = split_line[1]

                println( resource_description)
                println (resource_link)

                resource_nice['homepage'] = resource_link.replace("(", "").replace(")","").replace("\n", "").replace("\"", "").strip()
                resource_nice['title'] = resource_description.replace("[", "").replace("\n", "").replace("\"", "").strip()
                resource_nice["description"] = ''
                resource_description = resource_nice['title'].lower()

                if resource_description.__contains__('roku'):
                        resource_nice['category'] = 'roku'
                else:
                        resource_nice['category'] = ''

                if resource_description.__contains__('player'):
                        resource_nice['category'] = 'players'
                else:
                        resource_nice['category'] = ''

                if resource_description.__contains__('encoding'):
                        resource_nice['category'] = 'encoding'
                else:
                        resource_nice['category'] = ''

                if resource_description.__contains__('ffmpeg'):
                        resource_nice['category'] = 'ffmpeg'
                else:
                        resource_nice['category'] = ''

                if resource_description.__contains__('hls'):
                        resource_nice['category'] = 'hls'
                else:
                        resource_nice['category'] = ''
                
                resources_dict.append(resource_nice)
            except Exception as exception:
                print("could not get a [ in the given line]")
                println(line)
        
        with open('resources-1214.json', 'w') as outfile:
            json.dump(resources_dict, outfile, sort_keys=True, indent=4, ensure_ascii=False)
            println("wrote json to file")
    
if __name__ == "__main__":
    main()