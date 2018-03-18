The project aims at building a machine learning model that will be able to classify the various hand gestures used for fingerspelling in sign language. In this user independent model, classification machine learning algorithms are trained using a set of image data. Various machine learning algorithms are applied on the datasets, including Convolutional Neural Network (CNN). 

<b>Introduction</b>

Sign Language consists of fingerspelling, which spells out words character by character, and word level association which involves hand gestures that convey the word meaning. Fingerspelling is a vital tool in sign language, as it enables the communication of names, addresses and other words that do not carry a meaning in word level association. In spite of this, fingerspelling is not widely used as it is challenging to understand and difficult to use. Moreover, there is no universal sign language and very few people know it, which makes it an inadequate alternative for communication.  

A system for sign language recognition that classifies finger spelling can solve this problem. Various machine learning algorithms are used and their accuracies are recorded and compared in this project.

<b>Algorithms used:</b>

Classification machine learning algorithms like SVM, Softmax Classifier are used for supervised learning, which involves labeling the dataset before feeding it into the algorithm for training. For this project, various classification algorithms are used: SVM, Softmax Classifier and CNN.

<b>Support Vector Machine (SVM) </b> 

In SVM, each data point is plotted in an n-dimensional space (n is the number of features) with the value of each feature being the value of a particular coordinate. The classification is done by finding a hyper-plane that differentiates the classes the best.

A multi-class SVM has been implemented by feeding the HOG features of the images into the SVM model.

<b>CNN</b>

Convolutional Neural Networks (CNN), are deep neural networks used to process data that have a grid-like topology, e.g images that can be represented as a 2-D array of pixels. A CNN model consists of four main operations: Convolution, Non-Linearity (Relu), Pooling and Classification (Fully-connected layer ).  

Convolution: The purpose of convolution is to extract features from the input image. It preserves the spatial relationship between pixels by learning image features using small squares of input data. It is usually followed by Relu.

Relu: It is an element-wise operation that replaces all negative pixel values in the feature map by zero. Its purpose is to introduce non-linearity in a convolution network.

Pooling: Pooling (also called downsampling ) reduces the dimesionality of each feature map but retains important data.

Fully-connected layer: It is a multi layer perceptron that uses softmax function in the output layer. Its purpose is to use features from previous layers for classsifying the input image into various classes based on training data.  

The combination of these layers is used to create a CNN model. The last layer is a fully connected layer.

<b>HoG (Histogram of Gradients):</b> 

 A feature descriptor is a representation of an image or an image patch that simplifies the image by extracting useful information and throwing away extraneous information.

 Hog is a feature descriptor that calculates a histogram of gradient for the image pixels, which is a vector of 9 bins (numbers ) corresponding to the angles: 0, 20, 40, 60... 160. The images are divided into cells, (usually, 8x8 ), and for each cell, gradient magnitude and gradient angle is calculated, using which a histogram is created for a cell. The histogram of a block of cells is normalized, and the final feature vector for the entire image is calculated.
