# -*- coding: utf-8 -*-
import pandas as pd
import os
from io import StringIO
import pyspc
_ROOT = 'pyspc/sampledata/'

def read_csv(filename):
    data = pyspc.__loader__.get_data(filename).decode('utf-8')
    return pd.read_csv(StringIO(data))

pistonrings = read_csv(os.path.join(_ROOT, 'pistonrings.csv')).values
    
diameter = read_csv(os.path.join(_ROOT, 'diameter.csv')).values

parts = read_csv(os.path.join(_ROOT, 'parts.csv')).values
    
sizes = read_csv(os.path.join(_ROOT, 'sizes.csv')).values
    
chemical = read_csv(os.path.join(_ROOT, 'chemical.csv')).values
    
newproduct = read_csv(os.path.join(_ROOT, 'newproduct.csv')).values
    
waitingTime = read_csv(os.path.join(_ROOT, 'waitingTime.csv')).values

sandbox = read_csv(os.path.join(_ROOT, 'sandbox.csv')).values

canjuice = read_csv(os.path.join(_ROOT, 'canjuice.csv')).values

circuits = read_csv(os.path.join(_ROOT, 'circuits.csv')).values

inspection = read_csv(os.path.join(_ROOT, 'inspection.csv')).values

PaintMaterial = read_csv(os.path.join(_ROOT, 'PaintMaterial.csv')).values

Thickness = read_csv(os.path.join(_ROOT, 'thickness.csv')).values

viscosidade = read_csv(os.path.join(_ROOT, 'Viscosidade.csv')).values

plastic = read_csv(os.path.join(_ROOT, 'hotelling.csv')).values

experiment = read_csv(os.path.join(_ROOT, 'experiment.csv')).values

mewma_example = read_csv(os.path.join(_ROOT, 'dados.csv')).values
