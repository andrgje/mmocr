dataset_type1 = 'IcdarDataset'
data_root1 = 'data/icdar15'

train1 = dict(
    type=dataset_type1,
    ann_file=f'{data_root1}/instances_training.json',
    img_prefix=f'{data_root1}/imgs',
    pipeline=None)

test1 = dict(
    type=dataset_type1,
    ann_file=f'{data_root1}/instances_validation.json',
    img_prefix=f'{data_root1}/imgs',
    pipeline=None)

dataset_type2 = 'IcdarDataset'
data_root2 = 'data/icdar13'

train2 = dict(
    type=dataset_type2,
    ann_file=f'{data_root2}/instances_training.json',
    img_prefix=f'{data_root2}/imgs',
    pipeline=None)

test2 = dict(
    type=dataset_type2,
    ann_file=f'{data_root2}/instances_validation.json',
    img_prefix=f'{data_root2}/imgs',
    pipeline=None)

train_list = [train1,train2]

test_list = [test1,test2]
