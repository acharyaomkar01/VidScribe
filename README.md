# VidScribe

## Introduction
Giving the user the choice to watch the video or read its description even without playing it, or both, we present a model that generates natural language description of videos in English language. For this purpose, we are using deep learning algorithms with both convolutional and recurrent structure. Our system extracts features from the video frames using a pre-trained `Convolutional Neural Network` viz. `VGGNET` (16 layer) that is trained on `ImageNet` dataset. `Caffe`’s python module is used for the same. We feed these features to a `LSTM (Long Short Term Memory)` to generate the description for the input video. We trained the `LSTM` model on `MSCOCO` dataset and used `Chainer` framework for the related processing. Our system can find its application in video search engines that could provide better search results using video description instead of the existing systems that mainly rely on video titles. Also such a system can help the blind to comprehend video content.

We have written a paper of this project. Take a look at it [here](/project-paper.pdf)
