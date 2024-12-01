import os
import glob
import numpy as np
from tqdm import tqdm
from monai.transforms import (
    Compose,
    LoadImaged,
    ScaleIntensityRanged,
    RandFlipd,
    RandRotate90d,
    RandScaleIntensityd,
    SaveImage,
)


# Set preprocessed dataset path
dataset_dir = '/mnt/3bb01a96-4d48-4134-9dcc-1e1cdd11daa3/zkx/Datasets/ATM22' #### dataset path
image_output_folder = '/mnt/3bb01a96-4d48-4134-9dcc-1e1cdd11daa3/zkx/Datasets/FSC_rela/ATM22/images'  #### prepocess images save path
label_output_folder = '/mnt/3bb01a96-4d48-4134-9dcc-1e1cdd11daa3/zkx/Datasets/FSC_rela/ATM22/labels'  #### prepocess labels save path

os.makedirs(image_output_folder, exist_ok=True)
os.makedirs(label_output_folder, exist_ok=True)

# Transform image-label pair by Monai
transform_pair = Compose(
    [
        LoadImaged(keys=["image", "label"]),
        ScaleIntensityRanged(
            keys=["image"],
            a_min=-1000,
            a_max=600.0,
            b_min=0,
            b_max=1.0,
            clip=True
        ),
        RandFlipd(keys=["image", "label"], prob=0.2, spatial_axis=0),
        RandRotate90d(keys=["image", "label"], prob=0.2, max_k=3),
        RandScaleIntensityd(keys="image", factors=0.1, prob=0.1),

    ]
)

# Define the save transform for image and label
save_image_transform = SaveImage(output_dir=image_output_folder, output_dtype=np.float32,output_postfix='image', separate_folder=False)
save_label_transform = SaveImage(output_dir=label_output_folder, output_dtype=np.float32, output_postfix='label',separate_folder=False)

# Get the list of image-label pairs
image_files = sorted(glob.glob(os.path.join(dataset_dir, 'train/images/*.nii.gz'))) ##
label_files = sorted(glob.glob(os.path.join(dataset_dir, 'train/labels/*.nii.gz'))) ##

# Ensure that the number of images and labels match
assert len(image_files) == len(label_files), "Number of images and labels do not match!"

# Process each image-label pair
for idx, (image_file, label_file) in tqdm(enumerate(zip(image_files, label_files)), total=len(image_files),
                                          desc="Processing NIfTI files"):
    # Prepare data dictionary
    data_dict = {'image': image_file, 'label': label_file}

    # Apply transformations to the image-label pair
    transformed_data = transform_pair(data_dict)

    # Save the transformed image and label
    save_image_transform(transformed_data['image'])
    save_label_transform(transformed_data['label'])

print("Processing completed.")