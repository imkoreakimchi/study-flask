import json
from flask import Flask , request
app = Flask(__name__)

@app.route("/login",methods=["POTS"])
def signup():
    req = json.loads(request.get_data())
    # {"id":"hello", "pw":"www"}
    # "hello" <= post_result["id"]
    print(req)
    return f"로그인 완료"

@app.route("/member",methods=["POTS"])
def signIn():
    post_result = json.loads(request.get_data())
    return f"member의 id는 {post_result['id']}"

@app.route("/member")
def memberGet():
    return f"회원 가입 페이지를 작성 중 입니다"

@app.route("/login")
def login_error():
    return f"잘못된 HTTP 메서드를 요청 하였습니다"

# a = [0,1,2,3] -> a[3]
# a = {"a":0, "b":1, "c":2, "d":3} a['d']

# @app.route("/member")
# def member_list():
#     return f"question 변수의 값은 {request.args.get('id'),('pw'),('email')}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)