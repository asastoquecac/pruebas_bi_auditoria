import pandas as pd
# import numpy as np

df = pd.read_excel(rf'C:\Users\ksastoque\Music\nb\pautomate\py_tests\data\input_test.xlsx')

def multiplicacion(d):
    z = d['x'] * d['y']
    return z

df['z'] = df.apply(multiplicacion, axis=1)
df.to_excel(rf'C:\Users\ksastoque\Music\nb\pautomate\py_tests\data\output_test.xlsx', index=False)