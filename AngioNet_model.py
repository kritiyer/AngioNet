from tensorflow.keras.layers import Input, Conv2D, concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.regularizers import l1_l2
from deeplab_model import Deeplabv3


#DL_weights can be None, "pascal_voc", or "cityscapes".
#These weights are identical to those from the original Deeplabv3+ paper
#L1 and L2 refer to the regularization weights for L1-L2 regularization

def AngioNet(L1=0., L2= 0., DL_weights=None):
    inputs = Input(shape=(512,512,1))
    activation_func = None
    X1 = Conv2D(1, (5,5), strides=(1, 1), padding='same', dilation_rate=(1, 1), activation=activation_func,
                use_bias=False, data_format="channels_last")(inputs)
    X2 = Conv2D(1, (3,3), strides=(1, 1), padding='same', dilation_rate=(1, 1), activation=activation_func,
                use_bias=False, data_format="channels_last")(X1)
    X3 = Conv2D(16, (5,5), strides=(1, 1), padding='same', dilation_rate=(1, 1), activation=activation_func,
                use_bias=False, data_format="channels_last")(X2)
    X4 = Conv2D(16, (5,5), strides=(1, 1), padding='same', dilation_rate=(1, 1), activation=activation_func,
                use_bias=False, data_format="channels_last")(X3)
    X5 = Conv2D(16, (5,5), strides=(1, 1), padding='same', dilation_rate=(1, 1), activation=activation_func,
                use_bias=False, data_format="channels_last")(X4)
    X6 = Conv2D(1, (3,3), strides=(1, 1), padding='same', dilation_rate=(1, 1), activation='tanh',
                use_bias=False, data_format="channels_last")(X5)
    X7 = concatenate([X6, X6, X6], axis=3)

    unsharp_mask_model = Model(inputs=inputs, outputs=X7)
    unsharp_mask_model._name = "Preprocessing_Network"

    deeplab_model = Deeplabv3(weights=DL_weights, backbone="xception", input_shape = (512,512,3), classes=2)
    for layer in deeplab_model.layers:
        layer.kernel_regularizer = l1_l2(l1 = L1, l2=L2)

    combined_inputs = Input(shape=(512, 512, 1))
    unsharp_mask_img = unsharp_mask_model(combined_inputs)
    deeplab_img = deeplab_model(unsharp_mask_img)
    model = Model(combined_inputs, deeplab_img)

    return model
