import requests
import json
from datetime import datetime
import os

def requests_to_gas(url, data):
    # リクエストヘッダー
    headers = {
        'Content-Type': 'application/json'
    }

    # POSTリクエストを送信
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # レスポンスの確認
    if response.status_code == 200:
        print("リクエスト成功")
        response_data = response.json()  # JSONレスポンスを解析
        if "pdf_file_url" in response_data:
            pdf_file_url = response_data["pdf_file_url"]
            print("PDFファイルのURL:", pdf_file_url)
            # PDFファイルをダウンロード
            pdf_response = requests.get(pdf_file_url)
            if pdf_response.status_code == 200:
                # PDFファイルの保存
                dt_now = datetime.now()
                dt_str = dt_now.strftime('%Y%m%d')
                # 重複確認
                for i in range(1000):
                    counter = i + 1
                    if os.path.exists("./pdf-downloads/" + data["company"] + "_" + dt_str + "_" + str(counter) + ".pdf"):
                        pass
                    else:
                        file_name = "./pdf-downloads/" + data["company"] + "_" + dt_str + "_" + str(counter) + ".pdf"
                        break
                with open(file_name, "wb") as pdf_file:
                    pdf_file.write(pdf_response.content)
                print("PDFファイルがダウンロードされました。")
            else:
                print("PDFファイルのダウンロードに失敗しました。")
        else:
            print("レスポンスにpdf_file_urlが含まれていません。")
    else:
        print("リクエスト失敗:", response.status_code)