#!/usr/bin/env bash

#  --model_name_or_path ./T5-base/t5-base \
#  acos/acos_hide_classification/apparent
#  acos/acos_implicit_classification/explicit
#             # --do_train \
    
python main.py --task uabsa \
            --dataset rest15 \
            --paradigm annotation \
            --n_gpu 0 \
            --do_direct_eval \
            --train_batch_size 16 \
            --gradient_accumulation_steps 2 \
            --eval_batch_size 16 \
            --learning_rate 3e-4 \
            --num_train_epochs 20 