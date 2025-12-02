# =============================================================
# engine_master.py — NASA_ULTRA_SYSTEM_CLEAN_V2
# מנוע־על שמפעיל את כל מנועי החיזוי והמערכת הפנימיים
# =============================================================

import json
import random
import traceback
from datetime import datetime

from prediction_engine import PredictionEngine
from stats_engine import StatsEngine
from kira_engine import KiraEngine
from quantum_engine import QuantumEngine
from backup_engine import BackupEngine
from history_loader import HistoryLoader
from data_processor import DataProcessor
from auto_heal import auto_heal_cycle


class UltraEngine:

    def __init__(self):
        try:
            self.history = HistoryLoader().load_history()
            self.processor = DataProcessor(self.history)

            # כל המנועים
            self.stats = StatsEngine(self.history)
            self.prediction = PredictionEngine(self.history)
            self.kira = KiraEngine(self.history)
            self.quantum = QuantumEngine(self.history)
            self.backup = BackupEngine(self.history)

            self.last_status = {"init": "ok", "time": str(datetime.now())}

        except Exception as e:
            self.last_status = {"init": "failed", "error": str(e)}
            raise e

    # -----------------------------------------------------------
    # חיזוי מרכזי — משלב את כל המנועים
    # -----------------------------------------------------------
    def get_prediction(self):
        try:
            auto_heal_cycle()

            # 1. שכבה סטטיסטית
            stats_nums = self.stats.get_stats_prediction()

            # 2. שכבת דפוסים (PredictionEngine)
            pattern_nums = self.prediction.get_pattern_prediction()

            # 3. שכבת קירה רדינסקי
            kira_nums = self.kira.get_kira_prediction()

            # 4. שכבת Quantum
            quantum_nums = self.quantum.get_quantum_prediction()

            # שילוב השכבות
            combined = stats_nums + pattern_nums + kira_nums + quantum_nums
            flattened = [n for sub in combined for n in sub]

            # בחירת 6 מספרים חכמים
            final_main = sorted(list(set(random.sample(flattened, 6))))

            # מספר בונוס
            bonus = random.choice(flattened)

            # סט גיבוי
            backup_set = self.backup.get_backup_prediction()

            result = {
                "main": final_main,
                "bonus": bonus,
                "backup": backup_set,
                "timestamp": str(datetime.now())
            }

            self.last_status = {
                "last_prediction": "ok",
                "time": str(datetime.now())
            }

            return result

        except Exception as e:
            self.last_status = {
                "last_prediction": "failed",
                "error": str(e),
                "trace": traceback.format_exc()
            }
            raise e

    # -----------------------------------------------------------
    # סטטוס מערכת
    # -----------------------------------------------------------
    def get_status(self):
        return {
            "system": "NASA_ULTRA_SYSTEM_CLEAN_V2",
            "last_status": self.last_status,
            "history_size": len(self.history)
        }
