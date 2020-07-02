from flask import Flask, request, make_response


app = Flask(__name__)


@app.route("/api/token-auth/", methods=["POST"])
def login():
    email = request.form.get("username")
    password = request.form.get("password")
    print(email, password)
    return make_response({"token": "token"}, 500)


if __name__ == '__main__':
    app.run()
