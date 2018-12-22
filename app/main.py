from flask import Flask,jsonify
from app import Pangkat

app = Flask(__name__)

@app.route("/")
def hello():
    ''' 
    ini adalah fungsi utama, atau index di php

    '''
    return "Python API Example"

@app.route("/hitung-pangkat")
def pangkat():
    '''
    ini adalah fungsi untuk memanggil fungsi dari aplikasi kita pada file app.py (contoh)

    fungsi ini mengembalikan nilai hasil hitungan pangkat berupa json (api), yang nantinya akan dibaca oleh app lain dengan berbagai bahasa(misal php dll)
    '''

    app_pangkat = Pangkat()
    output = {}
    output['hasil_pangkat'] = app_pangkat.hitung(5)
    
    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)