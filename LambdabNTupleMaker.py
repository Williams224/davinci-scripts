from Gaudi.Configuration import *
from Configurables import DaVinci
#from Configurables import AlgTool
from Configurables import GaudiSequencer
MySequencer = GaudiSequencer('Sequence')

DaVinci.DDDBtag='dddb-20120831'
DaVinci.CondDBtag='sim-20121025-vc-md100'

simulation=True

#only for mdst
#from Configurables import EventNodeKiller
#eventNodeKiller = EventNodeKiller('DAQkiller')
#eventNodeKiller.Nodes = ['DAQ','pRec']
#MySequencer.Members+=[eventNodeKiller]   


#################################################################
#Rerun with stripping21 applied

if simulation:
    from StrippingConf.Configuration import StrippingConf, StrippingStream
    from StrippingSettings.Utils import strippingConfiguration
    from StrippingArchive.Utils import buildStreams
    from StrippingArchive import strippingArchive

    from Configurables import PhysConf
    PhysConf().CaloReProcessing=True

    stripping="stripping21"
    config=strippingConfiguration(stripping)
    archive=strippingArchive(stripping)
    streams=buildStreams(stripping=config,archive=archive)

    MyStream= StrippingStream("MyStream")
    MyLines= ["StrippingB2XEtaLb2pKetapLine"]

    for stream in streams:
        for line in stream.lines:
            if line.name() in MyLines:
                MyStream.appendLines( [ line ])

    from Configurables import ProcStatusCheck
    filterBadEvents=ProcStatusCheck()

    sc=StrippingConf( Streams= [ MyStream ],
                      MaxCandidates = 2000,
                      AcceptBadEvents = False,
                      BadEventSelection = filterBadEvents)

    DaVinci().appendToMainSequence([sc.sequence()])
    

            
##################Creating NTuples#####################################
from Configurables import DecayTreeTuple
from Configurables import TupleToolL0Calo
from DecayTreeTuple.Configuration import *
tuple=DecayTreeTuple()
tuple.Decay="[Lambda_b0 -> ^p+ ^K- ^(eta_prime -> ^pi- ^pi+ ^gamma)]CC"
tuple.Branches={"Lambda_b0":"[Lambda_b0 -> p+ K- (eta_prime -> pi- pi+ gamma)]CC"}
tuple.Inputs=["Phys/B2XEtaLb2pKetapLine/Particles"]
tuple.addTool(TupleToolL0Calo())
tuple.TupleToolL0Calo.TriggerClusterLocation="/Event/Trig/L0/Calo"
tuple.TupleToolL0Calo.WhichCalo="HCAL"


tuple.ToolList += [
    "TupleToolGeometry"
    , "TupleToolDira"
    , "TupleToolAngles"
   # , "TupleToolL0Calo"
    , "TupleToolPid"
    , "TupleToolKinematic"
    , "TupleToolPropertime"
    , "TupleToolPrimaries"
    , "TupleToolEventInfo"
    , "TupleToolTrackInfo"
    , "TupleToolVtxIsoln"
    , "TupleToolPhotonInfo"
    , "TupleToolMCTruth"
    , "TupleToolMCBackgroundInfo"
   # , "MCTupleTOolHierachy"
    , "TupleToolCaloHypo"
    , "TupleToolTrackIsolation"
    #, "TupleToolTagging" not used in microdst
    ]

#from Configurables import TupleToolMCTruth
#from TupleToolMCTruth.Configuration import *

#tuple.addTool(TupleToolMCTruth,name="TruthM")
#tuple.ToolList+= [ "TupleToolMCTruth/TruthM"]
#tuple.TruthM.ToolList = ["MCTupleToolHierachy/Hierachy"]
#tuple.TruthM.addTool(MCTupleToolHierachy,name="Hierachy")
#tuple.TupleToolMCTruth.addTool(MCTupleToolKinematic,name="MCTupleToolKinematic")
#tuple.TupleToolMCTruth.addTool(MCTupleToolHierachy,name="MCTupleToolHierachy")
#tuple.TupleToolMCTruth.addTool(MCTupleToolPID,name="MCTupleToolPID")


#####Look at adding branchesss##############
tuple.addTool(TupleToolDecay,name="Lambda_b0")

from Configurables import TupleToolDecayTreeFitter

tuple.Lambda_b0.addTool(TupleToolDecayTreeFitter("PVFit"))
tuple.Lambda_b0.PVFit.Verbose=True
tuple.Lambda_b0.PVFit.constrainToOriginVertex=True
tuple.Lambda_b0.PVFit.daughtersToConstrain = ["p+","K-","eta_prime"]
tuple.Lambda_b0.ToolList+=["TupleToolDecayTreeFitter/PVFit"]
                 

from Configurables import TupleToolTISTOS
tistos=tuple.Lambda_b0.addTupleTool(TupleToolTISTOS, name="TupleToolTISTOS")
tistos.VerboseL0=True
tistos.VerboseHlt1=True
tistos.VerboseHlt2=True
tistos.TriggerList=["L0PhotonDecision",
                    "L0ElectronDecision",
                    "Hlt1TrackPhotonDecision",
                    "Hlt1TrackAllL0Decision",
                    "Hlt1TrackMuonDecision",
                    "Hlt1TrackForwardPassThroughDecision",
                    "Hlt1TrackForwardPassThroughLooseDecision",
                    "Hlt1SingleElectronNoIPDecision",
                    "L0HadronDecision",
                    "L0LocalPi0Decision",
                    "L0GlobalPi0Decision",
                    "L0MuonDecision",
                    "Hlt2Topo2BodyBBDTDecision",
                    "Hlt2Topo3BodyBBDTDecision",
                    "Hlt2Topo4BodyBBDTDecision",
                    "Hlt2RadiativeTopoTrackTOSDecision",
                    "Hlt2RadiativeTopoPhotonL0Decision",
                    "Hlt2TopoRad2BodyBBDTDecision",
                    "Hlt2TopoRad2plus1BodyBBDTDecision",
                    "Hlt2Topo2BodySimpleDecision",
                    "Hlt2Topo3BodySimpleDecision",
                    "Hlt2Topo4BodySimpleDecision"]

etuple=EventTuple()
etuple.ToolList=["TupleToolEventInfo"]


from Configurables import MCDecayTreeTuple
mctuple=MCDecayTreeTuple("mctuple")
mctuple.ToolList+=["MCTupleToolKinematic","MCTupleToolReconstructed","MCTupleToolHierarchy","MCTupleToolDecayType","MCTupleToolPID"]

mctuple.Decay="[Lambda_b0 -> ^(p+) ^(K-) ^(eta_prime -> ^pi- ^pi+ ^gamma)]CC"

MySequencer.Members.append(etuple)
MySequencer.Members.append(tuple)
MySequencer.Members.append(mctuple)

DaVinci().InputType='DST'
DaVinci().UserAlgorithms+=[MySequencer]
DaVinci().TupleFile="Output.root"
DaVinci().HistogramFile="histos.root"
DaVinci().DataType='2012'
DaVinci().EvtMax=-1
DaVinci().PrintFreq=1000
DaVinci().MoniSequence=[tuple]
DaVinci().Simulation=simulation







