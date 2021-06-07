import pandas as pd
import numpy as np

file = pd.read_excel('output_code3.xlsx')

file['message_sent'] = np.zeros(file.shape[0])

file.to_excel('output_code3.xlsx',index=False)
