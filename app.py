from flask import Flask, jsonify
from engine_master import EngineMaster

app = Flask(__name__)
engine = EngineMaster()

@app.route("/")
def home():
    return jsonify({"status": "NASA ULTRA SYSTEM ONLINE"})

@app.route("/forecast")
def forecast():
    """תחזית מלאה: ראשי + גיבויים + סטטיסטיקות + קירה + קוואנטום"""
    try:
        result = engine.generate_full()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/update")
def update():
    """עדכון היסטוריה במידה ויש הגרלה חדשה באתר"""
    try:
        r = engine.update()
        return jsonify(r)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
