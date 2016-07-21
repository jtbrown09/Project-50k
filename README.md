# Project-50k

Figuring out Census Bureau data one column at a time...

DROP: age, birth_country_dad, birth_country_mom, birth_country_self, birth_country_self_cd, citizenship,class_of_worker,  education, industry_code, industry_recode, marital, move_within_reg, occupation_cd, occupation_recode, owner_self_employed, tgt_bin, target, veterans_admin, veterans_benefits, weeks_worked_year, year

GET DUMMIES: age_bucket, birth_country_dad_cd, birth_country_mom_cd, change_in_msa', 'change_in_reg',citizenship_cd, class_code, education_bucket, industry_major_cd, live_here_before, marital_code, occupation_cd_num, parents_country_cd, prev_resid_sunbelt region_prev_resid, under_18, weeks_worked_bin

NUMERIC: net_capital_gains,num_person_worked,tax_filer, wage_per_hour, household_summary, work_time_proxy

TARGET: target_bin
SAMPLE WEIGHT: weight
