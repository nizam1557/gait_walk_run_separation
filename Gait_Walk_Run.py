import pandas as pd
import numpy as np
import os
from scipy.signal import find_peaks

def label_gait(row):
    """Function to label the row as Walk or Run."""
    if row['Acc_X'] < 0.5 and row['Acc_Y'] < 0.5 and row['Acc_Z'] < 0.5:
        return 'Walk'
    else:
        return 'Run'

# Start the recursive search from the current directory
root_dir = '.'

# Navigate recursively through folders and subfolders
for dirpath, dirnames, filenames in os.walk(root_dir):
    for file in filenames:
        if file.endswith('.csv'):
            # Build the full file path
            full_path = os.path.join(dirpath, file)
            
            # Read the CSV file
            df = pd.read_csv(full_path)
            df['Gait_Type'] = df.apply(label_gait, axis=1)
            
            # Separate the DataFrame based on 'Gait_Type'
            walk_df = df[df['Gait_Type'] == 'Walk']
            run_df = df[df['Gait_Type'] == 'Run']
            
            # Save the walk and run data to separate Excel files
            walk_result_path = os.path.join(dirpath, f"Results_{file[:-4]}_Walk.xlsx")
            run_result_path = os.path.join(dirpath, f"Results_{file[:-4]}_Run.xlsx")
            
            walk_df.to_excel(walk_result_path, index=False)
            run_df.to_excel(run_result_path, index=False)