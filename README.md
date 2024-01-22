# Recycables-Classification-Application

## About 
This project aims to classify recycables such as boxes, glass bottles, soda cans, crushed soda cans and plastic bottles. Further development of this project could be applied for recycables segregation from general waste. The best model from this project is mobilenet, Tensorflow's first mobile computer vision model achieving a F1-score of 85.8% in classifying the catagories of recycables. 

## Summary 
Image Classification | Flask App | Model deployment 

## How to run? 
**Run locally**
1. Create and launch new Anaconda Python environment. 
```
conda create --name keras-tensorflow
conda activate keras-tensorflow
conda install -c conda-forge python=3.10
conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
python3 -m pip install tensorflow
conda install Flask 
```
2. Navigate to the project directory and run `python model.py`. 


## Sample results/ output
![](https://github.com/CH2001/Recycables-Classification-Application/blob/main/Demo.gif)

## Links 
Dataset: [Recycling dataset](http://web.cecs.pdx.edu/~singh/rcyc-web/index.html) <br> 