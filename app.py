from flask import Flask

app = Flask(_name_)

@app.route("/")
def main():
    return "welcome to my Flask page!"

if _name_ == "_main_":
    app.run(debug=True, host="0.0.0.0", port=80)



