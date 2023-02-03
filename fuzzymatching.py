#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 17:12:38 2022

@author: rithwiksivadasan
"""


import pandas as pd
import requests
import re
import difflib 



men_file=pd.read_csv('menWithRace.csv')

scrapped=pd.read_csv('scrapped.csv')
