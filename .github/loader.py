
from twisted.python.util import println
import json
from unicontent.extractors import get_metadata


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
                        
                        url_to_get_metadata =  project['homepage']

                        metadata_from_url= get_metadata(identifier=url_to_get_metadata, format='n3')
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
                        
        with open('../contents-new.json', 'w') as outfile:
                json.dump(contents, outfile, indent=4, ensure_ascii=False)
                println("wrote santized json to contents.json")             

def add_new_projects():
        with open('resources-1216.txt', 'r') as resources_file:
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
                                
                                url_to_get_metadata =  resource_nice['homepage']

                                data = get_metadata(identifier=url_to_get_metadata, format='n3')
                                resource_nice['metadata'] = data
                                resources_dict.append(resource_nice)
                        except Exception as exception:
                                print("could not get a [ in the given line]")
                                println(line)
        
        with open('resources-1217.json', 'w') as outfile:
            json.dump(resources_dict, outfile, sort_keys=True, indent=4, ensure_ascii=False)
            println("wrote json to file")        
        
def main():
    # First, we  sanitize the current contents
    read_and_sanitize_metadata_contents_json()
          
    
    
if __name__ == "__main__":
    main()