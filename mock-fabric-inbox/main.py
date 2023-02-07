from flask import Flask, jsonify, make_response
app = Flask(__name__)

data = [
    {
        "id": 1,
        "method": "GET",
        "url": " http://127.0.0.1:5000/page/1",
        "expected_response_code": 200,
        "headers": [],
        "timeout": 5,
        "retries": 3,
        "interval": 30,
        "body": "",
    },
    {
        "id": 2,
        "method": "GET",
        "url": " http://127.0.0.1:5000/page/2",
        "headers": [],
        "expected_response_code": 200,
        "timeout": 5,
        "retries": 3,
        "interval": 30,
        "body": "",
    },
    {
        "id": 3,
        "method": "GET",
        "url": " http://127.0.0.1:5000/page/3",
        "headers": [],
        "expected_response_code": 200,
        "timeout": 5,
        "retries": 3,
        "interval": 30,
        "body": "",
    },

]

@app.route("/")
def get_data():
    response = make_response( jsonify(data), 200)
    response.headers["Content-Type"] = "application/json"
    return response


@app.route("/page/<string:page_id>")
def get_page(page_id):
    response = make_response(jsonify( {"page": page_id } ), 200)
    response.headers["Content-Type"] = "application/json"
    return response


if __name__ == "__main__":
    app.run()
