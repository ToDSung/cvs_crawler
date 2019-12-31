#!/usr/bin/bash

this_file_path=`readlink -f $0`
this_dir_path=`dirname $this_file_path`
project_dir_path=`dirname $this_dir_path`

cd $project_dir_path

sudo docker build \
-f docker.local/Dockerfile \
-t cvs_api:20.1.1 \
.

cd -
