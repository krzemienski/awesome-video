
import json

from twisted.python.util import println
import re
from unicontent.extractors import get_metadata

def find(string): 
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)    
    return url 

def insertCharacterAtPos(char,string, index, ):
    return string[:index] + '-' + string[index:]

def read_and_sanitize_metadata_contents_json():
        santized_projects = []     
        contents = {}
        
        with open('../contents.json') as json_file:
                contents = json.load(json_file)
                for category in contents['categories']:
                        print('Category : ' + category['title'])
                        
                        if 'description' in category:
                                print('Description: ' + category['description'])
                                
                        print('Id: ' + category['id'])
                        
                        if 'parent' in category:
                                print('Parent: ' + category['parent'])
                        print('')
                
                for project in contents['projects']:
                        santized_project = {}
                
                        santized_project['category'] = project['category']
                        santized_project['homepage'] = project['homepage']
                        
                        print('CURRENT Title : ' + project['title'])
                        if isinstance(project['category'] , list):
                                 for a in project['category']:
                                        print('Category : ' + a)
                        else:
                                 print('Category : ' + project['category'])
                       
                        print('URL : ' + project['homepage'])
                        if 'description' in project:
                                print('CURRENT Description: ' + project['description'])
                       
                        url_to_get_metadata = project['homepage']
                        
                        if 'https' in url_to_get_metadata:                                
                                metadata_from_url = get_metadata(identifier=url_to_get_metadata, format='n3')
                                santized_project['description'] = metadata_from_url['description']
                                santized_project['title'] = metadata_from_url['title']            
                                santized_projects.append(santized_project)
                                
                                contents['projects'] = santized_projects
                                for project in contents['projects']:
                                        if 'title' in project and project['title'] != None:
                                                print('NEW Title : ' + project['title'])
                                        if isinstance(project['category'] , list):
                                                for a in project['category']:
                                                        print('Category : ' + a)
                                        else:
                                                print('Category : ' + project['category'])
                                                
                                        print('URL : ' + project['homepage'])
                                        if 'description' in project and project['description'] != None:
                                                print('NEW Description: ' + project['description'])
                        else: 
                              print("NEED TO FIX HTTPS " + project['homepage'])
        with open('../contents-new.json', 'w') as outfile:
                json.dump(contents, outfile, indent=4, ensure_ascii=False)
                println("wrote santized json to contents.json")             

def add_new_projects():
        with open('resources.txt', 'r') as resources_file:
                resources = resources_file.readlines()
                resources_dict = []

                for line in resources:
                        santized_project = {}
                        resource_url = find(line)
                        
                        print("PARSED URL" + resource_url) 
                        
                        if 'https' in resource_url:                                
                                metadata_from_url = get_metadata(identifier=resource_url, format='n3')
                                santized_project['description'] = metadata_from_url['description']
                                santized_project['title'] = metadata_from_url['title']                                          
                                santized_project['hopmepage'] = resource_url
                                santized_project['category'] = ''
                                
                                if santized_project['description'].__contains__('roku'):
                                       santized_project['category'] = 'roku'
                                

                                if santized_project['description'].__contains__('player'):
                                        santized_project['category'] = 'players'
                               

                                if santized_project['description'].__contains__('encoding'):
                                        santized_project['category'] = 'encoding'
                               

                                if santized_project['description'].__contains__('ffmpeg'):
                                        santized_project['category'] = 'ffmpeg'
                              

                                if santized_project['description'].__contains__('hls'):
                                        santized_project['category'] = 'hls'
                                

                        else:
                              print("NEED TO FIX HTTPS " + resource_url)
                        
                        resources_dict.append(santized_project)
                        with open('resources.json', 'w') as outfile:
                                json.dump(resources_dict, outfile, sort_keys=True, indent=4, ensure_ascii=False)
                                println("wrote resources.json to file")        
                        return resources_dict
        
        
        
def main():
# First, we  sanitize the current contents
        read_and_sanitize_metadata_contents_json()
        add_new_projects()


if __name__ == "__main__":
        main()
