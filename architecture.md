---
layout: page
title: The Y-Net
subtitle: An audio-visual deep neural network for singing voice separation
---

<div class="lead mb-0" align="justify" style="padding-bottom: 1em">
The Y-Net model consist of a U-Net conditioned with visual features.  
</div>

![Y-Net](../img/model.png)  

<div class="lead mb-0" align="justify" style="padding-bottom: 1em">
The system works with chunks of 4n seconds, where n ∈ N. The audio network takes as input a 256×16T n complex spectrogram and returns a complex mask.  The visual network in case of Y-Net-m and Y-Net-mr, is the video network (in red), which takes as input a set of 100n frames cropped around the mouth of the target singer. In case of Y-Net-g and Y-Net-gr, the visual network is the graph network (in green) which takes as input a sequence of 68n landmarks of the face of the target singer. The visual features are fused with the audio network’s latent space through a FiLM layer (we use T=16).  The FiLM broadcasts the 256×1×T visual features into the 256×16×T audio ones.  The spatial blocks of the U-Net downsample in both, the frequency and the temporal dimension, while the frequential block downsamples along the frequency dimension only.
<br><br>
Detailed layers are shown below. 
</div>

<h3  style="padding-bottom: 10px"> U-Net structure </h3>
<table>
    <tr>
        <td>Block #</td>
        <td>Type of block</td>
        <td>Output channels</td>
        <td>Kernel</td>
        <td>Padding</td>
        <td>Output shape</td>
    </tr>
    <!--<tr>
        <td>-</td>
        <td>Input tensor</td>
        <td>2</td>
        <td>-</td>
        <td>-</td>
        <td>256 x 256</td>
    </tr>-->
    <tr>
        <td>1</td>
        <td>Spatial</td>
        <td>32</td>
        <td>5 x 5</td>
        <td>2</td>
        <td>128 x 128</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Spatial</td>
        <td>64</td>
        <td>5 x 5</td>
        <td>2</td>
        <td>64 x 64</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Spatial</td>
        <td>128</td>
        <td>5 x 5</td>
        <td>2</td>
        <td>32 x 32</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Spatial</td>
        <td>256</td>
        <td>5 x 5</td>
        <td>2</td>
        <td>16 x 16</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Frequential</td>
        <td>256</td>
        <td>5 x 5</td>
        <td>2</td>
        <td>8 x 16</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Frequential</td>
        <td>256</td>
        <td>5 x 5</td>
        <td>2</td>
        <td>4 x 16</td>
    </tr>
    <tr>
        <td>-</td>
        <td>Bottleneck</td>
        <td>256</td>
        <td>3 x 3</td>
        <td>1</td>
        <td>8 x 16</td>
    </tr>
</table>
<br>
<h3  style="padding-bottom: 10px"> Video Network structure </h3>
<table>
    <tr>
        <td>Block #</td>
        <td>Type of block</td>
        <td>Output channels</td>
        <td>Kernel</td>
        <td>Padding</td>
        <td>Stride</td>
        <td>Output shape</td>
    </tr>
    <!--<tr>
        <td>-</td>
        <td>Input tensor</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>100 x 100</td>
    </tr>-->
    <tr>
        <td>0</td>
        <td>Basic Stem</td>
        <td>64</td>
        <td>3 x 7 x 7</td>
        <td>1 x 2 x 2</td>
        <td>1 x 3 x 3</td>
        <td>100 x 100</td>
    </tr>
    <tr>
        <td>1</td>
        <td>Spatio-temporal</td>
        <td>64</td>
        <td>3 x 3 x 3</td>
        <td>1 x 1 x 1</td>
        <td>1 x 1 x 1</td>
        <td>100 x 100</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Spatial</td>
        <td>128</td>
        <td>3 x 3</td>
        <td>1 x 1</td>
        <td>2 x 2</td>
        <td>100 x 100</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Spatial</td>
        <td>256</td>
        <td>3 x 3</td>
        <td>1 x 1</td>
        <td>2 x 2</td>
        <td>100 x 100</td>
    </tr>
</table>
<br>
<h3 style="padding-bottom: 10px">Graph Network structure </h3>
<table>
    <tr>
        <td>Block #</td>
        <td>Output channels</td>
        <td>Output shape</td>
    </tr>
    <!--<tr>
        <td>Input tensor</td>
        <td>2</td>
        <td>100 x 68</td>
    </tr>-->
    <tr>
        <td>1</td>
        <td>32</td>
        <td>100 x 68</td>
    </tr>
    <tr>
        <td>2</td>
        <td>32</td>
        <td>100 x 68</td>
    </tr>
    <tr>
        <td>3</td>
        <td>64</td>
        <td>50 x 68</td>
    </tr>
    <tr>
        <td>4</td>
        <td>64</td>
        <td>50 x 68</td>
    </tr>
    <tr>
        <td>5</td>
        <td>128</td>
        <td>25 x 68</td>
    </tr>
    <tr>
        <td>6</td>
        <td>128</td>
        <td>25 x 68</td>
    </tr>
    <tr>
        <td>7</td>
        <td>256</td>
        <td>13 x 68</td>
    </tr>
    <tr>
        <td>8</td>
        <td>256</td>
        <td>13 x 68</td>
    </tr>
</table>
