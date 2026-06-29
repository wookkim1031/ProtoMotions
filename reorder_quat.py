#!/usr/bin/env python3
"""
Reorder the root quaternion of a Unitree/GMR G1 CSV from xyzw -> wxyz
so ProtoMotions' convert_g1_csv_to_proto.py (--rot-format quat_wxyz) accepts it.

Layout (no header, no frame col): pos(3) | quat(4) | 29 joints  = 36 cols.
Only cols 3..6 are touched: [x,y,z,w] -> [w,x,y,z].
"""
import argparse, numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("inp"); ap.add_argument("out")
a = ap.parse_args()

d = np.loadtxt(a.inp, delimiter=",")
assert d.shape[1] == 36, f"expected 36 cols, got {d.shape[1]}"
q_xyzw = d[:, 3:7]
d[:, 3:7] = q_xyzw[:, [3, 0, 1, 2]]          # -> wxyz
np.savetxt(a.out, d, delimiter=",", fmt="%.10g")
print(f"{d.shape[0]} frames, quat xyzw->wxyz, wrote {a.out}")