# California Housing Prices: Linear Regression Analysis
This project fits a linear regression model to predict the median house values in California housing blocks using data from the 1990 U.S. Census. It explores the influence of geographic, demographic, and economic variables on housing prices, including proximity to major cities Los Angeles and San Francisco.

## You can read the report [here.](report.pdf)

## Overview
- Objective: Predict median house values using linear regression and investigate which features most influence housing prices.
- Data: 1990 U.S. Census data from "Sparse Spatial Autoregressions" by Pace R. Kelly and Ronald Barry.
- Sample Size: 19,675 housing blocks (after removing price-capped entries at $500,001).

## Feature Set
- x_dist: Weighted exponential proximity to Los Angeles and San Francisco
- x_pph: Population per household.
- x_tbi: Total block income (median income * population)
- x_mi: Median income.
- x_rph: Rooms per household.
- x_bpr: Bedrooms per room.

## Key Findings
- Positive predictors: Proximity to Los Angeles and San Francisco, rooms per household, bedrooms per room, and median income
- Negative predictors: Population per household, and total block income
- Model shows moderate explanatory power, with $R^2 = 0.5443$.

