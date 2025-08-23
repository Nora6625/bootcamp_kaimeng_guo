### Reflection: Outliers + Risk

- **Methods & thresholds chosen**
  - IQR with k=1.5 (standard choice, balances false positives/negatives).
  - Z-score with threshold=3.0 (classical setting, assumes normality).
  - Winsorizing at 5%/95% quantiles to reduce extreme influence.

- **Assumptions**
  - IQR: distribution reasonably summarized by quartiles; k controls strictness.
  - Z-score: roughly normal distribution; sensitive to heavy tails.
  - Winsorizing assumes extreme tails are noise rather than true signal.

- **Impacts on results**
  - Summary statistics: mean is highly sensitive to outliers.

- **Risks**
  - If outliers are actually meaningful events, removing them could erase important signals.
  - Winsorizing keeps sample size but may underestimate variance.
  - Method choice depends on context: anomaly detection vs. robust modeling.

**Conclusion:** 
  - Outlier treatment must balance robustness with information retention. 
