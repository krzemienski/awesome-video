import json

from twisted.python.util import println
import requests

def find(string):
    url = re.findall(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    return url


def insertCharacterAtPos(char, string, index, ):
    return string[:index] + '-' + string[index:]


def read_and_sanitize_metadata_contents_json():
        santized_projects = []
        contents = {}

        with open('../contents.json') as json_file:
                contents = json.load(json_file)
                for category in contents['categories']:
                        print('Category : ' + category['title'])

                        if 'description' in category:
                                print('Description: ' +
                                      category['description'])

                        print('Id: ' + category['id'])

                        if 'parent' in category:
                                print('Parent: ' + category['parent'])
                        print('')

                for project in contents['projects']:
                        santized_project = {}

                        santized_project['category'] = project['category']
                        santized_project['homepage'] = project['homepage']

                        if project['title'] != None: 
                                print('CURRENT Title : ' + project['title'])
                        if isinstance(project['category'], list):
                                 for a in project['category']:
                                        print('Category : ' + a)
                        else:
                                 print('Category : ' + project['category'])
                        
                        if project['homepage'] != None: 
                                print('URL : ' + project['homepage'])
                        if 'description' in project and project['description'] != None:
                                print('CURRENT Description: ' +
                                      project['description'])

                        url_to_get_metadata = project['homepage']

                        if 'https' in url_to_get_metadata:
                                santized_projects.append(create_project_from_raindrop(project))

                                contents['projects'] = santized_projects
                                
                        else:
                              print("NEED TO FIX HTTPS " + project['homepage'])
        with open('../contents-sanitized.json', 'w') as outfile:
                json.dump(contents, outfile, indent=4, ensure_ascii=False)
                println("wrote santized json to contents.json")


def add_new_projects():
        with open('resources.txt', 'r') as resources_file:
                resources = resources_file.readlines()
                resources_dict = []

                for line in resources:
                        cleaned_project = {}
                        resource_url = line.split(' ')                
                        if len(resource_url) > 0 and len(resource_url) > 0 and isinstance(resource_url, list) :
                                resource_url = resource_url[0]
                        print("PARSED URL" + resource_url)
                        if 'https' in resource_url:
                                try:                               
                                        metadata_from_url = get_metadata(identifier=resource_url, format='n3')
                                        cleaned_project['description'] = metadata_from_url['description']
                                        cleaned_project['title'] = metadata_from_url['title']                                          
                                        cleaned_project['hopmepage'] = resource_url
                                        cleaned_project['category'] = ''
                                        resource_description =  ''
                                        if cleaned_project['description']  != None:
                                                resource_description = cleaned_project['description'] 
                                        
                                                if resource_description.__contains__('roku'):
                                                        cleaned_project['category'] = 'roku'
                                                

                                                if cleaned_project['description'].__contains__('player'):
                                                        cleaned_project['category'] = 'players'
                                                

                                                if cleaned_project['description'].__contains__('encoding'):
                                                        cleaned_project['category'] = 'encoding'
                                                

                                                if cleaned_project['description'].__contains__('ffmpeg'):
                                                        cleaned_project['category'] = 'ffmpeg'
                                                

                                                if cleaned_project['description'].__contains__('hls'):
                                                        cleaned_project['category'] = 'hls'
                                except :
                                       print('filed parsin metadata for resource url ')
                        else: 
                                print("NEED TO FIX HTTPS " + resource_url)

                        resources_dict.append(cleaned_project)
                with open('resources.json', 'w') as outfile:
                        json.dump(resources_dict, outfile, sort_keys=True, indent=4, ensure_ascii=False)
                        println("wrote resources.json to file")        
                return resources_dict

def add_projects_from_raindrop_collection():
        url = "https://api.raindrop.io/v1/raindrops/11035632?sort=-created&page=1&perpage=1000"

        payload = {}
        headers = {
        'User-Agent': 'rn3/379 CFNetwork/1126 Darwin/19.5.0',
        'Host': 'api.raindrop.io',
        'Cookie': 'connect.sid=s%3AE6PpfChMzJaZBivrzTjbAvzip_HSSIGj.mTMUOokoewe6iBIhyrE34BZqdGzlALrUJ3mnhk%2FCBfQ; _ga=GA1.2.420119653.1585613645; __cfduid=d85eb790f0a74c61f126b3536d73535f51573300023; connect.sid=s%3AE6PpfChMzJaZBivrzTjbAvzip_HSSIGj.mTMUOokoewe6iBIhyrE34BZqdGzlALrUJ3mnhk%2FCBfQ'
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        projects_in_collection = response.json()['items']
        new_resources = []
        for project in projects_in_collection:
                new_resource = {}
                homepage = project['link']
                description = project['excerpt']
                title = project['title']
                description = description.replace(f"Contribute to {title} development by creating an account on GitHub.","")                
                new_resource['description'] = description
                new_resource['title'] = title 
                new_resource['hopmepage'] = homepage
                println(new_resource['hopmepage'])
                println(new_resource['title'])
                println(new_resource['description'])
                if len(project['tags']) > 0:
                        new_resource['category'] = project['tags']
                else:
                        new_resource['category'] = []
                new_resources.append(new_resource)
        with open('../contents-added.json', 'w') as outfile:
                json.dump(new_resources, outfile, indent=4, ensure_ascii=False)
                println("wrote santized json to contents-new.json")

def create_project_from_raindrop(current_resource):
        link_to_parse = current_resource['homepage']
        url = f"https://api.raindrop.io/v1/parse?url={link_to_parse}"

        payload = {}
        headers = {
        'User-Agent': 'extension/379 CFNetwork/1126 Darwin/19.5.0',
        'Host': 'api.raindrop.io',
        'Cookie': 'connect.sid=s%3AE6PpfChMzJaZBivrzTjbAvzip_HSSIGj.mTMUOokoewe6iBIhyrE34BZqdGzlALrUJ3mnhk%2FCBfQ; _ga=GA1.2.420119653.1585613645; __cfduid=d85eb790f0a74c61f126b3536d73535f51573300023; connect.sid=s%3AE6PpfChMzJaZBivrzTjbAvzip_HSSIGj.mTMUOokoewe6iBIhyrE34BZqdGzlALrUJ3mnhk%2FCBfQ'
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        json_response = response.json()
        if json_response['result'] == True:
                title = json_response['item']['title']
                current_resource['title'] = title
                description = json_response['item']['excerpt']
                description = description.replace(f"Contribute to {title} development by creating an account on GitHub.","")
                current_resource['description'] = description
        println(current_resource)
        return current_resource

def main():
        # First, we  sanitize the current contents
        read_and_sanitize_metadata_contents_json()
        add_projects_from_raindrop_collection()
if __name__ == "__main__":
        main()