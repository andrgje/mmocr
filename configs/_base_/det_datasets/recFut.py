dataset_type = 'IcdarDataset'
data_root = 'data/recFut'

test = dict(
    type=dataset_type,
    ann_file=f'{data_root}/instances_test.json',
    img_prefix=f'{data_root}/imgs',
    pipeline=None)

test_list = [test]
