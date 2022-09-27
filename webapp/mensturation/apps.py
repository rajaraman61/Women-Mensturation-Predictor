from django.apps import AppConfig
import os
from pathlib import Path
class MensturationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mensturation'

    ACTIVITY_MODEL = Path("model/gNB.sav")
    PERIOD_MODEL = Path("model/lstm_4000.h5")