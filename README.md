# Image-Augmentation-Python
This repo is a collection of image augmentation scripts written in Python. Types of augmentations are horizontal flip, vertical segmentation, and 9-parts image segmentation. This repo also includes scripts to augment XML files based on the PascalVOC standard.

1. Horizontal_flip.py
- Script to perform horizontal flip on images, number of images must be defined before running.
 
2. Flipper.py
- A better version of Horizontal_flip.py
- Contains two separate functions to perform horizontal flip on images and bounding boxes.
- Values that needs to be passed through the functions are image directory and directory of the XML files.

3. Segment.py
- Script to crop images into 3 vertical segments. The width of the segments can be customised and it will save to an existing ‘output’ folder (this can be changed)

4. SegmentXML.py
- Contain a function to crop bounding boxes to 3 vertical segments.
- The function requires 5 parameters which are x1, x2, directory of XML files, threshold, and segment section.
- x1 and x2 are the starting and ending coordinates of the segment.
- Threshold refers to the percentage overlap of the cropped bounding box over the original bounding box
- Segment section refers to which part of the image. The left section is 1, right section is 2, and the middle overlapping segment is 3. The width of the segments can be customised by changing the values of x1 and x2.

5. SegmentSquare.py
- Script to crop images into 9 overlapping square segments.
- The size of the segments are defined to work with any image size.

6. SegmentSquareXML-test1.py
- Contains a function to crop bounding boxes up to 9 overlapping square segments.
- The function requires 7 parameters which are x1, x2, y1, y2, directory of XML files, threshold, and segment number.
- The size of each square segments can be customised by defining x1,x2,y1,y2.

7. SegmentSquareXML-test2.py
- Contains a function to crop bounding boxes up to 9 fixed overlapping square segments. This will work on any image size.
- Only 3 parameters are needed which are directory of XML files, threshold, and segment number.
