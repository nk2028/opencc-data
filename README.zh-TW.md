# opencc-data [![](https://badge.fury.io/js/opencc-data.svg)](https://www.npmjs.com/package/opencc-data) [![JSDelivr badge](https://data.jsdelivr.com/v1/package/npm/opencc-data/badge)](https://www.jsdelivr.com/package/npm/opencc-data)

[English](README.md)

本套件收錄來自 [OpenCC](https://github.com/BYVoid/OpenCC) 專案的簡繁轉換詞典資料、配置與測試集。

## 相容性

本套件適用於 [opencc-js](https://github.com/nk2028/opencc-js)，也可供其他相容 OpenCC 詞典與設定檔格式的實作使用。

- **嚴格版本匹配**：只有在 `opencc-data` 與使用端套件版本完全一致時，才保證相容性。
- **破壞性變更**：不同版本的 `opencc-data` 之間不保證相容。資料結構或檔名可能會隨上游 OpenCC 更新而調整。

## 資料同步政策

本套件會從 OpenCC 產生的 resource zip 同步詞典 `.txt` 檔與設定 `.json` 檔，並從上游 repository 同步 `test/testcases/testcases.json`。每次同步都會保留上游 resource manifest 作為內部基準，之後可透過 resource hash 判斷是否有實質資料變更。

## 使用方式

請以套件內 `data/config/` 提供的設定檔作為詞典順序與轉換鏈行為的依據。設定內容可能隨 OpenCC 版本改變，因此使用端應載入其依賴版本對應的設定檔，而不是從 README 固定寫死詞典列表。

詞典文字檔位於 `data/`。設定檔會以檔名引用這些詞典，並保留 OpenCC 的 stage/group 排序語意。

Python 使用者可以從 PyPI 安裝 `opencc-data`，並透過 `opencc_data` module 定位套件內資源：

```python
import opencc_data

config_file = opencc_data.config_path("s2t.json")
dictionary_file = opencc_data.data_path("STCharacters.txt")
testcases_file = opencc_data.test_data_path("testcases.json")
```

正式版在 npm 與 PyPI 會使用相同版本號，例如 `1.3.2`。`next` prerelease 則會在 PyPI 使用對應的 PEP 440 版本：`1.3.2-next.20260628` 會以 `1.3.2.dev20260628` 發佈到 PyPI。
