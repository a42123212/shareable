from osgeo import gdal
import numpy as np

# 開啟原始影像
ds = gdal.Open("output_byte_2.tif", gdal.GA_Update)
band = ds.GetRasterBand(1)

# 設定 NoData
band.SetNoDataValue(0)

# 建立顏色表
ct = gdal.ColorTable()
ct.SetColorEntry(0, (0, 0, 0, 0))     # 0 = transparent
ct.SetColorEntry(1, (255, 0, 0, 255)) # 1 = red

# 指定顏色表給 band
band.SetRasterColorTable(ct)
band.SetRasterColorInterpretation(gdal.GCI_PaletteIndex)

# 關閉
band = None
ds = None
