#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

for file in os.listdir('data'):
    if file.endswith('.txt'):
        file = os.path.join('data', file)
        with open(file) as f:
            lines = sorted(f)
        with open(file, 'w') as f:
            for line in lines:
                f.write(line)
