import pandas as pd
import os





def table():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cwd = os.path.join(BASE_DIR, "datasource") 
    cwd = os.path.join(cwd, "Reportes.xlsx") 
    data = pd.read_excel(cwd,index_col=0)
    data = data.to_html()
    return data





