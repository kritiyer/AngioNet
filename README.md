# AngioNet
Semantic segmentation network for X-ray angiography images, containing a custom angiographic pre-processing network coupled with Deeplabv3+.

## Pre-requisites 
Tensorflow 2.0 or higher 

Python 2 or 3

This code has been tested using Tensorflow 2.0rc on Python 3.5 and Tensorflow 2.1 on Python 3.7.

## Installation
If required, install Tensorflow using:
```bash
pip install tensorflow==2.1  #tensorflow-gpu==2.1 if using GPUs for training (highly encouraged)
```
The model code can be installed using
```bash
git clone https://github.com/kritiyer/AngioNet.git
```

## How to use

```python
import tensorflow as tf
from AngioNet_model import AngioNet

model = AngioNet(L1=0, L2=0, DL_weights=None)

#expected time to load model: 8-10 seconds on a CPU, 15-17 seconds on a multi-GPU configuration
```
The output is an untrained model with AngioNet architecture that you can fine-tune with your own data using the keras model API (https://www.tensorflow.org/api_docs/python/tf/keras/Model). To use a pre-trained model, please see: Software as a Service Platform.

If training on your own data, please ensure images are 512x512 grayscale images. The input images should be normalized to the range [0,1]. Label images are expected to be binary images where 0 is a background pixel and 1 is a vessel pixel.

## Software as a Service Platform 
We are in the process of creating a Software as a Service platform to allow anyone to segment their images with our optimized weights. For further information, please contact `techtransfer@umich.edu`

## Citation
If you find this repository useful, please cite the following paper:
```
AngioNet: A Convolutional Neural Network for Vessel Segmentation in X-ray Angiography. Iyer, K., Najarian, C.P., Fattah, A.A., et al. Sci Reports. 11, 18066 (2021). https://doi.org/10.1038/s41598-021-97355-8
```
(c) 2018 The Regents of the University of Michigan
    AngioNet: A Convolutional Neural Network for Vessel Segmentation in X-ray Angiography
    Computational Vascular Biomechanics Lab - https://bloodflow.engin.umich.edu/  
    This software is provided for use solely under the PolyForm Noncommercial License 1.0.0
