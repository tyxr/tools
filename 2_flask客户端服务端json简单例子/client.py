import requests
time_out = 5
bert_host = '0.0.0.0'
bert_port = '50011'


def bert_qa(message,top10):
    # url = remote_host + ':' + config.medicine_port + '/nlp/api/v1.0/medicine_parse'
    #url = 'http://' + bert_host + ':' + bert_port + '/nlp/api/v1.0/gastric-qa'
    url = 'http://localhost:50011/nlp/api/v1.0/gastric-qa'

    data = {'msg': message,'top10':10}
    res = requests.post(url, json=data, timeout=time_out)
    print(res)
    if res.status_code == 200:

        res = res.json()
        print(res)
    else:
        pass
    return res


if __name__=="__main__":
    bert_qa("孙笑川NMSL",[1,2,3,4,5,6,7,8,9,10])
