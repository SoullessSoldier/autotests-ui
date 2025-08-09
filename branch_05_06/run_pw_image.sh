#!/bin/bash
export MSYS_NO_PATHCONV=1
docker run --rm -it -v $(pwd)/src:/opt/src playwright-python bash