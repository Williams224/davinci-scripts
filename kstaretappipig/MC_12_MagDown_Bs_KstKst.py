#-- GAUDI jobOptions generated on Mon Jul 13 10:04:51 2015
#-- Contains event types : 
#--   13104001 - 60 files - 1033339 events - 210.28 GBytes


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


#--  Processing Pass Step-124620 

#--  StepId : 124620 
#--  StepName : Digi13 with G4 dE/dx 
#--  ApplicationName : Boole 
#--  ApplicationVersion : v26r3 
#--  OptionFiles : $APPCONFIGOPTS/Boole/Default.py;$APPCONFIGOPTS/Boole/DataType-2012.py;$APPCONFIGOPTS/Boole/Boole-SiG4EnergyDeposit.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r164 
#--  Visible : Y 


#--  Processing Pass Step-124632 

#--  StepId : 124632 
#--  StepName : TCK-0x409f0045 Flagged for Sim08 2012 
#--  ApplicationName : Moore 
#--  ApplicationVersion : v14r8p1 
#--  OptionFiles : $APPCONFIGOPTS/Moore/MooreSimProductionWithL0Emulation.py;$APPCONFIGOPTS/Conditions/TCK-0x409f0045.py;$APPCONFIGOPTS/Moore/DataType-2012.py;$APPCONFIGOPTS/L0/L0TCK-0x0045.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r164 
#--  Visible : Y 


#--  Processing Pass Step-126217 

#--  StepId : 126217 
#--  StepName : Sim08e - 2012 - MD - Pythia8 
#--  ApplicationName : Gauss 
#--  ApplicationVersion : v45r7 
#--  OptionFiles : $APPCONFIGOPTS/Gauss/Sim08-Beam4000GeV-md100-2012-nu2.5.py;$DECFILESROOT/options/@{eventType}.py;$LBPYTHIA8ROOT/options/Pythia8.py;$APPCONFIGOPTS/Gauss/G4PL_FTFP_BERT_EmNoCuts.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : dddb-20130929-1 
#--  CONDDB : sim-20130522-1-vc-md100 
#--  ExtraPackages : AppConfig.v3r182;DecFiles.v27r19 
#--  Visible : Y 


#--  Processing Pass Step-124630 

#--  StepId : 124630 
#--  StepName : Stripping20-NoPrescalingFlagged for Sim08 
#--  ApplicationName : DaVinci 
#--  ApplicationVersion : v32r2p1 
#--  OptionFiles : $APPCONFIGOPTS/DaVinci/DV-Stripping20-Stripping-MC-NoPrescaling.py;$APPCONFIGOPTS/DaVinci/DataType-2012.py;$APPCONFIGOPTS/DaVinci/InputType-DST.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r164 
#--  Visible : Y 

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(['LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000001_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000002_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000003_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000004_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000005_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000006_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000007_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000008_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000009_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000010_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000011_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000012_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000013_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000014_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000015_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000016_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000017_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000018_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000019_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000020_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000021_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000022_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000023_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000024_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000025_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000026_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000027_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000028_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000029_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000030_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000031_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000032_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000033_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000034_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000035_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000036_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000037_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000038_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000039_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000040_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000041_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000042_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000043_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000044_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000045_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000046_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000047_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000048_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000049_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000050_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000051_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000052_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000053_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000054_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000055_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000056_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000057_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000058_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000059_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034856/0000/00034856_00000060_1.allstreams.dst'
], clear=True)
