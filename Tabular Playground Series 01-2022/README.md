# EDA and Model Evaluation of Time Series using Catboost Regressor
## Project: Tabular Playground Series 01-2022

### Install

This project requires **Python** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [seaborn](https://seaborn.pydata.org/)
- [Catboost](https://catboost.ai/en/docs/)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://jupyter.org/install.html).

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](https://www.anaconda.com/download/) distribution of Python, which already has the above packages and more included. 

### Code

Template code is provided in the `TPS_1_2022_CatBoost.ipynb` notebook file. You will also be required to use the included `train.csv` and `test.csv` datasets file to complete your work. 

### Run

In a terminal or command window, navigate to the top-level project directory `Tabular Playground Series 01-2022/` (that contains this README) and run one of the following commands:

```bash
ipython notebook TPS_1_2022_CatBoost.ipynb
```  
or
```bash
jupyter notebook TPS_1_2022_CatBoost.ipynb
```
or open with Juoyter Lab
```bash
jupyter lab
```

This will open the Jupyter Notebook software and project file in your browser.

### Data

The datsets are taken from the Kaggle Competition Tabular Playground Series - Jan 2022,time series prediction in which we are going to predict the sales of two fictitious kaggle stores in different countries and predict which store sells better in the future, the train dataset contains 26.3k data-points with 6 features with 'num_sold' being the target variable and test dataset contains 6570 datapoints with link here: [Kaggle](https://www.kaggle.com/competitions/tabular-playground-series-jan-2022/data).

**Features**
1. `row_id`: row_id
2. `Date`: Date
3. `country`: country
4. `store`: store
5. `product`: product

**Target Variable**
1. `num_sold`: numbers sold
