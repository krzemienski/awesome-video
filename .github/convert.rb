README = 'README.md'
CONTENTS = 'contents.json'

def get_json()
    require 'json'
    JSON.parse(File.read CONTENTS)
end

def output_linux(tags)
  return '' if tags.nil?
  return ':penguin: ' if tags.include? 'linux'
  ''
end

def output_projects(projects, category_id)
  output = ''
  projects.select { |project| project['category'] == category_id }
    .sort_by { |project| project['title'] }
    .each do |project|
    output << "* [#{project['title'].force_encoding('utf-8')}](#{project['homepage']}) #{output_linux project['tags']} - #{project['description']}\n"
  end
  output
end

# Returns true if the category has any projects
def has_projects(projects, category_id)
  projects.any? { |project| project['category'] == category_id }
end

# Returns true if the category or any of its subcategories have projects
def has_projects_recursive(projects, categories, category_id)
  return true if has_projects(projects, category_id)
  
  # Check if any children have projects
  children = categories.select { |category| category['parent'] == category_id }
  children.each do |child|
    return true if has_projects_recursive(projects, categories, child['id'])
  end
  
  return false
end

def output_content_category(category, indent)
  output = "\n"

  for i in 1..indent
    output << '#'
  end

  output << " #{category['title']}\n"
  output << "*#{category['description']}*\n" unless category['description'].nil?
  output << "[back to top](#readme) \n" if indent > 2
  output << "\n"

  output
end

def output_content(data)
  output = ''

  projects = data['projects']
  categories = data['categories']

  parents, children = categories.partition { |category| category['parent'].nil? }
  parents.each do |parent|
    parent_id = parent['id']
    # Only include parent categories with projects or that have children with projects
    if has_projects_recursive(projects, categories, parent_id)
      output << output_content_category(parent, 2)
      output << output_projects(projects, parent_id)

      children.sort_by { |category| category['id'] }
        .select { |category| category['parent'] == parent_id }.each do |child|
        child_id = child['id']
        
        # Only include child categories with projects or that have children with projects
        if has_projects_recursive(projects, categories, child_id)
          output << output_content_category(child, 3)
          output << output_projects(projects, child_id)

          children.sort_by { |category| category['id'] }
            .select { |category| category['parent'] == child_id }.each do |grandchild|
            grandchild_id = grandchild['id']
            
            # Only include grandchild categories with projects or that have children with projects
            if has_projects_recursive(projects, categories, grandchild_id)
              output << output_content_category(grandchild, 4)
              output << output_projects(projects, grandchild_id)

              children.sort_by { |category| category['id'] }
                .select { |category| category['parent'] == grandchild_id }.each do |great_grandchild|
                great_grandchild_id = great_grandchild['id']
                
                # Only include great-grandchild categories with projects
                if has_projects(projects, great_grandchild_id)
                  output << output_content_category(great_grandchild, 5)
                  output << output_projects(projects, great_grandchild_id)
                end
              end
            end
          end
        end
      end
    end
  end

  output
end

def output_header(data)
  header = data['header']
  num_projects = data['projects'].count

  output = header
  output << "\n\n"  
  # output << output_table(num_projects)
  output
end

def output_contributing(data)
  output = "\n\n### Contributing\n\n"
  output << data['header_contributing']
  output
end

def output_table(num_projects)
  require 'date'

  date = DateTime.now
  date_display = date.strftime "%B %d, %Y"

  output = "| Awesome | Linux | Projects | Updated\n| :-: | :-: | :-: | :-: | :-:\n"
  output << '[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) | '
  output << ' :penguin: | '
  output << "#{num_projects} | "
  output << date_display

  output
end

def output_toc(data)
  output = "\n\n### Contents\n\n"

  projects = data['projects']
  categories = data['categories']

  parents, children = categories.partition { |category| category['parent'].nil? }
  parents.each do |parent|
    parent_id = parent['id']
    # Only include parent categories with projects or with children that have projects
    if has_projects_recursive(projects, categories, parent_id)
      output << "- [#{parent['title']}](##{parent_id})\n"

      children.sort_by { |category| category['id'] }
        .select { |category| category['parent'] == parent_id }.each do |child|
        child_id = child['id']
        
        # Only include child categories with projects or with grandchildren that have projects
        if has_projects_recursive(projects, categories, child_id)
          output << "  - [#{child['title']}](##{child_id})\n"

          children.sort_by { |category| category['id'] }
            .select { |category| category['parent'] == child_id }.each do |grandchild|
            grandchild_id = grandchild['id']
            
            # Only include grandchild categories with projects or with great-grandchildren that have projects
            if has_projects_recursive(projects, categories, grandchild_id)
              output << "    - [#{grandchild['title']}](##{grandchild_id})\n"

              children.sort_by { |category| category['id'] }
                .select { |category| category['parent'] == grandchild_id }.each do |great_grandchild|
                great_grandchild_id = great_grandchild['id']
                
                # Only include great-grandchild categories with projects
                if has_projects(projects, great_grandchild_id)
                  output << "      - [#{great_grandchild['title']}](##{great_grandchild_id})\n"
                end
              end
            end
          end
        end
      end
    end
  end

  output
end

def write_readme(data, filename)
  output = output_header(data)
  output << output_toc(data)
  output << output_content(data)
  output << output_contributing(data)

  File.open(filename, 'w') { |file| file.write output }
  puts "Wrote #{filename} :-)"
end

data = get_json()
write_readme(data, README)
