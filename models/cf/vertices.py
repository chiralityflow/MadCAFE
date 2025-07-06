# This file was automatically created by FeynRules 1.7.69
# Mathematica version: 8.0 for Mac OS X x86 (64-bit) (November 6, 2010)
# Date: Mon 1 Oct 2012 14:58:25

from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L

# MS: If we add new particles, we must also add their vertices here
# AL: V1 to V4 used to create diagrams, 
# MS: ...s pecifically for internal photons
# AL: Lorentz structure will be updated when constructing Helas (after constructing diagrams)
# to one of either LRV, RLV, LLV, or RRV depending on process. L/R denote right/left fermions
V_1 = Vertex(name = 'V_1',
              particles = [ P.eR__plus__, P.eL__minus__, P.a ],
              color = [ '1' ], # color singlet
              lorentz = [ L.RLV1 ], # L for Lorentz, see lorentz.py in this folder
              couplings = {(0,0):C.GC_3}) # QCD singlet, see couplings.py

V_2 = Vertex(name = 'V_2',
              particles = [ P.eL__plus__, P.eR__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.LRV1 ],
              couplings = {(0,0):C.GC_3})
              

V_3 = Vertex(name = 'V_3',
              particles = [ P.muR__plus__, P.muL__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.RLV1 ],
              couplings = {(0,0):C.GC_3})

V_4 = Vertex(name = 'V_4',
              particles = [ P.muL__plus__, P.muR__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.LRV1 ],
              couplings = {(0,0):C.GC_3})


####################################################
# AL: Same vertices as above but with chiral photons
# MS: Use this for external photons
####################################################

# TODO: Check if lorentz structure will need any updating (I don't think it will)

V_5 = Vertex(name = 'V_5',
              particles = [ P.eR__plus__, P.eL__minus__, P.aL ],
              color = [ '1' ],
              lorentz = [ L.RLV1 ],
              couplings = {(0,0):C.GC_3})

V_6 = Vertex(name = 'V_6',
              particles = [ P.eR__plus__, P.eL__minus__, P.aR ],
              color = [ '1' ],
              lorentz = [ L.RLV1 ],
              couplings = {(0,0):C.GC_3})


V_7 = Vertex(name = 'V_7',
              particles = [ P.eL__plus__, P.eR__minus__, P.aL ],
              color = [ '1' ],
              lorentz = [ L.LRV1 ],
              couplings = {(0,0):C.GC_3})

V_8 = Vertex(name = 'V_8',
              particles = [ P.eL__plus__, P.eR__minus__, P.aR ],
              color = [ '1' ],
              lorentz = [ L.LRV1 ],
              couplings = {(0,0):C.GC_3})


V_9 = Vertex(name = 'V_9',
              particles = [ P.muR__plus__, P.muL__minus__, P.aL ],
              color = [ '1' ],
              lorentz = [ L.RLV1 ],
              couplings = {(0,0):C.GC_3})

V_10 = Vertex(name = 'V_10',
              particles = [ P.muR__plus__, P.muL__minus__, P.aR ],
              color = [ '1' ],
              lorentz = [ L.RLV1 ],
              couplings = {(0,0):C.GC_3})


V11 = Vertex(name = 'V_11',
              particles = [ P.muL__plus__, P.muR__minus__, P.aL ],
              color = [ '1' ],
              lorentz = [ L.LRV1 ],
              couplings = {(0,0):C.GC_3})

V_12 = Vertex(name = 'V_12',
              particles = [ P.muL__plus__, P.muR__minus__, P.aR ],
              color = [ '1' ],
              lorentz = [ L.LRV2 ],
              couplings = {(0,0):C.GC_3})

# ZW: Note -- W bosons only couple by RLV vertices, since the LRV vertices are proportional to
# the P_R projection, which has coupling 0 to the W boson
V_13 = Vertex(name = 'V_13',
               particles = [ P.eR__plus__, P.veL, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RLV2 ],
               couplings = {(0,0):C.GC_240})

V_14 = Vertex(name = 'V_14',
               particles = [ P.muR__plus__, P.vmL, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RLV2 ],
               couplings = {(0,0):C.GC_240})

V_15 = Vertex(name = 'V_15',
                particles = [ P.veR__tilde__, P.eL__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.RLV2 ],
                couplings={(0,0):C.GC_240})

V_16 = Vertex(name = 'V_16',
                particles = [ P.vmR__tilde__, P.muL__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.RLV2 ],
                couplings={(0,0):C.GC_240})

V_17 = Vertex(name = 'V_17',
               particles = [ P.veR__tilde__, P.veL, P.Z ],
               color = [ '1' ],
               lorentz = [ L.RLV4 ],
               couplings = {(0,0):C.GC_262})

V_18 = Vertex(name = 'V_18',
               particles = [ P.vmR__tilde__, P.vmL, P.Z ],
               color = [ '1' ],
               lorentz = [ L.RLV4 ],
               couplings = {(0,0):C.GC_262})

V_19 = Vertex(name = 'V_19',
               particles = [ P.eL__plus__, P.eR__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.LRV4 ],
               couplings = {(0,0):C.GC_259})
            
V_20 = Vertex(name = 'V_20',
               particles = [ P.eR__plus__, P.eL__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.RLV4 ],
               couplings = {(0,0):C.GC_250})

V_21 = Vertex(name = 'V_21',
               particles = [ P.muL__plus__, P.muR__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.LRV4 ],
               couplings = {(0,0):C.GC_259})

V_22 = Vertex(name = 'V_22',
               particles = [ P.muR__plus__, P.muL__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.RLV4 ],
               couplings = {(0,0):C.GC_250})

#SS: Added polarised Z and W bosons.

V_23 = Vertex(name = 'V_23',
               particles = [ P.eL__plus__, P.eR__minus__, P.ZP],
               color = [ '1' ],
               lorentz = [ L.LRV4 ],
               couplings = {(0,0):C.GC_259})

V_24 = Vertex(name = 'V_24',
               particles = [ P.eR__plus__, P.eL__minus__, P.ZP],
               color = [ '1' ],
               lorentz = [ L.RLV4 ],
               couplings = {(0,0):C.GC_250})

V_25 = Vertex(name = 'V_25',
               particles = [ P.eL__plus__, P.eR__minus__, P.ZM],
               color = [ '1' ],
               lorentz = [ L.LRV4 ],
               couplings = {(0,0):C.GC_259})

V_26 = Vertex(name = 'V_26',
               particles = [ P.eR__plus__, P.eL__minus__, P.ZM],
               color = [ '1' ],
               lorentz = [ L.RLV4 ],
               couplings = {(0,0):C.GC_250})

V_27 = Vertex(name = 'V_27',
               particles = [ P.eL__plus__, P.eR__minus__, P.ZZ],
               color = [ '1' ],
               lorentz = [ L.LRV4 ],
               couplings = {(0,0):C.GC_259})

V_28 = Vertex(name = 'V_28',
               particles = [ P.eR__plus__, P.eL__minus__, P.ZZ],
               color = [ '1' ],
               lorentz = [ L.RLV4 ],
               couplings = {(0,0):C.GC_250})

V_29 = Vertex(name = 'V_29',
               particles = [ P.muL__plus__, P.muR__minus__, P.ZP],
               color = [ '1' ],
               lorentz = [ L.LRV4 ],
               couplings = {(0,0):C.GC_259})

V_30 = Vertex(name = 'V_30',
               particles = [ P.muR__plus__, P.muL__minus__, P.ZP],
               color = [ '1' ],
               lorentz = [ L.RLV4 ],
               couplings = {(0,0):C.GC_250})

V_31 = Vertex(name = 'V_31',
               particles = [ P.muL__plus__, P.muR__minus__, P.ZM],
               color = [ '1' ],
               lorentz = [ L.LRV4 ],
               couplings = {(0,0):C.GC_259})

V_32 = Vertex(name = 'V_32',
               particles = [ P.muR__plus__, P.muL__minus__, P.ZM],
               color = [ '1' ],
               lorentz = [ L.RLV4 ],
               couplings = {(0,0):C.GC_250})

V_33 = Vertex(name = 'V_33',
               particles = [ P.muL__plus__, P.muR__minus__, P.ZZ],
               color = [ '1' ],
               lorentz = [ L.LRV4 ],
               couplings = {(0,0):C.GC_259})

V_34 = Vertex(name = 'V_34',
               particles = [ P.muR__plus__, P.muL__minus__, P.ZZ],
               color = [ '1' ],
               lorentz = [ L.RLV4 ],
               couplings = {(0,0):C.GC_250})

V_35 = Vertex(name = 'V_35',
               particles = [ P.veR, P.veL__tilde__, P.ZP],
               color = [ '1' ],
               lorentz = [ L.RLV4 ],
               couplings = {(0,0):C.GC_262})

V_36 = Vertex(name = 'V_36',
               particles = [ P.veR, P.veL__tilde__, P.ZM],
               color = [ '1' ],
               lorentz = [ L.RLV4 ],
               couplings = {(0,0):C.GC_262})

V_37 = Vertex(name = 'V_37',
               particles = [ P.veR, P.veL__tilde__, P.ZZ],
               color = [ '1' ],
               lorentz = [ L.RLV4 ],
               couplings = {(0,0):C.GC_262})

V_38 = Vertex(name = 'V_38',
               particles = [ P.vmR, P.vmL__tilde__, P.ZP],
               color = [ '1' ],
               lorentz = [ L.RLV4 ],
               couplings = {(0,0):C.GC_262})

V_39 = Vertex(name = 'V_39',
               particles = [ P.vmR, P.vmL__tilde__, P.ZM],
               color = [ '1' ],
               lorentz = [ L.RLV4 ],
               couplings = {(0,0):C.GC_262})

V_40 = Vertex(name = 'V_40',
               particles = [ P.vmR, P.vmL__tilde__, P.ZZ],
               color = [ '1' ],
               lorentz = [ L.RLV4 ],
               couplings = {(0,0):C.GC_262})

V_41 = Vertex(name = 'V_41',
               particles = [ P.eR__plus__, P.veL, P.WP__minus__],
               color = [ '1' ],
               lorentz = [ L.RLV2 ],
               couplings = {(0,0):C.GC_240})

V_42 = Vertex(name = 'V_42',
               particles = [ P.eR__plus__, P.veL, P.WM__minus__],
               color = [ '1' ],
               lorentz = [ L.RLV2 ],
               couplings = {(0,0):C.GC_240})

V_43 = Vertex(name = 'V_43',
               particles = [ P.eR__plus__, P.veL, P.WZ__minus__],
               color = [ '1' ],
               lorentz = [ L.RLV2 ],
               couplings = {(0,0):C.GC_240})

V_44 = Vertex(name = 'V_44',
               particles = [ P.muR__plus__, P.vmL, P.WP__minus__],
               color = [ '1' ],
               lorentz = [ L.RLV2 ],
               couplings = {(0,0):C.GC_240})

V_45 = Vertex(name = 'V_45',
               particles = [ P.muR__plus__, P.vmL, P.WM__minus__],
               color = [ '1' ],
               lorentz = [ L.RLV2 ],
               couplings = {(0,0):C.GC_240})

V_46 = Vertex(name = 'V_46',
               particles = [ P.muR__plus__, P.vmL, P.WZ__minus__],
               color = [ '1' ],
               lorentz = [ L.RLV2 ],
               couplings = {(0,0):C.GC_240})

V_47 = Vertex(name = 'V_47',
               particles = [ P.veR__tilde__, P.eL__minus__, P.WP__minus__],
               color = [ '1' ],
               lorentz = [ L.RLV2 ],
               couplings = {(0,0):C.GC_240})

V_48 = Vertex(name = 'V_48',
               particles = [ P.veR__tilde__, P.eL__minus__, P.WM__minus__],
               color = [ '1' ],
               lorentz = [ L.RLV2 ],
               couplings = {(0,0):C.GC_240})

V_49 = Vertex(name = 'V_49',
               particles = [ P.veR__tilde__, P.eL__minus__, P.WZ__minus__],
               color = [ '1' ],
               lorentz = [ L.RLV2 ],
               couplings = {(0,0):C.GC_240})

V_50 = Vertex(name = 'V_50',
               particles = [ P.vmR__tilde__, P.muL__minus__, P.WP__minus__],
               color = [ '1' ],
               lorentz = [ L.RLV2 ],
               couplings = {(0,0):C.GC_240})

V_51 = Vertex(name = 'V_51',
               particles = [ P.vmR__tilde__, P.muL__minus__, P.WM__minus__],
               color = [ '1' ],
               lorentz = [ L.RLV2 ],
               couplings = {(0,0):C.GC_240})

V_52 = Vertex(name = 'V_52',
               particles = [ P.vmR__tilde__, P.muL__minus__, P.WZ__minus__],
               color = [ '1' ],
               lorentz = [ L.RLV2 ],
               couplings = {(0,0):C.GC_240})

#SS: Defined the VVV vertices with polarised and unpolarised vector bosons.

V_53 = Vertex(name = 'V_53',
               particles = [ P.a, P.W__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_54 = Vertex(name = 'V_54',
               particles = [ P.a, P.W__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_55 = Vertex(name = 'V_55',
               particles = [ P.a, P.W__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_56 = Vertex(name = 'V_56',
               particles = [ P.a, P.W__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_57 = Vertex(name = 'V_57',
               particles = [ P.a, P.WP__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_58 = Vertex(name = 'V_58',
               particles = [ P.a, P.WP__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_59 = Vertex(name = 'V_59',
               particles = [ P.a, P.WP__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_60 = Vertex(name = 'V_60',
               particles = [ P.a, P.WP__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_61 = Vertex(name = 'V_61',
               particles = [ P.a, P.WM__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_62 = Vertex(name = 'V_62',
               particles = [ P.a, P.WM__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_63 = Vertex(name = 'V_63',
               particles = [ P.a, P.WM__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_64 = Vertex(name = 'V_64',
               particles = [ P.a, P.WM__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_65 = Vertex(name = 'V_65',
               particles = [ P.a, P.WZ__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_66 = Vertex(name = 'V_66',
               particles = [ P.a, P.WZ__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_67 = Vertex(name = 'V_67',
               particles = [ P.a, P.WZ__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_68 = Vertex(name = 'V_68',
               particles = [ P.a, P.WZ__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_69 = Vertex(name = 'V_69',
               particles = [ P.aL, P.W__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_70 = Vertex(name = 'V_70',
               particles = [ P.aL, P.W__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_71 = Vertex(name = 'V_71',
               particles = [ P.aL, P.W__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_72 = Vertex(name = 'V_72',
               particles = [ P.aL, P.W__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_73 = Vertex(name = 'V_73',
               particles = [ P.aL, P.WP__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_74 = Vertex(name = 'V_74',
               particles = [ P.aL, P.WP__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_75 = Vertex(name = 'V_75',
               particles = [ P.aL, P.WP__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_76 = Vertex(name = 'V_76',
               particles = [ P.aL, P.WP__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_77 = Vertex(name = 'V_77',
               particles = [ P.aL, P.WM__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_78 = Vertex(name = 'V_78',
               particles = [ P.aL, P.WM__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_79 = Vertex(name = 'V_79',
               particles = [ P.aL, P.WM__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_80 = Vertex(name = 'V_80',
               particles = [ P.aL, P.WM__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_81 = Vertex(name = 'V_81',
               particles = [ P.aL, P.WZ__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_82 = Vertex(name = 'V_82',
               particles = [ P.aL, P.WZ__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_83 = Vertex(name = 'V_83',
               particles = [ P.aL, P.WZ__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_84 = Vertex(name = 'V_84',
               particles = [ P.aL, P.WZ__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_85 = Vertex(name = 'V_85',
               particles = [ P.aR, P.W__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_86 = Vertex(name = 'V_86',
               particles = [ P.aR, P.W__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_87 = Vertex(name = 'V_87',
               particles = [ P.aR, P.W__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_88 = Vertex(name = 'V_88',
               particles = [ P.aR, P.W__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_89 = Vertex(name = 'V_89',
               particles = [ P.aR, P.WP__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_90 = Vertex(name = 'V_90',
               particles = [ P.aR, P.WP__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_91 = Vertex(name = 'V_91',
               particles = [ P.aR, P.WP__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_92 = Vertex(name = 'V_92',
               particles = [ P.aR, P.WP__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_93 = Vertex(name = 'V_93',
               particles = [ P.aR, P.WM__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_94 = Vertex(name = 'V_94',
               particles = [ P.aR, P.WM__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_95 = Vertex(name = 'V_95',
               particles = [ P.aR, P.WM__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_96 = Vertex(name = 'V_96',
               particles = [ P.aR, P.WM__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_97 = Vertex(name = 'V_97',
               particles = [ P.aR, P.WZ__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_98 = Vertex(name = 'V_98',
               particles = [ P.aR, P.WZ__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_99 = Vertex(name = 'V_99',
               particles = [ P.aR, P.WZ__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_100 = Vertex(name = 'V_100',
               particles = [ P.aR, P.WZ__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_109})

V_101 = Vertex(name = 'V_101',
               particles = [ P.Z, P.W__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_102 = Vertex(name = 'V_102',
               particles = [ P.Z, P.W__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_103 = Vertex(name = 'V_103',
               particles = [ P.Z, P.W__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_104 = Vertex(name = 'V_104',
               particles = [ P.Z, P.W__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_105 = Vertex(name = 'V_105',
               particles = [ P.Z, P.WP__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_106 = Vertex(name = 'V_106',
               particles = [ P.Z, P.WP__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_107 = Vertex(name = 'V_107',
               particles = [ P.Z, P.WP__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_108 = Vertex(name = 'V_108',
               particles = [ P.Z, P.WP__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_109 = Vertex(name = 'V_109',
               particles = [ P.Z, P.WM__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_110 = Vertex(name = 'V_110',
               particles = [ P.Z, P.WM__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_111 = Vertex(name = 'V_111',
               particles = [ P.Z, P.WM__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_112 = Vertex(name = 'V_112',
               particles = [ P.Z, P.WM__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_113 = Vertex(name = 'V_113',
               particles = [ P.Z, P.WZ__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_114 = Vertex(name = 'V_114',
               particles = [ P.Z, P.WZ__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_115 = Vertex(name = 'V_115',
               particles = [ P.Z, P.WZ__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_116 = Vertex(name = 'V_116',
               particles = [ P.Z, P.WZ__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_117 = Vertex(name = 'V_117',
               particles = [ P.ZP, P.W__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_118 = Vertex(name = 'V_118',
               particles = [ P.ZP, P.W__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_119 = Vertex(name = 'V_119',
               particles = [ P.ZP, P.W__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_120 = Vertex(name = 'V_120',
               particles = [ P.ZP, P.W__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_121 = Vertex(name = 'V_121',
               particles = [ P.ZP, P.WP__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_122 = Vertex(name = 'V_122',
               particles = [ P.ZP, P.WP__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_123 = Vertex(name = 'V_123',
               particles = [ P.ZP, P.WP__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_124 = Vertex(name = 'V_124',
               particles = [ P.ZP, P.WP__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_125 = Vertex(name = 'V_125',
               particles = [ P.ZP, P.WM__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_126 = Vertex(name = 'V_126',
               particles = [ P.ZP, P.WM__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_127 = Vertex(name = 'V_127',
               particles = [ P.ZP, P.WM__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_128 = Vertex(name = 'V_128',
               particles = [ P.ZP, P.WM__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_129 = Vertex(name = 'V_129',
               particles = [ P.ZP, P.WZ__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_130 = Vertex(name = 'V_130',
               particles = [ P.ZP, P.WZ__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_131 = Vertex(name = 'V_131',
               particles = [ P.ZP, P.WZ__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_132 = Vertex(name = 'V_132',
               particles = [ P.ZP, P.WZ__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_133 = Vertex(name = 'V_133',
               particles = [ P.ZM, P.W__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_134 = Vertex(name = 'V_134',
               particles = [ P.ZM, P.W__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_135 = Vertex(name = 'V_135',
               particles = [ P.ZM, P.W__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_136 = Vertex(name = 'V_136',
               particles = [ P.ZM, P.W__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_137 = Vertex(name = 'V_137',
               particles = [ P.ZM, P.WP__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_138 = Vertex(name = 'V_138',
               particles = [ P.ZM, P.WP__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_139 = Vertex(name = 'V_139',
               particles = [ P.ZM, P.WP__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_140 = Vertex(name = 'V_140',
               particles = [ P.ZM, P.WP__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_141 = Vertex(name = 'V_141',
               particles = [ P.ZM, P.WM__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_142 = Vertex(name = 'V_142',
               particles = [ P.ZM, P.WM__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_143 = Vertex(name = 'V_143',
               particles = [ P.ZM, P.WM__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_144 = Vertex(name = 'V_144',
               particles = [ P.ZM, P.WM__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_145 = Vertex(name = 'V_145',
               particles = [ P.ZM, P.WZ__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_146 = Vertex(name = 'V_146',
               particles = [ P.ZM, P.WZ__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_147 = Vertex(name = 'V_147',
               particles = [ P.ZM, P.WZ__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_148 = Vertex(name = 'V_148',
               particles = [ P.ZM, P.WZ__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_149 = Vertex(name = 'V_149',
               particles = [ P.ZZ, P.W__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_150 = Vertex(name = 'V_150',
               particles = [ P.ZZ, P.W__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_151 = Vertex(name = 'V_151',
               particles = [ P.ZZ, P.W__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_152 = Vertex(name = 'V_152',
               particles = [ P.ZZ, P.W__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_153 = Vertex(name = 'V_153',
               particles = [ P.ZZ, P.WP__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_154 = Vertex(name = 'V_154',
               particles = [ P.ZZ, P.WP__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_155 = Vertex(name = 'V_155',
               particles = [ P.ZZ, P.WP__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_156 = Vertex(name = 'V_156',
               particles = [ P.ZZ, P.WP__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_157 = Vertex(name = 'V_157',
               particles = [ P.ZZ, P.WM__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_158 = Vertex(name = 'V_158',
               particles = [ P.ZZ, P.WM__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_159 = Vertex(name = 'V_159',
               particles = [ P.ZZ, P.WM__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_160 = Vertex(name = 'V_160',
               particles = [ P.ZZ, P.WM__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_161 = Vertex(name = 'V_161',
               particles = [ P.ZZ, P.WZ__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_162 = Vertex(name = 'V_162',
               particles = [ P.ZZ, P.WZ__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_163 = Vertex(name = 'V_163',
               particles = [ P.ZZ, P.WZ__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

V_164 = Vertex(name = 'V_164',
               particles = [ P.ZZ, P.WZ__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_110})

    # SS: Defined VVVV for polarised and unpolarised vector bosons.
 
V_165 = Vertex(name = 'V_165',
               particles = [ P.W__plus__, P.W__minus__, P.W__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_166 = Vertex(name = 'V_166',
               particles = [ P.W__plus__, P.W__minus__, P.W__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_167 = Vertex(name = 'V_167',
               particles = [ P.W__plus__, P.W__minus__, P.W__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_168 = Vertex(name = 'V_168',
               particles = [ P.W__plus__, P.W__minus__, P.W__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_169 = Vertex(name = 'V_169',
               particles = [ P.W__plus__, P.W__minus__, P.WP__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_170 = Vertex(name = 'V_170',
               particles = [ P.W__plus__, P.W__minus__, P.WP__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_171 = Vertex(name = 'V_171',
               particles = [ P.W__plus__, P.W__minus__, P.WP__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_172 = Vertex(name = 'V_172',
               particles = [ P.W__plus__, P.W__minus__, P.WP__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_173 = Vertex(name = 'V_173',
               particles = [ P.W__plus__, P.W__minus__, P.WM__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_174 = Vertex(name = 'V_174',
               particles = [ P.W__plus__, P.W__minus__, P.WM__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_175 = Vertex(name = 'V_175',
               particles = [ P.W__plus__, P.W__minus__, P.WM__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_176 = Vertex(name = 'V_176',
               particles = [ P.W__plus__, P.W__minus__, P.WM__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_177 = Vertex(name = 'V_177',
               particles = [ P.W__plus__, P.W__minus__, P.WZ__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_178 = Vertex(name = 'V_178',
               particles = [ P.W__plus__, P.W__minus__, P.WZ__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_179 = Vertex(name = 'V_179',
               particles = [ P.W__plus__, P.W__minus__, P.WZ__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_180 = Vertex(name = 'V_180',
               particles = [ P.W__plus__, P.W__minus__, P.WZ__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_181 = Vertex(name = 'V_181',
               particles = [ P.W__plus__, P.WP__minus__, P.W__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_182 = Vertex(name = 'V_182',
               particles = [ P.W__plus__, P.WP__minus__, P.W__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_183 = Vertex(name = 'V_183',
               particles = [ P.W__plus__, P.WP__minus__, P.W__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_184 = Vertex(name = 'V_184',
               particles = [ P.W__plus__, P.WP__minus__, P.WP__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_185 = Vertex(name = 'V_185',
               particles = [ P.W__plus__, P.WP__minus__, P.WP__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_186 = Vertex(name = 'V_186',
               particles = [ P.W__plus__, P.WP__minus__, P.WP__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_187 = Vertex(name = 'V_187',
               particles = [ P.W__plus__, P.WP__minus__, P.WM__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_188 = Vertex(name = 'V_188',
               particles = [ P.W__plus__, P.WP__minus__, P.WM__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_189 = Vertex(name = 'V_189',
               particles = [ P.W__plus__, P.WP__minus__, P.WM__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_190 = Vertex(name = 'V_190',
               particles = [ P.W__plus__, P.WP__minus__, P.WZ__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_191 = Vertex(name = 'V_191',
               particles = [ P.W__plus__, P.WP__minus__, P.WZ__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_192 = Vertex(name = 'V_192',
               particles = [ P.W__plus__, P.WP__minus__, P.WZ__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_193 = Vertex(name = 'V_193',
               particles = [ P.W__plus__, P.WM__minus__, P.W__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_194 = Vertex(name = 'V_194',
               particles = [ P.W__plus__, P.WM__minus__, P.W__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_195 = Vertex(name = 'V_195',
               particles = [ P.W__plus__, P.WM__minus__, P.WP__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_196 = Vertex(name = 'V_196',
               particles = [ P.W__plus__, P.WM__minus__, P.WP__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_197 = Vertex(name = 'V_197',
               particles = [ P.W__plus__, P.WM__minus__, P.WM__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_198 = Vertex(name = 'V_198',
               particles = [ P.W__plus__, P.WM__minus__, P.WM__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_199 = Vertex(name = 'V_199',
               particles = [ P.W__plus__, P.WM__minus__, P.WZ__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_200 = Vertex(name = 'V_200',
               particles = [ P.W__plus__, P.WM__minus__, P.WZ__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_201 = Vertex(name = 'V_201',
               particles = [ P.W__plus__, P.WZ__minus__, P.W__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_202 = Vertex(name = 'V_202',
               particles = [ P.W__plus__, P.WZ__minus__, P.WP__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_203 = Vertex(name = 'V_203',
               particles = [ P.W__plus__, P.WZ__minus__, P.WM__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_204 = Vertex(name = 'V_204',
               particles = [ P.W__plus__, P.WZ__minus__, P.WZ__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_205 = Vertex(name = 'V_205',
               particles = [ P.WP__plus__, P.W__minus__, P.WP__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_206 = Vertex(name = 'V_206',
               particles = [ P.WP__plus__, P.W__minus__, P.WP__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_207 = Vertex(name = 'V_207',
               particles = [ P.WP__plus__, P.W__minus__, P.WP__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_208 = Vertex(name = 'V_208',
               particles = [ P.WP__plus__, P.W__minus__, P.WP__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_209 = Vertex(name = 'V_209',
               particles = [ P.WP__plus__, P.W__minus__, P.WM__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_210 = Vertex(name = 'V_210',
               particles = [ P.WP__plus__, P.W__minus__, P.WM__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_211 = Vertex(name = 'V_211',
               particles = [ P.WP__plus__, P.W__minus__, P.WM__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_212 = Vertex(name = 'V_212',
               particles = [ P.WP__plus__, P.W__minus__, P.WM__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_213 = Vertex(name = 'V_213',
               particles = [ P.WP__plus__, P.W__minus__, P.WZ__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_214 = Vertex(name = 'V_214',
               particles = [ P.WP__plus__, P.W__minus__, P.WZ__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_215 = Vertex(name = 'V_215',
               particles = [ P.WP__plus__, P.W__minus__, P.WZ__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_216 = Vertex(name = 'V_216',
               particles = [ P.WP__plus__, P.W__minus__, P.WZ__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_217 = Vertex(name = 'V_217',
               particles = [ P.WP__plus__, P.WP__minus__, P.WP__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_218 = Vertex(name = 'V_218',
               particles = [ P.WP__plus__, P.WP__minus__, P.WP__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_219 = Vertex(name = 'V_219',
               particles = [ P.WP__plus__, P.WP__minus__, P.WP__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_220 = Vertex(name = 'V_220',
               particles = [ P.WP__plus__, P.WP__minus__, P.WM__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_221 = Vertex(name = 'V_221',
               particles = [ P.WP__plus__, P.WP__minus__, P.WM__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_222 = Vertex(name = 'V_222',
               particles = [ P.WP__plus__, P.WP__minus__, P.WM__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_223 = Vertex(name = 'V_223',
               particles = [ P.WP__plus__, P.WP__minus__, P.WZ__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_224 = Vertex(name = 'V_224',
               particles = [ P.WP__plus__, P.WP__minus__, P.WZ__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_225 = Vertex(name = 'V_225',
               particles = [ P.WP__plus__, P.WP__minus__, P.WZ__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_226 = Vertex(name = 'V_226',
               particles = [ P.WP__plus__, P.WM__minus__, P.WP__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_227 = Vertex(name = 'V_227',
               particles = [ P.WP__plus__, P.WM__minus__, P.WP__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_228 = Vertex(name = 'V_228',
               particles = [ P.WP__plus__, P.WM__minus__, P.WM__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_229 = Vertex(name = 'V_229',
               particles = [ P.WP__plus__, P.WM__minus__, P.WM__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_230 = Vertex(name = 'V_230',
               particles = [ P.WP__plus__, P.WM__minus__, P.WZ__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_231 = Vertex(name = 'V_231',
               particles = [ P.WP__plus__, P.WM__minus__, P.WZ__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_232 = Vertex(name = 'V_232',
               particles = [ P.WP__plus__, P.WZ__minus__, P.WP__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_233 = Vertex(name = 'V_233',
               particles = [ P.WP__plus__, P.WZ__minus__, P.WM__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_234 = Vertex(name = 'V_234',
               particles = [ P.WP__plus__, P.WZ__minus__, P.WZ__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_235 = Vertex(name = 'V_235',
               particles = [ P.WM__plus__, P.W__minus__, P.WM__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_236 = Vertex(name = 'V_236',
               particles = [ P.WM__plus__, P.W__minus__, P.WM__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_237 = Vertex(name = 'V_237',
               particles = [ P.WM__plus__, P.W__minus__, P.WM__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_238 = Vertex(name = 'V_238',
               particles = [ P.WM__plus__, P.W__minus__, P.WM__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_239 = Vertex(name = 'V_239',
               particles = [ P.WM__plus__, P.W__minus__, P.WZ__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_240 = Vertex(name = 'V_240',
               particles = [ P.WM__plus__, P.W__minus__, P.WZ__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_241 = Vertex(name = 'V_241',
               particles = [ P.WM__plus__, P.W__minus__, P.WZ__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_242 = Vertex(name = 'V_242',
               particles = [ P.WM__plus__, P.W__minus__, P.WZ__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_243 = Vertex(name = 'V_243',
               particles = [ P.WM__plus__, P.WP__minus__, P.WM__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_244 = Vertex(name = 'V_244',
               particles = [ P.WM__plus__, P.WP__minus__, P.WM__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_245 = Vertex(name = 'V_245',
               particles = [ P.WM__plus__, P.WP__minus__, P.WM__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_246 = Vertex(name = 'V_246',
               particles = [ P.WM__plus__, P.WP__minus__, P.WZ__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_247 = Vertex(name = 'V_247',
               particles = [ P.WM__plus__, P.WP__minus__, P.WZ__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_248 = Vertex(name = 'V_248',
               particles = [ P.WM__plus__, P.WP__minus__, P.WZ__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_249 = Vertex(name = 'V_249',
               particles = [ P.WM__plus__, P.WM__minus__, P.WM__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_250 = Vertex(name = 'V_250',
               particles = [ P.WM__plus__, P.WM__minus__, P.WM__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_251 = Vertex(name = 'V_251',
               particles = [ P.WM__plus__, P.WM__minus__, P.WZ__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_252 = Vertex(name = 'V_252',
               particles = [ P.WM__plus__, P.WM__minus__, P.WZ__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_253 = Vertex(name = 'V_253',
               particles = [ P.WM__plus__, P.WZ__minus__, P.WM__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_254 = Vertex(name = 'V_254',
               particles = [ P.WM__plus__, P.WZ__minus__, P.WZ__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_255 = Vertex(name = 'V_255',
               particles = [ P.WZ__plus__, P.W__minus__, P.WZ__plus__, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_256 = Vertex(name = 'V_256',
               particles = [ P.WZ__plus__, P.W__minus__, P.WZ__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_257 = Vertex(name = 'V_257',
               particles = [ P.WZ__plus__, P.W__minus__, P.WZ__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_258 = Vertex(name = 'V_258',
               particles = [ P.WZ__plus__, P.W__minus__, P.WZ__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_259 = Vertex(name = 'V_259',
               particles = [ P.WZ__plus__, P.WP__minus__, P.WZ__plus__, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_260 = Vertex(name = 'V_260',
               particles = [ P.WZ__plus__, P.WP__minus__, P.WZ__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_261 = Vertex(name = 'V_261',
               particles = [ P.WZ__plus__, P.WP__minus__, P.WZ__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_262 = Vertex(name = 'V_262',
               particles = [ P.WZ__plus__, P.WM__minus__, P.WZ__plus__, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_263 = Vertex(name = 'V_263',
               particles = [ P.WZ__plus__, P.WM__minus__, P.WZ__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_264 = Vertex(name = 'V_264',
               particles = [ P.WZ__plus__, P.WZ__minus__, P.WZ__plus__, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_111})

V_265 = Vertex(name = 'V_265',
               particles = [ P.W__plus__, P.a, P.W__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_266 = Vertex(name = 'V_266',
               particles = [ P.W__plus__, P.a, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_267 = Vertex(name = 'V_267',
               particles = [ P.W__plus__, P.a, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_268 = Vertex(name = 'V_268',
               particles = [ P.W__plus__, P.a, P.WP__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_269 = Vertex(name = 'V_269',
               particles = [ P.W__plus__, P.a, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_270 = Vertex(name = 'V_270',
               particles = [ P.W__plus__, P.a, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_271 = Vertex(name = 'V_271',
               particles = [ P.W__plus__, P.a, P.WM__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_272 = Vertex(name = 'V_272',
               particles = [ P.W__plus__, P.a, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_273 = Vertex(name = 'V_273',
               particles = [ P.W__plus__, P.a, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_274 = Vertex(name = 'V_274',
               particles = [ P.W__plus__, P.a, P.WZ__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_275 = Vertex(name = 'V_275',
               particles = [ P.W__plus__, P.a, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_276 = Vertex(name = 'V_276',
               particles = [ P.W__plus__, P.a, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_277 = Vertex(name = 'V_277',
               particles = [ P.W__plus__, P.aL, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_278 = Vertex(name = 'V_278',
               particles = [ P.W__plus__, P.aL, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_279 = Vertex(name = 'V_279',
               particles = [ P.W__plus__, P.aL, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_280 = Vertex(name = 'V_280',
               particles = [ P.W__plus__, P.aL, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_281 = Vertex(name = 'V_281',
               particles = [ P.W__plus__, P.aL, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_282 = Vertex(name = 'V_282',
               particles = [ P.W__plus__, P.aL, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_283 = Vertex(name = 'V_283',
               particles = [ P.W__plus__, P.aL, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_284 = Vertex(name = 'V_284',
               particles = [ P.W__plus__, P.aL, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_285 = Vertex(name = 'V_285',
               particles = [ P.W__plus__, P.aR, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_286 = Vertex(name = 'V_286',
               particles = [ P.W__plus__, P.aR, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_287 = Vertex(name = 'V_287',
               particles = [ P.W__plus__, P.aR, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_288 = Vertex(name = 'V_288',
               particles = [ P.W__plus__, P.aR, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_289 = Vertex(name = 'V_289',
               particles = [ P.W__plus__, P.Z, P.W__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_290 = Vertex(name = 'V_290',
               particles = [ P.W__plus__, P.Z, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_291 = Vertex(name = 'V_291',
               particles = [ P.W__plus__, P.Z, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_292 = Vertex(name = 'V_292',
               particles = [ P.W__plus__, P.Z, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_293 = Vertex(name = 'V_293',
               particles = [ P.W__plus__, P.Z, P.W__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_294 = Vertex(name = 'V_294',
               particles = [ P.W__plus__, P.Z, P.W__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_295 = Vertex(name = 'V_295',
               particles = [ P.W__plus__, P.Z, P.W__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_296 = Vertex(name = 'V_296',
               particles = [ P.W__plus__, P.Z, P.WP__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_297 = Vertex(name = 'V_297',
               particles = [ P.W__plus__, P.Z, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_298 = Vertex(name = 'V_298',
               particles = [ P.W__plus__, P.Z, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_299 = Vertex(name = 'V_299',
               particles = [ P.W__plus__, P.Z, P.WP__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_300 = Vertex(name = 'V_300',
               particles = [ P.W__plus__, P.Z, P.WP__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_301 = Vertex(name = 'V_301',
               particles = [ P.W__plus__, P.Z, P.WP__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_302 = Vertex(name = 'V_302',
               particles = [ P.W__plus__, P.Z, P.WP__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_303 = Vertex(name = 'V_303',
               particles = [ P.W__plus__, P.Z, P.WM__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_304 = Vertex(name = 'V_304',
               particles = [ P.W__plus__, P.Z, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_305 = Vertex(name = 'V_305',
               particles = [ P.W__plus__, P.Z, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_306 = Vertex(name = 'V_306',
               particles = [ P.W__plus__, P.Z, P.WM__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_307 = Vertex(name = 'V_307',
               particles = [ P.W__plus__, P.Z, P.WM__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_308 = Vertex(name = 'V_308',
               particles = [ P.W__plus__, P.Z, P.WM__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_309 = Vertex(name = 'V_309',
               particles = [ P.W__plus__, P.Z, P.WM__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_310 = Vertex(name = 'V_310',
               particles = [ P.W__plus__, P.Z, P.WZ__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_311 = Vertex(name = 'V_311',
               particles = [ P.W__plus__, P.Z, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_312 = Vertex(name = 'V_312',
               particles = [ P.W__plus__, P.Z, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_313 = Vertex(name = 'V_313',
               particles = [ P.W__plus__, P.Z, P.WZ__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_314 = Vertex(name = 'V_314',
               particles = [ P.W__plus__, P.Z, P.WZ__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_315 = Vertex(name = 'V_315',
               particles = [ P.W__plus__, P.Z, P.WZ__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_316 = Vertex(name = 'V_316',
               particles = [ P.W__plus__, P.Z, P.WZ__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_317 = Vertex(name = 'V_317',
               particles = [ P.W__plus__, P.ZP, P.W__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_318 = Vertex(name = 'V_318',
               particles = [ P.W__plus__, P.ZP, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_319 = Vertex(name = 'V_319',
               particles = [ P.W__plus__, P.ZP, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_320 = Vertex(name = 'V_320',
               particles = [ P.W__plus__, P.ZP, P.W__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_321 = Vertex(name = 'V_321',
               particles = [ P.W__plus__, P.ZP, P.W__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_322 = Vertex(name = 'V_322',
               particles = [ P.W__plus__, P.ZP, P.W__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_323 = Vertex(name = 'V_323',
               particles = [ P.W__plus__, P.ZP, P.WP__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_324 = Vertex(name = 'V_324',
               particles = [ P.W__plus__, P.ZP, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_325 = Vertex(name = 'V_325',
               particles = [ P.W__plus__, P.ZP, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_326 = Vertex(name = 'V_326',
               particles = [ P.W__plus__, P.ZP, P.WP__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_327 = Vertex(name = 'V_327',
               particles = [ P.W__plus__, P.ZP, P.WP__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_328 = Vertex(name = 'V_328',
               particles = [ P.W__plus__, P.ZP, P.WP__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_329 = Vertex(name = 'V_329',
               particles = [ P.W__plus__, P.ZP, P.WM__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_330 = Vertex(name = 'V_330',
               particles = [ P.W__plus__, P.ZP, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_331 = Vertex(name = 'V_331',
               particles = [ P.W__plus__, P.ZP, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_332 = Vertex(name = 'V_332',
               particles = [ P.W__plus__, P.ZP, P.WM__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_333 = Vertex(name = 'V_333',
               particles = [ P.W__plus__, P.ZP, P.WM__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_334 = Vertex(name = 'V_334',
               particles = [ P.W__plus__, P.ZP, P.WM__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_335 = Vertex(name = 'V_335',
               particles = [ P.W__plus__, P.ZP, P.WZ__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_336 = Vertex(name = 'V_336',
               particles = [ P.W__plus__, P.ZP, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_337 = Vertex(name = 'V_337',
               particles = [ P.W__plus__, P.ZP, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_338 = Vertex(name = 'V_338',
               particles = [ P.W__plus__, P.ZP, P.WZ__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_339 = Vertex(name = 'V_339',
               particles = [ P.W__plus__, P.ZP, P.WZ__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_340 = Vertex(name = 'V_340',
               particles = [ P.W__plus__, P.ZP, P.WZ__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_341 = Vertex(name = 'V_341',
               particles = [ P.W__plus__, P.ZM, P.W__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_342 = Vertex(name = 'V_342',
               particles = [ P.W__plus__, P.ZM, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_343 = Vertex(name = 'V_343',
               particles = [ P.W__plus__, P.ZM, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_344 = Vertex(name = 'V_344',
               particles = [ P.W__plus__, P.ZM, P.W__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_345 = Vertex(name = 'V_345',
               particles = [ P.W__plus__, P.ZM, P.W__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_346 = Vertex(name = 'V_346',
               particles = [ P.W__plus__, P.ZM, P.WP__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_347 = Vertex(name = 'V_347',
               particles = [ P.W__plus__, P.ZM, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_348 = Vertex(name = 'V_348',
               particles = [ P.W__plus__, P.ZM, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_349 = Vertex(name = 'V_349',
               particles = [ P.W__plus__, P.ZM, P.WP__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_350 = Vertex(name = 'V_350',
               particles = [ P.W__plus__, P.ZM, P.WP__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_351 = Vertex(name = 'V_351',
               particles = [ P.W__plus__, P.ZM, P.WM__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_352 = Vertex(name = 'V_352',
               particles = [ P.W__plus__, P.ZM, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_353 = Vertex(name = 'V_353',
               particles = [ P.W__plus__, P.ZM, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_354 = Vertex(name = 'V_354',
               particles = [ P.W__plus__, P.ZM, P.WM__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_355 = Vertex(name = 'V_355',
               particles = [ P.W__plus__, P.ZM, P.WM__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_356 = Vertex(name = 'V_356',
               particles = [ P.W__plus__, P.ZM, P.WZ__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_357 = Vertex(name = 'V_357',
               particles = [ P.W__plus__, P.ZM, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_358 = Vertex(name = 'V_358',
               particles = [ P.W__plus__, P.ZM, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_359 = Vertex(name = 'V_359',
               particles = [ P.W__plus__, P.ZM, P.WZ__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_360 = Vertex(name = 'V_360',
               particles = [ P.W__plus__, P.ZM, P.WZ__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_361 = Vertex(name = 'V_361',
               particles = [ P.W__plus__, P.ZZ, P.W__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_362 = Vertex(name = 'V_362',
               particles = [ P.W__plus__, P.ZZ, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_363 = Vertex(name = 'V_363',
               particles = [ P.W__plus__, P.ZZ, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_364 = Vertex(name = 'V_364',
               particles = [ P.W__plus__, P.ZZ, P.W__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_365 = Vertex(name = 'V_365',
               particles = [ P.W__plus__, P.ZZ, P.WP__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_366 = Vertex(name = 'V_366',
               particles = [ P.W__plus__, P.ZZ, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_367 = Vertex(name = 'V_367',
               particles = [ P.W__plus__, P.ZZ, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_368 = Vertex(name = 'V_368',
               particles = [ P.W__plus__, P.ZZ, P.WP__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_369 = Vertex(name = 'V_369',
               particles = [ P.W__plus__, P.ZZ, P.WM__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_370 = Vertex(name = 'V_370',
               particles = [ P.W__plus__, P.ZZ, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_371 = Vertex(name = 'V_371',
               particles = [ P.W__plus__, P.ZZ, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_372 = Vertex(name = 'V_372',
               particles = [ P.W__plus__, P.ZZ, P.WM__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_373 = Vertex(name = 'V_373',
               particles = [ P.W__plus__, P.ZZ, P.WZ__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_374 = Vertex(name = 'V_374',
               particles = [ P.W__plus__, P.ZZ, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_375 = Vertex(name = 'V_375',
               particles = [ P.W__plus__, P.ZZ, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_376 = Vertex(name = 'V_376',
               particles = [ P.W__plus__, P.ZZ, P.WZ__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_377 = Vertex(name = 'V_377',
               particles = [ P.WP__plus__, P.a, P.W__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_378 = Vertex(name = 'V_378',
               particles = [ P.WP__plus__, P.a, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_379 = Vertex(name = 'V_379',
               particles = [ P.WP__plus__, P.a, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_380 = Vertex(name = 'V_380',
               particles = [ P.WP__plus__, P.a, P.WP__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_381 = Vertex(name = 'V_381',
               particles = [ P.WP__plus__, P.a, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_382 = Vertex(name = 'V_382',
               particles = [ P.WP__plus__, P.a, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_383 = Vertex(name = 'V_383',
               particles = [ P.WP__plus__, P.a, P.WM__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_384 = Vertex(name = 'V_384',
               particles = [ P.WP__plus__, P.a, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_385 = Vertex(name = 'V_385',
               particles = [ P.WP__plus__, P.a, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_386 = Vertex(name = 'V_386',
               particles = [ P.WP__plus__, P.a, P.WZ__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_387 = Vertex(name = 'V_387',
               particles = [ P.WP__plus__, P.a, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_388 = Vertex(name = 'V_388',
               particles = [ P.WP__plus__, P.a, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_389 = Vertex(name = 'V_389',
               particles = [ P.WP__plus__, P.aL, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_390 = Vertex(name = 'V_390',
               particles = [ P.WP__plus__, P.aL, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_391 = Vertex(name = 'V_391',
               particles = [ P.WP__plus__, P.aL, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_392 = Vertex(name = 'V_392',
               particles = [ P.WP__plus__, P.aL, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_393 = Vertex(name = 'V_393',
               particles = [ P.WP__plus__, P.aL, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_394 = Vertex(name = 'V_394',
               particles = [ P.WP__plus__, P.aL, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_395 = Vertex(name = 'V_395',
               particles = [ P.WP__plus__, P.aL, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_396 = Vertex(name = 'V_396',
               particles = [ P.WP__plus__, P.aL, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_397 = Vertex(name = 'V_397',
               particles = [ P.WP__plus__, P.aR, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_398 = Vertex(name = 'V_398',
               particles = [ P.WP__plus__, P.aR, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_399 = Vertex(name = 'V_399',
               particles = [ P.WP__plus__, P.aR, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_400 = Vertex(name = 'V_400',
               particles = [ P.WP__plus__, P.aR, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_401 = Vertex(name = 'V_401',
               particles = [ P.WP__plus__, P.Z, P.W__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_402 = Vertex(name = 'V_402',
               particles = [ P.WP__plus__, P.Z, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_403 = Vertex(name = 'V_403',
               particles = [ P.WP__plus__, P.Z, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_404 = Vertex(name = 'V_404',
               particles = [ P.WP__plus__, P.Z, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_405 = Vertex(name = 'V_405',
               particles = [ P.WP__plus__, P.Z, P.W__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_406 = Vertex(name = 'V_406',
               particles = [ P.WP__plus__, P.Z, P.W__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_407 = Vertex(name = 'V_407',
               particles = [ P.WP__plus__, P.Z, P.W__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_408 = Vertex(name = 'V_408',
               particles = [ P.WP__plus__, P.Z, P.WP__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_409 = Vertex(name = 'V_409',
               particles = [ P.WP__plus__, P.Z, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_410 = Vertex(name = 'V_410',
               particles = [ P.WP__plus__, P.Z, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_411 = Vertex(name = 'V_411',
               particles = [ P.WP__plus__, P.Z, P.WP__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_412 = Vertex(name = 'V_412',
               particles = [ P.WP__plus__, P.Z, P.WP__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_413 = Vertex(name = 'V_413',
               particles = [ P.WP__plus__, P.Z, P.WP__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_414 = Vertex(name = 'V_414',
               particles = [ P.WP__plus__, P.Z, P.WP__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_415 = Vertex(name = 'V_415',
               particles = [ P.WP__plus__, P.Z, P.WM__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_416 = Vertex(name = 'V_416',
               particles = [ P.WP__plus__, P.Z, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_417 = Vertex(name = 'V_417',
               particles = [ P.WP__plus__, P.Z, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_418 = Vertex(name = 'V_418',
               particles = [ P.WP__plus__, P.Z, P.WM__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_419 = Vertex(name = 'V_419',
               particles = [ P.WP__plus__, P.Z, P.WM__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_420 = Vertex(name = 'V_420',
               particles = [ P.WP__plus__, P.Z, P.WM__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_421 = Vertex(name = 'V_421',
               particles = [ P.WP__plus__, P.Z, P.WM__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_422 = Vertex(name = 'V_422',
               particles = [ P.WP__plus__, P.Z, P.WZ__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_423 = Vertex(name = 'V_423',
               particles = [ P.WP__plus__, P.Z, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_424 = Vertex(name = 'V_424',
               particles = [ P.WP__plus__, P.Z, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_425 = Vertex(name = 'V_425',
               particles = [ P.WP__plus__, P.Z, P.WZ__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_426 = Vertex(name = 'V_426',
               particles = [ P.WP__plus__, P.Z, P.WZ__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_427 = Vertex(name = 'V_427',
               particles = [ P.WP__plus__, P.Z, P.WZ__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_428 = Vertex(name = 'V_428',
               particles = [ P.WP__plus__, P.Z, P.WZ__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_429 = Vertex(name = 'V_429',
               particles = [ P.WP__plus__, P.ZP, P.W__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_430 = Vertex(name = 'V_430',
               particles = [ P.WP__plus__, P.ZP, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_431 = Vertex(name = 'V_431',
               particles = [ P.WP__plus__, P.ZP, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_432 = Vertex(name = 'V_432',
               particles = [ P.WP__plus__, P.ZP, P.W__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_433 = Vertex(name = 'V_433',
               particles = [ P.WP__plus__, P.ZP, P.W__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_434 = Vertex(name = 'V_434',
               particles = [ P.WP__plus__, P.ZP, P.W__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_435 = Vertex(name = 'V_435',
               particles = [ P.WP__plus__, P.ZP, P.WP__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_436 = Vertex(name = 'V_436',
               particles = [ P.WP__plus__, P.ZP, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_437 = Vertex(name = 'V_437',
               particles = [ P.WP__plus__, P.ZP, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_438 = Vertex(name = 'V_438',
               particles = [ P.WP__plus__, P.ZP, P.WP__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_439 = Vertex(name = 'V_439',
               particles = [ P.WP__plus__, P.ZP, P.WP__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_440 = Vertex(name = 'V_440',
               particles = [ P.WP__plus__, P.ZP, P.WP__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_441 = Vertex(name = 'V_441',
               particles = [ P.WP__plus__, P.ZP, P.WM__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_442 = Vertex(name = 'V_442',
               particles = [ P.WP__plus__, P.ZP, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_443 = Vertex(name = 'V_443',
               particles = [ P.WP__plus__, P.ZP, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_444 = Vertex(name = 'V_444',
               particles = [ P.WP__plus__, P.ZP, P.WM__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_445 = Vertex(name = 'V_445',
               particles = [ P.WP__plus__, P.ZP, P.WM__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_446 = Vertex(name = 'V_446',
               particles = [ P.WP__plus__, P.ZP, P.WM__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_447 = Vertex(name = 'V_447',
               particles = [ P.WP__plus__, P.ZP, P.WZ__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_448 = Vertex(name = 'V_448',
               particles = [ P.WP__plus__, P.ZP, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_449 = Vertex(name = 'V_449',
               particles = [ P.WP__plus__, P.ZP, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_450 = Vertex(name = 'V_450',
               particles = [ P.WP__plus__, P.ZP, P.WZ__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_451 = Vertex(name = 'V_451',
               particles = [ P.WP__plus__, P.ZP, P.WZ__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_452 = Vertex(name = 'V_452',
               particles = [ P.WP__plus__, P.ZP, P.WZ__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_453 = Vertex(name = 'V_453',
               particles = [ P.WP__plus__, P.ZM, P.W__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_454 = Vertex(name = 'V_454',
               particles = [ P.WP__plus__, P.ZM, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_455 = Vertex(name = 'V_455',
               particles = [ P.WP__plus__, P.ZM, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_456 = Vertex(name = 'V_456',
               particles = [ P.WP__plus__, P.ZM, P.W__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_457 = Vertex(name = 'V_457',
               particles = [ P.WP__plus__, P.ZM, P.W__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_458 = Vertex(name = 'V_458',
               particles = [ P.WP__plus__, P.ZM, P.WP__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_459 = Vertex(name = 'V_459',
               particles = [ P.WP__plus__, P.ZM, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_460 = Vertex(name = 'V_460',
               particles = [ P.WP__plus__, P.ZM, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_461 = Vertex(name = 'V_461',
               particles = [ P.WP__plus__, P.ZM, P.WP__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_462 = Vertex(name = 'V_462',
               particles = [ P.WP__plus__, P.ZM, P.WP__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_463 = Vertex(name = 'V_463',
               particles = [ P.WP__plus__, P.ZM, P.WM__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_464 = Vertex(name = 'V_464',
               particles = [ P.WP__plus__, P.ZM, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_465 = Vertex(name = 'V_465',
               particles = [ P.WP__plus__, P.ZM, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_466 = Vertex(name = 'V_466',
               particles = [ P.WP__plus__, P.ZM, P.WM__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_467 = Vertex(name = 'V_467',
               particles = [ P.WP__plus__, P.ZM, P.WM__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_468 = Vertex(name = 'V_468',
               particles = [ P.WP__plus__, P.ZM, P.WZ__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_469 = Vertex(name = 'V_469',
               particles = [ P.WP__plus__, P.ZM, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_470 = Vertex(name = 'V_470',
               particles = [ P.WP__plus__, P.ZM, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_471 = Vertex(name = 'V_471',
               particles = [ P.WP__plus__, P.ZM, P.WZ__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_472 = Vertex(name = 'V_472',
               particles = [ P.WP__plus__, P.ZM, P.WZ__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_473 = Vertex(name = 'V_473',
               particles = [ P.WP__plus__, P.ZZ, P.W__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_474 = Vertex(name = 'V_474',
               particles = [ P.WP__plus__, P.ZZ, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_475 = Vertex(name = 'V_475',
               particles = [ P.WP__plus__, P.ZZ, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_476 = Vertex(name = 'V_476',
               particles = [ P.WP__plus__, P.ZZ, P.W__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_477 = Vertex(name = 'V_477',
               particles = [ P.WP__plus__, P.ZZ, P.WP__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_478 = Vertex(name = 'V_478',
               particles = [ P.WP__plus__, P.ZZ, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_479 = Vertex(name = 'V_479',
               particles = [ P.WP__plus__, P.ZZ, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_480 = Vertex(name = 'V_480',
               particles = [ P.WP__plus__, P.ZZ, P.WP__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_481 = Vertex(name = 'V_481',
               particles = [ P.WP__plus__, P.ZZ, P.WM__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_482 = Vertex(name = 'V_482',
               particles = [ P.WP__plus__, P.ZZ, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_483 = Vertex(name = 'V_483',
               particles = [ P.WP__plus__, P.ZZ, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_484 = Vertex(name = 'V_484',
               particles = [ P.WP__plus__, P.ZZ, P.WM__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_485 = Vertex(name = 'V_485',
               particles = [ P.WP__plus__, P.ZZ, P.WZ__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_486 = Vertex(name = 'V_486',
               particles = [ P.WP__plus__, P.ZZ, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_487 = Vertex(name = 'V_487',
               particles = [ P.WP__plus__, P.ZZ, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_488 = Vertex(name = 'V_488',
               particles = [ P.WP__plus__, P.ZZ, P.WZ__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_489 = Vertex(name = 'V_489',
               particles = [ P.WM__plus__, P.a, P.W__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_490 = Vertex(name = 'V_490',
               particles = [ P.WM__plus__, P.a, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_491 = Vertex(name = 'V_491',
               particles = [ P.WM__plus__, P.a, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_492 = Vertex(name = 'V_492',
               particles = [ P.WM__plus__, P.a, P.WP__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_493 = Vertex(name = 'V_493',
               particles = [ P.WM__plus__, P.a, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_494 = Vertex(name = 'V_494',
               particles = [ P.WM__plus__, P.a, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_495 = Vertex(name = 'V_495',
               particles = [ P.WM__plus__, P.a, P.WM__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_496 = Vertex(name = 'V_496',
               particles = [ P.WM__plus__, P.a, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_497 = Vertex(name = 'V_497',
               particles = [ P.WM__plus__, P.a, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_498 = Vertex(name = 'V_498',
               particles = [ P.WM__plus__, P.a, P.WZ__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_499 = Vertex(name = 'V_499',
               particles = [ P.WM__plus__, P.a, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_500 = Vertex(name = 'V_500',
               particles = [ P.WM__plus__, P.a, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_501 = Vertex(name = 'V_501',
               particles = [ P.WM__plus__, P.aL, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_502 = Vertex(name = 'V_502',
               particles = [ P.WM__plus__, P.aL, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_503 = Vertex(name = 'V_503',
               particles = [ P.WM__plus__, P.aL, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_504 = Vertex(name = 'V_504',
               particles = [ P.WM__plus__, P.aL, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_505 = Vertex(name = 'V_505',
               particles = [ P.WM__plus__, P.aL, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_506 = Vertex(name = 'V_506',
               particles = [ P.WM__plus__, P.aL, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_507 = Vertex(name = 'V_507',
               particles = [ P.WM__plus__, P.aL, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_508 = Vertex(name = 'V_508',
               particles = [ P.WM__plus__, P.aL, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_509 = Vertex(name = 'V_509',
               particles = [ P.WM__plus__, P.aR, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_510 = Vertex(name = 'V_510',
               particles = [ P.WM__plus__, P.aR, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_511 = Vertex(name = 'V_511',
               particles = [ P.WM__plus__, P.aR, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_512 = Vertex(name = 'V_512',
               particles = [ P.WM__plus__, P.aR, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_513 = Vertex(name = 'V_513',
               particles = [ P.WM__plus__, P.Z, P.W__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_514 = Vertex(name = 'V_514',
               particles = [ P.WM__plus__, P.Z, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_515 = Vertex(name = 'V_515',
               particles = [ P.WM__plus__, P.Z, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_516 = Vertex(name = 'V_516',
               particles = [ P.WM__plus__, P.Z, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_517 = Vertex(name = 'V_517',
               particles = [ P.WM__plus__, P.Z, P.W__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_518 = Vertex(name = 'V_518',
               particles = [ P.WM__plus__, P.Z, P.W__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_519 = Vertex(name = 'V_519',
               particles = [ P.WM__plus__, P.Z, P.W__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_520 = Vertex(name = 'V_520',
               particles = [ P.WM__plus__, P.Z, P.WP__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_521 = Vertex(name = 'V_521',
               particles = [ P.WM__plus__, P.Z, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_522 = Vertex(name = 'V_522',
               particles = [ P.WM__plus__, P.Z, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_523 = Vertex(name = 'V_523',
               particles = [ P.WM__plus__, P.Z, P.WP__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_524 = Vertex(name = 'V_524',
               particles = [ P.WM__plus__, P.Z, P.WP__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_525 = Vertex(name = 'V_525',
               particles = [ P.WM__plus__, P.Z, P.WP__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_526 = Vertex(name = 'V_526',
               particles = [ P.WM__plus__, P.Z, P.WP__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_527 = Vertex(name = 'V_527',
               particles = [ P.WM__plus__, P.Z, P.WM__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_528 = Vertex(name = 'V_528',
               particles = [ P.WM__plus__, P.Z, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_529 = Vertex(name = 'V_529',
               particles = [ P.WM__plus__, P.Z, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_530 = Vertex(name = 'V_530',
               particles = [ P.WM__plus__, P.Z, P.WM__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_531 = Vertex(name = 'V_531',
               particles = [ P.WM__plus__, P.Z, P.WM__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_532 = Vertex(name = 'V_532',
               particles = [ P.WM__plus__, P.Z, P.WM__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_533 = Vertex(name = 'V_533',
               particles = [ P.WM__plus__, P.Z, P.WM__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_534 = Vertex(name = 'V_534',
               particles = [ P.WM__plus__, P.Z, P.WZ__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_535 = Vertex(name = 'V_535',
               particles = [ P.WM__plus__, P.Z, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_536 = Vertex(name = 'V_536',
               particles = [ P.WM__plus__, P.Z, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_537 = Vertex(name = 'V_537',
               particles = [ P.WM__plus__, P.Z, P.WZ__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_538 = Vertex(name = 'V_538',
               particles = [ P.WM__plus__, P.Z, P.WZ__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_539 = Vertex(name = 'V_539',
               particles = [ P.WM__plus__, P.Z, P.WZ__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_540 = Vertex(name = 'V_540',
               particles = [ P.WM__plus__, P.Z, P.WZ__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_541 = Vertex(name = 'V_541',
               particles = [ P.WM__plus__, P.ZP, P.W__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_542 = Vertex(name = 'V_542',
               particles = [ P.WM__plus__, P.ZP, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_543 = Vertex(name = 'V_543',
               particles = [ P.WM__plus__, P.ZP, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_544 = Vertex(name = 'V_544',
               particles = [ P.WM__plus__, P.ZP, P.W__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_545 = Vertex(name = 'V_545',
               particles = [ P.WM__plus__, P.ZP, P.W__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_546 = Vertex(name = 'V_546',
               particles = [ P.WM__plus__, P.ZP, P.W__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_547 = Vertex(name = 'V_547',
               particles = [ P.WM__plus__, P.ZP, P.WP__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_548 = Vertex(name = 'V_548',
               particles = [ P.WM__plus__, P.ZP, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_549 = Vertex(name = 'V_549',
               particles = [ P.WM__plus__, P.ZP, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_550 = Vertex(name = 'V_550',
               particles = [ P.WM__plus__, P.ZP, P.WP__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_551 = Vertex(name = 'V_551',
               particles = [ P.WM__plus__, P.ZP, P.WP__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_552 = Vertex(name = 'V_552',
               particles = [ P.WM__plus__, P.ZP, P.WP__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_553 = Vertex(name = 'V_553',
               particles = [ P.WM__plus__, P.ZP, P.WM__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_554 = Vertex(name = 'V_554',
               particles = [ P.WM__plus__, P.ZP, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_555 = Vertex(name = 'V_555',
               particles = [ P.WM__plus__, P.ZP, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_556 = Vertex(name = 'V_556',
               particles = [ P.WM__plus__, P.ZP, P.WM__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_557 = Vertex(name = 'V_557',
               particles = [ P.WM__plus__, P.ZP, P.WM__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_558 = Vertex(name = 'V_558',
               particles = [ P.WM__plus__, P.ZP, P.WM__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_559 = Vertex(name = 'V_559',
               particles = [ P.WM__plus__, P.ZP, P.WZ__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_560 = Vertex(name = 'V_560',
               particles = [ P.WM__plus__, P.ZP, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_561 = Vertex(name = 'V_561',
               particles = [ P.WM__plus__, P.ZP, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_562 = Vertex(name = 'V_562',
               particles = [ P.WM__plus__, P.ZP, P.WZ__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_563 = Vertex(name = 'V_563',
               particles = [ P.WM__plus__, P.ZP, P.WZ__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_564 = Vertex(name = 'V_564',
               particles = [ P.WM__plus__, P.ZP, P.WZ__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_565 = Vertex(name = 'V_565',
               particles = [ P.WM__plus__, P.ZM, P.W__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_566 = Vertex(name = 'V_566',
               particles = [ P.WM__plus__, P.ZM, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_567 = Vertex(name = 'V_567',
               particles = [ P.WM__plus__, P.ZM, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_568 = Vertex(name = 'V_568',
               particles = [ P.WM__plus__, P.ZM, P.W__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_569 = Vertex(name = 'V_569',
               particles = [ P.WM__plus__, P.ZM, P.W__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_570 = Vertex(name = 'V_570',
               particles = [ P.WM__plus__, P.ZM, P.WP__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_571 = Vertex(name = 'V_571',
               particles = [ P.WM__plus__, P.ZM, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_572 = Vertex(name = 'V_572',
               particles = [ P.WM__plus__, P.ZM, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_573 = Vertex(name = 'V_573',
               particles = [ P.WM__plus__, P.ZM, P.WP__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_574 = Vertex(name = 'V_574',
               particles = [ P.WM__plus__, P.ZM, P.WP__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_575 = Vertex(name = 'V_575',
               particles = [ P.WM__plus__, P.ZM, P.WM__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_576 = Vertex(name = 'V_576',
               particles = [ P.WM__plus__, P.ZM, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_577 = Vertex(name = 'V_577',
               particles = [ P.WM__plus__, P.ZM, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_578 = Vertex(name = 'V_578',
               particles = [ P.WM__plus__, P.ZM, P.WM__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_579 = Vertex(name = 'V_579',
               particles = [ P.WM__plus__, P.ZM, P.WM__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_580 = Vertex(name = 'V_580',
               particles = [ P.WM__plus__, P.ZM, P.WZ__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_581 = Vertex(name = 'V_581',
               particles = [ P.WM__plus__, P.ZM, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_582 = Vertex(name = 'V_582',
               particles = [ P.WM__plus__, P.ZM, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_583 = Vertex(name = 'V_583',
               particles = [ P.WM__plus__, P.ZM, P.WZ__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_584 = Vertex(name = 'V_584',
               particles = [ P.WM__plus__, P.ZM, P.WZ__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_585 = Vertex(name = 'V_585',
               particles = [ P.WM__plus__, P.ZZ, P.W__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_586 = Vertex(name = 'V_586',
               particles = [ P.WM__plus__, P.ZZ, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_587 = Vertex(name = 'V_587',
               particles = [ P.WM__plus__, P.ZZ, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_588 = Vertex(name = 'V_588',
               particles = [ P.WM__plus__, P.ZZ, P.W__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_589 = Vertex(name = 'V_589',
               particles = [ P.WM__plus__, P.ZZ, P.WP__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_590 = Vertex(name = 'V_590',
               particles = [ P.WM__plus__, P.ZZ, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_591 = Vertex(name = 'V_591',
               particles = [ P.WM__plus__, P.ZZ, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_592 = Vertex(name = 'V_592',
               particles = [ P.WM__plus__, P.ZZ, P.WP__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_593 = Vertex(name = 'V_593',
               particles = [ P.WM__plus__, P.ZZ, P.WM__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_594 = Vertex(name = 'V_594',
               particles = [ P.WM__plus__, P.ZZ, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_595 = Vertex(name = 'V_595',
               particles = [ P.WM__plus__, P.ZZ, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_596 = Vertex(name = 'V_596',
               particles = [ P.WM__plus__, P.ZZ, P.WM__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_597 = Vertex(name = 'V_597',
               particles = [ P.WM__plus__, P.ZZ, P.WZ__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_598 = Vertex(name = 'V_598',
               particles = [ P.WM__plus__, P.ZZ, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_599 = Vertex(name = 'V_599',
               particles = [ P.WM__plus__, P.ZZ, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_600 = Vertex(name = 'V_600',
               particles = [ P.WM__plus__, P.ZZ, P.WZ__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_601 = Vertex(name = 'V_601',
               particles = [ P.WZ__plus__, P.a, P.W__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_602 = Vertex(name = 'V_602',
               particles = [ P.WZ__plus__, P.a, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_603 = Vertex(name = 'V_603',
               particles = [ P.WZ__plus__, P.a, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_604 = Vertex(name = 'V_604',
               particles = [ P.WZ__plus__, P.a, P.WP__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_605 = Vertex(name = 'V_605',
               particles = [ P.WZ__plus__, P.a, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_606 = Vertex(name = 'V_606',
               particles = [ P.WZ__plus__, P.a, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_607 = Vertex(name = 'V_607',
               particles = [ P.WZ__plus__, P.a, P.WM__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_608 = Vertex(name = 'V_608',
               particles = [ P.WZ__plus__, P.a, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_609 = Vertex(name = 'V_609',
               particles = [ P.WZ__plus__, P.a, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_610 = Vertex(name = 'V_610',
               particles = [ P.WZ__plus__, P.a, P.WZ__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_611 = Vertex(name = 'V_611',
               particles = [ P.WZ__plus__, P.a, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_612 = Vertex(name = 'V_612',
               particles = [ P.WZ__plus__, P.a, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_613 = Vertex(name = 'V_613',
               particles = [ P.WZ__plus__, P.aL, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_614 = Vertex(name = 'V_614',
               particles = [ P.WZ__plus__, P.aL, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_615 = Vertex(name = 'V_615',
               particles = [ P.WZ__plus__, P.aL, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_616 = Vertex(name = 'V_616',
               particles = [ P.WZ__plus__, P.aL, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_617 = Vertex(name = 'V_617',
               particles = [ P.WZ__plus__, P.aL, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_618 = Vertex(name = 'V_618',
               particles = [ P.WZ__plus__, P.aL, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_619 = Vertex(name = 'V_619',
               particles = [ P.WZ__plus__, P.aL, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_620 = Vertex(name = 'V_620',
               particles = [ P.WZ__plus__, P.aL, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_621 = Vertex(name = 'V_621',
               particles = [ P.WZ__plus__, P.aR, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_622 = Vertex(name = 'V_622',
               particles = [ P.WZ__plus__, P.aR, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_623 = Vertex(name = 'V_623',
               particles = [ P.WZ__plus__, P.aR, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_624 = Vertex(name = 'V_624',
               particles = [ P.WZ__plus__, P.aR, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_114})

V_625 = Vertex(name = 'V_625',
               particles = [ P.WZ__plus__, P.Z, P.W__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_626 = Vertex(name = 'V_626',
               particles = [ P.WZ__plus__, P.Z, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_627 = Vertex(name = 'V_627',
               particles = [ P.WZ__plus__, P.Z, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_628 = Vertex(name = 'V_628',
               particles = [ P.WZ__plus__, P.Z, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_629 = Vertex(name = 'V_629',
               particles = [ P.WZ__plus__, P.Z, P.W__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_630 = Vertex(name = 'V_630',
               particles = [ P.WZ__plus__, P.Z, P.W__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_631 = Vertex(name = 'V_631',
               particles = [ P.WZ__plus__, P.Z, P.W__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_632 = Vertex(name = 'V_632',
               particles = [ P.WZ__plus__, P.Z, P.WP__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_633 = Vertex(name = 'V_633',
               particles = [ P.WZ__plus__, P.Z, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_634 = Vertex(name = 'V_634',
               particles = [ P.WZ__plus__, P.Z, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_635 = Vertex(name = 'V_635',
               particles = [ P.WZ__plus__, P.Z, P.WP__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_636 = Vertex(name = 'V_636',
               particles = [ P.WZ__plus__, P.Z, P.WP__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_637 = Vertex(name = 'V_637',
               particles = [ P.WZ__plus__, P.Z, P.WP__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_638 = Vertex(name = 'V_638',
               particles = [ P.WZ__plus__, P.Z, P.WP__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_639 = Vertex(name = 'V_639',
               particles = [ P.WZ__plus__, P.Z, P.WM__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_640 = Vertex(name = 'V_640',
               particles = [ P.WZ__plus__, P.Z, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_641 = Vertex(name = 'V_641',
               particles = [ P.WZ__plus__, P.Z, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_642 = Vertex(name = 'V_642',
               particles = [ P.WZ__plus__, P.Z, P.WM__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_643 = Vertex(name = 'V_643',
               particles = [ P.WZ__plus__, P.Z, P.WM__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_644 = Vertex(name = 'V_644',
               particles = [ P.WZ__plus__, P.Z, P.WM__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_645 = Vertex(name = 'V_645',
               particles = [ P.WZ__plus__, P.Z, P.WM__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_646 = Vertex(name = 'V_646',
               particles = [ P.WZ__plus__, P.Z, P.WZ__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_647 = Vertex(name = 'V_647',
               particles = [ P.WZ__plus__, P.Z, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_648 = Vertex(name = 'V_648',
               particles = [ P.WZ__plus__, P.Z, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_649 = Vertex(name = 'V_649',
               particles = [ P.WZ__plus__, P.Z, P.WZ__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_650 = Vertex(name = 'V_650',
               particles = [ P.WZ__plus__, P.Z, P.WZ__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_651 = Vertex(name = 'V_651',
               particles = [ P.WZ__plus__, P.Z, P.WZ__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_652 = Vertex(name = 'V_652',
               particles = [ P.WZ__plus__, P.Z, P.WZ__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_653 = Vertex(name = 'V_653',
               particles = [ P.WZ__plus__, P.ZP, P.W__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_654 = Vertex(name = 'V_654',
               particles = [ P.WZ__plus__, P.ZP, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_655 = Vertex(name = 'V_655',
               particles = [ P.WZ__plus__, P.ZP, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_656 = Vertex(name = 'V_656',
               particles = [ P.WZ__plus__, P.ZP, P.W__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_657 = Vertex(name = 'V_657',
               particles = [ P.WZ__plus__, P.ZP, P.W__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_658 = Vertex(name = 'V_658',
               particles = [ P.WZ__plus__, P.ZP, P.W__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_659 = Vertex(name = 'V_659',
               particles = [ P.WZ__plus__, P.ZP, P.WP__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_660 = Vertex(name = 'V_660',
               particles = [ P.WZ__plus__, P.ZP, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_661 = Vertex(name = 'V_661',
               particles = [ P.WZ__plus__, P.ZP, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_662 = Vertex(name = 'V_662',
               particles = [ P.WZ__plus__, P.ZP, P.WP__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_663 = Vertex(name = 'V_663',
               particles = [ P.WZ__plus__, P.ZP, P.WP__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_664 = Vertex(name = 'V_664',
               particles = [ P.WZ__plus__, P.ZP, P.WP__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_665 = Vertex(name = 'V_665',
               particles = [ P.WZ__plus__, P.ZP, P.WM__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_666 = Vertex(name = 'V_666',
               particles = [ P.WZ__plus__, P.ZP, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_667 = Vertex(name = 'V_667',
               particles = [ P.WZ__plus__, P.ZP, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_668 = Vertex(name = 'V_668',
               particles = [ P.WZ__plus__, P.ZP, P.WM__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_669 = Vertex(name = 'V_669',
               particles = [ P.WZ__plus__, P.ZP, P.WM__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_670 = Vertex(name = 'V_670',
               particles = [ P.WZ__plus__, P.ZP, P.WM__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_671 = Vertex(name = 'V_671',
               particles = [ P.WZ__plus__, P.ZP, P.WZ__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_672 = Vertex(name = 'V_672',
               particles = [ P.WZ__plus__, P.ZP, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_673 = Vertex(name = 'V_673',
               particles = [ P.WZ__plus__, P.ZP, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_674 = Vertex(name = 'V_674',
               particles = [ P.WZ__plus__, P.ZP, P.WZ__minus__, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_675 = Vertex(name = 'V_675',
               particles = [ P.WZ__plus__, P.ZP, P.WZ__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_676 = Vertex(name = 'V_676',
               particles = [ P.WZ__plus__, P.ZP, P.WZ__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_677 = Vertex(name = 'V_677',
               particles = [ P.WZ__plus__, P.ZM, P.W__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_678 = Vertex(name = 'V_678',
               particles = [ P.WZ__plus__, P.ZM, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_679 = Vertex(name = 'V_679',
               particles = [ P.WZ__plus__, P.ZM, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_680 = Vertex(name = 'V_680',
               particles = [ P.WZ__plus__, P.ZM, P.W__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_681 = Vertex(name = 'V_681',
               particles = [ P.WZ__plus__, P.ZM, P.W__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_682 = Vertex(name = 'V_682',
               particles = [ P.WZ__plus__, P.ZM, P.WP__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_683 = Vertex(name = 'V_683',
               particles = [ P.WZ__plus__, P.ZM, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_684 = Vertex(name = 'V_684',
               particles = [ P.WZ__plus__, P.ZM, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_685 = Vertex(name = 'V_685',
               particles = [ P.WZ__plus__, P.ZM, P.WP__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_686 = Vertex(name = 'V_686',
               particles = [ P.WZ__plus__, P.ZM, P.WP__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_687 = Vertex(name = 'V_687',
               particles = [ P.WZ__plus__, P.ZM, P.WM__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_688 = Vertex(name = 'V_688',
               particles = [ P.WZ__plus__, P.ZM, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_689 = Vertex(name = 'V_689',
               particles = [ P.WZ__plus__, P.ZM, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_690 = Vertex(name = 'V_690',
               particles = [ P.WZ__plus__, P.ZM, P.WM__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_691 = Vertex(name = 'V_691',
               particles = [ P.WZ__plus__, P.ZM, P.WM__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_692 = Vertex(name = 'V_692',
               particles = [ P.WZ__plus__, P.ZM, P.WZ__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_693 = Vertex(name = 'V_693',
               particles = [ P.WZ__plus__, P.ZM, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_694 = Vertex(name = 'V_694',
               particles = [ P.WZ__plus__, P.ZM, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_695 = Vertex(name = 'V_695',
               particles = [ P.WZ__plus__, P.ZM, P.WZ__minus__, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_696 = Vertex(name = 'V_696',
               particles = [ P.WZ__plus__, P.ZM, P.WZ__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_697 = Vertex(name = 'V_697',
               particles = [ P.WZ__plus__, P.ZZ, P.W__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_698 = Vertex(name = 'V_698',
               particles = [ P.WZ__plus__, P.ZZ, P.W__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_699 = Vertex(name = 'V_699',
               particles = [ P.WZ__plus__, P.ZZ, P.W__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_700 = Vertex(name = 'V_700',
               particles = [ P.WZ__plus__, P.ZZ, P.W__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_701 = Vertex(name = 'V_701',
               particles = [ P.WZ__plus__, P.ZZ, P.WP__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_702 = Vertex(name = 'V_702',
               particles = [ P.WZ__plus__, P.ZZ, P.WP__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_703 = Vertex(name = 'V_703',
               particles = [ P.WZ__plus__, P.ZZ, P.WP__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_704 = Vertex(name = 'V_704',
               particles = [ P.WZ__plus__, P.ZZ, P.WP__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_705 = Vertex(name = 'V_705',
               particles = [ P.WZ__plus__, P.ZZ, P.WM__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_706 = Vertex(name = 'V_706',
               particles = [ P.WZ__plus__, P.ZZ, P.WM__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_707 = Vertex(name = 'V_707',
               particles = [ P.WZ__plus__, P.ZZ, P.WM__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_708 = Vertex(name = 'V_708',
               particles = [ P.WZ__plus__, P.ZZ, P.WM__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

V_709 = Vertex(name = 'V_709',
               particles = [ P.WZ__plus__, P.ZZ, P.WZ__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_710 = Vertex(name = 'V_710',
               particles = [ P.WZ__plus__, P.ZZ, P.WZ__minus__, P.aL ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_711 = Vertex(name = 'V_711',
               particles = [ P.WZ__plus__, P.ZZ, P.WZ__minus__, P.aR ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_113})

V_712 = Vertex(name = 'V_712',
               particles = [ P.WZ__plus__, P.ZZ, P.WZ__minus__, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_112})

