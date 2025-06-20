from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)
@app.route('/hash', methods=['GET'])
def generate_hash_get():
    text  = request.args.get('text', '')
    hevorix = request.args.get('hevorix', 'md5')

    try:
        h = hashlib.new(hevorix)
        h.update(text.encode())
        return jsonify({
            "algorithm": hevorix,
            "input": text,
            "hash": h.hexdigest()
        })
    except ValueError:
        return jsonify({"error": "notogri algorithm"})

if __name__ == '__main__':
    app.run()