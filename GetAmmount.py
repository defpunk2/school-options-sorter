import pandas as pd
from collections import Counter

def GetAmmount(x):
    amountdict = {}
    df = pd.read_csv(x, header=None)
    subjects = df.iloc[:, 1:].to_numpy().flatten()  
    subjects = list(subjects)
    subject_counts = Counter(subjects)
    for sub,num in subject_counts.items():
        amountdict.update({sub:num})

    return(amountdict)
