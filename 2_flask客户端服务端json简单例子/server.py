from flask import Flask, request,jsonify
ga_app = Flask(__name__)


@ga_app.route("/nlp/api/v1.0/gastric-qa", methods=["POST"])
def loop_answers():
    text_a = request.json.get('msg')
    top10_index = request.json.get('top10')
    res = {'text_a':text_a}
    print(text_a)
    print(top10_index)
    return jsonify(res)


if __name__=="__main__":
    ga_app.run(host='0.0.0.0', port=50011)