# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: exoplanet-ml
#     language: python
#     name: exoplanet-ml
# ---

# %%
from light_curve import kepler_io
import matplotlib.pyplot as plt
import numpy as np
import glob

# %%
# %matplotlib inline
plt.rcParams['figure.figsize'] = (40.0, 20.0)
KEPLER_DATA_DIR = "/run/media/julian/fcc15beb-83a1-4606-ac14-07fdc2ffa10f/kepler/"

for dir in sorted(glob.glob(KEPLER_DATA_DIR+"/*/*"), key=lambda x: int(x.split("/")[-1])):
    KEPLER_ID = int(dir.split("/")[-1])
    file_names = kepler_io.kepler_filenames(KEPLER_DATA_DIR, KEPLER_ID)
    assert file_names, "Failed to find .fits files in {}".format(KEPLER_DATA_DIR)
    all_time, all_flux = kepler_io.read_kepler_light_curve(file_names)
    all_flux = [f/np.median(f) for f in all_flux]
    print("Read light curve with {} segments".format(len(all_time)))
    plt.plot(np.concatenate(all_time), np.concatenate(all_flux), ".")
    plt.title(str(KEPLER_ID))
    plt.figure
    plt.show()
