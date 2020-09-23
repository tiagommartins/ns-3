#!/bin/bash
LOCAL_PATH=$PWD
NS3_HOME=${NS3_HOME:="$HOME/unilasalle/workspace/ns-allinone-3.31/ns-3.31"}
cd $NS3_HOME
./waf --pyrun $LOCAL_PATH/$1 --vis