---
layout: page
title: The Y-Net
subtitle: An audio-visual CNN for singing voice separation
---

<div class="lead mb-0" align="justify" style="padding-bottom: 1em">
The Y-Net model consist of a U-Net conditioned with visual features.  
</div>

![Y-Net](../img/model.png)  

<div class="lead mb-0" align="justify" style="padding-bottom: 1em">
U-Net is an encoder-decoder architecture with skip-connections in between. The original U-Net was proposed for biomedical imaging. Each block has two convolutions followed by max-pooling in that work. Instead, we use a single 5x5 convolution with stride 1 and padding 2, batch normalization, relu and max-pooling.  
<br><br>
The video network consist of a set three  convolutional blocks. The first one is a 3D convolutional block which models spatio-temporal information (motion) meanwhile the latter blocks are 2D convolutional blocks which just makes use of the spatial information. 
<br><br>
The Y-Net takes as input a complex spectrogram and the video of  the target singer and  returns a complex mask. The complex product between the mask and and the mixture spectrogram allows to recover the singing voice corresponding to the singer chosen.  
Since it's a convolutional neural network, the duration of the track is limited by the gpu-memory. 
<br><br>
Detailed layers are shown below. 
</div>
<div style="padding-top: 1em" markdown="1">
```
VnNet(
  (encoder): Sequential(
    (0): ConvolutionalBlock(
      (layer): Sequential(
        (0): Conv2d(2, 32, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2), bias=False)
        (1): BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
      (ReLu): LeakyReLU(negative_slope=0.1, inplace=True)
      (MaxPooling): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    )
    (1): ConvolutionalBlock(
      (layer): Sequential(
        (0): Conv2d(32, 64, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2), bias=False)
        (1): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
      (ReLu): LeakyReLU(negative_slope=0.1, inplace=True)
      (MaxPooling): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    )
    (2): ConvolutionalBlock(
      (layer): Sequential(
        (0): Conv2d(64, 128, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2), bias=False)
        (1): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
      (ReLu): LeakyReLU(negative_slope=0.1, inplace=True)
      (MaxPooling): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    )
    (3): ConvolutionalBlock(
      (layer): Sequential(
        (0): Conv2d(128, 256, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2), bias=False)
        (1): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
      (ReLu): LeakyReLU(negative_slope=0.1, inplace=True)
      (MaxPooling): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    )
  )
  (decoder): Sequential(
    (0): TransitionBlock(
      (layer): Sequential(
        (0): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
        (1): BatchNorm2d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
      (ReLu): ReLU(inplace=True)
      (AtrousConv): Upsample(scale_factor=2.0, mode=bilinear)
    )
    (1): AtrousBlock(
      (layer): Sequential(
        (0): Conv2d(512, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
        (1): BatchNorm2d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
      (ReLu): ReLU(inplace=True)
      (AtrousConv): Upsample(scale_factor=2.0, mode=bilinear)
    )
    (2): AtrousBlock(
      (layer): Sequential(
        (0): Conv2d(256, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
        (1): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
      (ReLu): ReLU(inplace=True)
      (AtrousConv): Upsample(scale_factor=2.0, mode=bilinear)
    )
    (3): AtrousBlock(
      (layer): Sequential(
        (0): Conv2d(128, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
        (1): BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
      (ReLu): ReLU(inplace=True)
      (AtrousConv): Upsample(scale_factor=2.0, mode=bilinear)
    )
    (4): AtrousBlock(
      (layer): Sequential(
        (0): Conv2d(64, 32, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
        (1): BatchNorm2d(32, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      )
      (ReLu): ReLU(inplace=True)
    )
  )
  (final_conv): Conv2d(32, 2, kernel_size=(1, 1), stride=(1, 1))
)
```
</div>
<div style="" markdown="1">
```
  (motion_net): VideoResNet(
    (stem): BasicStem(
      (0): Conv3d(3, 64, kernel_size=(3, 7, 7), stride=(1, 2, 2), padding=(1, 3, 3), bias=False)
      (1): BatchNorm3d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (2): ReLU(inplace=True)
    )
    (layer1): Sequential(
      (0): BasicBlock(
        (conv1): Sequential(
          (0): Conv3DSimple(64, 64, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1), bias=False)
          (1): BatchNorm3d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          (2): ReLU(inplace=True)
        )
        (conv2): Sequential(
          (0): Conv3DSimple(64, 64, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1), bias=False)
          (1): BatchNorm3d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        )
        (relu): ReLU(inplace=True)
      )
      (1): BasicBlock(
        (conv1): Sequential(
          (0): Conv3DSimple(64, 64, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1), bias=False)
          (1): BatchNorm3d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          (2): ReLU(inplace=True)
        )
        (conv2): Sequential(
          (0): Conv3DSimple(64, 64, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1), bias=False)
          (1): BatchNorm3d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        )
        (relu): ReLU(inplace=True)
      )
    )
    (layer2): Sequential(
      (0): BasicBlock(
        (conv1): Sequential(
          (0): Conv3DNoTemporal(64, 128, kernel_size=(1, 3, 3), stride=(1, 2, 2), padding=(0, 1, 1), bias=False)
          (1): BatchNorm3d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          (2): ReLU(inplace=True)
        )
        (conv2): Sequential(
          (0): Conv3DNoTemporal(128, 128, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1), bias=False)
          (1): BatchNorm3d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        )
        (relu): ReLU(inplace=True)
        (downsample): Sequential(
          (0): Conv3d(64, 128, kernel_size=(1, 1, 1), stride=(1, 2, 2), bias=False)
          (1): BatchNorm3d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        )
      )
      (1): BasicBlock(
        (conv1): Sequential(
          (0): Conv3DNoTemporal(128, 128, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1), bias=False)
          (1): BatchNorm3d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          (2): ReLU(inplace=True)
        )
        (conv2): Sequential(
          (0): Conv3DNoTemporal(128, 128, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1), bias=False)
          (1): BatchNorm3d(128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        )
        (relu): ReLU(inplace=True)
      )
    )
    (layer3): Sequential(
      (0): BasicBlock(
        (conv1): Sequential(
          (0): Conv3DNoTemporal(128, 256, kernel_size=(1, 3, 3), stride=(1, 2, 2), padding=(0, 1, 1), bias=False)
          (1): BatchNorm3d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          (2): ReLU(inplace=True)
        )
        (conv2): Sequential(
          (0): Conv3DNoTemporal(256, 256, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1), bias=False)
          (1): BatchNorm3d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        )
        (relu): ReLU(inplace=True)
        (downsample): Sequential(
          (0): Conv3d(128, 256, kernel_size=(1, 1, 1), stride=(1, 2, 2), bias=False)
          (1): BatchNorm3d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        )
      )
      (1): BasicBlock(
        (conv1): Sequential(
          (0): Conv3DNoTemporal(256, 256, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1), bias=False)
          (1): BatchNorm3d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
          (2): ReLU(inplace=True)
        )
        (conv2): Sequential(
          (0): Conv3DNoTemporal(256, 256, kernel_size=(1, 3, 3), stride=(1, 1, 1), padding=(0, 1, 1), bias=False)
          (1): BatchNorm3d(256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        )
        (relu): ReLU(inplace=True)
      )
    )
  )
  (temporal_pooling): AdaptiveAvgPool2d(output_size=(16, None))
```
</div>