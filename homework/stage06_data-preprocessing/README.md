## Cleaning Strategy

### Missing values
- For numbers (age, income, score, extra_data), I filled the missing spots with the **median** of each column.  
- I also dropped rows if they had too many missing cells. I used a rule that at least 80% of the columns must have data. This way, rows with too many blanks are removed.

### Scaling
- I scaled the numeric columns with **z-score** (mean = 0, std = 1).  
- I picked z-score because it keeps the shape of the data and works better if values have very different ranges. Min-max would also work, but I wanted something standard.

### Path and steps
1. Start with raw file in `data/raw/`  
2. Apply cleaning functions in the notebook  
3. Save the cleaned file into `data/processed/`  

### Notes and trade-offs
- `zipcode` and `city` are text info, I didn’t scale them.  
- `extra_data` had lots of missing values. I filled it with median first, then applied the drop rule. This way I don’t lose all rows right away.  
- Some rows are removed, but it keeps the dataset more reliable.  

