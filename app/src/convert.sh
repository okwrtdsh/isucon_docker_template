#!/usr/bin/env bash
#
gprof2dot -f pstats --colour-nodes-by-selftime --show-samples /tmp/profile/* > profile.dot
dot -Tpng profile.dot > profile.png
