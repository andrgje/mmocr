from mmocr.utils.ocr import MMOCR


ocr=MMOCR(det_config='/home/andreas/Documents/Master/mmocr/configs/textdet/dbnet/dbnet_r50dcnv2_fpnc_1200e_icdar2015.py', det_ckpt='/home/andreas/Documents/Master/mmocr/checkpoints/textdet/dbnet/dbnet_r50dcnv2_fpnc_sbn_1200e_icdar2015_20211025-9fe3b590.pth')

results = ocr.readtext('	test/test/',output='test/test_out/',export='test/test_out/')
