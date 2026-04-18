# Dataset Viewer

[![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://github.com/Hillpro/dataset-viewer/blob/main/LICENSE)
[![Supported Python versions](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FHillpro%2Fdataset-viewer%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=%24%5Bproject%5D.requires-python&label=python&color=blue&link=https%3A%2F%2Fpypi.org%2Fproject%2Fdataset-viewer%2F
)](https://python.org)
[![Python package index](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FHillpro%2Fdataset-viewer%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=%24%5Bproject%5D.version&label=pypi&color=orange&link=https%3A%2F%2Fpypi.org%2Fproject%2Fdataset-viewer%2F
)](https://pypi.org/project/dataset-viewer)
[![Python package index download statistics](https://img.shields.io/pypi/dm/dataset-viewer)](https://pypistats.org/packages/dataset-viewer)
[![Development Status](https://img.shields.io/badge/status-beta-yellow.svg)](https://en.wikipedia.org/wiki/Software_release_life_cycle#Beta)

A small [napari](https://napari.org) wrapper that lets you step through a folder of images and paint / edit segmentation labels for each one. Labels are saved to disk as PNGs, one per image.

## Install

It is recommended to install the dataset viewer into a virtual environment. To install, run: 

```sh
python -m pip install "dataset_viewer[gui]"
```

The `[gui]` extra installs PyQt5 as the napari Qt backend. Omit it if you already have a Qt binding available in your environment.

> **Python version** — developed and tested on Python 3.9. `requires-python = ">=3.9"` allows newer interpreters, but no testing has been done on 3.10+; use at your own risk.

## Data layout

The viewer expects a directory with two sub-folders:

```
<data_path>/
├── images/     # .jpg, .jpeg or .png source images
└── labels/     # .png label masks, created/updated by the viewer
```

Labels are always written as PNG (other formats compress and corrupt label values) and named after the source image stem — e.g. `images/cat_01.jpg` → `labels/cat_01.png`. An image with an all-zero label array is represented by the **absence** of the label file; the viewer deletes the file when you clear a mask.

## Usage

```python
from pathlib import Path
from dataset_viewer import Viewer, Dataset

Viewer(Dataset(Path("path/to/data"))).start()
```

`Dataset()` with no argument defaults to `./data` relative to the **current working directory**.

### Key bindings

| Key      | Action                               |
| -------- | ------------------------------------ |
| `Left`   | Previous image (saves current mask)  |
| `Right`  | Next image (saves current mask)      |
| `l`      | Print the active layer name          |
| `Escape` | Close the viewer                     |

Painting/erasing uses napari's standard labels-layer controls.

## License

MIT — see [LICENSE](LICENSE).
