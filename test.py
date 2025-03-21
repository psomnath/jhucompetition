import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from pathlib import Path
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.stylable_container import stylable_container  #
from streamlit_gsheets import GSheetsConnection
from sklearn import metrics
import hashlib
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload,MediaIoBaseDownload
from google.oauth2 import service_account
import datetime
import io
import pandas as pd

import re
import numpy as np
import pandas as pd
from collections import Counter
import itertools
from Bio.SeqUtils.ProtParam import ProteinAnalysis

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, roc_auc_score,
    confusion_matrix, classification_report
)

import matplotlib.pyplot as plt
import seaborn as sns