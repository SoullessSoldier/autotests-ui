#!/bin/bash
export MSYS_NO_PATHCONV=1
docker run --name pw_python_sshd -d -p 2222:22 -v $(dirname $(pwd)):/home/vscode/workspace playwright-python-sshd-v2
