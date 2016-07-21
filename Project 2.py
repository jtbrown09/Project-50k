#Project 2

# imports
import re
import os
import json
import pprint
import datetime
import pandas as pd
import numpy as np
%matplotlib inline
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

#Import CSV files
census_train = pd.read_csv("C:/Users/FGG851/Documents/Training/BDA Data Science Bootcamp/ct16_cap1_ds6/project_2/data/ad_placement/census-income.csv", header=None)

census_train.columns= ['age', 'class_of_worker', 'industry_recode','occupation_recode', 'education', 'wage_per_hour', \
                      'enroll_in_ed', 'marital', 'industry_cd', 'occupation_cd', 'race', 'hispanic_origin', 'sex', \
                      'labor_union', 'reason_unemployed', 'employ_stat', 'capital_gains', 'capital_losses', 'dividends', \
                      'tax_filer', 'region_prev_resid', 'state_prev_resid', 'household_stat','household_summary', 'weight',\
                      'change_in_msa', 'change_in_reg', 'move_within_reg', 'live_here_before', 'prev_resid_sunbelt',\
                      'num_person_worked', 'under_18', 'birth_country_dad', 'birth_country_mom', 'birth_country_self', \
                      'citizenship', 'owner_self_employed', 'veterans_admin', 'veterans_benefits', 'weekes_worked_year', 'year', \
                       'target']

census_train.head()

census_train_test = pd.read_csv("C:/Users/FGG851/Documents/Training/BDA Data Science Bootcamp/ct16_cap1_ds6/project_2/data/ad_placement/census-income-test.csv", header=None)
census_train_test.columns= ['age', 'class_of_worker', 'industry_recode','occupation_recode', 'education', 'wage_per_hour', \
                      'enroll_in_ed', 'marital', 'industry_cd', 'occupation_cd', 'race', 'hispanic_origin', 'sex', \
                      'labor_union', 'reason_unemployed', 'employ_stat', 'capital_gains', 'capital_losses', 'dividends', \
                      'tax_filer', 'region_prev_resid', 'state_prev_resid', 'household_stat','household_summary', 'weight',\
                      'change_in_msa', 'change_in_reg', 'move_within_reg', 'live_here_before', 'prev_resid_sunbelt',\
                      'num_person_worked', 'under_18', 'birth_country_dad', 'birth_country_mom', 'birth_country_self', \
                      'citizenship', 'owner_self_employed', 'veterans_admin', 'veterans_benefits', 'weekes_worked_year', 'year', \
                       'target']

census_train.info()

#Capital Gains to Household Summary
census_train_reformatted = census_train

#Capital_Gains & Capital_Losses & Dividends
#census_train_reformatted.dividends = census_train_reformatted.dividends.str.strip()
census_train_reformatted["net_capital_gains"] = census_train_reformatted.capital_gains - census_train_reformatted.capital_losses + census_train_reformatted.dividends
del census_train_reformatted['capital_gains']
del census_train_reformatted['capital_losses']
del census_train_reformatted['dividends']

#Tax_filer
census_train_reformatted.tax_filer = census_train_reformatted.tax_filer.str.strip()

census_train_reformatted.tax_filer.replace('Nonfiler',0, inplace=True)
census_train_reformatted.tax_filer.replace('Joint both under 65',1, inplace=True)
census_train_reformatted.tax_filer.replace('Single',1, inplace=True)
census_train_reformatted.tax_filer.replace('Joint both 65+',1, inplace=True)
census_train_reformatted.tax_filer.replace('Head of household',1, inplace=True)
census_train_reformatted.tax_filer.replace('Joint one under 65 & one 65+',1, inplace=True)

#Region_prev_resid
census_train_reformatted.region_prev_resid = census_train_reformatted.region_prev_resid.str.strip()

census_train_reformatted.region_prev_resid.replace('Not in universe',0, inplace=True)
census_train_reformatted.region_prev_resid.replace('South',1, inplace=True)
census_train_reformatted.region_prev_resid.replace('West',2, inplace=True)
census_train_reformatted.region_prev_resid.replace('Midwest',3, inplace=True)
census_train_reformatted.region_prev_resid.replace('Northeast',4, inplace=True)
census_train_reformatted.region_prev_resid.replace('Abroad',5, inplace=True)

#State_prev_resid
del census_train_reformatted['state_prev_resid']

#household_stat
del census_train_reformatted['household_stat']

#household_summary
census_train_reformatted.household_summary = census_train_reformatted.household_summary.str.strip()

census_train_reformatted.household_summary.replace('Householder',1, inplace=True)
census_train_reformatted.household_summary.replace('Child under 18 never married',0, inplace=True)
census_train_reformatted.household_summary.replace('Spouse of householder',0, inplace=True)
census_train_reformatted.household_summary.replace('Child 18 or older',0, inplace=True)
census_train_reformatted.household_summary.replace('Other relative of householder',0, inplace=True)
census_train_reformatted.household_summary.replace('Nonrelative of householder',0, inplace=True)
census_train_reformatted.household_summary.replace('Group Quarters- Secondary individual',0, inplace=True)
census_train_reformatted.household_summary.replace('Child under 18 ever married',0, inplace=True)

census_train_reformatted.info()

census_train_reformatted.tax_filer.value_counts()

print(census_train_reformatted.net_capital_gains[0:25])

census_train_reformatted.region_prev_resid.value_counts()
#household_stat
#household_summary

# Not in universe    183750
# South                4889
# West                 4074
# Midwest              3575
# Northeast            2705
# Abroad                530

census_train_reformatted.household_summary.value_counts()
#75475 householders
