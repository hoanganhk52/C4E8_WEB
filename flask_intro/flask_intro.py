from flask import *
from datetime import *
app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(url_for("login"))

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




if __name__ == '__main__':
    app.run()

