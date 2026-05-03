# opencc-data [![](https://badge.fury.io/js/opencc-data.svg)](https://www.npmjs.com/package/opencc-data) [![JSDelivr badge](https://data.jsdelivr.com/v1/package/npm/opencc-data/badge)](https://www.jsdelivr.com/package/npm/opencc-data)

A collection of word lists for Simplified and Traditional Chinese conversions from the [OpenCC](https://github.com/BYVoid/OpenCC) project.

## Compatibility

This project is primarily maintained for use with [opencc-js](https://github.com/nk2028/opencc-js).

- **Strict Version Matching**: Compatibility is only guaranteed when the version of `opencc-data` strictly matches the version of the consumer package.
- **Breaking Changes**: We do not guarantee compatibility between different versions of `opencc-data`. Structure or file names may change to align with upstream OpenCC updates.

## Data Sync Policy

This package only syncs upstream-authored content that should not be mechanically generated downstream: OpenCC dictionary `.txt` files and `test/testcases/testcases.json`. Reverse dictionaries are included only when they are present in upstream OpenCC; this repository does not generate additional reverse dictionary files locally.

## Usage

The data files prioritize canonical data from the OpenCC project. The following configurations are strictly consistent with the logic in OpenCC's `.json` configuration files:

- **Outer Array (Stages)**: Represents the conversion-chain stages.
- **Inner Array (Groups)**: Represents a dictionary group used within one stage; dictionaries earlier in the group have higher priority when their entries overlap (merged relationship).

**From Chinese variants to OpenCC standard:**

```json
{
  "cn": [["STPhrases", "STCharacters"]],
  "hk": [["HKVariantsRevPhrases", "HKVariantsRev"]],
  "tw": [["TWVariantsRevPhrases", "TWVariantsRev"]],
  "twp": [["TWPhrasesRev", "TWVariantsRevPhrases", "TWVariantsRev"]],
  "jp": [["JPShinjitaiPhrases", "JPShinjitaiCharacters", "JPVariantsRev"]]
}
```

**From OpenCC standard to Chinese variants:**

```json
{
  "cn": [["TSPhrases", "TSCharacters"]],
  "hk": [["HKVariants"]],
  "tw": [["TWVariants"]],
  "twp": [["TWPhrases"], ["TWVariants"]],
  "jp": [["JPVariants"]]
}
```

**Explanation of the Chinese variants above:**

- `cn`: Simplified Chinese (Mainland China)
- `tw`: Traditional Chinese (Taiwan)
- `twp`: Traditional Chinese (Taiwan, with phrase conversion)
- `hk`: Traditional Chinese (Hong Kong)
- `jp`: Japanese Shinjitai
