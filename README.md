# opencc-data [![JSDelivr badge](https://data.jsdelivr.com/v1/package/npm/opencc-data/badge)](https://www.jsdelivr.com/package/npm/opencc-data)

Collection of [OpenCC](https://github.com/BYVoid/OpenCC) data.

## 用法

以下是 opencc-data 版本 1.0.0 的文件列表。

將各變體轉換為 OpenCC 標準：

```json
{ 'cn': ['STCharacters', 'STPhrases']
, 'hk': ['HKVariantsRev', 'HKVariantsRevPhrases']
, 'tw': ['TWVariantsRev', 'TWVariantsRevPhrases']
, 'twp': ['TWVariantsRev', 'TWVariantsRevPhrases', 'TWPhrasesRev']
, 'jp': ['JPVariantsRev', 'JPShinjitaiCharacters', 'JPShinjitaiPhrases']
}
```

將 OpenCC 標準轉換為各變體：

```json
{ 'cn': ['TSCharacters', 'TSPhrases']
, 'hk': ['HKVariants']
, 'tw': ['TWVariants']
, 'twp': ['TWVariants', 'TWPhrasesIT', 'TWPhrasesName', 'TWPhrasesOther']
, 'jp': ['JPVariants']
}
```
