
import os
import gdown
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
        "google_calibrator_id": "1FxHNo0HqXYyiUKE_k2bjatVt9e64J9Li"}}


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



###############################################################################################

import os
import gdown

# Define the NAME_TO_FILE dictionary as provided
NAME_TO_FILE = {
    "sybil_base": {
        "checkpoint": ["28a7cd44f5bcd3e6cc760b65c7e0d54d"],
        "google_checkpoint_id": ["1ftYbav_BbUBkyR3HFCGnsp-h4uH1yhoz"],
        "google_calibrator_id": "1F5TOtzueR-ZUvwl8Yv9Svs2NPP5El3HY"}}

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
