import pandas as pd
import numpy as np
columnns=["Movie ID","Titles","Gengers"]
df=pd.read_csv('untitled.csv',engine = 'python',names=columnns, delimiter='::')
