# EDA and Model building
## Project: Titanic - Machine Learning from Disaster

### Install

This project requires **Python** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [seaborn](https://seaborn.pydata.org/)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://jupyter.org/install.html).

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](https://www.anaconda.com/download/) distribution of Python, which already has the above packages and more included. 

### Code

Template code is provided in the `Titanic_dataset_EDA_ML.ipynb` notebook file. You will also be required to use the included `train.csv` and `test.csv` datasets file to complete your work. 

### Run

In a terminal or command window, navigate to the top-level project directory `boston_housing/` (that contains this README) and run one of the following commands:

```bash
ipython notebook boston_housing.ipynb
```  
or
```bash
jupyter notebook boston_housing.ipynb
```
or open with Juoyter Lab
```bash
jupyter lab
```

This will open the Jupyter Notebook software and project file in your browser.

### Data

The datsets are taken from the Kaggle Competition and the train dataset contains 891 data-points with 12 features with 'Survived' being the target variable and test dataset contains 418 datapoints with [Kaggle](https://www.kaggle.com/competitions/titanic/data).

**Features**
1. `pclass`: Ticket class of passenger
2. `sex`: Sex
3. `Age`: Age in years
4. `sibsp`: # of siblings / spouses aboard the Titanic
5. `parch`: # of parents / children aboard the Titanic
6. `ticket` : Ticket number
7. `fare`: Passenger fare
8. `cabin` : Cabin number
9. `embarked` : Port of Embarkation

**Target Variable**
1. `Survived`: Survival; 0 = No, 1 = Yes
