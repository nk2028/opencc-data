# opencc-data [![](https://badge.fury.io/js/opencc-data.svg)](https://www.npmjs.com/package/opencc-data) [![JSDelivr badge](https://data.jsdelivr.com/v1/package/npm/opencc-data/badge)](https://www.jsdelivr.com/package/npm/opencc-data)

A collection of word lists for Simplified and Traditional Chinese conversions from the [OpenCC](https://github.com/BYVoid/OpenCC) project

## Usage

The data files of opencc-data (version 1.0.x) is listed below.

**From Chinese variants to OpenCC standard:**

```json
{
  "cn": ["STCharacters", "STPhrases"],
  "tw": ["TWVariantsRev", "TWVariantsRevPhrases"],
  "twp": ["TWVariantsRev", "TWVariantsRevPhrases", "TWPhrasesRev"],
  "hk": ["HKVariantsRev", "HKVariantsRevPhrases"],
  "jp": ["JPVariantsRev", "JPShinjitaiCharacters", "JPShinjitaiPhrases"]
}
```

**From OpenCC standard to Chinese variants:**

```json
{
  "cn": ["TSCharacters", "TSPhrases"],
  "hk": ["HKVariants"],
  "tw": ["TWVariants"],
  "twp": ["TWVariants", "TWPhrasesIT", "TWPhrasesName", "TWPhrasesOther"],
  "jp": ["JPVariants"]
}
```

**Explanation of the Chinese variants above:**

- `cn`: Simplified Chinese (Mainland China)
- `tw`: Traditional Chinese (Taiwan)
- `twp`: Traditional Chinese (Taiwan, with phrase conversion)
- `hk`: Traditional Chinese (Hong Kong)
- `jp`: Japanese Shinjitai
