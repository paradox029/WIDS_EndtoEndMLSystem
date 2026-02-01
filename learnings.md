# Objective of the project

The primary objective of the project so far has been to create a machine learning model that can reliably distinguish between leaves of different plants, including ones that are diseased using the "plantvillage dataset" available on kaggle.

# Approach so far

We first started off with basic EDA in the first week. We went ahead and looked at the structure of the data, recognising that major imbalance exists between the classes. This imbalance would need additional techniques later in the training process so 
as to not have the model be biased towards those classes with a higher number of samples. 

In the second week, we used classical ML models such as Support Vector Machines and Random Forest to classify the data. Here, the effects of the class imbalance were prominent as metrics such as the F1-score were looking pretty bleak for some classes
with lesser examples for the model to learn from. 

The third week was our introduction to Deep Learning, more specifically, Convolutional Neural Networks that bring the power of conventional neural networks over to the domain of image classification. This is where we really started seeing some great results in
terms of accuracies and macro averages. 

Onto the fourth week, we put our models against real world constraints of privacy and distributed data which is solved using Federated Learning, a concept that allows a central model to train on decentralised data distributed across multiple devices or clients. To simulate such constraints we used the Flower library by creating client and server app proxies. 

For the final week, we explored the concept of differentiating the training from the inference. To that end, we used Streamlit to visualise and analyse the performance of the Federated Learning model across training rounds. 

# The Weeks in Detail

## Week 1

Here, we primarily wanted to gauge the structure and the nature of our dataset. We started off with checking the number of examples in each class within the color folder and then visually examining them. This was also our first introduction to parrallel processing, 
using the daskbag library which uses a technique called lazy computation that waits until the compute method is called to extract the data. 
Going through the other folders we found an extra image in the segmented folder, which did not seem to be problematic upon inspection.
We also searched for blurry images using the Variance of Laplacian method which includes taking the convolution of an image with the Laplacian kernel and then calculating the variance to obtain the blur score. 
Finally, we used an open source library called clustimage to cluster the images belonging to the Tomato family (which had the most amount of disease folders and a healthy folder as well) within the HOG (Histogram of Oriented Gradients) feature space. We observed that the classes were quite
overlapping at the borders, an observation that would help us in the following week's training process. 

## Week 2

In week 2, we trained a few models such as SVC, LinearSVC, SGDClassifier and RandomForestClassifier available through the scikit learn library. Here, once again we used the HOG feature space followed by PCA (Principal Component Analysis) to use only those features 
that explained 95% of the variance within the dataset. On running the different models on this dataset, our accuracies were capped at around 75% with the macro averages at around 70%. 
This led us to use a technique known as BorderlineSMOTE, a special type of SMOTE, that creates synthetic minority samples only at the borders thus providing a more prominent boundary and a greater number of support vectors from SVM based algorithms. 
Following this we ran the models once again, but SVC, due to its radial basis function kernel having to calculate a lot of pairwise distances (n^2), took a lot of time. So we tried to approximate the RBF using the Nystroem object coelesced with an SGD classifier. 
The best performance we shown by the RandomForestClassifier with an accuracy of 82% and a macro f1 average of 81%. 

## Week 3 

This week we used Tensorflow to build a CNN and also to use transfer learning with MobileNetV2 as the base model. The simple CNN, only a few layers deep, initially showed signs of overfitting with large differences between the training accuracy and the validation accuracy.
So we used data augmentation and dropout in the higher layers to deal with this issue, which, though lowered the training accuracy, dealt with the issue appreciably. The logic behind applying dropout to the higher layers was to introduce noise into the higher level features as opposed to lower level features such as edges which the lower layers would be dealing with and which would 
not exactly be beneficial as it would just add noise to the basic signal extraction part. 
Then we used MobileNetV2 as the base model, followed first by feature extraction keeping the whole model without the top classifier layer freezed and then adding a classifier layer to get the network customed to our end purpose. We followed this up by then unfreezing the top 54 layers of the network,
along with the classifier and then training the parameters associated with these layers. 
At the end, we ended up with an accuracy of 98% and a macro f1 average of 97% on the validation dataset. 

## Week 4 

In the fourth week, we utilised the Flower framework to create a Flower app that simulates client and server apps allowing us to bring the logic of how Federated Learning works in the real world into a single notebook. The concepts in this week primarily dealt with data loaidng and preparation, callbacks and what is known as 'Strategy'. Strategy encompasses the logic behind how both local model parameters as well as evaluation metrics from the client apps are coalesced to produce the required updates at the centralised model at the server. We also explored different partitioners primarily on the criteria of whether or not they create I.I.D (Independent and Identically Distributed) partitions. 
We observed that due to smaller datasets and class imbalance, as expected, the accuracies are lower than what we got when training on a centralised data set. Moreover, due to GPU constraints on Kaggle, we also could not get a maximally good result. 
This final model, we saved, along with the metrics, which we shall use in the fifth week to run the Streamlit visualisations. 

## Week 5

We wrapped up the project in the final week by separating the inference of the model from the training itself. To compare the performance across rounds we used a Streamlit app to create a line chart that visualised the accuracies and losses across multiple rounds. This allowed us to see that though the accuracies were less, the overall upward trend displayed that the Federated Learning model was working as required, proving that even if we could not achieve the best results due to resource constraints, we were atleast on the right track. 
This concluded our project that went from basic data analytics right to real world training and inference. 


THANK YOU!
