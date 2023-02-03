#!/bin/bash
echo "****Installing vk manager****"
pkg install -y python
curl -o vk_share.py https://raw.githubusercontent.com/Yellastro2/vk-Manager/main/vk_share.py
python vk_share.py
