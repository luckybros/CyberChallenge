from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Definisci la directory in cui i file saranno memorizzati
FILE_DIR = '/home/parallels/Desktop/CyberChallenge/docker/test2/app'

# Assicurati che la cartella esista
if not os.path.exists(FILE_DIR):
    os.makedirs(FILE_DIR)

@app.route('/write', methods=['POST'])
def write_file():
    # Prendi il nome del file e il contenuto dal body della richiesta
    data = request.get_json()
    file_name = data.get('file_name')
    content = data.get('content')

    if not file_name or not content:
        return jsonify({'error': 'file_name and content are required'}), 400

    file_path = os.path.join(FILE_DIR, file_name)

    # Scrivi il contenuto nel file
    with open(file_path, 'w') as file:
        file.write(content)

    return jsonify({'message': f'File {file_name} scritto con successo!'}), 200

@app.route('/read/<file_name>', methods=['GET'])
def read_file(file_name):
    file_path = os.path.join(FILE_DIR, file_name)

    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404

    # Leggi il contenuto del file
    with open(file_path, 'r') as file:
        content = file.read()

    return jsonify({'file_name': file_name, 'content': content}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
