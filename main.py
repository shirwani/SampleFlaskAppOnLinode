from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def run():
    return render_template("index.html",
                           image_path='https://chloe-nomura-home.atl1.cdn.digitaloceanspaces.com/website-images/home_page_collage_hero.jpg',
                           js_path='static/js/script.js')

if __name__ == '__main__':
    app.run(debug=True, port=5010)
