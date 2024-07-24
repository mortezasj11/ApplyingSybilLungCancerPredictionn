# Running Docker (Have your folders in the mapping part)
docker run -it --rm --gpus "device=7" --shm-size=192G --user $(id -u):$(id -g) --cpuset-cpus=100-120 \
-v /rsrch1/ip/msalehjahromi/codes/:/Code \
-v /rsrch7/wulab/Mori:/Data \
--name sybit11 sybit:Mori

docker run -it --rm --gpus "device=6" --shm-size=192G --cpuset-cpus=150-174 \
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


CUDA_VISIBLE_DEVICES=0  python 

# for test (1 folder)cd /ho 
python 0_test.py

# for predicting 
python 1_predict_loop.py


# Giving addditional Information (`voxel_spacing`)
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

# Downloading Manually base
import os
import gdown

# Define the NAME_TO_FILE dictionary as provided
NAME_TO_FILE = {
    "sybil_base": {
        "checkpoint": ["28a7cd44f5bcd3e6cc760b65c7e0d54d"],
        "google_checkpoint_id": ["1ftYbav_BbUBkyR3HFCGnsp-h4uH1yhoz"],
        "google_calibrator_id": "1F5TOtzueR-ZUvwl8Yv9Svs2NPP5El3HY",
    },
    # ... other models
}

# class Prediction(NamedTuple):
#     scores: List[List[float]]

# class Evaluation(NamedTuple):
#     auc: List[float]
#     c_index: float
#     scores: List[List[float]]

def download_sybil(name, cache):
    """Download trained models and calibrator from Google Drive

    Parameters
    ----------
    name (str): name of model to use. A key in NAME_TO_FILE
    cache (str): path to directory where files are downloaded

    Returns
    -------
        download_model_paths (list): paths to .ckpt models
        download_calib_path (str): path to calibrator
    """
    # Create cache folder if not exists
    cache = os.path.expanduser(cache)
    os.makedirs(cache, exist_ok=True)

    # Download if needed
    model_files = NAME_TO_FILE[name]

    # Download models
    download_model_paths = []
    for model_name, google_id in zip(
        model_files["checkpoint"], model_files["google_checkpoint_id"]
    ):
        model_path = os.path.join(cache, f"{model_name}.ckpt")
        if not os.path.exists(model_path):
            print(f"Downloading model to {cache}")
            gdown.download(id=google_id, output=model_path, quiet=False)
        download_model_paths.append(model_path)

    # download calibrator
    download_calib_path = os.path.join(cache, f"{name}.p")
    if not os.path.exists(download_calib_path):
        gdown.download(
            id=model_files["google_calibrator_id"],
            output=download_calib_path,
            quiet=False,
        )

    return download_model_paths, download_calib_path

# Specify the model name and cache directory
model_name = "sybil_base"
cache_directory = "./cache_directory"

# Call the function to download the model
download_model_paths, download_calib_path = download_sybil(model_name, cache_directory)

print("Model files downloaded to:", download_model_paths)
print("Calibrator file downloaded to:", download_calib_path)


# Downloading Manually ensemple

NAME_TO_FILE = {
    "sybil_ensemble": {
        "checkpoint": [
            "28a7cd44f5bcd3e6cc760b65c7e0d54d",
            "56ce1a7d241dc342982f5466c4a9d7ef",
            "624407ef8e3a2a009f9fa51f9846fe9a",
            "64a91b25f84141d32852e75a3aec7305",
            "65fd1f04cb4c5847d86a9ed8ba31ac1a",
        ],
        "google_checkpoint_id": [
            "1ftYbav_BbUBkyR3HFCGnsp-h4uH1yhoz",
            "1rscGi1grSxaVGzn-tqKtuAR3ipo0DWgA",
            "1DV0Ge7n9r8WAvBXyoNRPwyA7VL43csAr",
            "1Acz_yzdJMpkz3PRrjXy526CjAboMEIHX",
            "1uV58SD-Qtb6xElTzWPDWWnloH1KB_zrP",
        ],
        "google_calibrator_id": "1FxHNo0HqXYyiUKE_k2bjatVt9e64J9Li",
    },
}


def download_sybil(name, cache):
    """Download trained models and calibrator from Google Drive

    Parameters
    ----------
    name (str): name of model to use. A key in NAME_TO_FILE
    cache (str): path to directory where files are downloaded

    Returns
    -------
        download_model_paths (list): paths to .ckpt models
        download_calib_path (str): path to calibrator
    """
    # Create cache folder if not exists
    cache = os.path.expanduser(cache)
    os.makedirs(cache, exist_ok=True)

    # Download if needed
    model_files = NAME_TO_FILE[name]

    # Download models
    download_model_paths = []
    for model_name, google_id in zip(
        model_files["checkpoint"], model_files["google_checkpoint_id"]
    ):
        model_path = os.path.join(cache, f"{model_name}.ckpt")
        if not os.path.exists(model_path):
            print(f"Downloading model to {cache}")
            gdown.download(id=google_id, output=model_path, quiet=False)
        download_model_paths.append(model_path)

    # download calibrator
    download_calib_path = os.path.join(cache, f"{name}.p")
    if not os.path.exists(download_calib_path):
        gdown.download(
            id=model_files["google_calibrator_id"],
            output=download_calib_path,
            quiet=False,
        )

    return download_model_paths, download_calib_path

# Specify the model name and cache directory
model_name = "sybil_ensemble"
cache_directory = "./cache_directory"

# Call the function to download the model
download_model_paths, download_calib_path = download_sybil(model_name, cache_directory)

print("Model files downloaded to:", download_model_paths)
print("Calibrator file downloaded to:", download_calib_path)