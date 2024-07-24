import os
import re

def has_long_numeric_extension(filename):
    """Check if the file has a long numeric extension."""
    base, ext = os.path.splitext(filename)
    return re.fullmatch(r'\d{5,}', ext[1:]) is not None

def add_dcm_extension(filename):
    """Add .dcm extension to the filename."""
    return filename + '.dcm'

finding_dcm_organized = False

if __name__ == '__main__':
    path = "/Data/sophie1/"  # containing .nii.gz files

    output_list_all = []
    dicom_files = []
    counter = 1

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
                                # Check if it's a directory
                                if os.path.isdir(third_level_path):
                                    # List all files within the third level folder
                                    for filename in os.listdir(third_level_path):
                                        file_path = os.path.join(third_level_path, filename)
                                        # Check if the file has a long numeric extension
                                        if os.path.isfile(file_path) and has_long_numeric_extension(filename):
                                            # Rename the file by adding .dcm extension
                                            new_filename = add_dcm_extension(filename)
                                            new_file_path = os.path.join(third_level_path, new_filename)
                                            os.rename(file_path, new_file_path)
                                            print(f'Renamed {file_path} to {new_file_path}')
