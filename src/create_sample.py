from pathlib import Path

import h5py
import numpy as np


project_root = Path(__file__).resolve().parent.parent
output_path = project_root / "data" / "sample.h5"

cube = np.random.randint(
    low=0,
    high=65535,
    size=(256, 256, 16),
    dtype=np.uint16,
)

with h5py.File(output_path, "w") as file:
    dataset = file.create_dataset(
        "hyperspectral_cube",
        data=cube,
    )

    dataset.attrs["wavelength_start_nm"] = 400
    dataset.attrs["wavelength_end_nm"] = 700
    dataset.attrs["number_of_bands"] = 16

    metadata = file.create_group("metadata")
    metadata.attrs["manuscript"] = "Training sample"
    metadata.attrs["purpose"] = "BROKENSONG HDF5 practice"
    metadata.attrs["created_by"] = "Shristi"


print(f"Created: {output_path}")