from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# 模拟真实股票列表（会随机波动）
def get_stock_list():
    stocks = [
        {"代码": "600000", "名称": "浦发银行", "最新价": 7.82, "涨跌幅": 0.65, "成交量": 12560000},
        {"代码": "600036", "名称": "招商银行", "最新价": 32.56, "涨跌幅": -1.24, "成交量": 8950000},
        {"代码": "601318", "名称": "中国平安", "最新价": 42.18, "涨跌幅": 2.31, "成交量": 23450000},
        {"代码": "000001", "名称": "平安银行", "最新价": 11.35, "涨跌幅": -0.85, "成交量": 7820000},
        {"代码": "600519", "名称": "贵州茅台", "最新价": 1725.66, "涨跌幅": 1.56, "成交量": 3250000},
    ]

    # 随机波动，让前端能看到实时变化
    for s in stocks:
        s["最新价"] = round(s["最新价"] + random.uniform(-0.5, 0.5), 2)
        s["涨跌幅"] = round(s["涨跌幅"] + random.uniform(-0.3, 0.3), 2)
        s["成交量"] = int(s["成交量"] * random.uniform(0.9, 1.1))
    return stocks

# 仪表盘数据（包含股票列表）
@app.route("/api/dashboard")
def dashboard():
    hs300 = round(3800 + random.uniform(-20, 20), 2)
    rate = round(random.uniform(-2.5, 2.5), 2)
    hs300Rate = f"+{rate}%" if rate >= 0 else f"{rate}%"

    return jsonify({
        "hs300": hs300,
        "hs300Rate": hs300Rate,
        "stocks": get_stock_list()
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)