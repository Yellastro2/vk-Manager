#!/bin/bash
echo "Installing vk manager\n"
pkg install -y python
curl -o vk_share.py https://github.com/Yellastro2/vk-Manager/raw/main/vk_share.py
python vk_share.py