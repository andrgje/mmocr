dataset_type= 'IcdarDataset'
data_root = 'data/totaltext/'

train = dict(
    type = dataset_type,
    ann_file=f'{data_root}/instances_training.json',
    img_prefix=f'{data_root}/imgs',
    pipeline=None)

validation = dict(
    type = dataset_type,
    ann_file = f'{data_root}/instances_validation',
    img_prefix = f'{data_root}/imgs',
    pipeline = None)

test = dict(
    type=dataset_type,
    ann_file=f'{data_root}/instances_test.json',
    img_prefix=f'{data_root}/imgs',
    pipeline=None)

train_list = [train]
validation_list = [validation]
test_list = [test]