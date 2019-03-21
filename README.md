# Skin-Detection-Naive-Bayes-
Skin detection detection using naive Bayes classification (python)

#### NOTE:
- The code is for demonstration only, python codes are not optimized in function calls
- Used Naive Bayes to classify skin probable colors and non skin colors
- First all pixels (256x256x256) in RGB, is taken to extract their frequencies as skin color or non skin color
- ^ this is done by comparing mask photos to their original photos
- Then each pixel value [r,g,b] is mapped to its probability of being a skin color
- Finally test any image to extract its skin as white color

#### RUN:
- Run gather.py (Build a file with probabilitys for each pixel in rgb plane)
- Run test.py

#### NEED:
- pip install pillow
- python > 3.5

#### CREDIT:
- https://github.com/MinhasKamal/SkinDetector 
