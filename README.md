<p align="center">
  <img alt="LeRobot, Hugging Face Robotics Library" src="https://raw.githubusercontent.com/huggingface/lerobot/main/media/lerobot-logo-thumbnail.png" width="100%">
  <br/>
  <br/>
</p>

<div align="center">

[![Tests](https://github.com/huggingface/lerobot/actions/workflows/nightly.yml/badge.svg?branch=main)](https://github.com/huggingface/lerobot/actions/workflows/nighty.yml?query=branch%3Amain)
[![Python versions](https://img.shields.io/pypi/pyversions/lerobot)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/huggingface/lerobot/blob/main/LICENSE)
[![Status](https://img.shields.io/pypi/status/lerobot)](https://pypi.org/project/lerobot/)
[![Version](https://img.shields.io/pypi/v/lerobot)](https://pypi.org/project/lerobot/)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.1-ff69b4.svg)](https://github.com/huggingface/lerobot/blob/main/CODE_OF_CONDUCT.md)
[![Discord](https://dcbadge.vercel.app/api/server/C5P34WJ68S?style=flat)](https://discord.gg/s3KuuzsPFb)

</div>

<h2 align="center">
    <p><a href="https://huggingface.co/docs/lerobot/hope_jr">
        Build Your Own HopeJR Robot!</a></p>
</h2>

<div align="center">
  <img
    src="https://raw.githubusercontent.com/huggingface/lerobot/main/media/hope_jr/hopejr.png"
    alt="HopeJR robot"
    title="HopeJR robot"
    width="60%"
  />

  <p><strong>Meet HopeJR – A humanoid robot arm and hand for dexterous manipulation!</strong></p>
  <p>Control it with exoskeletons and gloves for precise hand movements.</p>
  <p>Perfect for advanced manipulation tasks! 🤖</p>

  <p><a href="https://huggingface.co/docs/lerobot/hope_jr">
      See the full HopeJR tutorial here.</a></p>
</div>

<br/>

<h2 align="center">
    <p><a href="https://huggingface.co/docs/lerobot/so101">
        Build Your Own SO-101 Robot!</a></p>
</h2>

<div align="center">
  <table>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/huggingface/lerobot/main/media/so101/so101.webp" alt="SO-101 follower arm" title="SO-101 follower arm" width="90%"/></td>
      <td align="center"><img src="https://raw.githubusercontent.com/huggingface/lerobot/main/media/so101/so101-leader.webp" alt="SO-101 leader arm" title="SO-101 leader arm" width="90%"/></td>
    </tr>
  </table>

  <p><strong>Meet the updated SO100, the SO-101 – Just €114 per arm!</strong></p>
  <p>Train it in minutes with a few simple moves on your laptop.</p>
  <p>Then sit back and watch your creation act autonomously! 🤯</p>

  <p><a href="https://huggingface.co/docs/lerobot/so101">
      See the full SO-101 tutorial here.</a></p>

  <p>Want to take it to the next level? Make your SO-101 mobile by building LeKiwi!</p>
  <p>Check out the <a href="https://huggingface.co/docs/lerobot/lekiwi">LeKiwi tutorial</a> and bring your robot to life on wheels.</p>

  <img src="https://raw.githubusercontent.com/huggingface/lerobot/main/media/lekiwi/kiwi.webp" alt="LeKiwi mobile robot" title="LeKiwi mobile robot" width="50%">
</div>

<br/>

<h3 align="center">
    <p>LeRobot: State-of-the-art AI for real-world robotics</p>
</h3>

---

🤗 LeRobot aims to provide models, datasets, and tools for real-world robotics in PyTorch. The goal is to lower the barrier to entry to robotics so that everyone can contribute and benefit from sharing datasets and pretrained models.

🤗 LeRobot contains state-of-the-art approaches that have been shown to transfer to the real-world with a focus on imitation learning and reinforcement learning.

🤗 LeRobot already provides a set of pretrained models, datasets with human collected demonstrations, and simulation environments to get started without assembling a robot. In the coming weeks, the plan is to add more and more support for real-world robotics on the most affordable and capable robots out there.

🤗 LeRobot hosts pretrained models and datasets on this Hugging Face community page: [huggingface.co/lerobot](https://huggingface.co/lerobot)

#### Examples of pretrained models on simulation environments

<table>
  <tr>
    <td><img src="https://raw.githubusercontent.com/huggingface/lerobot/main/media/gym/aloha_act.gif" width="100%" alt="ACT policy on ALOHA env"/></td>
    <td><img src="https://raw.githubusercontent.com/huggingface/lerobot/main/media/gym/simxarm_tdmpc.gif" width="100%" alt="TDMPC policy on SimXArm env"/></td>
    <td><img src="https://raw.githubusercontent.com/huggingface/lerobot/main/media/gym/pusht_diffusion.gif" width="100%" alt="Diffusion policy on PushT env"/></td>
  </tr>
  <tr>
    <td align="center">ACT policy on ALOHA env</td>
    <td align="center">TDMPC policy on SimXArm env</td>
    <td align="center">Diffusion policy on PushT env</td>
  </tr>
</table>

## Installation

LeRobot works with Python 3.10+ and PyTorch 2.2+.

This project uses [Pixi](https://pixi.sh/) for environment and dependency management.
You do not need to manually install conda, pip, or ffmpeg — Pixi handles everything.

### 1. Install Pixi

```bash
curl -fsSL https://pixi.sh/install.sh | sh
```

### 2. Clone the repository

```bash
git clone https://github.com/huggingface/lerobot.git
cd lerobot
```

### 3. Install dependencies

```bash
pixi install
```

Pixi will automatically set up Python 3.10, ffmpeg, cmake, and all required Python packages.

### 4. Enter the environment

```bash
pixi shell
```

You are now inside the fully configured environment. No `conda activate` or `pip install` needed.

---

## Optional Environments

For simulation environments or specific hardware support, install the relevant pixi environment:

```bash
pixi install -e aloha       # ALOHA simulation
pixi install -e pusht       # PushT simulation
pixi install -e xarm        # XArm simulation
pixi install -e dynamixel   # Dynamixel motors
pixi install -e feetech     # Feetech motors
pixi install -e hopejr      # HopeJR humanoid robot
pixi install -e lekiwi      # LeKiwi mobile robot
pixi install -e gamepad     # Gamepad controller
pixi install -e kinematics  # Kinematics support
pixi install -e realsense   # Intel RealSense camera
pixi install -e pi0         # Pi0 policy
pixi install -e smolvla     # SmolVLA policy
pixi install -e hilserl     # HiLSERL policy
pixi install -e dev         # Development tools
pixi install -e test        # Test dependencies
```

Enter a specific environment shell:

```bash
pixi shell -e aloha
```

---

## Usage

All commands are run via `pixi run <task>`. You do not need to activate the environment first.

### Robot Tasks

**Teleoperate a robot:**
```bash
pixi run teleoperate
```

**Record a dataset:**
```bash
pixi run record
```

**Replay a recorded dataset:**
```bash
pixi run replay
```

**Calibrate a robot:**
```bash
pixi run calibrate
```

**Setup motors:**
```bash
pixi run setup-motors
```

**Find available cameras:**
```bash
pixi run find-cameras
```

**Find available ports:**
```bash
pixi run find-port
```

### Training & Evaluation

**Train a policy:**
```bash
pixi run train
```

To pass arguments:
```bash
pixi run train -- --config_path=lerobot/diffusion_pusht --wandb.enable=true
```

**Evaluate a pretrained policy:**
```bash
pixi run eval
```

To pass arguments:
```bash
pixi run eval -- \
    --policy.path=lerobot/diffusion_pusht \
    --env.type=pusht \
    --eval.batch_size=10 \
    --eval.n_episodes=10 \
    --policy.device=cuda
```

Note: After training your own policy, you can re-evaluate checkpoints with:
```bash
pixi run eval -- --policy.path={OUTPUT_DIR}/checkpoints/last/pretrained_model
```

### Running in a Specific Environment

To run any task inside a specific pixi environment, use `-e`:

```bash
pixi run -e aloha train
pixi run -e pusht eval
pixi run -e feetech teleoperate
pixi run -e hopejr record
pixi run -e lekiwi teleoperate
```

### Development Tasks

**Run linter:**
```bash
pixi run lint
```

**Run formatter:**
```bash
pixi run format
```

**Run tests:**
```bash
pixi run test
```

**Run security scan:**
```bash
pixi run security
```

---

## Weights & Biases

To use [Weights and Biases](https://docs.wandb.ai/quickstart) for experiment tracking, log in with:

```bash
wandb login
```

Then enable WandB when training by passing `--wandb.enable=true`:

```bash
pixi run train -- --wandb.enable=true
```

---

## Visualize Datasets

Check out [example 1](https://github.com/huggingface/lerobot/blob/main/examples/1_load_lerobot_dataset.py) that illustrates how to use our dataset class which automatically downloads data from the Hugging Face hub.

You can also locally visualize episodes from a dataset on the hub by executing our script from the command line:

```bash
python -m lerobot.scripts.visualize_dataset \
    --repo-id lerobot/pusht \
    --episode-index 0
```

or from a dataset in a local folder with the `root` option and the `--local-files-only` flag:

```bash
python -m lerobot.scripts.visualize_dataset \
    --repo-id lerobot/pusht \
    --root ./my_local_data_dir \
    --local-files-only 1 \
    --episode-index 0
```

It will open `rerun.io` and display the camera streams, robot states and actions.

Our script can also visualize datasets stored on a distant server. See `python -m lerobot.scripts.visualize_dataset --help` for more instructions.

---

## The `LeRobotDataset` Format

A dataset in `LeRobotDataset` format is very simple to use. It can be loaded from a repository on the Hugging Face hub or a local folder simply with e.g. `dataset = LeRobotDataset("lerobot/aloha_static_coffee")` and can be indexed into like any Hugging Face and PyTorch dataset. For instance `dataset[0]` will retrieve a single temporal frame from the dataset containing observation(s) and an action as PyTorch tensors ready to be fed to a model.

A specificity of `LeRobotDataset` is that, rather than retrieving a single frame by its index, we can retrieve several frames based on their temporal relationship with the indexed frame, by setting `delta_timestamps` to a list of relative times with respect to the indexed frame. For example, with `delta_timestamps = {"observation.image": [-1, -0.5, -0.2, 0]}` one can retrieve, for a given index, 4 frames: 3 "previous" frames 1 second, 0.5 seconds, and 0.2 seconds before the indexed frame, and the indexed frame itself (corresponding to the 0 entry). See example [1_load_lerobot_dataset.py](https://github.com/huggingface/lerobot/blob/main/examples/1_load_lerobot_dataset.py) for more details on `delta_timestamps`.

Here are the important details and internal structure of a typical `LeRobotDataset`:

```
dataset attributes:
  ├ hf_dataset: a Hugging Face dataset (backed by Arrow/parquet). Typical features example:
  │  ├ observation.images.cam_high (VideoFrame):
  │  │   VideoFrame = {'path': path to a mp4 video, 'timestamp' (float32): timestamp in the video}
  │  ├ observation.state (list of float32): position of an arm joints (for instance)
  │  ... (more observations)
  │  ├ action (list of float32): goal position of an arm joints (for instance)
  │  ├ episode_index (int64): index of the episode for this sample
  │  ├ frame_index (int64): index of the frame for this sample in the episode ; starts at 0 for each episode
  │  ├ timestamp (float32): timestamp in the episode
  │  ├ next.done (bool): indicates the end of an episode ; True for the last frame in each episode
  │  └ index (int64): general index in the whole dataset
  ├ episode_data_index: contains 2 tensors with the start and end indices of each episode
  │  ├ from (1D int64 tensor): first frame index for each episode — shape (num episodes,) starts with 0
  │  └ to: (1D int64 tensor): last frame index for each episode — shape (num episodes,)
  ├ stats: a dictionary of statistics (max, mean, min, std) for each feature in the dataset, for instance
  │  ├ observation.images.cam_high: {'max': tensor with same number of dimensions (e.g. `(c, 1, 1)` for images, `(c,)` for states), etc.}
  │  ...
  ├ info: a dictionary of metadata on the dataset
  │  ├ codebase_version (str): this is to keep track of the codebase version the dataset was created with
  │  ├ fps (float): frame per second the dataset is recorded/synchronized to
  │  ├ video (bool): indicates if frames are encoded in mp4 video files to save space or stored as png files
  │  └ encoding (dict): if video, this documents the main options that were used with ffmpeg to encode the videos
  ├ videos_dir (Path): where the mp4 videos or png images are stored/accessed
  └ camera_keys (list of string): the keys to access camera features in the item returned by the dataset (e.g. `["observation.images.cam_high", ...]`)
```

A `LeRobotDataset` is serialised using several widespread file formats for each of its parts, namely:

- `hf_dataset` stored using Hugging Face datasets library serialization to parquet
- videos are stored in mp4 format to save space
- metadata are stored in plain json/jsonl files

Dataset can be uploaded/downloaded from the HuggingFace hub seamlessly. To work on a local dataset, you can specify its location with the `root` argument if it's not in the default `~/.cache/huggingface/lerobot` location.

---

## Reproduce State-of-the-Art (SOTA)

We provide some pretrained policies on our [hub page](https://huggingface.co/lerobot) that can achieve state-of-the-art performances. You can reproduce their training by loading the config from their run:

```bash
pixi run train -- --config_path=lerobot/diffusion_pusht
```

reproduces SOTA results for Diffusion Policy on the PushT task.

---

## Contribute

If you would like to contribute to 🤗 LeRobot, please check out our [contribution guide](https://github.com/huggingface/lerobot/blob/main/CONTRIBUTING.md).

### Add a Pretrained Policy

Once you have trained a policy you may upload it to the Hugging Face hub using a hub id that looks like `${hf_user}/${repo_name}` (e.g. [lerobot/diffusion_pusht](https://huggingface.co/lerobot/diffusion_pusht)).

You first need to find the checkpoint folder located inside your experiment directory (e.g. `outputs/train/2024-05-05/20-21-12_aloha_act_default/checkpoints/002500`). Within that there is a `pretrained_model` directory which should contain:

- `config.json`: A serialized version of the policy configuration (following the policy's dataclass config).
- `model.safetensors`: A set of `torch.nn.Module` parameters, saved in [Hugging Face Safetensors](https://huggingface.co/docs/safetensors/index) format.
- `train_config.json`: A consolidated configuration containing all parameters used for training. The policy configuration should match `config.json` exactly. This is useful for anyone who wants to evaluate your policy or for reproducibility.

To upload these to the hub, run the following:

```bash
huggingface-cli upload ${hf_user}/${repo_name} path/to/pretrained_model
```

See [eval.py](https://github.com/huggingface/lerobot/blob/main/src/lerobot/scripts/eval.py) for an example of how other people may use your policy.

---

## Acknowledgment

- The LeRobot team 🤗 for building SmolVLA [Paper](https://arxiv.org/abs/2506.01844), [Blog](https://huggingface.co/blog/smolvla).
- Thanks to Tony Zhao, Zipeng Fu and colleagues for open sourcing ACT policy, ALOHA environments and datasets. Ours are adapted from [ALOHA](https://tonyzhaozh.github.io/aloha) and [Mobile ALOHA](https://mobile-aloha.github.io).
- Thanks to Cheng Chi, Zhenjia Xu and colleagues for open sourcing Diffusion policy, Pusht environment and datasets, as well as UMI datasets. Ours are adapted from [Diffusion Policy](https://diffusion-policy.cs.columbia.edu) and [UMI Gripper](https://umi-gripper.github.io).
- Thanks to Nicklas Hansen, Yunhai Feng and colleagues for open sourcing TDMPC policy, Simxarm environments and datasets. Ours are adapted from [TDMPC](https://github.com/nicklashansen/tdmpc) and [FOWM](https://www.yunhaifeng.com/FOWM).
- Thanks to Antonio Loquercio and Ashish Kumar for their early support.
- Thanks to [Seungjae (Jay) Lee](https://sjlee.cc/), [Mahi Shafiullah](https://mahis.life/) and colleagues for open sourcing [VQ-BeT](https://sjlee.cc/vq-bet/) policy and helping us adapt the codebase to our repository. The policy is adapted from [VQ-BeT repo](https://github.com/jayLEE0301/vq_bet_official).

---

## Citation

If you want, you can cite this work with:

```bibtex
@misc{cadene2024lerobot,
    author = {Cadene, Remi and Alibert, Simon and Soare, Alexander and Gallouedec, Quentin and Zouitine, Adil and Palma, Steven and Kooijmans, Pepijn and Aractingi, Michel and Shukor, Mustafa and Aubakirova, Dana and Russi, Martino and Capuano, Francesco and Pascal, Caroline and Choghari, Jade and Moss, Jess and Wolf, Thomas},
    title = {LeRobot: State-of-the-art Machine Learning for Real-World Robotics in Pytorch},
    howpublished = "\url{https://github.com/huggingface/lerobot}",
    year = {2024}
}
```

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=huggingface/lerobot&type=Timeline)](https://star-history.com/#huggingface/lerobot&Timeline)