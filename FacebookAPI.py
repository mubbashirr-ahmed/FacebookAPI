from flask import Flask, request, jsonify
from dbOperation import get_all_rows, insert_data

app = Flask(__name__)

@app.route('/post_message', methods=['POST'])
def post_message():
    page_id = request.form.get('page_id')
    access_token = request.form.get('access_token')
    message = request.form.get('message')
    timestamp = request.form.get('timestamp')
    image_bytes = request.files.get('image')

    if not page_id or not access_token or not message or not image_bytes or not timestamp:
        return jsonify({'error': 'Missing page_id, access_token, message, or image'}), 400

    if insert_data(page_id, access_token, message, image_bytes, timestamp):
        return jsonify({'success': 'Data inserted successfully'}), 200
    else:
        return jsonify({'error': 'Failed to insert data into the database'}), 500

@app.route('/verify', methods=['GET'])
def verify():
    return jsonify({'Success': 'API Working'}), 200

@app.route('/data', methods=['GET'])
def getsize():
    row_count =  get_all_rows()
    if row_count==0:
        return jsonify({'size', 'empty'})
    return jsonify({'size': row_count}), 200



    
if __name__ == '__main__':
    app.run()
