# DVF database analysis

This project gathers data.gouv.fr open source data.

To get more data, I choose to compile all years available (from 2015 to 2020).

I also choose to retrieve Paris' property values (department = 75) and to focus on apartments' and houses' sales.

## Model's choice

Scikit-learn module and more especially Random Forest regressor algorithm has been chosen.  

Continuous data have been normalized and categorical data have been categorized.

## Use

Install dependencies

```bash
make json
```



