from Gaudi.Configuration import *
from Configurables import DaVinci
from Configurables import GaudiSequencer

simulation=False

stream='Bhadron'
line='B2XEtaLb2pKetapLine'

from Configurables import DecayTreeTuple
from DecayTreeTuple.Configuration import *
tuple=DecayTreeTuple()
tuple.Decay="[Lambda_b0 -> ^p+ ^K- ^(eta_prime -> ^pi- ^pi+ ^gamma)]CC"
tuple.Branches={"Lambda_b0":"[Lambda_b0 -> p+ K- (eta_prime -> pi- pi+ gamma)]CC"}
tuple.Inputs=['Phys/{0}/Particles'.format(line)]

tuple.ToolList += [
    "TupleToolGeometry"
    , "TupleToolDira"
    , "TupleToolAngles"
    , "TupleToolPid"
    , "TupleToolKinematic"
    , "TupleToolPropertime"
    , "TupleToolPrimaries"
    , "TupleToolEventInfo"
    , "TupleToolTrackInfo"
    , "TupleToolVtxIsoln"
    , "TupleToolPhotonInfo"
    #, "TupleToolMCTruth"
    #, "TupleToolMCBackgroundInfo"
    , "TupleToolCaloHypo"
    , "TupleToolRecoStats"
    #, "TupleToolTrackIsolation"
    ]

tuple.addTool(TupleToolDecay,name="Lambda_b0")

from Configurables import TupleToolDecayTreeFitter

#==============================REFIT WITH ALL CONSTRAINED======================================
tuple.Lambda_b0.addTupleTool('TupleToolDecayTreeFitter/DTFAll')
tuple.Lambda_b0.DTFAll.Verbose=True
tuple.Lambda_b0.DTFAll.constrainToOriginVertex=True
tuple.Lambda_b0.DTFAll.daughtersToConstrain = ["eta_prime"]
#==============================REFIT WITH ONLY  PV CONTRAINED==============================
tuple.Lambda_b0.addTupleTool('TupleToolDecayTreeFitter/DTFPVOnly')
tuple.Lambda_b0.DTFPVOnly.Verbose=True
tuple.Lambda_b0.DTFPVOnly.constrainToOriginVertex=True
#========================================REFIT WITH JUST DAUGHTERS CONSTRAINED================================
tuple.Lambda_b0.addTupleTool('TupleToolDecayTreeFitter/DTFPVNo')
tuple.Lambda_b0.DTFPVNo.Verbose=True
tuple.Lambda_b0.DTFPVNo.constrainToOriginVertex=False
tuple.Lambda_b0.DTFPVNo.daughtersToConstrain = ["eta_prime"]
#==============================REFIT WITH K SWAPPED FOR PI ALL CONSTRAINED ==============================
tuple.Lambda_b0.addTupleTool('TupleToolDecayTreeFitter/DTFKforpi')
tuple.Lambda_b0.DTFKforpi.Verbose=True
tuple.Lambda_b0.DTFKforpi.constrainToOriginVertex=True
tuple.Lambda_b0.DTFKforpi.daughtersToConstrain = ["eta_prime"]
tuple.Lambda_b0.DTFKforpi.Substitutions={
    "Lambda_b0 -> p+ ^K- (eta_prime -> pi- pi+ gamma)" : "pi-",
    "Lambda_b~0 -> p~- ^K+ (eta_prime -> pi- pi+ gamma)" : "pi+",
    }

#==============================REFIT WITH P SWAPPED FOR PI ALL CONSTRAINED ==============================
tuple.Lambda_b0.addTupleTool('TupleToolDecayTreeFitter/DTFPforpi')
tuple.Lambda_b0.DTFPforpi.Verbose=True
tuple.Lambda_b0.DTFPforpi.constrainToOriginVertex=True
tuple.Lambda_b0.DTFPforpi.daughtersToConstrain = ["eta_prime"]
tuple.Lambda_b0.DTFPforpi.Substitutions={
    "Lambda_b0 -> ^p+ K- (eta_prime -> pi- pi+ gamma)" : "pi+",
    "Lambda_b~0 -> ^p~- K+ (eta_prime -> pi- pi+ gamma)" : "pi-",
    }

#==============================REFIT WITH P SWAPPED FOR K ALL CONSTRAINED ==============================
tuple.Lambda_b0.addTupleTool('TupleToolDecayTreeFitter/DTFPforK')
tuple.Lambda_b0.DTFPforK.Verbose=True
tuple.Lambda_b0.DTFPforK.constrainToOriginVertex=True
tuple.Lambda_b0.DTFPforK.daughtersToConstrain = ["eta_prime"]
tuple.Lambda_b0.DTFPforK.Substitutions={
    "Lambda_b0 -> ^p+ K- (eta_prime -> pi- pi+ gamma)" : "K+",
    "Lambda_b~0 -> ^p~- K+ (eta_prime -> pi- pi+ gamma)" : "K-",
    }

########################################=LOKI FUNCOR VARIABLES===============================================

tuple.addBranches({'Proton':'[Lambda_b0 -> ^p+ K- (eta_prime -> pi- pi+ gamma)]CC',
                   'Kaon' : '[Lambda_b0 -> p+ ^K- (eta_prime -> pi- pi+ gamma)]CC',
                   'eta_prime' : '[Lambda_b0 -> p+ K- ^(eta_prime -> pi- pi+ gamma)]CC',
                   'piminus' : '[Lambda_b0 -> p+ K- (eta_prime -> ^pi- pi+ gamma)]CC',
                   'piplus' : '[Lambda_b0 -> p+ K- (eta_prime -> pi- ^pi+ gamma)]CC',
                   'gamma' : '[Lambda_b0 -> p+ K- (eta_prime -> pi- pi+ ^gamma)]CC',
                   })

from LoKiPhys.decorators import MAXTREE,MINTREE,ISBASIC,HASTRACK,SUMTREE,PT,ABSID,NINTREE,ETA,TRPCHI2
Lb_hybrid=tuple.Lambda_b0.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_Lambda_b0')
Proton_hybrid=tuple.Proton.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_Proton')
Kaon_hybrid=tuple.Kaon.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_Kaon')
eta_prime_hybrid=tuple.eta_prime.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_eta_prime')
piminus_hybrid=tuple.piminus.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_piminus')
piplus_hybrid=tuple.piplus.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_piplus')
gamma_hybrid=tuple.gamma.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_gamma')

preamble=[
    'TRACK_MAX_PT= MAXTREE(PT, ISBASIC & HASTRACK, -666)',
    'TRACK_MIN_PT= MINTREE(PT, ISBASIC & HASTRACK)',
    'SUMTRACK_PT= SUMTREE((211 == ABSID)|(-211 == ABSID)|(321 == ABSID)|(-321 == ABSID)|(2212 == ABSID)|(-2212 == ABSID),PT)',
    'SUM_PCHI2= SUMTREE((211 == ABSID)|(-211 == ABSID)|(321 == ABSID)|(-321 == ABSID)|(2212 == ABSID)|(-2212 == ABSID),TRPCHI2)'
    ]
Lb_hybrid.Preambulo=preamble

Lb_hybrid.Variables = {
    'max_pt_track' : 'TRACK_MAX_PT',
    'min_pt_track' : 'TRACK_MIN_PT',
    'sum_track_pt' : 'SUMTRACK_PT',
    'sum_pchi2' : 'SUM_PCHI2',
    'n_highpt_tracks' : 'NINTREE(ISBASIC & HASTRACK & (PT>250.0*MeV))',
    'ETA':'ETA'
    }

Proton_hybrid.Variables ={
    'branch_mass':'MM',
    'ETA': 'ETA'
 }

Kaon_hybrid.Variables ={
    'branch_mass':'MM',
    'ETA': 'ETA'
    }

eta_prime_hybrid.Variables ={
    'ETA': 'ETA'
    }

piminus_hybrid.Variables ={
    'ETA': 'ETA'
    }

piplus_hybrid.Variables ={
    'ETA': 'ETA'
    }

gamma_hybrid.Variables = {
    'ETA':'ETA'
    }

#==============================MassSubs=====================================
from Configurables import TupleToolSubMass

tuple.Lambda_b0.addTool(TupleToolSubMass)
tuple.Lambda_b0.ToolList += ["TupleToolSubMass"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["p+ => K+"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["p+ => pi+"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["K- => pi-"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["K- => p~-"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["pi+ => p+"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["pi+ => K+"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["pi- => p~-"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["pi- => K-"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["gamma => e-"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["gamma => e+"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["pi+ => mu+"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["pi- => mu-"]
tuple.Lambda_b0.TupleToolSubMass.DoubleSubstitution += ["K+/pi- => pi+/K-"]
tuple.Lambda_b0.TupleToolSubMass.DoubleSubstitution += ["pi+/pi- => pi-/pi+"]
tuple.Lambda_b0.TupleToolSubMass.DoubleSubstitution += ["pi+/pi- => mu+/mu-"]


#==============================TRIGGER DECISIONS==============================


from Configurables import TupleToolTISTOS
tistos = tuple.Lambda_b0.addTupleTool(TupleToolTISTOS, name="TupleToolTISTOS")
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

from Configurables import TupleToolL0Calo

tuple.Kaon.addTool(TupleToolL0Calo,name="KaonL0Calo")
tuple.Kaon.ToolList += ["TupleToolL0Calo/KaonL0Calo"]
tuple.Kaon.KaonL0Calo.WhichCalo="HCAL"

tuple.piplus.addTool(TupleToolL0Calo,name="piplusL0Calo")
tuple.piplus.ToolList += ["TupleToolL0Calo/piplusL0Calo"]
tuple.piplus.piplusL0Calo.WhichCalo="HCAL"

tuple.piminus.addTool(TupleToolL0Calo,name="piminusL0Calo")
tuple.piminus.ToolList += ["TupleToolL0Calo/piminusL0Calo"]
tuple.piminus.piminusL0Calo.WhichCalo="HCAL"

tuple.Proton.addTool(TupleToolL0Calo,name="ProtonL0Calo")
tuple.Proton.ToolList += ["TupleToolL0Calo/ProtonL0Calo"]
tuple.Proton.ProtonL0Calo.WhichCalo="HCAL"


DaVinci().InputType='MDST'
DaVinci().RootInTES='/Event/{0}'.format(stream)
DaVinci().UserAlgorithms+=[tuple]
DaVinci().TupleFile="Output.root"
DaVinci().HistogramFile="histos.root"
DaVinci().DataType='2011'
DaVinci().EvtMax=-1
DaVinci().Lumi=True
DaVinci().PrintFreq=1000
DaVinci().MoniSequence=[tuple]
DaVinci().Simulation=False


#from GaudiConf import IOHelper

# Use the local input data
#IOHelper().inputFiles([
 #   '00041836_00000481_1.bhadron.mdst'
  #  ], clear=True)





