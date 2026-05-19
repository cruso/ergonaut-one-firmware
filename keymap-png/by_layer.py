from pathlib import Path
import subprocess
import yaml
import os

KEYMAP = Path('keymap.yaml')
OUT = Path('out')
OUT.mkdir(parents=True, exist_ok=True)

with open(KEYMAP, 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

layers = data['layers'].keys()

layer_number = 0

for layer in layers:
    svg_path = OUT / f'layer_{layer_number}.svg'
    png_path = OUT / f'layer_{layer_number}.png'

    cmd = [
        'keymap',
        '-c',
        '../keymap-drawer/config.yaml',
        'draw',
        '-k',
        'corne_rotated',
        '-l',
        'LAYOUT_split_3x6_3',
        'keymap.yaml',
        '--select-layers',
        layer,
        '-o',
        svg_path
    ]

    result = subprocess.run(cmd, cwd=r'.', capture_output=True, text=True, shell=True)

    if(result.returncode!= 0):
        print(result)

    layer_number = layer_number + 1

    print(f'Generated: {png_path}')