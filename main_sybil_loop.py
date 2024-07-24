# applying lung segmentation
# define the lower and upper slide number 
# Save the New CT based on that maybe rename to _for_sybil_
# convert to dcm
# read it by sybil
# I need to copy one scm files from each case to here

from sybil import Serie, Sybil
import os
import pandas as pd
#from lungmask import mask
import os
import numpy as np
import pandas as pd
import nibabel as nib
import SimpleITK as sitk
from joblib import Parallel, delayed #pip install joblib
from src.segment import make_save_seg, convert_to_dictionary
import subprocess
from src.Nifti2Dicom  import nifti2dicom_1file




could_not_nii2dcm = []
not_list = []# ['2303759_D']



if __name__=='__main__':
    para = False
    path = "/Data/non_smoker_March"
    path_seg        = "/Data/non_smoker_March/"
    path_csv        = "/Data/non_smoking_2_processing/nii2dcm/csv_all" #??????????????????????????????????????????????????
    path_temp_dicom = "/Data/non_smoking_2_processing/nii2dcm/Dicom_temp"
    os.makedirs(path_temp_dicom, exist_ok=True)
    ### Remove files
    #################################
    for i in os.listdir(path_temp_dicom):
        file_to_remove = os.path.join(path_temp_dicom, i)
        os.remove(file_to_remove)

    for mrn in os.listdir(path):
        if mrn.endswith('_D') and (mrn not in not_list):

            

            mrn_path = os.path.join(path, mrn)
            dates_path = [os.path.join(mrn_path,i) for i in os.listdir(mrn_path) if (('other' not in i.lower()) and os.path.isdir(os.path.join(mrn_path,i)))]
            list_ct_sybil = []
            for date_path in dates_path:
                path_date = [os.path.join(date_path,x) for x in os.listdir(date_path) if \
                             (os.path.getsize(os.path.join(date_path,x))>4000000 and x.endswith('.nii.gz') and ('_sybil' in x.lower()) )]
                if len(path_date)!=0:
                    list_ct_sybil.append(path_date[0])

            if len(list_ct_sybil)<5:
                output_list_all = []
                for idx, ct_list_i in enumerate(list_ct_sybil):
                    root, nifti_file = os.path.dirname(ct_list_i) ,os.path.basename(ct_list_i)
                    nifti_name = nifti_file[:-7] if nifti_file.endswith('.nii.gz') else nifti_file[:-4]

                    csv_file_all = os.path.join(os.path.dirname(root), nifti_name.split('_')[0] + '_'+ str(len(list_ct_sybil)) +'_all_dcm_ens.csv')
                    if os.path.isfile(csv_file_all) and os.path.getsize(csv_file_all)>500:
                        print(csv_file_all, os.path.getsize(csv_file_all) , ' was thereEEEEEEEEEEEEEEEEEEEEEEEE!!!  '  )
                        break

                    if os.path.isfile(csv_file_all) and os.path.getsize(csv_file_all)<10:
                        print(csv_file_all, os.path.getsize(csv_file_all) , ' was there but EMPTYYYYYYYYYYYY!!!  '  )


                    print(root, nifti_file)
                    sybil_file = os.path.join(root, nifti_file) #truncated CT lung
                    pxl_spacing = np.abs(np.diag(nib.load(ct_list_i).affine)[:3])
                    #### Convert to dcm
                    try:
                        nifti2dicom_1file(sybil_file, path_temp_dicom, pxl_spacing, root)
                    except:
                        could_not_nii2dcm.append(sybil_file)
                        print(ct_list_i, 'Could not Convert!!')
                        #breakpoint()
                    #command = 'nii2dcm'+ ' ' + sybil_file + ' ' + path_temp_dicom # result = subprocess.run(command, shell=True, capture_output=True, text=True)
                    #command = ['nii2dcm', sybil_file , path_temp_dicom];subprocess.run(command)

                    #### Calculate Risk and save
                    output_list = []
                    csv_file = os.path.join(os.path.dirname(root), nifti_name + '.csv')  # The risks will be saved here.
                    model = Sybil("sybil_ensemble")  #sybil_ensemble
                    dcm_files = [os.path.join(path_temp_dicom,i) for i in os.listdir(path_temp_dicom) ] #if i.endswith('.dcm')
                    serie_i = Serie(dcm_files, voxel_spacing=pxl_spacing) #serie_i = Serie(dcm_files) 
                    scores_i = model.predict([serie_i])# model prediction
                    result = convert_to_dictionary(scores_i, nifti_name)# saving to csv file
                    output_list.append((result))
                    serie_i_rev = Serie(dcm_files[::-1], voxel_spacing=pxl_spacing) #serie_i = Serie(dcm_files) 
                    scores_i_rev = model.predict([serie_i_rev])# model prediction
                    result_rev = convert_to_dictionary(scores_i_rev, nifti_name+'_reverse')# saving to csv file
                    output_list.append((result_rev))
                    #df = pd.DataFrame(output_list)
                    #df.to_csv( csv_file , index=False)
                    output_list_all.append((result)); output_list_all.append((result_rev))

                    print('###########################################################################')
                    print(root, nifti_file)
                    print(idx , len(list_ct_sybil)-1)
                    if idx == len(list_ct_sybil)-1:
                        
                        #breakpoint()
                        df_all = pd.DataFrame(output_list_all)
                        df_all.to_csv( csv_file_all , index=False)
                        print(df_all)
                        #breakpoint()
    print(could_not_nii2dcm)


# docker run -it --rm --gpus "device=6" --shm-size=192G --cpuset-cpus=150-174 \
# -v /rsrch1/ip/msalehjahromi/codes/:/Code \
# -v /rsrch7/wulab/Mori:/Data \
# --name sybit22 sybit:Mori

#pip install lungmask

# CUDA_VISIBLE_DEVICES=0  python main_sybil_loop.py