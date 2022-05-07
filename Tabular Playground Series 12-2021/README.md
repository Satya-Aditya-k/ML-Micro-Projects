# Model building and Evaluation using Tensorflow
## Project: Tabular Playground Series 12-2021

### Install

This project requires **Python** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [Tensorflow](https://www.tensorflow.org/install)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://jupyter.org/install.html).

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](https://www.anaconda.com/download/) distribution of Python, which already has the above packages and more included. 

### Code

Template code is provided in the `TPS_12_2021_nn.ipynb` notebook file. You will also be required to use the included `train.csv` and `test.csv` datasets file to complete your work. 

### Run

In a terminal or command window, navigate to the top-level project directory `Tabular Playground Series 12-2021/` (that contains this README) and run one of the following commands:

```bash
ipython notebook TPS_12_2021_nn.ipynb
```  
or
```bash
jupyter notebook TPS_12_2021_nn.ipynb
```
or open with Jupyter Lab
```bash
jupyter lab
```

This will open the Jupyter Notebook software and project file in your browser.

### Data

The datsets are taken from the Kaggle Competition Tabular Playground Series - Dec 2021, time series prediction which deals with the prediction of the forest cover type based on different features and build a NN model using the tensorflow module, `train` consists of 4.00M datapoints and test consists of 1000k datapoints. The datasets can be found here:[Kaggle](https://www.kaggle.com/competitions/tabular-playground-series-dec-2021/data).

**Features**
1. `Elevation`: Elevation in meters
2. `Aspect`: Aspect in degrees azimuth
3. `Slope`: Slope in degrees
4. `Horizontal_Distance_To_Hydrology`: Horz Dist to nearest surface water features
5. `Vertical_Distance_To_Hydrology `: Vert Dist to nearest surface water features
6. `Horizontal_Distance_To_Roadways`: Horz Dist to nearest roadway
7. `Hillshade_9am`: (0 to 255 index) - Hillshade index at 9am, summer solstice
8. `Hillshade_Noon`:(0 to 255 index) - Hillshade index at noon, summer solstice
9. `Hillshade_3pm`:(0 to 255 index) - Hillshade index at 3pm, summer solstice
10.`Horizontal_Distance_To_Fire_Points`:Horz Dist to nearest wildfire ignition points
11.`Wilderness_Area`:(4 binary columns, 0 = absence or 1 = presence) - Wilderness area designation
12. `Soil_Type`:(40 binary columns, 0 = absence or 1 = presence) - Soil Type designation

**Target Variable**
1. `Cover_Type` (7 types, integers 1 to 7) - Forest Cover Type designation
