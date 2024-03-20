def validate_data(data):
    # subtitleListの要素数を検証
    if len(data["subtitleList"]) >= 19:
        raise ValueError("subtitleListの要素数が19個以上です。")
    elif len(data["subtitleList"]) < 1:
        raise ValueError("subtitleListの要素数が1個未満です。")
    # infoListの要素数を検証
    if len(data["infoList"]) >= 5:
        raise ValueError("infoListの要素数が5個以上です。")
    # すべての検証を通過した場合
    print("JSONデータは正常です。")