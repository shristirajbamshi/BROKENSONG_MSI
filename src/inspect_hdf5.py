"""

inspect_hdf5.py

Inspect the structure and metadata of an HDF5 file.

Learning goals:

1. Explore the file structure.

2. Distinguish Groups from Datasets.

3. Inspect dataset properties.

4. Read dataset metadata (attributes).

Author: Shristi Rajbamshi
"""

from pathlib import Path
import h5py
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------
# Locate the HDF5 file
# ---------------------------------------------------------------------
# __file__ is the location of this Python script.
# parent       -> src/
# parent.parent -> project root (BROKENSONG_MSI/)
#
# This approach works regardless of where the project is stored.
project_root = Path(__file__).resolve().parent.parent

# Construct the path to the sample HDF5 file.
file_path = project_root / "data" / "sample.h5"


# ---------------------------------------------------------------------
# Open the HDF5 file
# ---------------------------------------------------------------------
# "r" means read-only mode.
# The file is automatically closed after leaving the 'with' block.
with h5py.File(file_path, "r") as f:

    # ==============================================================
    # STEP 1: Inspect the root level of the HDF5 file
    # ==============================================================
    # f.keys() returns the names of all objects stored at the root
    # of the HDF5 file.
    print("=" * 60)
    print("STEP 1: Root objects")
    print("=" * 60)

    print(list(f.keys()))

    # ==============================================================
    # STEP 2: Identify the type of each object
    # ==============================================================
    # Every object in an HDF5 file is usually either:
    #
    # - Dataset -> stores actual numerical data
    # - Group   -> acts like a folder containing other objects
    print("\n" + "=" * 60)
    print("STEP 2: Object types")
    print("=" * 60)

    for name in f.keys():

        obj = f[name]

        print(f"\nObject: {name}")

        print(f"Type: {type(obj).__name__}")

    # ==============================================================
    # STEP 3: Inspect the hyperspectral image dataset
    # ==============================================================
    # Access the dataset by its name.
    cube = f["hyperspectral_cube"]

    print("\n" + "=" * 60)
    print("STEP 3: Dataset information")
    print("=" * 60)

    # Shape of the dataset
    #
    # (height, width, spectral bands)
    #
    # Example:
    # (256, 256, 16)
    #   -> image height = 256 pixels
    #   -> image width  = 256 pixels
    #   -> 16 wavelength bands
    print(f"Shape      : {cube.shape}")

    # Data type stored for every pixel.
    #
    # uint16 means every pixel value occupies
    # 16 bits (unsigned integer).
    print(f"Data type  : {cube.dtype}")

    # Number of dimensions.
    #
    # A multispectral image is typically 3-dimensional:
    # (height, width, spectral bands)
    print(f"Dimensions : {cube.ndim}")

    # ==============================================================
    # STEP 4: Inspect metadata (attributes)
    # ==============================================================
    #
    # Attributes describe the dataset rather than storing image data.
    #
    # Examples:
    # - wavelength range
    # - camera information
    # - acquisition date
    # - calibration settings
    print("\n" + "=" * 60)
    print("STEP 4: Dataset attributes")
    print("=" * 60)

    for key, value in cube.attrs.items():
        print(f"{key}: {value}")

    # ==============================================================
    # Step 5: Load the dataset into a NumPy array
    # ==============================================================
    # The [:] operator reads the entire dataset into memory.
    # The result is a NumPy array instead of an HDF5 Dataset.

    cube_array = cube[:]

    print("\n" + "=" * 60)
    print("STEP 5: NumPy array")
    print("=" * 60)

    print(f"Type       : {type(cube_array).__name__}")
    print(f"Shape      : {cube_array.shape}")
    print(f"Data type  : {cube_array.dtype}")

    # ==============================================================
    # Step 6: Extract one spectral band
    # ==============================================================
    # cube_array[:, :, 0]
    #
    # :  -> all rows
    # :  -> all columns
    # 0  -> first spectral band

    band0 = cube_array[:, :, 0]

    print("\n" + "=" * 60)
    print("STEP 6: First spectral band")
    print("=" * 60)

    print(f"Type       : {type(band0).__name__}")
    print(f"Shape      : {band0.shape}")

# ---------------------------------------------------------------------
# Display the image
# ---------------------------------------------------------------------
    plt.imshow(band0, cmap="gray")
    plt.title("Band 0")
    plt.colorbar()
    plt.show()