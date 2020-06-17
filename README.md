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

If you find this repository useful, please cite the following paper:
TBD
