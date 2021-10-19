---
layout: page
title: The Circle of Life
subtitle: An acappella singing voice montage with ground-truth sources
---

<div class="lead mb-0" align="justify">
Evaluating algorithms in real world examples is an important step to verify those work in real challenging situations. 
We recorded an amateur singer to compose a 6-voice montage which permits to evaluate in real world examples but having ground-truth sources to compare with.

<br><br>

To do so, we have chosen <a href="https://en.wikipedia.org/wiki/Circle_of_Life">The Circle of Life</a> song. The reasons are:
<ul>
    <li>Two-languages song, english and zulu.</li>  
    <li>Humming-like sounds which are more challenging than separating lyrics.</li>  
    <li>Synchronized voices and chorals which are slightly delayed on time.</li>
</ul>

We also add an instrumental backtrack in order to provide musical coherence and sonority.

<div style="padding-top: 10px" markdown="1">
```
Song: The Circle of Life    
Compositor: Elton John  
Owner: Walt Disney Studio 
Duration: 4:34  
Voices (top left, clockwise): Backtrack, Antelope 2, Lioness, Lion, Rafiki, Antelope 1.
```
</div>
<iframe width="926" height="618" src="https://www.youtube.com/embed/XvBOH8FGias" title="The circle of lifre" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<div markdown="1">
The original recordings can be found in [GDrive](https://drive.google.com/file/d/1M1IRC-OJx75F4BKuPIzuYFX13exXEvZr/view?usp=sharing)  
```
Encoder: h264
Pixel format: yuv 420p
Framerate: 30 FPS
Montage shape: 2000x3000

Audio encoder: wav pcm_s32be 
Samplerate: 44.1 KHz
2 Channels
```
  
Ready-to-use files can be found in [GDrive](https://drive.google.com/drive/folders/1mYF3ARkSKhV5a09G5MsefD7foFNRqHlt?usp=sharing)  

```
Framerate: 25 FPS  
Video format: npy (numpy arrays)
Colorspace: RGB  
Array shape: 6850x128x96x3 (TxHxWxC)
Sample Rate: 16384 Hz  
Audio format: wav pcm_s16le mono
```
</div>
</div>
