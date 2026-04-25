from flask import Flask, jsonify, request
from flask_cors import CORS
import akshare as ak
import time

app = Flask(__name__)
CORS(app)

# 你要监控的股票
CODES = ["600519", "000858", "002594", "601318", "600036"]

# 全局缓存（超级关键，防止卡死）
CACHE_DATA = []
CACHE_TIME = 0
CACHE_GAP = 3

def get_real_data():
    global CACHE_DATA, CACHE_TIME
    now = time.time()

    # 3秒内用缓存，不重复请求，解决慢的问题
    if now - CACHE_TIME < CACHE_GAP and len(CACHE_DATA) > 0:
        return CACHE_DATA

    try:
        # 一次性获取所有A股实时行情（速度最快，不会卡）
        df = ak.stock_zh_a_spot()
        df = df[df["代码"].isin(CODES)]

        res = []
        for _, row in df.iterrows():
            res.append({
                "代码": row["代码"],
                "名称": row["名称"],
                "最新价": float(row["最新价"]),
                "涨跌幅": float(row["涨跌幅"]),
                "涨跌额": float(row["涨跌额"]),
                "成交量": float(row["成交量"]),
            })

        CACHE_DATA = res
        CACHE_TIME = now
        return res

    except Exception as e:
        print("获取数据失败", e)
        return CACHE_DATA

# 分页接口
@app.route("/api/market")
def market():
    data = get_real_data()

    page = int(request.args.get("page", 1))
    size = int(request.args.get("size", 5))
    total = len(data)

    start = (page-1)*size
    end = start + size
    page_data = data[start:end]

    return jsonify({
        "total": total,
        "stocks": page_data
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)