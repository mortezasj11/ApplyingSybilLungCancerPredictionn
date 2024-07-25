# SYBIL Lung Cancer Prediction


## Setup Instructions



1. Adding `.dcm` Extension to DICOM Data

    If the downloaded DICOM data does not have `.dcm` like in Sophie's data, run:
```sh
python Adding_dot_dcm.py
```



2. To download the model(s), not necessary but good to avoid permission error:
```sh
python downloading_model.py
```


3. Running on a directory containing multiple Dicoms with/without ensempling
**It goes until third-level path, modify based on your own dataset foldering.**

```sh
python main_sophie_data.py --ensemble
python main_sophie_data.py
```



## About SYBIL and DICOM
    **Giving addditional Information (`voxel_spacing`)**

```sh
class Serie:
    def __init__(
        self,
        dicoms: List[str],
        voxel_spacing: Optional[List[float]] = None,
        label: Optional[int] = None,
        censor_time: Optional[int] = None,
        file_type: Literal["png", "dicom"] = "dicom",
        split: Literal["train", "dev", "test"] = "test",
    ):
        """Initialize a Serie.
        Parameters
        ----------
        `dicoms` : List[str]
            [description]
        `voxel_spacing`: Optional[List[float]], optional
            The voxel spacing associated with input CT
            as (row spacing, col spacing, slice thickness)
        `label` : Optional[int], optional
            Whether the patient associated with this serie
            has or ever developped cancer.
        `censor_time` : Optional[int]
            Number of years until cancer diagnostic.
            If less than 1 year, should be 0.
        `file_type`: Literal['png', 'dicom']
            File type of CT slices
        `split`: Literal['train', 'dev', 'test']
            Dataset split into which the serie falls into.
            Assumed to be test by default
        """


opencv-python==4.5.5.64 
scikit-learn==1.0.2
torchvision==0.12.0     # Gave Error!!
 


(0025, 0010) Private Creator                     LO: '1.2.840.114051.6.0_NovaradGeneralData'
(0028, 0002) Samples per Pixel                   US: 1
(0028, 0004) Photometric Interpretation          CS: 'MONOCHROME2'
(0028, 0010) Rows                                US: 512
(0028, 0011) Columns                             US: 512
(0028, 0030) Pixel Spacing                       DS: [0.955078125, 0.955078125]
(0028, 0100) Bits Allocated                      US: 16
(0028, 0101) Bits Stored                         US: 12
(0028, 0102) High Bit                            US: 11
(0028, 0103) Pixel Representation                US: 0
(0028, 0106) Smallest Image Pixel Value          US: 0
(0028, 0107) Largest Image Pixel Value           US: 2471
(0028, 1050) Window Center                       DS: [-600, 50]
(0028, 1051) Window Width                        DS: [1200, 350]
(0028, 1052) Rescale Intercept                   DS: '-1024.0'
(0028, 1053) Rescale Slope                       DS: '1.0'
(0028, 1055) Window Center & Width Explanation   LO: ['WINDOW1', 'WINDOW2']
(0028, 2110) Lossy Image Compression             CS: '01'
(0028, 2112) Lossy Image Compression Ratio       DS: '7.477437'
(0029, 0010) Private Creator                     LO: 'SIEMENS CSA HEADER'
(0029, 0011) Private Creator                     LO: 'SIEMENS MEDCOM HEADER'
(0029, 1008) [CSA Image Header Type]             CS: 'SOM 5'
(0029, 1009) [CSA Image Header Version]          LO: 'VA10A 971201'
(0029, 1010) [CSA Image Header Info]             OB: Array of 740 elements
(0029, 1140)  [Application Header Sequence]  1 item(s) ----
   (0029, 0010) Private Creator                     LO: 'SIEMENS MEDCOM HEADER'
   (0029, 1041) [Application Header Type]           CS: 'SOM 5 TPOS'
   (0029, 1042) [Application Header ID]             LO: 'SOM 5 NULLPOSITION'
   (0029, 1043) [Application Header Version]        LO: 'VB10A 20030626'
   (0029, 1044) [Application Header Info]           OB: b'-000005750\x00A'
   ---------
(0032, 000a) Study Status ID                     CS: 'UNMATCHED'
(0032, 1032) Requesting Physician                PN: 'PRINE^MATTHEW^^^'
(0032, 1060) Requested Procedure Description     LO: 'CT CHEST WITH & WO'
(0040, 0244) Performed Procedure Step Start Date DA: '20170509'
(0040, 0245) Performed Procedure Step Start Time TM: '085405.474000'
(0040, 0253) Performed Procedure Step ID         SH: '5'
(0040, 0254) Performed Procedure Step Descriptio LO: 'CT CHEST WITH & WO'
(0040, 0275)  Request Attributes Sequence  1 item(s) ----
   (0040, 0007) Scheduled Procedure Step Descriptio LO: 'CT CHEST WITH & WO'
   (0040, 0009) Scheduled Procedure Step ID         SH: '5'
   (0040, 1001) Requested Procedure ID              SH: '181930'
   (0040, 100a)  Reason for Requested Procedure Code Sequence  0 item(s) ----
   ---------
(0040, 1003) Requested Procedure Priority        SH: 'ROUTINE'
(0050, 0065)                                     LO: 'LA - Richardson'
(0073, 0010) Private Creator                     LO: 'STENTOR'
(0073, 1001) [Unknown]                           ST: 'unknown'
(0073, 1002) [Private Creator]                   ST: '192.168.5.6'
(0073, 1003) [Stentor Remote AETitle Element]    ST: 'LILA'
(0073, 1004) [Stentor Local AETitle Element]     ST: 'STENTOR_SCP'
(0073, 1006) [Stentor Transfer Syntax Value]     LO: '1.2.840.10008.1.2.1'
(7fe0, 0010) Pixel Data                          OW: Array of 524288 elements
```

### Running Docker (Have your folders in the mapping part)
docker run -it --rm --gpus "device=7" --shm-size=192G --user $(id -u):$(id -g) --cpuset-cpus=100-120 \
-v /rsrch1/ip/msalehjahromi/codes/:/Code \
-v /rsrch7/wulab/Mori:/Data \
--name sybit11 sybit:Mori

pip install nii2dcm, lungmask
pip install lungmask

when --user $(id -u):$(id -g)
    nii2dcm /Code/non_smoking_2_processing/nii2dcm/493464_080606_sybil.nii.gz /Code/non_smoking_2_processing/nii2dcm/Dicom_temp

when --user $(id -u):$(id -g)
    Permission denied: '/Data/non_smoker_March/493464_D/090320_'

when not --user:
    nii2dcm  NOT WORKS
    Permission denied: '/Code/non_smoking_2_processing/nii2dcm/Dicom_temp/IM_0001'