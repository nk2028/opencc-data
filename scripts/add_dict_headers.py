#!/usr/bin/env python3
"""Prepend stable copyright headers to generated OpenCC dictionary txt files.

Reads source metadata from the opencc-resource-manifest.json produced by the
//data:opencc_resources_zip Bazel target. Files that already contain OpenCC's
native dictionary header are left untouched.

Usage:
    python3 scripts/add_dict_headers.py <manifest_path> [upstream_ref]
"""

import glob
import json
import os
import sys

# Mirrors the genrule relationships in data/dictionary/BUILD.bazel.
# Update this map when upstream adds or changes generation rules.
GENERATED_FROM = {
    "HKVariantsRev.txt": "HKVariants.txt",
    "HKVariantsRevPhrases.txt": "HKVariantsPhrases.txt",
    "TWVariantsRev.txt": "TWVariants.txt",
    "TWVariantsRevPhrases.txt": "TWVariantsPhrases.txt",
    "JPShinjitaiCharactersRev.txt": "JPShinjitaiCharacters.txt",
    "JPVariantsRev.txt": "JPVariants.txt",
    "TSCharactersExt.txt": "TSCharacters.txt",
    "STPhrases_GeneratedFromRegionalPhrases.txt": "HKPhrases.txt, TWPhrases.txt",
    "STPhrases_WithGeneratedFromRegionalPhrases.txt": "STPhrases.txt, HKPhrases.txt, TWPhrases.txt",
}


def main():
    manifest_path = sys.argv[1] if len(sys.argv) > 1 else "/tmp/opencc-resources/opencc-resource-manifest.json"

    with open(manifest_path) as f:
        manifest = json.load(f)

    source_url = manifest.get("source_url", "https://github.com/BYVoid/OpenCC")

    for p in sorted(glob.glob("data/*.txt")):
        filename = os.path.basename(p)
        with open(p) as f:
            content = f.read()

        if content.startswith("# Open Chinese Convert (OpenCC) Dictionary"):
            continue

        source = GENERATED_FROM.get(filename)
        file_line = f"# File: {filename}" + (f" (Generated from: {source})" if source else "")
        header = "\n".join([
            "# Open Chinese Convert (OpenCC) Dictionary",
            file_line,
            "# License: Apache-2.0 (see LICENSE)",
            f"# Source: {source_url}",
            "",
            "",
        ])

        with open(p, "w") as f:
            f.write(header + content)


if __name__ == "__main__":
    main()
