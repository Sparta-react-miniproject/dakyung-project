from flask import Flask, render_template, request, jsonify

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.t8n3okz.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

app = Flask(__name__)


@app.route('/')
def home():

    return render_template('index.html')


@app.route("/homework", methods=["POST"])
def homework_post():

    # 원래 db에 있는 개수 +1을 한거구나 (db가 5개여야겠네? 애초에 들어갈때 db1, db2, db3, db4, db5)
    count = list(db.homeworktest.find({}, {'_id': False}))
    num = len(count) + 1

    # data: {nickname_give: nickname, comment_give: comment},
    name_receive = request.form['nickname_give']
    comment_receive = request.form['comment_give']


    # 컬럼명 지정해서 넣어주는 걸 까먹었네
    doc = {
        'membernum' : num,
        'name' : name_receive,
        'comment': comment_receive,
    }

    # 저장
    db.homeworktest.insert_one(doc)
    return jsonify({'msg': '응원 저장이 완료되었습니다!!'})



@app.route("/homework", methods=["GET"])
def homework_get():

    # db에서 list로 모든 데이터 내용을 불러와서 all_comment라는 객체에 저장하고
    all_comment = list(db.homeworktest.find({}, {'_id': False}))
    # comments라는 이름으로 response에 담아 index.html에 리턴해준다.
    return jsonify({'comments': all_comment})


@app.route("/deletecomment", methods=["POST"])
def deletecomment_post():

    delete_receive = request.form['delete_give']
    db.homeworktest.delete_one({'membernum': int(delete_receive)})
    return jsonify({'msg': '데이터 삭제가 완료되었습니다'})


@app.route('/study')
def start():
    return render_template('study.html')



@app.route('/test12')
def start12():
    return render_template('study.html')



if __name__ == '__main__':
    app.run('0.0.0.0', port=5050, debug=True)
