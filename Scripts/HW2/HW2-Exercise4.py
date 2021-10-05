# Identify a data set online (10 points) that you find interesting that could potentially be used for the final project; the main requirements is that there needs to be many (hundreds or more) data items with several identifiable variables, 
# at least one of which could be viewed as an output variable that you could predict from the others.

import pandas as pd 

data = pd.read_csv('RANDS3.csv') 
# Downloaded from https:////www.cdc.gov/nchs/rands/data.htm. 
data.head()
print(len(data)) # 2646

# Describe the dataset (10 points) Your answer should address (but not be limited to): 
# how many variables? 

print(list(data.columns))
# ['AASMEV', 'AASSMERYR', 'AASSMYR', 'AASSTILL', 'ACINERV', 'ACIRSTLS_A', 'ACIRSTLS_B', 'ACIRSTLS_C', 'ACISAD', 'ACIWTHLS', 'AGE', 'ANX_1', 'ANX_2', 'ANX_3', 'A_CHPAIN6M', 'A_ECIGEV_A', 'A_PAINLMT6', 'A_PHQA', 'A_PHQB', 'A_PHQC', 'A_PHQD', 'A_PHQE', 'A_PHQF', 'A_PHQG', 'A_PHQH', 'A_PHQIMP', 'A_PHSTAT', 'A_PROBE33_1', 'A_PROBE33_2', 'A_PROBE33_3', 'A_PROBE33_4', 'A_PROBE33_5', 'B_ECIGEV_A', 'B_GADA', 'B_GADB', 'B_GADC', 'B_GADD', 'B_GADE', 'B_GADF', 'B_GADG', 'B_GADIMP', 'B_PAINLMT3', 'B_PAIN_2', 'B_PHSTAT', 'B_PROBE34_1', 'B_PROBE34_2', 'B_PROBE34_3', 'B_PROBE34_4', 'B_PROBE34_5', 'CHLEV', 'CHLMDNW2', 'CHLYR', 'CaseID', 'DEP_1', 'DEP_2', 'DEP_3', 'DIBAGE_A', 'DIBEV_A', 'DIBINS_A', 'DIBPILL_A', 'DIBTYPE_A', 'DOV_OPIOID', 'EDUC', 'EMPLOY', 'GENDER', 'GESDIB_A', 'HOME_TYPE', 'HOUSING', 'HYPDIF_A', 'HYPEV', 'HYPMED2', 'HYPYR', 'INCOME', 'INJURY1', 'INJURY12', 'INJURY13', 'INJURY2', 'INJURY3', 'INJURY4', 'INJURY5', 'INJURY6_A', 'INJURY6_B', 'INJURY6_C', 'INJURY6_D', 'INJURY6_E', 'INJURY6_F', 'INTERNET', 'MARITAL', 'MODLNGNO_NUM', 'MODLNGNO_UNIT', 'MODNO_NUM', 'MODNO_UNIT', 'NEWLUNG', 'OPIOID1', 'OPIOID1_2', 'OPIOID2_1', 'OPIOID2_10', 'OPIOID2_11', 'OPIOID2_12', 'OPIOID2_13', 'OPIOID2_14', 'OPIOID2_15', 'OPIOID2_16', 'OPIOID2_17', 'OPIOID2_18', 'OPIOID2_19', 'OPIOID2_2', 'OPIOID2_20', 'OPIOID2_21', 'OPIOID2_22', 'OPIOID2_23', 'OPIOID2_24', 'OPIOID2_25', 'OPIOID2_26', 'OPIOID2_27', 'OPIOID2_28', 'OPIOID2_29', 'OPIOID2_2_1', 'OPIOID2_2_10', 'OPIOID2_2_11', 'OPIOID2_2_12', 'OPIOID2_2_13', 'OPIOID2_2_14', 'OPIOID2_2_15', 'OPIOID2_2_16', 'OPIOID2_2_17', 'OPIOID2_2_18', 'OPIOID2_2_19', 'OPIOID2_2_2', 'OPIOID2_2_20', 'OPIOID2_2_21', 'OPIOID2_2_22', 'OPIOID2_2_23', 'OPIOID2_2_24', 'OPIOID2_2_25', 'OPIOID2_2_26', 'OPIOID2_2_27', 'OPIOID2_2_28', 'OPIOID2_2_29', 'OPIOID2_2_3', 'OPIOID2_2_30', 'OPIOID2_2_31', 'OPIOID2_2_32', 'OPIOID2_2_33', 'OPIOID2_2_34', 'OPIOID2_2_35', 'OPIOID2_2_36', 'OPIOID2_2_4', 'OPIOID2_2_5', 'OPIOID2_2_6', 'OPIOID2_2_7', 'OPIOID2_2_8', 'OPIOID2_2_9', 'OPIOID2_2_NONE_FIRST', 'OPIOID2_2_NONE_FOURTH', 
# 'OPIOID2_2_NONE_SECOND', 'OPIOID2_2_NONE_THIRD', 'OPIOID2_3', 'OPIOID2_30', 'OPIOID2_31', 'OPIOID2_32', 'OPIOID2_33', 'OPIOID2_34', 'OPIOID2_35', 'OPIOID2_36', 'OPIOID2_4', 'OPIOID2_5...]
len(list(data.columns))
# There are 415 variables. 
