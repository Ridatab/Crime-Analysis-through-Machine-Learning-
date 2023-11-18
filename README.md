# Crime-Analysis-through-Machine-Learning-
ABSTRACT:
This project investigates machine-learning-based crime prediction. In this work, Telangana crime data for the last 15 years is analyzed using two different data-processing approaches. Machine-Learning predictive models, K-nearest neighbor and boosted decision tree, are implemented and a crime prediction accuracy between 39% to 44% is obtained when predicting crime in Vancouver.

INTRODUCTION:
Crime is a socio-economical problem affecting life quality and economic growth. The specifics of how crime is conducted changes depending on the type of society and community. Previous researches in crime prediction have found that factors like education, poverty, employment, and climate affect the crime rate. Vancouver is one of the most populous, ethnically-diverse, and multi-cultural urban cities in Canada. The overall crime rate in Vancouver dropped 1.5% in 2017, but high vehicle break-ins and theft is still an issue. Recently, the Vancouver Police Department (VPD) introduced a crime predictive model to predict crimes related to property break-ins and, once implemented, the city of Vancouver witnessed a 27% drop in residential break-ins. Crime prediction is a law enforcement technique that uses data and statistical analysis for the identification of crimes most likely to occur. 

OBJECTIVE:
The primary objective of this work is to create a prediction model that can accurately predict crime. 
In our research, two classification algorithms, K-Nearest Neighbor (KNN) and boosted decision tree, were implemented to analyze the VPD crime dataset compiled between 2003 and 2018 with more than 560,000 records.

EXISTING SYSTEM:
  Machine learning is the science of having computers make decisions without human intervention. 
  Recently, machine learning has been applied in self-driving cars, speech recognition, web search, and an improved understanding of the human genome. 
  It has also made predicting crime based on referenced data feasible. 
  Classification is a supervised prediction technique which allows for nominal class labels.
  Classification has been used in many domains including weather forecasting, medical care, finances and banking, homeland security, and business intelligence. 

PROPOSED SYSTEM:
  In the first approach, each neighborhood and crime category were given a unique number when a certain crime happens in a certain neighborhood.
  In the second approach, the neighborhood and the day of the week during which the crime was committed were given a binary number and marked as 1 when the crime happened on that day in that neighborhood, and 0 otherwise.
  
DATA SOURCE:
The original datasets were obtained from the open data catalog of the city of Vancouver. There are two datasets used for this project: crime and neighborhood. The crime dataset has been collected by the VPD since 2003 and is updated every Sunday morning. It provides information on the type of crime committed and the time and location of the offence. The neighborhood dataset contains the boundaries for the city’s 22 local areas in the Geographic Information System (GIS).

PREPROCESSING:
The original dataset needs to be preprocessed to fill the empty cells, delete unnecessary columns, and add several relevant features to the original and preprocessed datasets.

STATISTICAL ANALYSIS:
The distribution of the crime dataset described in based on year, month, and day. In Vancouver, the average number of crime incidents is around 31624 per year, 2720 per month, and 90 per day. The dataset tends to show a normal distribution as the time intervals lengthen. However, the graph of each day has an abnormal max value of 650 incidents, which is suspected as an outlier - and turns out to indicate the Stanley- Cup riot on June 15, 2011.

CLASSIFICATION:
After statistical analysis we classify the prediction values of the crime rate in Vancouver. Machine Learning predictive models KNN and boosted decision tree were used to obtain crime-prediction accuracy between 85% to 90%. The accuracy, complexity, and training time of algorithms were slightly different for different approaches and algorithms. Finally, we get the prediction of the Vancouver crime rate.

TECHNIQUE USED OR ALGORITHM USED:
  Support Vector Machine
    The objective of the support vector machine algorithm is to find a hyperplane in an N-dimensional space (N — the number of features) that distinctly classifies the data points. To separate the two classes of data points, there are many possible hyperplanes that could be chosen. Our objective is to find a plane that has the maximum margin, i.e., the maximum distance between data points of both classes. Maximizing the margin distance provides some reinforcement so that future data points can be classified with more confidence
