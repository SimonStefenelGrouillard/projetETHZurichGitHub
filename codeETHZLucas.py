#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 15:43:44 2022

@author: simonstefenel
"""

##____________________CHOICE OF CONTROL COHORT AND PSEUDO-ONSETS OF SEPSIS_____
## adaptation of Julianne Klatt's code


##_________________________________Packages____________________________________

import datetime          as     dt
#import matplotlib.pyplot as     plt
import numpy             as     np
import pandas            as     pd

from   pathlib           import Path


##_________________________________Directories_________________________________

data_path=r'/Volumes/borgwardt/Projects/sepsis/HiRID/hirid-a-high-time-resolution-icu-dataset-1.1.1/merged_stage/merged_stage/parquet/'


##_________________________________Data________________________________________

core_data=Path(data_path+'part-1.parquet')
core_df=pd.read_parquet(core_data)


##_________________________________Stay_Time Alignment_________________________

lab_values=[col for col in core_df.columns if col not in ["patientid","datetime"]]


##_________________________________Lab Value availability______________________

(~pd.isnull(core_df.loc[:, lab_values])).mean() > 0.075

