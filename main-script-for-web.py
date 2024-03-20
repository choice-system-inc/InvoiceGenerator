from flask import Flask, request, render_template, redirect, url_for, flash, render_template_string, jsonify
from flask_httpauth import HTTPBasicAuth
from modules.reader import read_setting, read_template_by_id
from modules.gas_req import requests_to_gas

app = Flask(__name__, static_folder="./pdf-downloads")
app.secret_key = 'your_secret_key'  # Flashメッセージ用の秘密鍵
auth = HTTPBasicAuth()
url, user_id, password = read_setting()
USER_DATA = {
    user_id: password
}

@auth.verify_password
def verify_password(username, password):
    if username in USER_DATA and USER_DATA[username] == password:
        return username

@app.route('/', methods=['GET'])
def form():
    # フォームを表示
    return render_template("index.html")

@app.route('/complete', methods=['GET'])
def complete():
    # フォームを表示
    download_url = request.args.get('downloadUrl', None)
    return render_template("complete.html", download_url=download_url)

@app.route('/', methods=['POST'])
@auth.login_required
def send_data():
    template_id = request.form['template_id']
    custom_code = request.form.get('custom_code', 0)  # custom_codeがない場合は0をデフォルト値とする
    # バリデーション
    if not template_id:
        flash('*Template IDは必須です。', 'error')
        return redirect(url_for('form'))
    url, user_id, password = read_setting()
    send_json_data = read_template_by_id(template_id, custom_code)
    response, file_name = requests_to_gas(url, send_json_data)
    download_url = url_for('static', filename=file_name)
    # ファイルダウンロードURLとリダイレクト先をJSONで返す
    redirect_url = url_for('complete') + "?downloadUrl=" + download_url
    return jsonify({'redirectUrl': redirect_url})

if __name__ == "__main__":
    app.run(debug=True)