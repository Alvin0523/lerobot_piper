# Copyright 2024 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from typing import Any

import cv2
import numpy as np
import rerun as rr


def _init_rerun(session_name: str = "lerobot_control_loop") -> None:
    """Initializes the Rerun SDK for visualizing the control loop."""
    # Large flush threshold: reduces how often Python blocks waiting for gRPC proxy.
    # Small values (e.g. 5MB) cause frequent flushes that can freeze the control loop
    # when the gRPC proxy hits its 1 GiB memory limit and stalls.
    batch_size = os.getenv("RERUN_FLUSH_NUM_BYTES", "100000000")  # 100 MB
    os.environ["RERUN_FLUSH_NUM_BYTES"] = batch_size
    rr.init(session_name)
    memory_limit = os.getenv("LEROBOT_RERUN_MEMORY_LIMIT", "50%")
    rr.spawn(memory_limit=memory_limit)


_rerun_frame_index = 0


def log_rerun_data(observation: dict[str | Any], action: dict[str | Any]):
    global _rerun_frame_index
    # Set a monotonic frame index so rerun treats each call as a new timestep.
    # This allows the viewer to overwrite old frames instead of accumulating them,
    # which prevents the gRPC server from hitting its 1 GiB memory limit.
    rr.set_time("frame", sequence=_rerun_frame_index)
    _rerun_frame_index += 1

    for obs, val in observation.items():
        if isinstance(val, float):
            rr.log(f"observation.{obs}", rr.Scalars(val))
        elif isinstance(val, np.ndarray):
            if val.ndim == 1:
                for i, v in enumerate(val):
                    rr.log(f"observation.{obs}_{i}", rr.Scalars(float(v)))
            else:
                if val.ndim == 2:  # depth map (H, W) uint16
                    depth_normalized = cv2.normalize(val, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
                    display_img = cv2.applyColorMap(depth_normalized, cv2.COLORMAP_TURBO)

                        # 当前
                       # cv2.applyColorMap(depth_normalized, cv2.COLORMAP_JET)   # 蓝→红
                        # 其他选项
                        #cv2.applyColorMap(depth_normalized, cv2.COLORMAP_TURBO)  # 更清晰的近远区分
                        #cv2.applyColorMap(depth_normalized, cv2.COLORMAP_HOT)    # 黑→白热力图

                    display_img = cv2.resize(display_img, (320, 240))
                else:
                    display_img = cv2.resize(val, (320, 240))
                rr.log(f"observation.{obs}", rr.Image(display_img))
    for act, val in action.items():
        if isinstance(val, float):
            rr.log(f"action.{act}", rr.Scalars(val))
        elif isinstance(val, np.ndarray):
            for i, v in enumerate(val):
                rr.log(f"action.{act}_{i}", rr.Scalars(float(v)))

init_rerun = _init_rerun # to integrate with vlash-piper