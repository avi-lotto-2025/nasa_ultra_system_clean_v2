# ================================
# server.py — NASA_ULTRA_SYSTEM_CLEAN_V2
# שרת Flask ראשי שמטפל בהרצה, חיזוי וסטטוס
# ================================

from flask import Flask, jsonify
from engine_master import UltraEngine
from auto_heal import auto_heal_cycle

app = Flask(__name__)

# יצירת מנוע ראשי (נטען פעם אחת בלבד)
engine = UltraEngine()

@app.route("/")
def home():
    return jsonify({
        "system": "NASA_ULTRA_SYSTEM_CLEAN_V2",
        "status": "online",
        "message": "🚀 המערכת פעילה ועובדת תקין",
    })

@app.route("/predict")
def predict():
    try:
        # בדיקה עצמית לפני חיזוי
        auto_heal_cycle()

        # חיזוי
        result = engine.get_prediction()

        return jsonify({
            "status": "success",
            "forecast": result
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "error": str(e)
        })

@app.route("/status")
def status():
    return jsonify(engine.get_status())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
