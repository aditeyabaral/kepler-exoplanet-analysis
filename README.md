# kepler-exoplanet-analysis

Analysis of Kepler Objects of Interest using Machine Learning for Exoplanet Identification.

## Team Members 

[Aditeya Baral](https://github.com/aditeyabaral)
[Ameya Rajendra Bhamare](https://github.com/ameyabhamare)
[Saarthak Agarwal(https://github.com/saarthak-agarwal)

## Exoplanet Analysis
For several decades, planet identification has been a
task performed by specialized astronomers and domain experts.
With the advent of computational methods and access to satellite
data from space missions, this trend has changed. For instance,
NASA’s Exoplanet Exploration program has provided us
with vast amounts of data on celestial objects to assist in space
exploration. One such mission of interest is the Kepler mission.
Over 3500 transiting exoplanets have been identified since the
commencement of the mission in 2007. It’s focus lay on exploring
planets and planetary systems. It has provided us with a catalog
of discoveries that help in computing planet occurrence rates
as a function of size, star type, insolation flux and orbital
period. This information is catalogued in the Cumulative Kepler
Object of Information table available for public domain use
on NASA’s exoplanet archive. Four basic models have been
compared. Namely, Support Vector Machines, Random Forest
Classifiers, AdaBoost and Deep Neural Networks. The AdaBoost
classifier was selected as the optimum machine learning model
and returned an F-1 score of 98% on the dataset.
 
## Directory Structure

root
├── data
    ├── [CLEANED]kepler-data.csv
    └── kepler-data.csv

├── docs
    ├── Project Guidelines and Requirements Documents

├── model
    ├── adaboost-error.model
    ├── adaboost.model
    ├── nn-model-error.h5
    ├── nn-model.h5
    ├── random-forest-error.model
    ├── random-forest.model
    ├── svm-error.model
    └── svm.model
   
├── notebook
    └── Notebooks containing data preprocessing, model training, visualisation and analysis

├── plots
    └── All possible plots based on preprocessing, visualisation and model training

├── report
    ├── Final Report
    └── Presentation

└── scripts
    ├── getPlotsMatplotLib.py
    └── getPlotsPlotly.py

## How to run the code?

1. Clone this repository
```bash
git clone https://github.com/aditeyabaral/kepler-exoplanet-analysis
```

2. Navigate to the repoand install the required dependencies.
```bash
cd kepler-exoplanet-analysis/
pip3 install -r requirements.txt
```

3. Open Jupyter Notebook in the notebook directory
```bash
cd notebook/
jupyter notebook
```

4. Run any notebook by executing all the code cells.

**Advisory**: Each model training script takes a long time to run, sometimes almost an hour. This is because of cross-validation
and GridSearch.