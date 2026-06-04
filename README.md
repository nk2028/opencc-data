# opencc-data [![](https://badge.fury.io/js/opencc-data.svg)](https://www.npmjs.com/package/opencc-data) [![JSDelivr badge](https://data.jsdelivr.com/v1/package/npm/opencc-data/badge)](https://www.jsdelivr.com/package/npm/opencc-data)

A collection of word lists for Simplified and Traditional Chinese conversions from the [OpenCC](https://github.com/BYVoid/OpenCC) project.

## Compatibility

This project is primarily maintained for use with [opencc-js](https://github.com/nk2028/opencc-js).

- **Strict Version Matching**: Compatibility is only guaranteed when the version of `opencc-data` strictly matches the version of the consumer package.
- **Breaking Changes**: We do not guarantee compatibility between different versions of `opencc-data`. Structure or file names may change to align with upstream OpenCC updates.

## Data Sync Policy

This package syncs upstream OpenCC dictionary `.txt` files, config `.json` files, and `test/testcases/testcases.json`. It also generates and checks in derived dictionaries during data sync: `TSCharactersExt.txt` from `TSCharacters.txt`, plus the reverse variant dictionaries `HKVariantsRev.txt`, `TWVariantsRev.txt`, and `JPVariantsRev.txt` from their corresponding variant dictionaries.

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
  "cn": [["TSPhrases", "TSCharactersExt", "TSCharacters"]],
  "hk": [["HKVariantsPhrases", "HKVariants"]],
  "tw": [["TWVariantsPhrases", "TWVariants"]],
  "twp": [["TWPhrases"], ["TWVariantsPhrases", "TWVariants"]],
  "jp": [["JPVariants"]]
}
```

`TSCharactersExt` contains rare inferred simplified forms that may render as tofu (missing glyph boxes) in common fonts. It should generally be omitted unless those extended mappings are explicitly required.

**Explanation of the Chinese variants above:**

- `cn`: Simplified Chinese (Mainland China)
- `tw`: Traditional Chinese (Taiwan)
- `twp`: Traditional Chinese (Taiwan, with phrase conversion)
- `hk`: Traditional Chinese (Hong Kong)
- `jp`: Japanese Shinjitai
