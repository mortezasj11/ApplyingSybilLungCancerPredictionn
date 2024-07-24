from sybil import Serie, Sybil
import os
import pandas as pd
from lungmask import mask
import os
import numpy as np
import pandas as pd
#import nibabel as nib
import SimpleITK as sitk
from joblib import Parallel, delayed #pip install joblib
from src.segment import make_save_seg, convert_to_dictionary
import subprocess
from src.Nifti2Dicom  import nifti2dicom_1file
import pydicom


def get_dicom_file_paths(case_i_dics):
    dicom_file_paths = []
    for filename in os.listdir(case_i_dics):
        if filename.endswith(".dcm"):
            filepath = os.path.join(case_i_dics, filename)
            dicom_file_paths.append(filepath)
    return dicom_file_paths


def sort_dicom_files_by_instance_number_and_get_voxel_spacing(dicom_file_paths):
    dicom_files_with_instance = []

    for filepath in dicom_file_paths:
        dicom_file = pydicom.dcmread(filepath)
        instance_number = int(dicom_file.InstanceNumber)
        dicom_files_with_instance.append((filepath, instance_number))
    dicom_files_with_instance.sort(key=lambda x: x[1])
    sorted_dicom_file_paths = [filepath for filepath, _ in dicom_files_with_instance]
    # Extract voxel spacing from the first DICOM file
    first_dicom_file = pydicom.dcmread(sorted_dicom_file_paths[0])
    pixel_spacing = [float(item) for item in first_dicom_file.PixelSpacing]  # [row spacing, column spacing]
    slice_thickness = float(first_dicom_file.SliceThickness)
    voxel_spacing = np.abs(pixel_spacing + [slice_thickness])
    return sorted_dicom_file_paths, voxel_spacing


ensemple = False 
if ensemple:
    name_or_path_fn = ["28a7cd44f5bcd3e6cc760b65c7e0d54depoch=10.ckpt","56ce1a7d241dc342982f5466c4a9d7ef.ckpt", "64a91b25f84141d32852e75a3aec7305.ckpt",\
                    "65fd1f04cb4c5847d86a9ed8ba31ac1a.ckpt", '624407ef8e3a2a009f9fa51f9846fe9a.ckpt']
    name_or_path = [os.path.join('/Code/non_smoking_2_processing/nii2dcm/sybil/', i) for i in name_or_path_fn] 
    calibrator_path = "/Code/non_smoking_2_processing/nii2dcm/sybil/sybil_ensemble.p"
else:
    name_or_path = ['/Code/non_smoking_2_processing/nii2dcm/sybil/28a7cd44f5bcd3e6cc760b65c7e0d54depoch=10.ckpt']
    calibrator_path='/Code/non_smoking_2_processing/nii2dcm/sybil/28a_calibrator.p'

finding_dcm_organized = False
if __name__=='__main__':
    
    path  =  "/Data/sophie1/"  # containing .nii.gz files
    path_csv  = "/Data/sophieCSV/"; os.makedirs(path_csv, exist_ok=True)

    output_list_all = []
    dicom_files = []
    counter = 0
    for mrn in os.listdir(path):

        mrn_path = os.path.join(path, mrn)
        # Check if it's a directory
        if os.path.isdir(mrn_path):
            # List all folders within the MRN folder (first level)
            for first_level in os.listdir(mrn_path):
                first_level_path = os.path.join(mrn_path, first_level)
                
                # Check if it's a directory
                if os.path.isdir(first_level_path):
                    # List all folders within the first level folder (second level)
                    for second_level in os.listdir(first_level_path):
                        second_level_path = os.path.join(first_level_path, second_level)
                        
                        # Check if it's a directory
                        if os.path.isdir(second_level_path):
                            # List all folders within the second level folder (third level)
                            for third_level in os.listdir(second_level_path):
                                third_level_path = os.path.join(second_level_path, third_level)

                                if finding_dcm_organized:
                                    dicom_file_paths = get_dicom_file_paths(third_level_path)
                                    sorted_dicom_file_paths, voxel_spacing = sort_dicom_files_by_instance_number_and_get_voxel_spacing(dicom_file_paths)
                                    dcm_files = sorted_dicom_file_paths #[os.path.join(path_temp_dicom,i) for i in os.listdir(path_temp_dicom) ] #if i.endswith('.dcm')
                                else:
                                    dcm_files = [os.path.join(third_level_path,i) for i in os.listdir(third_level_path)] # if i.endswith('.dcm') ] 

                                output_list = []
                                csv_file = os.path.join(path_csv, mrn + '.csv')  # The risks will be saved here.

                                model = Sybil(name_or_path = name_or_path, calibrator_path=calibrator_path) 

                                serie_i = Serie(dcm_files)     # serie_i = Serie(dcm_files, voxel_spacing=voxel_spacing) #serie_i = Serie(dcm_files)
                                scores_i = model.predict([serie_i])# model prediction
                                result = convert_to_dictionary(scores_i, mrn)# saving to csv file
                                result["#slices"] = len(dcm_files)
                                output_list.append((result))

                                df = pd.DataFrame(output_list)
                                output_list_all.append((result))
                                counter += 1

                                text_name = "ensemble_" if ensemple else ""
                                csv_file_all = os.path.join(path_csv, text_name + str(counter) +'_all.csv')
                                df_all = pd.DataFrame(output_list_all)
                                df_all.to_csv( csv_file_all , index=False)