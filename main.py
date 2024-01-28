from fastapi import FastAPI
from starlette.responses import HTMLResponse
import os
from jinja2 import Environment, FileSystemLoader
from markdown2 import markdown
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/templates", StaticFiles(directory="templates"), name="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")
content_folder = './content'
public_folder = './public'
current_dir = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(current_dir))

def generate_blog_html(blog_entries):
    blog_template = env.get_template('templates/blog_template.html')
    blog_html = blog_template.render(blog_entries=blog_entries)
    return blog_html

def extract_metadata(md_content):
    lines = md_content.split('\n')
    metadata = {
        'title': 'No Title',
        'description': '',
        'pubDate': '',
        'tags': []
    }
    for line in lines:
        if line.startswith('title:'):
            metadata['title'] = line.split(':', 1)[1].strip()
        elif line.startswith('description:'):
            metadata['description'] = line.split(':', 1)[1].strip()
        elif line.startswith('pubDate:'):
            metadata['pubDate'] = line.split(':', 1)[1].strip()
        elif line.startswith('tags:'):
            metadata['tags'] = [tag.strip() for tag in line.split(':', 1)[1].split(',') if tag.strip()]
    return metadata

def generate_html(blog_entries):
    navbar_template = env.get_template('templates/navbar_template.html')
    list_template = env.get_template('templates/list_template.html')
    navbar_html = navbar_template.render()
    list_html = list_template.render(blog_entries=blog_entries)
    return navbar_html + list_html


@app.get("/", response_class=HTMLResponse)
async def read_blog():
    # Read and parse 'config/about-me.md'
    about_me_path = os.path.join(current_dir, 'config', 'about-me.md')
    with open(about_me_path, 'r') as about_me_file:
        about_me_md = about_me_file.read()
        about_me_html = markdown(about_me_md)

    # Prepare navbar HTML
    navbar_template = env.get_template('templates/navbar_template.html')
    navbar_html = navbar_template.render()

    # Prepare blog entries
    blog_entries = []
    for filename in os.listdir(content_folder):
        if filename.endswith('.md'):
            with open(os.path.join(content_folder, filename), 'r') as file:
                md_content = file.read()
                metadata = extract_metadata(md_content)
                html_content = markdown(md_content)
                blog_entries.append({
                    'filename': filename[:-3],
                    'title': metadata['title'],
                    'description': metadata['description'],
                    'pubDate': metadata['pubDate'],
                    'tags': metadata['tags'],
                    'html_content': html_content
                })
    blog_entries.sort(key=lambda x: x['pubDate'], reverse=True)

    # Render the final HTML
    list_template = env.get_template('templates/list_template.html')
    html = list_template.render(navbar_html=navbar_html, about_me_html=about_me_html, blog_entries=blog_entries)
    return HTMLResponse(html, media_type="text/html")


@app.get("/blog/{filename}", response_class=HTMLResponse)
async def read_file(filename: str):
    file_path = os.path.join(content_folder, filename + '.md')
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            md_content = file.read()
            metadata, content = md_content.split('---', 2)[1:]
            metadata = extract_metadata(metadata)
            title = metadata.get('title', 'No Title')
            description = metadata.get('description', '') 
            tags = metadata.get('tags', []) 
            html_content = markdown(content.strip())
            navbar_html = ""
            template = env.get_template('templates/md_template.html')
            rendered_content = template.render(title=title, description=description, tags=tags, content=html_content, navbar=navbar_html)
            return HTMLResponse(rendered_content, media_type="text/html")
    return HTMLResponse("File not found", status_code=404)

@app.get("/blog", response_class=HTMLResponse)
async def list_all_blogs():
    blog_entries = []
    for filename in os.listdir(content_folder):
        if filename.endswith('.md'):
            with open(os.path.join(content_folder, filename), 'r') as file:
                md_content = file.read()
                metadata = extract_metadata(md_content)
                html_content = markdown(md_content)
                blog_entries.append({
                    'filename': filename[:-3],
                    'title': metadata['title'],
                    'description': metadata['description'],
                    'pubDate': metadata['pubDate'],
                    'tags': metadata['tags'],
                    'html_content': html_content
                })
    blog_entries.sort(key=lambda x: x['pubDate'], reverse=True)
    html = generate_blog_html(blog_entries)
    return HTMLResponse(html, media_type="text/html")


@app.get("/tag/{tag}", response_class=HTMLResponse)
async def list_blogs_by_tag(tag: str):
    blog_entries = []
    for filename in os.listdir(content_folder):
        if filename.endswith('.md'):
            with open(os.path.join(content_folder, filename), 'r') as file:
                md_content = file.read()
                metadata = extract_metadata(md_content)
                html_content = markdown(md_content)
                if tag in metadata['tags']:
                    blog_entries.append({
                        'filename': filename[:-3],
                        'title': metadata['title'],
                        'description': metadata['description'],
                        'pubDate': metadata['pubDate'],
                        'tags': metadata['tags'],
                        'html_content': html_content
                    })
    blog_entries.sort(key=lambda x: x['pubDate'], reverse=True)
    html = generate_blog_html(blog_entries)
    return HTMLResponse(html, media_type="text/html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
