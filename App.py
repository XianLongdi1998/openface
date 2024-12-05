from flask import Flask, request, jsonify
import subprocess
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)



openface_path = '/App/openface/FeatureExtraction.exe'

@app.route("/run_openface/<path>", methods=["GET"])
def run_openface(path):
    print(path)
    f=f'./video/{path}'
    print(f)
    intermediate_path = f'./output'
    print(f"Input file: {f}")
    print(f"Output directory: {intermediate_path}")
    verbose=False
    print("aaaaaaaa")
    try:
        command = [openface_path, '-f', f, '-out_dir', intermediate_path, '-aus']
        if verbose:
            command.append('-verbose')
        subprocess.run(command, check=True)
        return jsonify({'message': 'OpenFace executed successfully'}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    port = int(os.environ.get('PORT', 5999))
    app.run(host='0.0.0.0', port=port)