# AngioNet
Semantic segmentation network for X-ray angiography images, containing a custom angiographic pre-processing network coupled with Deeplabv3+.

## Pre-requisites 
Tensorflow 2.0 or higher

## How to use

AngioNet was created using the keras model API.

```
import tensorflow as tf
from AngioNet_model import AngioNet

model = AngioNet(L1=0, L2=0, DL_weights=None)

```

## Software as a Service Platform 
We are in the process of creating a Software as a Service platform to allow anyone to segment their images with optimized weights. For further information, please contact `techtransfer@umich.edu`

## Citation
If you find this repository useful, please cite the following paper:
```
AngioNet: A Convolutional Neural Network for Vessel Segmentation in X-ray Angiography. Iyer, K., Najarian, C.P., Fattah, A.A., et al.
```
(c) 2018 The Regents of the University of Michigan
    AngioNet: A Convolutional Neural Network for Vessel Segmentation in X-ray Angiography
    Computational Vascular Biomechanics Lab - https://bloodflow.engin.umich.edu/
    This software is provided for use solely under the PolyForm Noncommercial License 1.0.0
