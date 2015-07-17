#-- GAUDI jobOptions generated on Mon Jul  6 15:32:07 2015
#-- Contains event types : 
#--   11104125 - 43 files - 501996 events - 151.82 GBytes


#--  Extra information about the data processing phases:


#--  Processing Pass Step-123901 

#--  StepId : 123901 
#--  StepName : Stripping20-NoPrescalingFlagged for MC MagUp 
#--  ApplicationName : DaVinci 
#--  ApplicationVersion : v32r2p1 
#--  OptionFiles : $APPCONFIGOPTS/DaVinci/DV-Stripping20-Stripping-MC-NoPrescaling.py;$APPCONFIGOPTS/DaVinci/DataType-2012.py;$APPCONFIGOPTS/DaVinci/InputType-DST.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : dddb-20120831 
#--  CONDDB : sim-20121025-vc-mu100 
#--  ExtraPackages : AppConfig.v3r155 
#--  Visible : Y 


#--  Processing Pass Step-124440 

#--  StepId : 124440 
#--  StepName : Sim06b with Nu=2.5 - MU - MayJune 2012 
#--  ApplicationName : Gauss 
#--  ApplicationVersion : v42r4 
#--  OptionFiles : $APPCONFIGOPTS/Gauss/Beam4000GeV-mu100-MayJun2012-nu2.5.py;$DECFILESROOT/options/@{eventType}.py;$LBPYTHIAROOT/options/Pythia.py;$APPCONFIGOPTS/Gauss/G4PL_LHEP_EmNoCuts.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : dddb-20120831 
#--  CONDDB : sim-20121025-vc-mu100 
#--  ExtraPackages : AppConfig.v3r160;DecFiles.v26r24 
#--  Visible : Y 


#--  Processing Pass Step-124055 

#--  StepId : 124055 
#--  StepName : Digi12 w/o spillover - MU - L0TCK 0x003D 
#--  ApplicationName : Boole 
#--  ApplicationVersion : v24r0 
#--  OptionFiles : $APPCONFIGOPTS/Boole/Default.py;$APPCONFIGOPTS/Boole/DataType-2012.py;$APPCONFIGOPTS/L0/L0TCK-0x003D.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : dddb-20120831 
#--  CONDDB : sim-20121025-vc-mu100 
#--  ExtraPackages : AppConfig.v3r155 
#--  Visible : N 


#--  Processing Pass Step-123755 

#--  StepId : 123755 
#--  StepName : Reco14 for MC - MagUp 
#--  ApplicationName : Brunel 
#--  ApplicationVersion : v43r2p2 
#--  OptionFiles : $APPCONFIGOPTS/Brunel/DataType-2012.py;$APPCONFIGOPTS/Brunel/MC-WithTruth.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : dddb-20120831 
#--  CONDDB : sim-20121025-vc-mu100 
#--  ExtraPackages : AppConfig.v3r151 
#--  Visible : Y 


#--  Processing Pass Step-124019 

#--  StepId : 124019 
#--  StepName : Trigger - TCK 0x4097003d Flagged - MU - MayJune 2012 
#--  ApplicationName : Moore 
#--  ApplicationVersion : v14r2p1 
#--  OptionFiles : $APPCONFIGOPTS/Moore/MooreSimProduction.py;$APPCONFIGOPTS/Conditions/TCK-0x4097003d.py;$APPCONFIGOPTS/Moore/DataType-2012.py;$APPCONFIGOPTS/L0/L0TCK-0x003D.py 
#--  DDDB : dddb-20120831 
#--  CONDDB : sim-20121025-vc-mu100 
#--  ExtraPackages : AppConfig.v3r155 
#--  Visible : Y 

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(['LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000001_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000002_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000003_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000004_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000005_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000006_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000007_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000008_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000009_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000010_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000011_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000012_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000013_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000014_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000015_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000016_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000017_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000018_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000019_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000020_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000021_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000022_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000023_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000024_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000025_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000026_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000027_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000028_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000029_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000030_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000031_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000032_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000033_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000034_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000035_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000036_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000037_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000038_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000039_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000040_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000041_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000042_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00023160/0000/00023160_00000044_1.allstreams.dst'
], clear=True)
