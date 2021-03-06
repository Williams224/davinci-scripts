#-- GAUDI jobOptions generated on Mon Jul 27 18:45:41 2015
#-- Contains event types : 
#--   11104411 - 146 files - 3021344 events - 881.15 GBytes


#--  Extra information about the data processing phases:


#--  Processing Pass Step-124834 

#--  StepId : 124834 
#--  StepName : Reco14a for MC 
#--  ApplicationName : Brunel 
#--  ApplicationVersion : v43r2p7 
#--  OptionFiles : $APPCONFIGOPTS/Brunel/DataType-2012.py;$APPCONFIGOPTS/Brunel/MC-WithTruth.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r164 
#--  Visible : Y 


#--  Processing Pass Step-125836 

#--  StepId : 125836 
#--  StepName : Stripping20-NoPrescalingFlagged for Sim08 - Implicit merging. 
#--  ApplicationName : DaVinci 
#--  ApplicationVersion : v32r2p1 
#--  OptionFiles : $APPCONFIGOPTS/DaVinci/DV-Stripping20-Stripping-MC-NoPrescaling.py;$APPCONFIGOPTS/DaVinci/DataType-2012.py;$APPCONFIGOPTS/DaVinci/InputType-DST.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r164 
#--  Visible : Y 

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(['LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000001_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000002_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000003_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000004_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000005_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000006_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000007_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000008_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000009_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000010_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000011_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000012_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000013_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000014_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000015_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000016_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000017_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000018_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000019_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000020_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000021_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000022_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000023_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000024_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000025_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000026_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000027_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000028_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000029_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000030_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000031_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000032_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000033_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000034_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000035_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000036_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000037_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000038_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000039_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000040_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000041_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000042_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000043_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000044_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000045_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000046_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000047_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000048_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000049_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000050_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000051_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000052_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000053_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000054_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000055_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000056_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000057_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000058_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000059_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000060_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000061_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000062_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000063_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000064_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000065_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000066_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000067_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000068_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000069_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000070_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000071_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000072_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000073_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000074_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000075_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000076_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000077_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000078_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000079_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000080_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000081_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000082_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000083_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000084_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000085_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000086_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000087_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000088_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000089_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000090_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000091_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000092_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000094_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000096_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000097_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000098_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000099_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000100_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000101_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000102_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000103_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000104_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000105_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000106_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000107_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000108_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000109_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000110_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000111_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000112_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000113_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000114_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000115_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000116_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000118_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000119_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000120_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000121_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000122_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000123_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000124_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000125_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000126_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000127_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000128_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000129_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000130_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000131_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000132_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000133_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000134_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000135_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000136_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000137_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000138_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000139_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000140_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000141_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000142_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000143_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000144_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000145_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000146_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000147_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000149_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00038849/0000/00038849_00000150_2.AllStreams.dst'
], clear=True)
