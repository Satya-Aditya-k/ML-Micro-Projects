# Model building, evaluation using Pytorch
## Project: MNIST Digit Recognizer

### Install

This project requires **Python** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [Pytorch](https://pytorch.org/get-started/locally/)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://jupyter.org/install.html).

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](https://www.anaconda.com/download/) distribution of Python, which already has the above packages and more included. 

### Code

Template code is provided in the `TPS_1_2022_CatBoost.ipynb` notebook file. You will also be required to use the included `train.csv` and `test.csv` datasets file to successfully execute the code. 

### Run

In a terminal or command window, navigate to the top-level project directory `MNIST Digit Recognizer/` (that contains this README) and run one of the following commands:

```bash
ipython notebook MNIST_pytorch_NN.ipynb
```  
or
```bash
jupyter notebook MNIST_pytorch_NN.ipynb
```
or open with Juoyter Lab
```bash
jupyter lab
```

This will open the Jupyter Notebook software and project file in your browser.

### Data

The datsets are taken from the Kaggle Competition Digit Recognizer, our goal is to correctly identify digits from a dataset of tens of thousands of handwritten images.  [Kaggle](https://www.kaggle.com/competitions/digit-recognizer/code).

**Features**
Each image is 28 pixels in height and 28 pixels in width, for a total of 784 pixels in total

**Target Variable**
Target is the `label` column with labels from 0-9
