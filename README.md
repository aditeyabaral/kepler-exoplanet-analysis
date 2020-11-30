# kepler-exoplanet-analysis

Analysis of Kepler Objects of Interest using Machine Learning for Exoplanet Identification. 

This repository contains the source code as well as the visualisations and models created as a part of the Final Project for the Data Analytics course (UE18CS312) at PES University.

The Final Report for the document can be found [here](https://github.com/aditeyabaral/kepler-exoplanet-analysis/blob/master/report/057_Meu_Kepler_Exoplanet_Search_Results-FinalReport.pdf).

## Team Members 

[Aditeya Baral](https://github.com/aditeyabaral) <br>
[Ameya Rajendra Bhamare](https://github.com/ameyabhamare) <br>
[Saarthak Agarwal](https://github.com/saarthak-agarwal)
 
## Directory Structure

```
kepler-exoplanet-analysis
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

├── presentation
    └── Presentation and Video

├── report
    ├── Final Report
    └── Plagiarism Check

└── scripts
    ├── getPlotsMatplotLib.py
    └── getPlotsPlotly.py

```

## How to run the code?

**Advisory**: Each model training script takes a long time to run, sometimes almost an hour. This is because of cross-validation
and GridSearch.

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

## Exoplanet Analysis
For several decades, planet identification has been a
task performed by specialized astronomers and domain experts.
With the advent of computational methods and access to satellite data from space missions, this trend has changed. For instance, **NASA’s Exoplanet Exploration Program** has provided us with vast amounts of data on celestial objects to assist in space exploration. One such mission of interest is the Kepler mission.


**Over 4300 transiting exoplanets have been identified since the
commencement of the mission in 2007**. It’s focus lay on exploring planets and planetary systems. It has provided us with a catalog of discoveries that help in computing planet occurrence rates as a function of size, star type, insolation flux and orbital period. 

## The Kepler Mission
**[The Kepler Space Telescope](https://www.nasa.gov/mission_pages/kepler/main/index.html) launched in 2009, has been the
most successful telescope to aid the discovery of exoplanets**. It has identified several thousand objects of interest, with over 4300 of them confirmed exoplanets. **The mission has been designed to survey a portion of the Milky Way galaxy and discovers hundreds of Earth-size and smaller planets in or near the habitable zone**. It additionally determines the fraction of the billions of stars in our galaxy that might have their own solar system. 

The satellite was officially retired in October 2018 because it ran out of fuel. Years later, the statistical data that Kepler produced continues to produce new exoplanet discoveries.

## Dataset
Measurements from the Kepler satellite are available for public domain use. These records are maintained by CalTech in the [Kepler Cumulative Object of Interest (KCOI)](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=cumulative) table. The KCOI table contains 50 features recorded from Kepler data.

## Predictive Modelling
This study focuses on a binary classification of Objects of Interest as “FALSE POSITIVE” or “CONFIRMED” exoplanets. NASA uses the label of “FALSE POSITIVE” to indicate the satellite incorrectly tracked an object. We do not consider the observations labelled as “CANDIDATE” since these are yet to be labelled by NASA and hence, are unknown to us. For our analysis, we have used four models, each with its own unique characteristics to tackle the problem at hand from different angles. 

The four models used are 
1. Support Vector Machine
2. Random Forest
3. AdaBoost
4. Feed-Forward Neural Network.

## Evaluation of Model Performance

To counter the imbalance of the dataset, we propose different
evaluation metrics, which take in account the imbalance.
These include the **F1 Score, Cohen Kappa score, Balanced
Accuracy Score and finally the Confusion Matrix**.

Additionally, to test out our classifier on different sets, we
use **K-Fold cross-validation across our entire dataset** to ensure that we are not underfitting our classifier by introducing high bias. 

Since the dataset is imbalanced, we again use both -

* A non-stratified split
* A stratified split

This is to ensure that within each fold the number of positive and negative examples are equal. We measure our classifier’s performance across each split and finally take the mean of the performance achieved.

## Model Results
We obtain two sets of results, when we consider and omit the attributes corresponding to error metrics. We can conclude that the models built with the Error attributes tend to do better than the models built after removing the error attributes. Although all models perform almost equally well, the AdaBoost classifier outperforms the rest.

### With Error Attributes

| Model          | Stratified F-1 Score | Non-Stratified F-1 Score |
|----------------|----------------------|--------------------------|
| SVM            | 98.28%               | 98.31%                   |
| Random Forest  | 97.68%               | 97.61%                   |
| AdaBoost       | 98.01%               | 98.17%                   |
| Neural Network | 98.16%               | 98.27%                   |

### Without Error Attributes

| Model          | Stratified F-1 Score | Non-Stratified F-1 Score |
|----------------|----------------------|--------------------------|
| SVM            | 97.72%               | 97.66%                   |
| Random Forest  | 98%                  | 98.13%                   |
| AdaBoost       | 98.03%               | 98.11%                   |
| Neural Network | 97.78%               | 97.46%                   |

## Observations and Conclusions

1. We observe that there is significant overlap between the different classes of exoplanets, making it increasingly difficult for scientists to predict their habitability.

2. We also observe that most of the exoplanet characteristics are independent of each other, with very few attributes having significant correlation.

3. A difference in feature rank importance was observed across the different algorithms, showing the differences in the working of each model.

4. Additionally, we see that machine learning algorithms prefer categorical variables for classification as it allows them to form decisions faster and reduce entropy quicker.