from flask import Flask, jsonify, make_response, request, stream_with_context, Response
app = Flask(__name__)
from Cipher import xor_tool
import json


@app.route('/bruteforce/', methods=['POST'])
def bruteforce():
    # Todo: make this method return with the possible encryptions
    
    content = request.get_json()

    if len(content['text']) == 0:
        return Response('Encrypted text is empty', status= 400)
    try:
        data = list(map(int, content['text'].split(',')))
    except:
        return Response('Data need to containt split "," intergers', status= 400)

    keys = xor_tool.guess_key(data, content['size'])
    
    def generate():
        
        yield '['

        try:
            k = next(keys)
            yield json.dumps(k, default=list)
        except StopIteration:
            yield ']'
            raise StopIteration
        
        for k in keys:
            yield ',' + json.dumps(k, default=list)

        yield ']'
        
    
    resp = Response( stream_with_context(generate()), content_type='application/json')

   
    # This fix CORS issues with different ports between UI and backend
    #resp = make_response(jsonify([["aa", "a@#sdf asd"], ["ab", "ad@!!#dv"]]))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
