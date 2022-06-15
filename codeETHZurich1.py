#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 09:11:54 2022

@author: simonstefenel
"""

import glob
import math
import numpy as np
import os
import pandas as pd
import re
import shutil
import sys

import pyarrow as pa
import pyarrow.parquet as pq

data_path=r'/Volumes/borgwardt/Projects/sepsis/HiRID/'
#df=pd.read_parquet(data_path, engine='pyarrow')
#table = pa.Table.from_pandas(df)
#pq.write_table(table, data_path)

part=4

df_part = pd.read_parquet(os.path.join(data_path,'merged_stage','parquet', f'part-{part}.parquet'))
df_part['patientid'].count()

patientid = 3

def load_patient_index(path):
    df_ind = pd.read_csv(path)
    return { pid : part for (pid, part) in zip(df_ind['patientid'], df_ind['part'])}

pat_index = load_patient_index(os.path.join(data_path, 'merged_stage', 'merged_stage_index.csv'))