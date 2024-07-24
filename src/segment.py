#from lungmask import mask
import os
import numpy as np
import nibabel as nib
import SimpleITK as sitk

def obtain_lung_seg(path_ct):
    print('Obtaining lung segmentation...')
    input_image = sitk.ReadImage(path_ct)
    segmentation = mask.apply_fused(input_image)
    segmentation[segmentation!=0] = 1
    segmentation = np.transpose(segmentation,[1,2,0])
    shape = segmentation.shape
    seg_final = np.zeros((shape[1],shape[0],shape[2]))
    for i in range(segmentation.shape[2]):
        seg_final[:,:,i] = np.rot90( np.fliplr(segmentation[:,:,i]),1)
    return seg_final

def man_min_slide(seg, thresh = 7):
    shape = seg.shape
    sum_vec = seg.sum(0).sum(0)   # 1D, gives the number of non-zero pixels in each slide, [ 0,   0,   0, 141, 190, 228, 0, 0]
    sele_idx = np.nonzero(sum_vec)             # array([3, 4, 5])
    min_slide, max_slide = sele_idx[0][0], sele_idx[0][-1]
    min_slide = max(min_slide-thresh, 0)
    max_slide = min(max_slide+thresh, shape[2])
    return min_slide, max_slide

def make_save_seg_para(i, list_ct):
    path_ct = list_ct[i]
    seg = obtain_lung_seg(path_ct)
    seg = seg.astype(np.int8)
    min_slide, max_slide = man_min_slide(seg)
    ct = nib.load(path_ct).get_fdata()
    affine = nib.load(path_ct).affine
    ct_min_max = ct[:,:,min_slide:max_slide]
    root, nifti_file =os.path.dirname(path_ct) ,os.path.basename(path_ct)
    seg_NIFTI = nib.Nifti1Image(ct_min_max, affine)
    outer_path = os.path.join(root, nifti_file[:-7]+'_sybil.nii.gz')
    seg_NIFTI.to_filename(outer_path)

def make_save_seg(path_ct, name = '_sybil.nii.gz'):
    seg = obtain_lung_seg(path_ct)
    seg = seg.astype(np.int8)
    min_slide, max_slide = man_min_slide(seg)
    ct = nib.load(path_ct).get_fdata()
    affine = nib.load(path_ct).affine
    ct_min_max = ct[:,:,min_slide:max_slide]
    root, nifti_file =os.path.dirname(path_ct) ,os.path.basename(path_ct)
    seg_NIFTI = nib.Nifti1Image(ct_min_max, affine)
    outer_path = os.path.join(name)
    seg_NIFTI.to_filename(outer_path)

def convert_to_dictionary(scores, name):
    output = {}
    output["file_name"] = name
    col_names = ['1-Year Risk', '2-Year Risk', '3-Year Risk', '4-Year Risk', '5-Year Risk', '6-Year Risk']
    for i in range(6):
        output[col_names[i]] = scores[0][0][i]
    return output