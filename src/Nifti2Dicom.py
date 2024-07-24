import tqdm
import nibabel
import pydicom
import os


def convertNsave(arr,file_dir, index=0, pxl_spacing= [1,1], root = None):
    """
    `arr`: parameter will take a numpy array that represents only one slice.
    `file_dir`: parameter will take the path to save the slices
    `index`: parameter will represent the index of the slice, so this parameter will be used to put 
    the name of each slice while using a for loop to convert all the slices
    """
    dicom_sample = os.path.join(root, 'ct.3')
    if os.path.isfile(dicom_sample):
        dicom_file = pydicom.dcmread(dicom_sample)
    else:
        dicom_file = pydicom.dcmread("/Data/non_smoking_2_processing/nii2dcm/CT")
    arr = arr.astype('int16')
    dicom_file.RescaleIntercept = 0.0
    dicom_file.PixelSpacing = list(pxl_spacing)
    dicom_file.Rows = arr.shape[0]
    dicom_file.Columns = arr.shape[1]
    dicom_file.PhotometricInterpretation = "MONOCHROME2"
    dicom_file.SamplesPerPixel = 1
    dicom_file.BitsStored = 16
    dicom_file.BitsAllocated = 16
    dicom_file.HighBit = 15
    dicom_file.PixelRepresentation = 1
    dicom_file.PixelData = arr.tobytes()
    dicom_file.save_as(os.path.join(file_dir, f'slice{index}.dcm'))



def nifti2dicom_1file(nifti_dir, out_dir, pxl_spacing, root):
    """
    This function is to convert only one nifti file into dicom series
    `nifti_dir`: the path to the one nifti file
    `out_dir`: the path to output
    """
    nifti_file = nibabel.load(nifti_dir)
    nifti_array = nifti_file.get_fdata()
    number_slices = nifti_array.shape[2]
    #for slice_ in tqdm(range(number_slices)):
    for slice_ in range(number_slices):
        convertNsave(nifti_array[:,:,slice_], out_dir, slice_, pxl_spacing[:2], root)