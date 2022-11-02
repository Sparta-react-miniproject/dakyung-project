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

@app.route('/home')
def home1():
    return render_template('index.html')

@app.route('/hjPage')
def move1():
    return render_template('hjPage.html')

@app.route('/kdPage')
def move2():
    return render_template('kdPage.html')

@app.route('/kiPage')
def move3():
    return render_template('kiPage.html')

@app.route('/yjPage')
def move4():
    return render_template('yjPage.html')
@app.route('/dkPage')
def move5():
    return render_template('dkPage.html')




#방명록 등록(다경)
@app.route("/savecomment1", methods=["POST"])
def savecomment1_post():

    # 원래 db에 있는 개수 +1을 한거구나 (db가 5개여야겠네? 애초에 들어갈때 db1, db2, db3, db4, db5)
    count = list(db.member1.find({}, {'_id': False}))
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
    db.member1.insert_one(doc)
    return jsonify({'msg': '💜다경 대원에게 방명록이 등록되었습니다!!💜'})


#방명록 조회(다경)
@app.route("/showcomment1", methods=["GET"])
def showcomment1_get():

    # db에서 list로 모든 데이터 내용을 불러와서 all_comment라는 객체에 저장하고
    all_comment = list(db.member1.find({}, {'_id': False}))
    # comments라는 이름으로 response에 담아 index.html에 리턴해준다.
    return jsonify({'comments': all_comment})

#방명록 삭제(다경)
@app.route("/deletecomment1", methods=["POST"])
def deletecomment1_post():

    delete_receive = request.form['delete_give']
    db.member1.delete_one({'membernum': int(delete_receive)})
    return jsonify({'msg': '방명록 삭제가 완료되었습니다'})


#좋아요 수 플러스(다경)

@app.route("/likes1", methods=["POST"])
def likes_post1():

    likes_count = list(db.like1.find({}, {'_id': False}))
    count = len(likes_count) + 1

    doc = {
        'num': int(count),
    }

    db.like1.insert_one(doc)
    return jsonify({'msg':'💜좋아요! 성공💜'})

# 좋아요 수 보여주기(다경)
@app.route("/likes1", methods=["GET"])
def likes_get1():

    likes_count = list(db.like1.find({},{'_id':False}))
    return jsonify({'likes': likes_count})





#------------------------------------------------------

#방명록 등록(강익)
@app.route("/savecomment2", methods=["POST"])
def savecomment2_post():

    count = list(db.member2.find({}, {'_id': False}))
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
    db.member2.insert_one(doc)
    return jsonify({'msg': '💚강익 대원에게 방명록 등록이 되었습니다!💚'})


#방명록 조회(강익)
@app.route("/showcomment2", methods=["GET"])
def showcomment2_get():

    # db에서 list로 모든 데이터 내용을 불러와서 all_comment라는 객체에 저장하고
    all_comment = list(db.member2.find({}, {'_id': False}))
    # comments라는 이름으로 response에 담아 index.html에 리턴해준다.
    return jsonify({'comments': all_comment})

#방명록 삭제(강익)
@app.route("/deletecomment2", methods=["POST"])
def deletecomment2_post():

    delete_receive = request.form['delete_give']
    db.member2.delete_one({'membernum': int(delete_receive)})
    return jsonify({'msg': '방명록 삭제가 완료되었습니다'})


#좋아요 수 플러스(강익)

@app.route("/likes2", methods=["POST"])
def likes_post2():

    likes_count = list(db.like2.find({}, {'_id': False}))
    count = len(likes_count) + 1

    doc = {
        'num': int(count),
    }

    db.like2.insert_one(doc)
    return jsonify({'msg':'좋아요! 성공💚'})

# 좋아요 수 보여주기(강익)
@app.route("/likes2", methods=["GET"])
def likes_get2():

    likes_count = list(db.like2.find({},{'_id':False}))
    return jsonify({'likes': likes_count})



#---------------------------------------------------

#방명록 등록(기동)
@app.route("/savecomment3", methods=["POST"])
def savecomment3_post():

    count = list(db.member3.find({}, {'_id': False}))
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
    db.member3.insert_one(doc)
    return jsonify({'msg': '💙기동 대장에게 방명록이 등록되었습니다!!💙'})


#방명록 조회(기동)
@app.route("/showcomment3", methods=["GET"])
def showcomment3_get():

    # db에서 list로 모든 데이터 내용을 불러와서 all_comment라는 객체에 저장하고
    all_comment = list(db.member3.find({}, {'_id': False}))
    # comments라는 이름으로 response에 담아 index.html에 리턴해준다.
    return jsonify({'comments': all_comment})

#방명록 삭제(기동)
@app.route("/deletecomment3", methods=["POST"])
def deletecomment3_post():

    delete_receive = request.form['delete_give']
    db.member3.delete_one({'membernum': int(delete_receive)})
    return jsonify({'msg': '방명록 삭제가 완료되었습니다'})


#좋아요 수 플러스(기동)

@app.route("/likes3", methods=["POST"])
def likes_post3():

    likes_count = list(db.like3.find({}, {'_id': False}))
    count = len(likes_count) + 1

    doc = {
        'num': int(count),
    }

    db.like3.insert_one(doc)
    return jsonify({'msg':'좋아요! 완료💙'})

# 좋아요 수 보여주기(기동)
@app.route("/likes3", methods=["GET"])
def likes_get3():

    likes_count = list(db.like3.find({},{'_id':False}))
    return jsonify({'likes': likes_count})


#---------------------------------------------------

#방명록 등록(희진)
@app.route("/savecomment4", methods=["POST"])
def savecomment4_post():

    count = list(db.member4.find({}, {'_id': False}))
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
    db.member4.insert_one(doc)
    return jsonify({'msg': ' 💛희진 대원에게 방명록 등록이 완료되었습니다!!💛'})


#방명록 조회(희진)
@app.route("/showcomment4", methods=["GET"])
def showcomment4_get():

    # db에서 list로 모든 데이터 내용을 불러와서 all_comment라는 객체에 저장하고
    all_comment = list(db.member4.find({}, {'_id': False}))
    # comments라는 이름으로 response에 담아 index.html에 리턴해준다.
    return jsonify({'comments': all_comment})

#방명록 삭제(희진)
@app.route("/deletecomment4", methods=["POST"])
def deletecomment4_post():

    delete_receive = request.form['delete_give']
    db.member4.delete_one({'membernum': int(delete_receive)})
    return jsonify({'msg': '방명록 삭제가 완료되었습니다'})


#좋아요 수 플러스(희진)

@app.route("/likes4", methods=["POST"])
def likes_post4():

    likes_count = list(db.like4.find({}, {'_id': False}))
    count = len(likes_count) + 1

    doc = {
        'num': int(count),
    }

    db.like4.insert_one(doc)
    return jsonify({'msg':'좋아요! 성공💛'})

# 좋아요 수 보여주기(희진)
@app.route("/likes4", methods=["GET"])
def likes_get4():

    likes_count = list(db.like4.find({},{'_id':False}))
    return jsonify({'likes': likes_count})


#---------------------------------------------------


#방명록 등록(영진)
@app.route("/savecomment5", methods=["POST"])
def savecomment5_post():

    count = list(db.member5.find({}, {'_id': False}))
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
    db.member5.insert_one(doc)
    return jsonify({'msg': '🖤영진 대원에게 방명록이 등록되었습니다!!🖤'})


#방명록 조회(영진)
@app.route("/showcomment5", methods=["GET"])
def showcomment5_get():

    # db에서 list로 모든 데이터 내용을 불러와서 all_comment라는 객체에 저장하고
    all_comment = list(db.member5.find({}, {'_id': False}))
    # comments라는 이름으로 response에 담아 index.html에 리턴해준다.
    return jsonify({'comments': all_comment})

#방명록 삭제(영진)
@app.route("/deletecomment5", methods=["POST"])
def deletecomment5_post():

    delete_receive = request.form['delete_give']
    db.member5.delete_one({'membernum': int(delete_receive)})
    return jsonify({'msg': '방명록 삭제가 완료되었습니다'})


#좋아요 수 플러스(영진)

@app.route("/likes5", methods=["POST"])
def likes_post5():

    likes_count = list(db.like5.find({}, {'_id': False}))
    count = len(likes_count) + 1

    doc = {
        'num': int(count),
    }

    db.like5.insert_one(doc)
    return jsonify({'msg':'좋아요! 성공🖤'})

# 좋아요 수 보여주기(영진)
@app.route("/likes5", methods=["GET"])
def likes_get5():

    likes_count = list(db.like5.find({},{'_id':False}))
    return jsonify({'likes': likes_count})


#----------------------------------------------------------




if __name__ == '__main__':
    app.run('0.0.0.0', port=5050, debug=True)
