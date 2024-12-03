from app import db
from models import Assignment,User,Proofread
from flask import jsonify
def get_list_sentence_task(data):
    listSentence=[]
    indexSentence=[]
    for d in data:
        print(d)
        user_id=d.get("user_id")
        start=d.get("start_index")
        end=d.get("end_index")
        indexSentence.append({start,end})
    listSentence=[]
    for start,end in indexSentence:
        for index in range(start,end+1):
            proofRead=Proofread.query.filter_by(id=index).first()
            sentence={
                "id":proofRead.id,
                "input":proofRead.input,
                "expect":proofRead.expect,}
            listSentence.append(sentence)
    return jsonify(listSentence), 200