_base_ = [
    '../../_base_/runtime_10e.py',
    '../../_base_/schedules/schedule_sgd_1200e.py',
    '../../_base_/det_models/dbnet_r50dcnv2_fpnc.py',
    '../../_base_/det_datasets/recFut.py',
    '../../_base_/det_pipelines/dbnet_pipeline.py'
]

test_list = {{_base_.test_list}}

test_pipeline_4068_1024 = {{_base_.test_pipeline_4068_1024}}

load_from = '../../backbone/dbnet/dbnet_r50dcnv2_fpnc_sbn_2e_synthtext_20210325-aa96e477.pth'

data = dict(
    samples_per_gpu=1,
    workers_per_gpu=1,
    val_dataloader=dict(samples_per_gpu=1),
    test_dataloader=dict(samples_per_gpu=1),
    train=dict(
        type='UniformConcatDataset',
        datasets=test_list,
        pipeline=test_pipeline_4068_1024),
    val=dict(
        type='UniformConcatDataset',
        datasets=test_list,
        pipeline=test_pipeline_4068_1024),
    test=dict(
        type='UniformConcatDataset',
        datasets=test_list,
        pipeline=test_pipeline_4068_1024))

evaluation = dict(interval=100, metric='hmean-iou')
    