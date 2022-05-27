# Model building
## Project: Natural Language Processing with Disaster tweets

### Install

This project requires **Python** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [tensorflow](https://www.tensorflow.org/install/)
- [transformers](https://huggingface.co/docs/transformers/installation)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://jupyter.org/install.html).

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](https://www.anaconda.com/download/) distribution of Python, which already has the above packages and more included. 

### Code

code is provided in the `NLP w Disaster tweets feat. DistilBERT.ipynb` notebook file. You will also be required to use the included `train.csv` and `test.csv` datasets file to complete your work. 

### Run

In a terminal or command window, navigate to the top-level project directory `Sentiment Analysis of NLP with Disaster tweets/` (that contains this README) and run one of the following commands:

```bash
ipython notebook NLP w Disaster tweets feat. DistilBERT.ipynb
```  
or
```bash
jupyter notebook NLP w Disaster tweets feat. DistilBERT.ipynb
```
or open with Juoyter Lab
```bash
jupyter lab
```

This will open the Jupyter Notebook software and project file in your browser.

### Data

The datsets are taken from the Kaggle Competition and the train dataset contains 891 data-points with 12 features with 'Survived' being the target variable and test dataset contains 418 datapoints with [Kaggle](https://www.kaggle.com/competitions/titanic/data).

**Features**
1. `text`: Tweets


**Target Variable**
1. `Target`: Disaster or not; 0 = Not a Disaster, 1 = Disaster
