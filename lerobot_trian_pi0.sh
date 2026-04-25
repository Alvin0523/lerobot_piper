cd /home/orin/vlash_piper/lerobot_piper

# Prefer the pixi environment's C++ runtime so binary wheels like pyarrow
# don't accidentally bind against the older system libstdc++ on Jetson.
export LD_LIBRARY_PATH=/home/orin/vlash_piper/.pixi/envs/default/lib:${LD_LIBRARY_PATH:-}

python -m lerobot.scripts.train \
  --policy.path=lerobot/pi0 \
  --policy.device=cuda \
  --policy.push_to_hub=false \
  --dataset.repo_id=comp4901/test3 \
  --dataset.root=/home/orin/comp4901/test3 \
  --dataset.video_backend=pyav \
  --dataset.use_imagenet_stats=false \
  --output_dir=outputs/train/pi0_piper_test3 \
  --job_name=pi0_piper_test3 \
  --batch_size=8 \
  --steps=20000 \
  --num_workers=0 \
  --seed=1000 \
  --use_policy_training_preset=false \
  --optimizer.type=adamw \
  --optimizer.lr=5.0e-5 \
  --optimizer.betas=[0.9,0.95] \
  --optimizer.weight_decay=1.0e-10 \
  --scheduler.type=cosine_decay_with_warmup \
  --scheduler.num_warmup_steps=1000 \
  --scheduler.peak_lr=5.0e-5 \
  --scheduler.decay_lr=2.5e-6 \
  --scheduler.num_decay_steps=30000 \
  --save_checkpoint=true \
  --save_freq=5000 \
  --log_freq=100 \
  --wandb.enable=false