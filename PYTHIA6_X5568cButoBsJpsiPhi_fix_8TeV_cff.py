import FWCore.ParameterSet.Config as cms
from Configuration.Generator.PythiaUEZ2starSettings_cfi import *


generator = cms.EDFilter("Pythia6GeneratorFilter",
       ExternalDecays = cms.PSet(
       EvtGen = cms.untracked.PSet(
          use_default_decay = cms.untracked.bool(False),
          decay_table = cms.FileInPath('GeneratorInterface/ExternalDecays/data/DECAY_NOLONGLIFE_X5568mod.DEC'),
          particle_property_file =cms.FileInPath('GeneratorInterface/ExternalDecays/data/evtX5568cBumod2.pdl'),
          user_decay_file =cms.FileInPath('GeneratorInterface/ExternalDecays/data/X5568cBu_Bspi_Jpsiphi.dec'),
          list_forced_decays = cms.vstring('myX5568+','myX5568-'),
            operates_on_particles = cms.vint32(0)
       ),
       parameterSets = cms.vstring('EvtGen')
    ),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(8000.0),
    crossSection = cms.untracked.double(2909834.),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
    pythiaUESettingsBlock,
        bbbarSettings = cms.vstring('MSEL = 1'),
        parameterSets = cms.vstring('pythiaUESettings','bbbarSettings')
    )
)

bfilter = cms.EDFilter("PythiaFilter",
	MaxEta = cms.untracked.double(9999.),
	MinEta = cms.untracked.double(-9999.),
	MinPt = cms.untracked.double(6.5),
	MotherID = cms.untracked.int32(521),
	ParticleID = cms.untracked.int32(531)
	)

Xfilter = cms.EDFilter( "PythiaFilter",
	MaxEta = cms.untracked.double(9999.),
	MinEta = cms.untracked.double(-9999.),
	ParticleID = cms.untracked.int32(521)
	)

jpsiDaufilter = cms.EDFilter( "PythiaDauVFilter",
	verbose = cms.untracked.int32(0),
	NumberDaughters = cms.untracked.int32(2),
	MotherID = cms.untracked.int32(531),
	ParticleID = cms.untracked.int32(443),
	DaughterIDs = cms.untracked.vint32(13, -13),
	MinPt = cms.untracked.vdouble(3.5, 3.5),
	MinEta = cms.untracked.vdouble(-2.7, -2.7),
	MaxEta = cms.untracked.vdouble( 2.7,2.7)
	)

phiDaufilter = cms.EDFilter("PythiaDauVFilter",
	verbose = cms.untracked.int32(0),
	NumberDaughters = cms.untracked.int32(2),
	MotherID = cms.untracked.int32(531),
	ParticleID = cms.untracked.int32(333),
	DaughterIDs = cms.untracked.vint32(321,-321),
	MinPt = cms.untracked.vdouble(0.4,0.4),
	MinEta = cms.untracked.vdouble(-3.5,-3.5),
	MaxEta = cms.untracked.vdouble(3.5,3.5)
	)

bDaufilter = cms.EDFilter("PythiaDauVFilter",
	verbose = cms.untracked.int32(0),
	NumberDaughters = cms.untracked.int32(2),
	MotherID = cms.untracked.int32(521),
	ParticleID = cms.untracked.int32(531),
	DaughterIDs = cms.untracked.vint32(443, 333),
	MinPt = cms.untracked.vdouble(6.3, 0.5),
	MinEta = cms.untracked.vdouble(-9999., -9999.),
	MaxEta = cms.untracked.vdouble(9999., 9999.)
	)

pifilter = cms.EDFilter( "PythiaFilter",
	MaxEta = cms.untracked.double(3.5),
	MinEta = cms.untracked.double(-3.5),
	MinPt = cms.untracked.double(0.3),
	MotherID = cms.untracked.int32(521),
	ParticleID = cms.untracked.int32(211)
	)	

ProductionFilterSequence = cms.Sequence(generator*Xfilter*bfilter*pifilter*bDaufilter*jpsiDaufilter*phiDaufilter)
