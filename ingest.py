import pandas as pd
import os

def ingest(path: str):

    df = pd.DataFrame(columns=['phrase', 'sentiment'])

    for dirpath, dirname, filenames in os.walk(path):

        for file in filenames:

            if file.endswith('.txt'):

                with open(os.path.join(dirpath, file), 'r') as f:

                    df = df._append({'phrase': f.read(), 
                                    'sentiment': os.path.basename(dirpath)}, 
                                    ignore_index=True)
    
    df.to_csv(f"{path}_dataset.csv", index=False)



ingest("test")
ingest("train")
