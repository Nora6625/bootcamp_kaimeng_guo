## Data Cleaning Strategy

The dataset is cleaned following a systematic preprocessing approach:

1. **Filling Missing Values**: Numerical columns ('age',`income`, `score`) are filled with their median values. This choice mitigates the impact of extreme values compared to the mean.
2. **Dropping Columns**: Columns with more than 50% missing values (`extra_data`) are dropped.
3. **Normalization**: Numerical columns are scaled to the [0,1] range using MinMaxScaler for consistent comparison and modeling.
4. **Preserving Categorical Data**: Text columns (`zipcode`, `city`) are retained as-is for potential categorical analysis.
5. **Assumptions**: It is assumed that median imputation preserves the central tendency of numerical features and that deleted columns are non-essential.
