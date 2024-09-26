import os
from datetime import datetime

def generate_sitemap(directory):
    urls = []
    base_url = "https://astro-cosmos.github.io/"
    
    # Busca archivos HTML y genera URLs
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file).replace("\\", "/")
                url = base_url + path.split(directory)[-1][1:]
                lastmod = datetime.now().strftime("%Y-%m-%d")
                urls.append(f"<url><loc>{url}</loc><lastmod>{lastmod}</lastmod><changefreq>weekly</changefreq></url>")
    
    # Escribe el sitemap.xml
    with open("sitemap.xml", "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        f.write("\n".join(urls))
        f.write('\n</urlset>')

if __name__ == "__main__":
    generate_sitemap('htmls/')


