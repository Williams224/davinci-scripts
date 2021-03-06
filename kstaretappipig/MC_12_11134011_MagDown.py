#-- GAUDI jobOptions generated on Mon Jul 20 10:20:06 2015
#-- Contains event types : 
#--   11134011 - 46 files - 987788 events - 276.67 GBytes


#--  Extra information about the data processing phases:


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


#--  Processing Pass Step-127969 

#--  StepId : 127969 
#--  StepName : Reco14c for MC - 2012 
#--  ApplicationName : Brunel 
#--  ApplicationVersion : v43r2p11 
#--  OptionFiles : $APPCONFIGOPTS/Brunel/DataType-2012.py;$APPCONFIGOPTS/Brunel/MC-WithTruth.py;$APPCONFIGOPTS/Persistency/DST-multipleTCK-2012.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r218 
#--  Visible : Y 

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(['LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000001_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000002_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000003_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000004_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000005_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000006_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000007_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000008_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000009_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000010_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000011_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000012_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000013_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000014_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000015_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000016_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000017_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000018_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000019_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000020_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000021_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000022_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000023_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000024_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000025_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000026_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000027_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000028_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000029_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000030_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000031_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000032_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000033_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000034_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000035_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000036_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000037_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000038_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000039_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000040_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000041_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000042_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000043_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000044_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000045_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00046299/0000/00046299_00000046_2.AllStreams.dst'
], clear=True)
