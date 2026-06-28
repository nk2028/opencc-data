# opencc-data [![](https://badge.fury.io/js/opencc-data.svg)](https://www.npmjs.com/package/opencc-data) [![JSDelivr badge](https://data.jsdelivr.com/v1/package/npm/opencc-data/badge)](https://www.jsdelivr.com/package/npm/opencc-data)

[繁體中文](README.zh-TW.md)

A collection of dictionary data, configs, and test data for Simplified and Traditional Chinese conversions from the [OpenCC](https://github.com/BYVoid/OpenCC) project.

## Compatibility

This package is intended for [opencc-js](https://github.com/nk2028/opencc-js) and other OpenCC-compatible implementations that consume OpenCC dictionary and config data.

- **Strict Version Matching**: Compatibility is only guaranteed when the version of `opencc-data` strictly matches the version of the consumer package.
- **Breaking Changes**: We do not guarantee compatibility between different versions of `opencc-data`. Structure or file names may change to align with upstream OpenCC updates.

## Data Sync Policy

This package syncs dictionary `.txt` files and config `.json` files from OpenCC's generated resource zip, plus `test/testcases/testcases.json` from the upstream repository. Each sync keeps the upstream resource manifest as an internal baseline so future updates can detect substantive data changes by resource hash.

## Usage

Use the config files shipped in `data/config/` as the source of truth for dictionary order and conversion-chain behavior. Config contents can change between OpenCC versions, so consumers should load the matching config file for the package version they depend on instead of hard-coding dictionary lists from this README.

Dictionary text files are shipped in `data/`. Config files reference those dictionaries by file name and preserve OpenCC's stage/group ordering semantics.

Python consumers can install the `opencc-data` package from PyPI and use the `opencc_data` module to locate packaged resources:

```python
import opencc_data

config_file = opencc_data.config_path("s2t.json")
dictionary_file = opencc_data.data_path("STCharacters.txt")
testcases_file = opencc_data.test_data_path("testcases.json")
```

Release versions match across npm and PyPI, such as `1.3.2`. For `next` prereleases, PyPI uses the PEP 440 equivalent of the npm version: `1.3.2-next.20260628` is published to PyPI as `1.3.2.dev20260628`.
