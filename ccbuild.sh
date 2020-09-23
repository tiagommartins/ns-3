#!/bin/bash
NS3_HOME=${NS3_HOME:="$HOME/unilasalle/workspace/ns-allinone-3.31/ns-3.31"}
cp **/*.h $NS3_HOME/scratch/
cp **/*.cc $NS3_HOME/scratch/
cd $NS3_HOME
./waf