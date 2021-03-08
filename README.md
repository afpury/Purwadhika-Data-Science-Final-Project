## Final Project Job Connector Data Science
## Purwadhika Startup and Coding School 2020
# Telemarketing Term Deposit Prediction

### Term Deposit?

Term deposits are a major source of income for a bank. A term deposit is a cash investment held at a financial institution. Your money is invested for an agreed rate of interest over a fixed amount of time, or term. The bank has various outreach plans to sell term deposits to their customers such as email marketing, advertisements, telephonic marketing, and digital marketing.

### Why Telemarketing?

Telephonic marketing campaigns still remain one of the most effective way to reach out to people. However, they require huge investment as large call centers are hired to actually execute these campaigns. Hence, it is crucial to identify the customers most likely to convert beforehand so that they can be specifically targeted via call.

### And Our Goal?

The classification goal is to predict if the client will subscribe to a term deposit or not.


> ### Content
The data is related to the direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed by the customer or not


> # The Data:
> > ## Personal Data
1 - Age (numeric)<br>
2 - Job : Type of job (categorical)<br>
3 - Marital : Marital status (categorical)<br>
4 - Education : Last education (categorical)<br>
5 - Default: Has credit in default? (binary)<br>
6 - Balance: Average yearly balance, in euros (numeric)<br>
7 - Housing: Has housing loan? (binary)<br>
8 - Loan: Has personal loan? (binary)<br>
> > ## Related with the last contact of the current campaign:
9 - Contact: Contact communication type (categorical)<br>
10 - Day: Last contact day of the month (numeric)<br>
11 - Month: Last contact month of year (categorical)<br>
12 - Duration: Last contact duration, in seconds (numeric)<br>
> > ## Other attributes:
13 - Campaign: Number of contacts performed during this campaign and for this client (numeric)<br>
14 - Pdays: Number of days that passed by after the client was last contacted from a previous campaign (numeric)<br>
15 - Previous: Number of contacts performed before this campaign and for this client (numeric)<br>
16 - Poutcome: Outcome of the previous marketing campaign (categorical)<br>

> > ## Output variable (desired target):
17 - y - Has the client subscribed a term deposit? (binary)<br>

Citation
This dataset is publicly available for research. It has been picked up from the UCI Machine Learning with random sampling and a few additional columns.

Past Usage
The full dataset was described and analyzed in:

S. Moro, R. Laureano and P. Cortez. Using Data Mining for Bank Direct Marketing: An Application of the CRISP-DM Methodology.
In P. Novais et al. (Eds.), Proceedings of the European Simulation and Modelling Conference - ESM'2011, pp. 117-121, Guimarães, Portugal, October, 2011. EUROSIS.
Acknowledgement
Created by: Paulo Cortez (Univ. Minho) and Sérgio Moro (ISCTE-IUL) @ 2012. Thanks to Berkin Kaplanoğlu for helping with the proper column descriptions.


Workflow:

Data Analysis
Visualization
Insight & Conclusion

Data Cleaning :

Dropping unnecessary and unknown columns
Dropping rows with insignificant values
Imputing missing value with mode (based on the context)

Feature Engineering
Binning
Encoding

Model Building

Train Test Split<br>
Using pipeline for model building<br>
Creating base model (DTC, Log Reg, RFC)<br>
Hyperparameter tuning on all algorithm<br>
checking evaluation matrix on the tuned model<br>
Export the model with the best score<br>
Dashboard Building Using Flask

