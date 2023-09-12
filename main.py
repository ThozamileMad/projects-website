from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms import MessageForm
from datetime import datetime
import random

app = Flask(__name__)
random_lst = list("xncja7SW8DNKC.DB;[R]HKKPQOONvybqjfnevnooi")
random.shuffle(random_lst)
app.config["SECRET_KEY"] = "".join(random_lst)
Bootstrap(app)


@app.route("/", methods=["GET", "POST"])
def home():
    form = MessageForm()
    form.validate_on_submit()
    png_srcs = [{"scripting": ["https://cdn-icons-png.flaticon.com/512/2572/2572523.png",
                               "Scripting",
                               "Python scripting projects. For Loops, OOP, Functions, if/else statements and more."],

                "gui": ["https://cdn-icons-png.flaticon.com/512/6470/6470993.png",
                        "GUI",
                        "GUI programs and applications. Tkinter, Web Applications and more."],

                "games": ["https://cdn-icons-png.flaticon.com/512/1083/1083364.png",
                          "Games",
                          "Game projects Tkinter and Turtle Graphics."],
                 },

                {"http_requests_and_apis": ["https://cdn-icons-png.flaticon.com/512/718/718064.png",
                                            "HTTP Requests and APIs",
                                            "Knowledge of APIs GET/POST/PATCH/PUT methods and HTTP request methods using python request module."],

                "web_scraping_and_automation": ["https://cdn-icons-png.flaticon.com/512/7984/7984713.png",
                                                "Web Scraping and Automation",
                                                "Web scraping projects using Beautiful Soup and Selenium."],

                "web_development": ["https://cdn-icons-png.flaticon.com/512/2888/2888407.png",
                                    "Web Development",
                                    "Web Development projects with HTML, CSS, Javascript, Flask, Jinja and Bootstrap."],
                 },

                {"data_science": ["https://cdn-icons-png.flaticon.com/512/2821/2821637.png",
                                  "Data Science",
                                  "Data science projects with pandas, numpy, matplotlib, plotly and seaborn."]
                 }
                ]

    year = datetime.now().year
    return render_template("mad's_projects.html",
                           cat_data=png_srcs,
                           form=form,
                           current_year=year)
                    

if __name__ == "__main__":
    app.run(debug=True)
