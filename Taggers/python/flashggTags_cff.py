import FWCore.ParameterSet.Config as cms
from flashgg.MicroAOD.flashggJets_cfi import flashggBTag, maxJetCollections

flashggUnpackedJets = cms.EDProducer("FlashggVectorVectorJetUnpacker",
                                     JetsTag = cms.InputTag("flashggFinalJets"),
                                     NCollections = cms.uint32(maxJetCollections)
                                     )

UnpackedJetCollectionVInputTag = cms.VInputTag()
for i in range(0,maxJetCollections):
    UnpackedJetCollectionVInputTag.append(cms.InputTag('flashggUnpackedJets',str(i)))

flashggUntagged = cms.EDProducer("FlashggUntaggedTagProducer",
#                                 DiPhotonTag=cms.InputTag('flashggDiPhotons'),
                                 DiPhotonTag=cms.InputTag('flashggPreselectedDiPhotons'),
                                 SystLabel=cms.string(""),
                                 MVAResultTag=cms.InputTag('flashggDiPhotonMVA'),
                                 GenParticleTag=cms.InputTag( "flashggPrunedGenParticles" ),
                                 Boundaries=cms.untracked.vdouble(-0.089,0.563,0.798,0.945) #,1.000)
)

flashggTTHHadronicTag = cms.EDProducer("FlashggTTHHadronicTagProducer",
                                       DiPhotonTag=cms.InputTag('flashggPreselectedDiPhotons'),
                                       SystLabel=cms.string(""),
                                       MVAResultTag=cms.InputTag('flashggDiPhotonMVA'),
                                       #JetTag=cms.InputTag('flashggSelectedJets'),
                                       inputTagJets= UnpackedJetCollectionVInputTag,
                                       bDiscriminatorLoose = cms.untracked.double(0.275),
                                       bDiscriminatorMedium = cms.untracked.double(0.545),
                                       jetsNumberThreshold = cms.untracked.int32(4),
                                       bjetsNumberThreshold = cms.untracked.int32(0),
                                       bTag = cms.untracked.string(flashggBTag),
                                       GenParticleTag=cms.InputTag( "flashggPrunedGenParticles" ),
)

flashggVBFTag = cms.EDProducer("FlashggVBFTagProducer",
                               DiPhotonTag=cms.InputTag('flashggPreselectedDiPhotons'),
                               SystLabel=cms.string(""),
                               MVAResultTag=cms.InputTag('flashggDiPhotonMVA'),
                               VBFDiPhoDiJetMVAResultTag=cms.InputTag('flashggVBFDiPhoDiJetMVA'),
                               VBFMVAResultTag=cms.InputTag('flashggVBFMVA'),
                               GenParticleTag=cms.InputTag( "flashggPrunedGenParticles" ),
                               GenJetTag = cms.InputTag("slimmedGenJets"),
                               # Boundaries=cms.untracked.vdouble(0.21,0.6,0.81)
                               # for the moment we have two categories VBF-0 and VBF-1: to be changed when the diphoton MVA is ready 
                               # Boundaries=cms.untracked.vdouble(0.26,0.79) 
                               # new boudaries using the prety new combined VBF-MVA (new dipho/dijet MVA's)
                               Boundaries=cms.untracked.vdouble(0.64,0.92) 
                               )


flashggVHEtTag = cms.EDProducer("FlashggVHEtTagProducer",
                                DiPhotonTag=cms.InputTag('flashggPreselectedDiPhotons'),
                                SystLabel=cms.string(""),
                                GenParticleTag=cms.InputTag( "flashggPrunedGenParticles" ),
                                MVAResultTag=cms.InputTag('flashggDiPhotonMVA'),
                                METTag=cms.InputTag('slimmedMETs'),
                                #metThreshold = cms.untracked.double(70),
                                #Boundaries=cms.untracked.vdouble(0.21,0.6,0.81)
)

flashggTTHLeptonicTag = cms.EDProducer("FlashggTTHLeptonicTagProducer",
                                       DiPhotonTag=cms.InputTag('flashggPreselectedDiPhotons'),
                                       SystLabel=cms.string(""),
                                       MVAResultTag=cms.InputTag('flashggDiPhotonMVA'),
                                       #JetTag=cms.InputTag('flashggSelectedJets'),
                                       inputTagJets= UnpackedJetCollectionVInputTag,
                                       ElectronTag=cms.InputTag('flashggSelectedElectrons'),
                                       MuonTag=cms.InputTag('flashggSelectedMuons'),
                                       VertexTag=cms.InputTag('offlineSlimmedPrimaryVertices'),
                                       GenParticleTag=cms.InputTag( "flashggPrunedGenParticles" ),
                                       leptonPtThreshold = cms.untracked.double(20),
                                       leptonEtaThreshold = cms.untracked.double(2.4),
                                       leadPhoOverMassThreshold = cms.untracked.double(0.5),
                                       subleadPhoOverMassThreshold = cms.untracked.double(0.25),
                                       MVAThreshold = cms.untracked.double(-0.6),
                                       deltaRLepPhoThreshold = cms.untracked.double(0.5),
                                       deltaRJetLepThreshold = cms.untracked.double(0.5),
                                       jetsNumberThreshold = cms.untracked.double(2.),
                                       bjetsNumberThreshold = cms.untracked.double(1.),
                                       jetPtThreshold = cms.untracked.double(30.),
                                       jetEtaThreshold= cms.untracked.double(2.4),
                                       deltaRJetLeadPhoThreshold = cms.untracked.double(0.5),
                                       deltaRJetSubLeadPhoThreshold = cms.untracked.double(0.5),
                                       bDiscriminator=cms.untracked.vdouble(0.275,0.545),
                                       bTag = cms.untracked.string(flashggBTag),
                                       muPFIsoSumRelThreshold = cms.untracked.double(0.2),
                                       deltaRMuonJetcountThreshold = cms.untracked.double(2.),
                                       PuIDCutoffThreshold = cms.untracked.double(0.8),
                                       PhoMVAThreshold = cms.untracked.double(-0.2),
                                       ElectronPtThreshold = cms.untracked.double(20.),
                                       DeltaRTrkElec = cms.untracked.double(1.),
                                       TransverseImpactParam = cms.untracked.double(0.2),
                                       LongitudinalImpactParam = cms.untracked.double(0.02),
                                       LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
                                       MidPtEtaPhoThreshold = cms.untracked.double(1.566),
                                       HighEtaPhoThreshold = cms.untracked.double(2.5),
                                       deltaRPhoElectronThreshold = cms.untracked.double(1.),
                                       Zmass_ = cms.untracked.double(91.9),
                                       deltaMassElectronZThreshold_ = cms.untracked.double(10.),
                                       EtaCuts=cms.untracked.vdouble(1.442,1.566,2.5),
                                       nonTrigMVAThreshold = cms.untracked.double(0.9),
                                       electronIsoThreshold = cms.untracked.double(0.15),
                                       electronNumOfHitsThreshold = cms.untracked.double(1)
)
flashggVHLooseTag = cms.EDProducer("FlashggVHLooseTagProducer",
                                   DiPhotonTag=cms.InputTag('flashggPreselectedDiPhotons'),
                                   SystLabel=cms.string(""),
                                   #JetTag=cms.InputTag('flashggSelectedJets'),
                                   inputTagJets= UnpackedJetCollectionVInputTag,
                                   ElectronTag=cms.InputTag('flashggSelectedElectrons'),
                                   MuonTag=cms.InputTag('flashggSelectedMuons'),
                                   VertexTag=cms.InputTag('offlineSlimmedPrimaryVertices'),
                                   MVAResultTag=cms.InputTag('flashggDiPhotonMVA'),
                                   METTag=cms.InputTag('slimmedMETs'),
                                   GenParticleTag=cms.InputTag( "flashggPrunedGenParticles" ),
                                   leptonPtThreshold = cms.untracked.double(20),
                                   leptonEtaThreshold = cms.untracked.double(2.4),
                                   leadPhoOverMassThreshold = cms.untracked.double(0.375),
                                   subleadPhoOverMassThreshold = cms.untracked.double(0.25),
                                   MVAThreshold = cms.untracked.double(-0.6),
                                   deltaRLepPhoThreshold = cms.untracked.double(1),
                                   jetsNumberThreshold = cms.untracked.double(3.),
                                   jetPtThreshold = cms.untracked.double(20.),
                                   jetEtaThreshold= cms.untracked.double(2.4),
                                   muPFIsoSumRelThreshold = cms.untracked.double(0.2),
                                   PuIDCutoffThreshold = cms.untracked.double(0.8),
                                   PhoMVAThreshold = cms.untracked.double(-0.2),
                                   METThreshold = cms.untracked.double(45.),
                                   LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
                                   MidPtEtaPhoThreshold = cms.untracked.double(1.566),
                                   HighEtaPhoThreshold = cms.untracked.double(2.5),
                                   ElectronPtThreshold = cms.untracked.double(20.),
                                   DeltaRTrkElec = cms.untracked.double(1.),
                                   TransverseImpactParam = cms.untracked.double(0.2),
                                   LongitudinalImpactParam = cms.untracked.double(0.02),
                                   deltaRPhoElectronThreshold = cms.untracked.double(1.),
                                   Zmass_ = cms.untracked.double(91.9),
                                   deltaMassElectronZThreshold_ = cms.untracked.double(10.),
                                   EtaCuts=cms.untracked.vdouble(1.442,1.566,2.5),
                                   nonTrigMVAThreshold = cms.untracked.double(0.9),
                                   electronIsoThreshold = cms.untracked.double(0.15),
                                   electronNumOfHitsThreshold = cms.untracked.double(1)

				    )
flashggVHTightTag = cms.EDProducer("FlashggVHTightTagProducer",
                                   DiPhotonTag=cms.InputTag('flashggPreselectedDiPhotons'),
                                   SystLabel=cms.string(""),
                                   #JetTag=cms.InputTag('flashggSelectedJets'),
                                   inputTagJets= UnpackedJetCollectionVInputTag,
                                   ElectronTag=cms.InputTag('flashggSelectedElectrons'),
                                   MuonTag=cms.InputTag('flashggSelectedMuons'),
                                   VertexTag=cms.InputTag('offlineSlimmedPrimaryVertices'),
                                   MVAResultTag=cms.InputTag('flashggDiPhotonMVA'),
                                   METTag=cms.InputTag('slimmedMETs'),
                                   GenParticleTag=cms.InputTag( "flashggPrunedGenParticles" ),
                                   leptonPtThreshold = cms.untracked.double(20),
                                   leptonEtaThreshold = cms.untracked.double(2.4),
                                   leadPhoOverMassThreshold = cms.untracked.double(0.375),
                                   subleadPhoOverMassThreshold = cms.untracked.double(0.25),
                                   MVAThreshold = cms.untracked.double(-0.6),
                                   deltaRLepPhoThreshold = cms.untracked.double(1),
                                   jetsNumberThreshold = cms.untracked.double(3.),
                                   jetPtThreshold = cms.untracked.double(20.),
                                   jetEtaThreshold= cms.untracked.double(2.4),
                                   muPFIsoSumRelThreshold = cms.untracked.double(0.2),
                                   PuIDCutoffThreshold = cms.untracked.double(0.8),
                                   PhoMVAThreshold = cms.untracked.double(-0.2),
                                   METThreshold = cms.untracked.double(45.),
                                   deltaRJetMuonThreshold = cms.untracked.double(0.5),
                                   invMassLepLowThreshold = cms.untracked.double(70.),
                                   invMassLepHighThreshold = cms.untracked.double(110.),
                                   numberOfLowPtMuonsThreshold = cms.untracked.double(2.),
                                   numberOfHighPtMuonsThreshold = cms.untracked.double(1.),
                                   leptonLowPtThreshold = cms.untracked.double(10.),
                                   deltaRLowPtMuonPhoThreshold = cms.untracked.double(0.5),
                                   deltaRPhoLeadJet = cms.untracked.double(0.5),
                                   deltaRPhoSubLeadJet = cms.untracked.double(0.5),
                                   LowPtEtaPhoThreshold = cms.untracked.double(1.4447),
                                   MidPtEtaPhoThreshold = cms.untracked.double(1.566),
                                   HighEtaPhoThreshold = cms.untracked.double(2.5),
                                   ElectronPtThreshold = cms.untracked.double(20.),
                                   DeltaRTrkElec = cms.untracked.double(1.),
                                   TransverseImpactParam = cms.untracked.double(0.2),
                                   LongitudinalImpactParam = cms.untracked.double(0.02),
                                   deltaRPhoElectronThreshold = cms.untracked.double(1.),
                                   Zmass_ = cms.untracked.double(91.9),
                                   deltaMassElectronZThreshold_ = cms.untracked.double(10.),
                                   EtaCuts=cms.untracked.vdouble(1.442,1.566,2.5),
                                   nonTrigMVAThreshold = cms.untracked.double(0.9),
                                   electronIsoThreshold = cms.untracked.double(0.15),
                                   electronNumOfHitsThreshold = cms.untracked.double(1)
)


flashggVHHadronicTag = cms.EDProducer("FlashggVHHadronicTagProducer",
                                      DiPhotonTag = cms.InputTag('flashggPreselectedDiPhotons'),
                                      SystLabel=cms.string(""),
                                      MVAResultTag=cms.InputTag('flashggDiPhotonMVA'),
                                      #JetTag = cms.InputTag('flashggSelectedJets'),
                                      inputTagJets= UnpackedJetCollectionVInputTag,
                                      GenParticleTag=cms.InputTag( "flashggPrunedGenParticles" ),
                                      leadPhoOverMassThreshold = cms.untracked.double(0.375),
                                      subleadPhoOverMassThreshold = cms.untracked.double(0.25),
                                      MVAThreshold = cms.untracked.double(-0.6),
                                      jetsNumberThreshold = cms.untracked.double(2.),
                                      jetPtThreshold = cms.untracked.double(40.),
                                      jetEtaThreshold= cms.untracked.double(2.4),
                                      dRJetToPhoLThreshold = cms.untracked.double(0.5),
                                      dRJetToPhoSThreshold = cms.untracked.double(0.5),
                                      dijetMassLowThreshold = cms.untracked.double(60.),
                                      dijetMassHighThreshold = cms.untracked.double(120.),
                                      cosThetaStarThreshold = cms.untracked.double(0.5),
                                      PhoMVAThreshold = cms.untracked.double(-0.2)
)



