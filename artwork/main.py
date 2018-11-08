from flask import (Flask,
                   render_template,
                   request,
                   make_response,
                   redirect
                   )
                  

from models import artwork
                  
app = Flask('app')


@app.route('/')
def index():
  description="Tis is a wider card with supporting text below as a"
  images=[
    {
      'description':description,
      'thumbnail_link':art.thumbnail_link,
      'fullimage_link':art.fullimage_link
    }
    ]
    results.append(art_item)
  return render_template("index.html",images=images)




 


app.run( host='0.0.0.0', port=8080)
