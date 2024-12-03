# AirWSeg

## Project Overview

This project focuses on the preprocessing of lung airway datasets. It includes data augmentation steps for both images and labels. The preprocessing pipeline involves scaling intensity, flipping, rotation, and saving the transformed image-label pairs in a specified output directory.

## Feature Description

1. **Intensity Scaling**: Normalize image intensity values within a specific range.
2. **Augmentations**：
   - **Random Flip**: Flip images and labels along the vertical axis with a probability of 20%.
   - **Random Rotation**: Rotate images and labels by multiples of 90° with a probability of 20%.
   - **Intensity Scaling**: Scale image intensities randomly with a probability of 10%.
3. **Data Saving**：
   - Save preprocessed images and labels in separate output directories.

## Source Directory

This directory contains the code, file of outputs, and documentation for image preprocessing.

### Files

- [README.md](./README.md/): Contains a basic introduction to this project.
- [preprocess_img.py](./preprocess_img.py/): Process image files to generate usable patches.

### Subfolders

- [AirWSeg](./AirWSeg/): Contains the processed images and original images.


## Usage Instructions

### Environment Requirements

- Python 3.x
- Monai == 1.4.0
- numpy
- tqdm

### Steps to Run

1. Set the paths for the input dataset (`dataset_dir`), output images (`image_output_folder`), and output labels (`label_output_folder`).
2. Ensure the input dataset contains subfolders `train/images/` and `train/labels/` with `.nii.gz` files.
3. Run the script in a Python environment.

## Notes and Precautions

- Verify that the input directory contains the correct file format (`.nii.gz`) and structure.
- Ensure sufficient storage space in the output directory.
- Adjust parameters like `a_min`, `a_max`, and augmentation probabilities (`prob`) to match the dataset's requirements.

## Result Dataset

The data structure should be like this:

	/AirWSeg
 		/AirWSeg_preprocess
	    	/ExACT09
	            /images
	                /CASE01_image.nii.gz
	                /CASE02_image.nii.gz
	                ...
	            /labels
	                /CASE01_label.nii.gz
	                /CASE02_label.nii.gz
	                ...

	    	/BAS
	            /train
	                /images
	                    /1.3.6.1.4.1.14519.5.2.1.6279.6001.100225287222365663678666836860_image.nii.gz
	                    /1.3.6.1.4.1.14519.5.2.1.6279.6001.100332161840553388986847034053_image.nii.gz
	                    ...	
	                /labels
	                	/1.3.6.1.4.1.14519.5.2.1.6279.6001.100225287222365663678666836860_label.nii.gz
	                	/1.3.6.1.4.1.14519.5.2.1.6279.6001.100332161840553388986847034053_label.nii.gz
	                    ...	
	            /valid
	            	...
	          	/test
	  				...
	     		...
	     /AirWSeg_ori	
	     	/ExACT09
	            /images
	               /CASE01.nii.gz
	               /CASE02.nii.gz
	               ...
	            /labels
	               /CASE01.nii.gz
	               /CASE02.nii.gz
	                ...	

## Version History

- Initial version: December 1, 2024

## Contact Information

If you have any questions or need further assistance, please contact us via [Contact Information](mailto:kysonzhou602@163.com).
