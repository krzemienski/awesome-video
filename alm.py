from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import requests
import json
import base64
from bs4 import BeautifulSoup

# Flask Setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///awesomeness.db'
app.config['SECRET_KEY'] = 'mysecret'

# Database Setup
db = SQLAlchemy(app)

# Flask-Admin Setup
admin = Admin(app, name='AwesomeList Admin', template_mode='bootstrap3')

# Models
class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(150), unique=True, nullable=False)
    name = db.Column(db.String(100))
    description = db.Column(db.String(300))

# Add administrative views
admin.add_view(ModelView(Link, db.session))

def extract_metadata(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.find('title').text if soup.find('title') else 'No Title'
            meta_description = soup.find('meta', attrs={'name': 'description'})
            og_description = soup.find('meta', attrs={'property': 'og:description'})
            if meta_description and meta_description.get('content'):
                description = meta_description['content']
            elif og_description and og_description.get('content'):
                description = og_description['content']
            else:
                description = 'No Description'
            return {
                'title': title,
                'description': description,
            }
    except requests.RequestException:
        return None

def generate_readme():
    links = Link.query.all()
    readme_content = "# Awesome Video\\n\\nA curated list of awesome video resources.\\n\\n"
    for link in links:
        readme_content += f"- [{link.name}]({link.url}) - {link.description}\\n"
    return readme_content

def get_repo_contents_sha():
    url = f'https://api.github.com/repos/krzemienski/awesome-video/contents/README.md'
    headers = {'Authorization': 'token your_github_token'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('sha')
    return None

def update_github_readme(readme_content):
    sha = get_repo_contents_sha()
    if not sha:
        print("Error: Unable to fetch README metadata")
        return False
    url = f'https://api.github.com/repos/krzemienski/awesome-video/contents/README.md'
    headers = {'Authorization': 'token your_github_token'}
    data = {
        "message": "Update README.md",
        "content": base64.b64encode(readme_content.encode()).decode(),
        "sha": sha
    }
    response = requests.put(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print("README updated successfully")
        return True
    else:
        print(f"Error: {response.content}")
        return False

@app.route('/submit', methods=['POST'])
def submit_url():
    data = request.json
    url = data.get('url')
    metadata = extract_metadata(url)
    if not metadata:
        return {'message': 'Failed to extract metadata'}, 400
    new_link = Link(url=url, name=metadata.get('title', ''), description=metadata.get('description', ''))
    db.session.add(new_link)
    db.session.commit()
    readme_content = generate_readme()
    update_github_readme(readme_content)
    return {'message': 'URL submitted successfully'}

def main():
    db.create_all()
    app.run(debug=True)

if __name__ == "__main__":
    main()
