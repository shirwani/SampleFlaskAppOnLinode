from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def run():
    return render_template("index.html",
                           image_path='https://testbucket7846.atl1.cdn.digitaloceanspaces.com/online-store/home_page_collage_hero.jpg',
                           js_path='static/js/script.js')

if __name__ == '__main__':
    app.run(debug=True, port=5010)
