from flask import *
from datetime import *
app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(url_for("foodblog"))

girl_list = [
    {
        "src" : "http://68.media.tumblr.com/c2b359d90b868247565a37b4f70ea2d9/tumblr_omu6agTv6b1qbd81ro1_1280.jpg",
        "title" : "12343 by Đinh Văn Linh ♥",
        "tag" : "A lot more at http://xkcn.info - Xinh Ko Chiu Noi ♥"
    },
    {
        "src" : "http://68.media.tumblr.com/fdce8d90185f8f38a5f36a69b198a271/tumblr_ojqkfv1h7c1qbd81ro1_1280.jpg",
        "title" : "lightstudio | 0966726996 by Leo White | 0966 72 6996 | 0164 960 8794 ♥",
        "tag" : "A lot more at http://xkcn.info - Xinh Ko Chiu Noi ♥"
    },
{
        "src":"http://68.media.tumblr.com/333c275f13f585bb49a55f9e7b8fa9c8/tumblr_of8kztZ3QA1qbd81ro1_1280.jpg",
        "title" : "lightstudio | 0966726996 by Leo White | 0966 72 6996 | 0164 960 8794 ♥",
        "tag" : "A lot more at http://xkcn.info - Xinh Ko Chiu Noi ♥"
    },
{
        "src" : "http://68.media.tumblr.com/6707567f4007a0ebb6e342f37692da0b/tumblr_of8kzf8gMp1qbd81ro1_1280.jpg",
        "title" : "lightstudio | 0966726996 by Leo White | 0966 72 6996 | 0164 960 8794 ♥",
        "tag" : "A lot more at http://xkcn.info - Xinh Ko Chiu Noi ♥"
    }
]

my_contact = {
    "Avatar": "https://scontent.fhan2-1.fna.fbcdn.net/v/t1.0-9/1655910_258291991014902_2123799782_n.jpg?oh=d4ff603db8ca1b9ce9f5e3f00e549cfe&oe=596903F7",
    "Fullname": "Pham Hoang Anh",
    "DOB": "03-11-1989",
    "Location": "Ha noi, Viet Nam",
    "Martial Status": "Maried",
    "Email": "hoanganhctm7@gmail.com",
    "Phone": "01628338711",
    "Education": "Bach Khoa University"
}

foodlist=[
[
{
    "src" : "../static/images/food1.png",
    "alt" : "Sandwich",
    "title" : "The Perfect Sandwich, A Real NYC Classic",
    "information" : "Just some random text, lorem ipsum text praesent tincidunt ipsum lipsum."
    },
{
    "src" : "../static/images/food2.png",
    "alt" : "Steak",
    "title" : "Let Me Tell You About This Steak",
    "information" : "Once again, some random text to lorem lorem lorem lorem ipsum text praesent tincidunt ipsum lipsum."
    },
{
    "src" : "../static/images/food3.png",
    "alt" : "Cherries",
    "title" : "Cherries, interrupted",
    "information" : "Lorem ipsum text praesent tincidunt ipsum lipsum."
    },
{
    "src" : "../static/images/food4.png",
    "alt" : "Pasta and Wine",
    "title" : "Once Again, Robust Wine and Vegetable Pasta",
    "information" : "Lorem ipsum text praesent tincidunt ipsum lipsum."
    }
],
[
{
    "src" : "../static/images/food5.png",
    "alt" : "Popsicle",
    "title" : "All I Need Is a Popsicle",
    "information" : "Just some random text, lorem ipsum text praesent tincidunt ipsum lipsum."
    },
{
    "src" : "../static/images/food6.png",
    "alt" : "Salmon",
    "title" : "Salmon For Your Skin",
    "information" : "Once again, some random text to lorem lorem lorem lorem ipsum text praesent tincidunt ipsum lipsum."
    },
{
    "src" : "../static/images/food7.png",
    "alt" : "Sandwich",
    "title" : "The Perfect Sandwich, A Real Classic",
    "information" : "Just some random text, lorem ipsum text praesent tincidunt ipsum lipsum."
    },
{
    "src" : "../static/images/food8.png",
    "alt" : "Croissant",
    "title" : "Le French",
    "information" : "Lorem lorem lorem lorem ipsum text praesent tincidunt ipsum lipsum."
    }
]
]



number_of_visitor = 0

@app.route('/contact')
def contact():
    return render_template("contact.html", contact=my_contact)

@app.route('/login')
def login():
    global number_of_visitor
    number_of_visitor += 1
    current_time_on_server = str(datetime.now())
    return render_template("login.html",current_time_on_server=current_time_on_server, number_of_visitor=number_of_visitor*1000)

@app.route('/food')
def food():
    return render_template("food.html", list_girl=girl_list)

@app.route('/cssdemo')
def cssdemo():
    return render_template("cssdemo.html")

@app.route('/w3cssdemo')
def w3cssdemo():
    return render_template("w3cssdemo.html")

@app.route('/foodblog')
def foodblog():
    return render_template("foodblog.html", foodlist=foodlist)



if __name__ == '__main__':
    app.run()

