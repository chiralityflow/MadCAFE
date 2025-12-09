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

#SS: Including Higgs to the 3 boson vertex.

V_737 = Vertex(name = 'V_737',
               particles = [ P.W__plus__, P.W__plus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_115})

V_738 = Vertex(name = 'V_738',
               particles = [ P.W__plus__, P.WP__plus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_115})

V_739 = Vertex(name = 'V_739',
               particles = [ P.W__plus__, P.WM__plus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_115})

V_740 = Vertex(name = 'V_740',
               particles = [ P.W__plus__, P.WZ__plus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_115})

V_741 = Vertex(name = 'V_741',
               particles = [ P.WP__plus__, P.WP__plus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_115})

V_742 = Vertex(name = 'V_742',
               particles = [ P.WP__plus__, P.WM__plus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_115})

V_743 = Vertex(name = 'V_743',
               particles = [ P.WP__plus__, P.WZ__plus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_115})

V_744 = Vertex(name = 'V_744',
               particles = [ P.WM__plus__, P.WM__plus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_115})

V_745 = Vertex(name = 'V_745',
               particles = [ P.WM__plus__, P.WZ__plus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_115})

V_746 = Vertex(name = 'V_746',
               particles = [ P.WZ__plus__, P.WZ__plus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_115})

V_747 = Vertex(name = 'V_747',
               particles = [ P.W__minus__, P.W__minus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_115})

V_748 = Vertex(name = 'V_748',
               particles = [ P.W__minus__, P.WP__minus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_115})

V_749 = Vertex(name = 'V_749',
               particles = [ P.W__minus__, P.WM__minus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_115})

V_750 = Vertex(name = 'V_750',
               particles = [ P.W__minus__, P.WZ__minus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_115})

V_751 = Vertex(name = 'V_751',
               particles = [ P.WP__minus__, P.WP__minus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_115})

V_752 = Vertex(name = 'V_752',
               particles = [ P.WP__minus__, P.WM__minus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_115})

V_753 = Vertex(name = 'V_753',
               particles = [ P.WP__minus__, P.WZ__minus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_115})

V_754 = Vertex(name = 'V_754',
               particles = [ P.WM__minus__, P.WM__minus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_115})

V_755 = Vertex(name = 'V_755',
               particles = [ P.WM__minus__, P.WZ__minus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_115})

V_756 = Vertex(name = 'V_756',
               particles = [ P.WZ__minus__, P.WZ__minus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_115})

V_757 = Vertex(name = 'V_757',
               particles = [ P.Z, P.Z, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_116})

V_758 = Vertex(name = 'V_758',
               particles = [ P.Z, P.ZP, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_116})

V_759 = Vertex(name = 'V_759',
               particles = [ P.Z, P.ZM, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_116})

V_760 = Vertex(name = 'V_760',
               particles = [ P.Z, P.ZZ, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_116})

V_761 = Vertex(name = 'V_761',
               particles = [ P.ZP, P.ZP, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_116})

V_762 = Vertex(name = 'V_762',
               particles = [ P.ZP, P.ZM, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_116})

V_763 = Vertex(name = 'V_763',
               particles = [ P.ZP, P.ZZ, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_116})

V_764 = Vertex(name = 'V_764',
               particles = [ P.ZM, P.ZM, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_116})

V_765 = Vertex(name = 'V_765',
               particles = [ P.ZM, P.ZZ, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_116})

V_766 = Vertex(name = 'V_766',
               particles = [ P.ZZ, P.ZZ, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_116})

V_767 = Vertex(name = 'V_767',
               particles = [ P.h, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_117})
               
# Including higgs in 4 boson vertex.

V_768 = Vertex(name = 'V_768',
               particles = [ P.W__plus__, P.W__minus__, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_118})

V_769 = Vertex(name = 'V_769',
               particles = [ P.W__plus__, P.WP__minus__, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_118})

V_770 = Vertex(name = 'V_770',
               particles = [ P.W__plus__, P.WM__minus__, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_118})

V_771 = Vertex(name = 'V_771',
               particles = [ P.W__plus__, P.WZ__minus__, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_118})

V_772 = Vertex(name = 'V_772',
               particles = [ P.WP__plus__, P.W__minus__, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_118})

V_773 = Vertex(name = 'V_773',
               particles = [ P.WP__plus__, P.WP__minus__, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_118})

V_774 = Vertex(name = 'V_774',
               particles = [ P.WP__plus__, P.WM__minus__, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_118})

V_775 = Vertex(name = 'V_775',
               particles = [ P.WP__plus__, P.WZ__minus__, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_118})

V_776 = Vertex(name = 'V_776',
               particles = [ P.WM__plus__, P.W__minus__, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_118})

V_777 = Vertex(name = 'V_777',
               particles = [ P.WM__plus__, P.WP__minus__, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_118})

V_778 = Vertex(name = 'V_778',
               particles = [ P.WM__plus__, P.WM__minus__, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_118})

V_779 = Vertex(name = 'V_779',
               particles = [ P.WM__plus__, P.WZ__minus__, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_118})

V_780 = Vertex(name = 'V_780',
               particles = [ P.WZ__plus__, P.W__minus__, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_118})

V_781 = Vertex(name = 'V_781',
               particles = [ P.WZ__plus__, P.WP__minus__, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_118})

V_782 = Vertex(name = 'V_782',
               particles = [ P.WZ__plus__, P.WM__minus__, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_118})

V_783 = Vertex(name = 'V_783',
               particles = [ P.WZ__plus__, P.WZ__minus__, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_118})

V_784 = Vertex(name = 'V_784',
               particles = [ P.Z, P.Z, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_119})

V_785 = Vertex(name = 'V_785',
               particles = [ P.Z, P.ZP, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_119})

V_786 = Vertex(name = 'V_786',
               particles = [ P.Z, P.ZM, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_119})

V_787 = Vertex(name = 'V_787',
               particles = [ P.Z, P.ZZ, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_119})

V_788 = Vertex(name = 'V_788',
               particles = [ P.ZP, P.ZP, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_119})

V_789 = Vertex(name = 'V_789',
               particles = [ P.ZP, P.ZM, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_119})

V_790 = Vertex(name = 'V_790',
               particles = [ P.ZP, P.ZZ, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_119})

V_791 = Vertex(name = 'V_791',
               particles = [ P.ZM, P.ZM, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_119})

V_792 = Vertex(name = 'V_792',
               particles = [ P.ZM, P.ZZ, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_119})

V_793 = Vertex(name = 'V_793',
               particles = [ P.ZZ, P.ZZ, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_119})

V_794 = Vertex(name = 'V_794',
               particles = [ P.h, P.h, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_120})

# All Neutrino Vertices

V_795 = Vertex(name = 'V_795',
               particles = [ P.veR__tilde__, P.eL__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_240})

V_796 = Vertex(name = 'V_796',
               particles = [ P.veR__tilde__, P.eL__minus__, P.WP__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_240})

V_797 = Vertex(name = 'V_797',
               particles = [ P.veR__tilde__, P.eL__minus__, P.WM__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_240})

V_798 = Vertex(name = 'V_798',
               particles = [ P.veR__tilde__, P.eL__minus__, P.WZ__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_240})

V_799 = Vertex(name = 'V_799',
               particles = [ P.eR__plus__, P.veL, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_240})

V_800 = Vertex(name = 'V_800',
               particles = [ P.eR__plus__, P.veL, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_240})

V_801 = Vertex(name = 'V_801',
               particles = [ P.eR__plus__, P.veL, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_240})
               
V_802 = Vertex(name = 'V_802',
               particles = [ P.eR__plus__, P.veL, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_240})

V_803 = Vertex(name = 'V_803',
               particles = [ P.veR__tilde__, P.veL, P.Z ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_262})

V_804 = Vertex(name = 'V_804',
               particles = [ P.veR__tilde__, P.veL, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_262})

V_805 = Vertex(name = 'V_805',
               particles = [ P.veR__tilde__, P.veL, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_262})

V_806 = Vertex(name = 'V_806',
               particles = [ P.veR__tilde__, P.veL, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_262})

V_807 = Vertex(name = 'V_807',
               particles = [ P.vmR__tilde__, P.muL__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_240})

V_808 = Vertex(name = 'V_808',
               particles = [ P.vmR__tilde__, P.muL__minus__, P.WP__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_240})

V_809 = Vertex(name = 'V_809',
               particles = [ P.vmR__tilde__, P.muL__minus__, P.WM__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_240})

V_810 = Vertex(name = 'V_810',
               particles = [ P.vmR__tilde__, P.muL__minus__, P.WZ__plus__ ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_240})

V_811 = Vertex(name = 'V_811',
               particles = [ P.muR__plus__, P.vmL, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_240})

V_812 = Vertex(name = 'V_812',
               particles = [ P.muR__plus__, P.vmL, P.WP__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_240})

V_813 = Vertex(name = 'V_813',
               particles = [ P.muR__plus__, P.vmL, P.WM__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_240})
               
V_814 = Vertex(name = 'V_814',
               particles = [ P.muR__plus__, P.vmL, P.WZ__minus__ ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_240})

V_815 = Vertex(name = 'V_815',
               particles = [ P.vmR__tilde__, P.vmL, P.Z ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_262})

V_816 = Vertex(name = 'V_816',
               particles = [ P.vmR__tilde__, P.vmL, P.ZP ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_262})

V_817 = Vertex(name = 'V_817',
               particles = [ P.vmR__tilde__, P.vmL, P.ZM ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_262})

V_818 = Vertex(name = 'V_818',
               particles = [ P.vmR__tilde__, P.vmL, P.ZZ ],
               color = [ '1' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_262})

# SS: Including Goldstone Boson Vertices

V_819 = Vertex(name = 'V_819',
             particles = [ P.G0, P.G0, P.G0, P.G0 ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_33})

V_820 = Vertex(name = 'V_820',
             particles = [ P.G0, P.G0, P.G__minus__, P.G__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_31})
             
V_821 = Vertex(name = 'V_821',
             particles = [ P.G0, P.G0, P.h, P.h ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_31})

V_822 = Vertex(name = 'V_822',
             particles = [ P.G0, P.G0, P.h ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_68})

V_823 = Vertex(name = 'V_823',
              particles = [ P.a, P.W__minus__, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_824 = Vertex(name = 'V_824',
              particles = [ P.a, P.WZ__minus__, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_825 = Vertex(name = 'V_825',
              particles = [ P.a, P.WP__minus__, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_826 = Vertex(name = 'V_826',
              particles = [ P.a, P.WM__minus__, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_827 = Vertex(name = 'V_827',
              particles = [ P.aL, P.W__minus__, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_828 = Vertex(name = 'V_828',
              particles = [ P.aL, P.WZ__minus__, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_829 = Vertex(name = 'V_829',
              particles = [ P.aL, P.WP__minus__, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_830 = Vertex(name = 'V_830',
              particles = [ P.aL, P.WM__minus__, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_831 = Vertex(name = 'V_831',
              particles = [ P.aR, P.W__minus__, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_832 = Vertex(name = 'V_832',
              particles = [ P.aR, P.WZ__minus__, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_833 = Vertex(name = 'V_833',
              particles = [ P.aR, P.WP__minus__, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_834 = Vertex(name = 'V_834',
              particles = [ P.aR, P.WM__minus__, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_835 = Vertex(name = 'V_835',
              particles = [ P.a, P.W__minus__, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_54})

V_836 = Vertex(name = 'V_836',
              particles = [ P.a, P.WZ__minus__, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_54})

V_837 = Vertex(name = 'V_837',
              particles = [ P.a, P.WP__minus__, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_54})

V_838 = Vertex(name = 'V_838',
              particles = [ P.a, P.WM__minus__, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_54})

V_839 = Vertex(name = 'V_839',
              particles = [ P.aL, P.W__minus__, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_54})

V_840 = Vertex(name = 'V_840',
              particles = [ P.aL, P.WZ__minus__, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_54})

V_841 = Vertex(name = 'V_841',
              particles = [ P.aL, P.WP__minus__, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_54})

V_842 = Vertex(name = 'V_842',
              particles = [ P.aL, P.WM__minus__, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_54})

V_843 = Vertex(name = 'V_843',
              particles = [ P.aR, P.W__minus__, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_54})

V_844 = Vertex(name = 'V_844',
              particles = [ P.aR, P.WZ__minus__, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_54})

V_845 = Vertex(name = 'V_845',
              particles = [ P.aR, P.WP__minus__, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_54})

V_846 = Vertex(name = 'V_846',
              particles = [ P.aR, P.WM__minus__, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_54})

V_847 = Vertex(name = 'V_847',
              particles = [ P.W__minus__, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_39})

V_848 = Vertex(name = 'V_848',
              particles = [ P.WZ__minus__, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_39})

V_849 = Vertex(name = 'V_849',
              particles = [ P.WP__minus__, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_39})

V_850 = Vertex(name = 'V_850',
              particles = [ P.WM__minus__, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_39})

V_851 = Vertex(name = 'V_851',
              particles = [ P.W__minus__, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_37})

V_852 = Vertex(name = 'V_852',
              particles = [ P.WZ__minus__, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_37})

V_853 = Vertex(name = 'V_853',
              particles = [ P.WP__minus__, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_37})

V_854 = Vertex(name = 'V_854',
              particles = [ P.WM__minus__, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_37})

V_855 = Vertex(name = 'V_855',
              particles = [ P.a, P.W__plus__, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_856 = Vertex(name = 'V_856',
              particles = [ P.a, P.WZ__plus__, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_857 = Vertex(name = 'V_857',
              particles = [ P.a, P.WP__plus__, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_858 = Vertex(name = 'V_858',
              particles = [ P.a, P.WM__plus__, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_859 = Vertex(name = 'V_859',
              particles = [ P.aL, P.W__plus__, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_860 = Vertex(name = 'V_860',
              particles = [ P.aL, P.WZ__plus__, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_861 = Vertex(name = 'V_861',
              particles = [ P.aL, P.WP__plus__, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_862 = Vertex(name = 'V_862',
              particles = [ P.aL, P.WM__plus__, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_863 = Vertex(name = 'V_863',
              particles = [ P.aR, P.W__plus__, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_864 = Vertex(name = 'V_864',
              particles = [ P.aR, P.WZ__plus__, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_865 = Vertex(name = 'V_865',
              particles = [ P.aR, P.WP__plus__, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_866 = Vertex(name = 'V_866',
              particles = [ P.aR, P.WM__plus__, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_55})

V_867 = Vertex(name = 'V_867',
              particles = [ P.a, P.W__plus__, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_56})

V_868 = Vertex(name = 'V_868',
              particles = [ P.a, P.WZ__plus__, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_56})

V_869 = Vertex(name = 'V_869',
              particles = [ P.a, P.WP__plus__, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_56})

V_870 = Vertex(name = 'V_870',
              particles = [ P.a, P.WM__plus__, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_56})

V_871 = Vertex(name = 'V_871',
              particles = [ P.aL, P.W__plus__, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_56})

V_872 = Vertex(name = 'V_872',
              particles = [ P.aL, P.WZ__plus__, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_56})

V_873 = Vertex(name = 'V_873',
              particles = [ P.aL, P.WP__plus__, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_56})

V_874 = Vertex(name = 'V_874',
              particles = [ P.aL, P.WM__plus__, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_56})

V_875 = Vertex(name = 'V_875',
              particles = [ P.aR, P.W__plus__, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_56})

V_876 = Vertex(name = 'V_876',
              particles = [ P.aR, P.WZ__plus__, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_56})

V_877 = Vertex(name = 'V_877',
              particles = [ P.aR, P.WP__plus__, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_56})

V_878 = Vertex(name = 'V_878',
              particles = [ P.aR, P.WM__plus__, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_56})

V_879 = Vertex(name = 'V_879',
              particles = [ P.a, P.W__plus__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_75})

V_880 = Vertex(name = 'V_880',
              particles = [ P.a, P.WZ__plus__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_75})

V_881 = Vertex(name = 'V_881',
              particles = [ P.a, P.WP__plus__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_75})

V_882 = Vertex(name = 'V_882',
              particles = [ P.a, P.WM__plus__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_75})

V_883 = Vertex(name = 'V_883',
              particles = [ P.aL, P.W__plus__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_75})

V_884 = Vertex(name = 'V_884',
              particles = [ P.aL, P.WZ__plus__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_75})

V_885 = Vertex(name = 'V_885',
              particles = [ P.aL, P.WP__plus__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_75})

V_886 = Vertex(name = 'V_886',
              particles = [ P.aL, P.WM__plus__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_75})

V_887 = Vertex(name = 'V_887',
              particles = [ P.aR, P.W__plus__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_75})

V_888 = Vertex(name = 'V_888',
              particles = [ P.aR, P.WZ__plus__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_75})

V_889 = Vertex(name = 'V_889',
              particles = [ P.aR, P.WP__plus__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_75})

V_890 = Vertex(name = 'V_890',
              particles = [ P.aR, P.WM__plus__, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_75})

V_891 = Vertex(name = 'V_891',
              particles = [ P.W__plus__, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_38})

V_892 = Vertex(name = 'V_892',
              particles = [ P.WZ__plus__, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_38})

V_893 = Vertex(name = 'V_893',
              particles = [ P.WP__plus__, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_38})

V_894 = Vertex(name = 'V_894',
              particles = [ P.WM__plus__, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_38})

V_895 = Vertex(name = 'V_895',
              particles = [ P.W__plus__, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_37})

V_896 = Vertex(name = 'V_896',
              particles = [ P.WZ__plus__, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_37})

V_897 = Vertex(name = 'V_897',
              particles = [ P.WP__plus__, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_37})

V_898 = Vertex(name = 'V_898',
              particles = [ P.WM__plus__, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_37})

V_899 = Vertex(name = 'V_899',
              particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_900 = Vertex(name = 'V_900',
              particles = [ P.W__minus__, P.WZ__plus__, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_901 = Vertex(name = 'V_901',
              particles = [ P.W__minus__, P.WP__plus__, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_902 = Vertex(name = 'V_902',
              particles = [ P.W__minus__, P.WM__plus__, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_903 = Vertex(name = 'V_903',
              particles = [ P.WZ__minus__, P.W__plus__, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_904 = Vertex(name = 'V_904',
              particles = [ P.WZ__minus__, P.WZ__plus__, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_905 = Vertex(name = 'V_905',
              particles = [ P.WZ__minus__, P.WP__plus__, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_906 = Vertex(name = 'V_906',
              particles = [ P.WZ__minus__, P.WM__plus__, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_907 = Vertex(name = 'V_907',
              particles = [ P.WP__minus__, P.W__plus__, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_908 = Vertex(name = 'V_908',
              particles = [ P.WP__minus__, P.WZ__plus__, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_909 = Vertex(name = 'V_909',
              particles = [ P.WP__minus__, P.WP__plus__, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_910 = Vertex(name = 'V_910',
              particles = [ P.WP__minus__, P.WM__plus__, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_911 = Vertex(name = 'V_911',
              particles = [ P.WM__minus__, P.W__plus__, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_912 = Vertex(name = 'V_912',
              particles = [ P.WM__minus__, P.WZ__plus__, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_913 = Vertex(name = 'V_913',
              particles = [ P.WM__minus__, P.WP__plus__, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_914 = Vertex(name = 'V_914',
              particles = [ P.WM__minus__, P.WM__plus__, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_915 = Vertex(name = 'V_915',
              particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_916 = Vertex(name = 'V_916',
              particles = [ P.W__minus__, P.WZ__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_917 = Vertex(name = 'V_917',
              particles = [ P.W__minus__, P.WP__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_918 = Vertex(name = 'V_918',
              particles = [ P.W__minus__, P.WM__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_919 = Vertex(name = 'V_919',
              particles = [ P.WZ__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_920 = Vertex(name = 'V_920',
              particles = [ P.WZ__minus__, P.WZ__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_921 = Vertex(name = 'V_921',
              particles = [ P.WZ__minus__, P.WP__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_922 = Vertex(name = 'V_922',
              particles = [ P.WZ__minus__, P.WM__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_923 = Vertex(name = 'V_923',
              particles = [ P.WP__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_924 = Vertex(name = 'V_924',
              particles = [ P.WP__minus__, P.WZ__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_925 = Vertex(name = 'V_925',
              particles = [ P.WP__minus__, P.WP__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_926 = Vertex(name = 'V_926',
              particles = [ P.WP__minus__, P.WM__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_927 = Vertex(name = 'V_927',
              particles = [ P.WM__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_928 = Vertex(name = 'V_928',
              particles = [ P.WM__minus__, P.WZ__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_929 = Vertex(name = 'V_929',
              particles = [ P.WM__minus__, P.WP__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_930 = Vertex(name = 'V_930',
              particles = [ P.WM__minus__, P.WM__plus__, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_34})

V_931 = Vertex(name = 'V_931',
              particles = [ P.a, P.Z, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_63})

V_932 = Vertex(name = 'V_932',
              particles = [ P.a, P.ZZ, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_63})

V_933 = Vertex(name = 'V_933',
              particles = [ P.a, P.ZP, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_63})

V_934 = Vertex(name = 'V_934',
              particles = [ P.a, P.ZM, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_63})

V_935 = Vertex(name = 'V_935',
              particles = [ P.aL, P.Z, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_63})

V_936 = Vertex(name = 'V_936',
              particles = [ P.aL, P.ZZ, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_63})

V_937 = Vertex(name = 'V_937',
              particles = [ P.aL, P.ZP, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_63})

V_938 = Vertex(name = 'V_938',
              particles = [ P.aL, P.ZM, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_63})

V_939 = Vertex(name = 'V_939',
              particles = [ P.aR, P.Z, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_63})

V_940 = Vertex(name = 'V_940',
              particles = [ P.aR, P.ZZ, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_63})

V_941 = Vertex(name = 'V_941',
              particles = [ P.aR, P.ZP, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_63})

V_942 = Vertex(name = 'V_942',
              particles = [ P.aR, P.ZM, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_63})

V_943 = Vertex(name = 'V_943',
              particles = [ P.Z, P.G0, P.h ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_60})

V_944 = Vertex(name = 'V_944',
              particles = [ P.ZZ, P.G0, P.h ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_60})

V_945 = Vertex(name = 'V_945',
              particles = [ P.ZP, P.G0, P.h ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_60})

V_946 = Vertex(name = 'V_946',
              particles = [ P.ZM, P.G0, P.h ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_60})

V_947 = Vertex(name = 'V_947',
              particles = [ P.Z, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_61})

V_948 = Vertex(name = 'V_948',
              particles = [ P.ZZ, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_61})

V_949 = Vertex(name = 'V_949',
              particles = [ P.ZP, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_61})

V_950 = Vertex(name = 'V_950',
              particles = [ P.ZM, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_61})

V_951 = Vertex(name = 'V_951',
              particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_952 = Vertex(name = 'V_952',
              particles = [ P.W__minus__, P.ZZ, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_953 = Vertex(name = 'V_953',
              particles = [ P.W__minus__, P.ZP, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_954 = Vertex(name = 'V_954',
              particles = [ P.W__minus__, P.ZM, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_955 = Vertex(name = 'V_955',
              particles = [ P.WZ__minus__, P.Z, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_956 = Vertex(name = 'V_956',
              particles = [ P.WZ__minus__, P.ZZ, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_957 = Vertex(name = 'V_957',
              particles = [ P.WZ__minus__, P.ZP, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_958 = Vertex(name = 'V_958',
              particles = [ P.WZ__minus__, P.ZM, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_959 = Vertex(name = 'V_959',
              particles = [ P.WP__minus__, P.Z, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_960 = Vertex(name = 'V_960',
              particles = [ P.WP__minus__, P.ZZ, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_961 = Vertex(name = 'V_961',
              particles = [ P.WP__minus__, P.ZP, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_962 = Vertex(name = 'V_962',
              particles = [ P.WP__minus__, P.ZM, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_963 = Vertex(name = 'V_963',
              particles = [ P.WM__minus__, P.Z, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_964 = Vertex(name = 'V_964',
              particles = [ P.WM__minus__, P.ZZ, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_965 = Vertex(name = 'V_965',
              particles = [ P.WM__minus__, P.ZP, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_966 = Vertex(name = 'V_966',
              particles = [ P.WM__minus__, P.ZM, P.G0, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_967 = Vertex(name = 'V_967',
              particles = [ P.W__minus__, P.Z, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_968 = Vertex(name = 'V_968',
              particles = [ P.W__minus__, P.ZZ, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_969 = Vertex(name = 'V_969',
              particles = [ P.W__minus__, P.ZP, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_970 = Vertex(name = 'V_970',
              particles = [ P.W__minus__, P.ZM, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_971 = Vertex(name = 'V_971',
              particles = [ P.WZ__minus__, P.Z, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_972 = Vertex(name = 'V_972',
              particles = [ P.WZ__minus__, P.ZZ, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_973 = Vertex(name = 'V_973',
              particles = [ P.WZ__minus__, P.ZP, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_974 = Vertex(name = 'V_974',
              particles = [ P.WZ__minus__, P.ZM, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_975 = Vertex(name = 'V_975',
              particles = [ P.WP__minus__, P.Z, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_976 = Vertex(name = 'V_976',
              particles = [ P.WP__minus__, P.ZZ, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_977 = Vertex(name = 'V_977',
              particles = [ P.WP__minus__, P.ZP, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_978 = Vertex(name = 'V_978',
              particles = [ P.WP__minus__, P.ZM, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_979 = Vertex(name = 'V_979',
              particles = [ P.WM__minus__, P.Z, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_980 = Vertex(name = 'V_980',
              particles = [ P.WM__minus__, P.ZZ, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_981 = Vertex(name = 'V_981',
              particles = [ P.WM__minus__, P.ZP, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_982 = Vertex(name = 'V_982',
              particles = [ P.WM__minus__, P.ZM, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_983 = Vertex(name = 'V_983',
              particles = [ P.W__minus__, P.Z, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_67})

V_984 = Vertex(name = 'V_984',
              particles = [ P.W__minus__, P.ZZ, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_67})

V_985 = Vertex(name = 'V_985',
              particles = [ P.W__minus__, P.ZP, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_67})

V_986 = Vertex(name = 'V_986',
              particles = [ P.W__minus__, P.ZM, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_67})

V_987 = Vertex(name = 'V_987',
              particles = [ P.WZ__minus__, P.Z, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_67})

V_988 = Vertex(name = 'V_988',
              particles = [ P.WZ__minus__, P.ZZ, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_67})

V_989 = Vertex(name = 'V_989',
              particles = [ P.WZ__minus__, P.ZP, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_67})

V_990 = Vertex(name = 'V_990',
              particles = [ P.WZ__minus__, P.ZM, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_67})

V_991 = Vertex(name = 'V_991',
              particles = [ P.WP__minus__, P.Z, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_67})

V_992 = Vertex(name = 'V_992',
              particles = [ P.WP__minus__, P.ZZ, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_67})

V_993 = Vertex(name = 'V_993',
              particles = [ P.WP__minus__, P.ZP, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_67})

V_994 = Vertex(name = 'V_994',
              particles = [ P.WP__minus__, P.ZM, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_67})

V_995 = Vertex(name = 'V_995',
              particles = [ P.WM__minus__, P.Z, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_67})

V_996 = Vertex(name = 'V_996',
              particles = [ P.WM__minus__, P.ZZ, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_67})

V_997 = Vertex(name = 'V_997',
              particles = [ P.WM__minus__, P.ZP, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_67})

V_998 = Vertex(name = 'V_998',
              particles = [ P.WM__minus__, P.ZM, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_67})

V_999 = Vertex(name = 'V_999',
              particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_1000 = Vertex(name = 'V_1000',
              particles = [ P.W__plus__, P.ZZ, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_1001 = Vertex(name = 'V_1001',
              particles = [ P.W__plus__, P.ZP, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_1002 = Vertex(name = 'V_1002',
              particles = [ P.W__plus__, P.ZM, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_1003 = Vertex(name = 'V_1003',
              particles = [ P.WZ__plus__, P.Z, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_1004 = Vertex(name = 'V_1004',
              particles = [ P.WZ__plus__, P.ZZ, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_1005 = Vertex(name = 'V_1005',
              particles = [ P.WZ__plus__, P.ZP, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_1006 = Vertex(name = 'V_1006',
              particles = [ P.WZ__plus__, P.ZM, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_1007 = Vertex(name = 'V_1007',
              particles = [ P.WP__plus__, P.Z, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_1008 = Vertex(name = 'V_1008',
              particles = [ P.WP__plus__, P.ZZ, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_1009 = Vertex(name = 'V_1009',
              particles = [ P.WP__plus__, P.ZP, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_1010 = Vertex(name = 'V_1010',
              particles = [ P.WP__plus__, P.ZM, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_1011 = Vertex(name = 'V_1011',
              particles = [ P.WM__plus__, P.Z, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_1012 = Vertex(name = 'V_1012',
              particles = [ P.WM__plus__, P.ZZ, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_1013 = Vertex(name = 'V_1013',
              particles = [ P.WM__plus__, P.ZP, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_1014 = Vertex(name = 'V_1014',
              particles = [ P.WM__plus__, P.ZM, P.G0, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_1015 = Vertex(name = 'V_1015',
              particles = [ P.W__plus__, P.Z, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_7})

V_1016 = Vertex(name = 'V_1016',
              particles = [ P.W__plus__, P.ZZ, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_7})

V_1017 = Vertex(name = 'V_1017',
              particles = [ P.W__plus__, P.ZP, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_7})

V_1018 = Vertex(name = 'V_1018',
              particles = [ P.W__plus__, P.ZM, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_7})

V_1019 = Vertex(name = 'V_1019',
              particles = [ P.WZ__plus__, P.Z, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_7})

V_1020 = Vertex(name = 'V_1020',
              particles = [ P.WZ__plus__, P.ZZ, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_7})

V_1021 = Vertex(name = 'V_1021',
              particles = [ P.WZ__plus__, P.ZP, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_7})

V_1022 = Vertex(name = 'V_1022',
              particles = [ P.WZ__plus__, P.ZM, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_7})

V_1023 = Vertex(name = 'V_1023',
              particles = [ P.WP__plus__, P.Z, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_7})

V_1024 = Vertex(name = 'V_1024',
              particles = [ P.WP__plus__, P.ZZ, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_7})

V_1025 = Vertex(name = 'V_1025',
              particles = [ P.WP__plus__, P.ZP, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_7})

V_1026 = Vertex(name = 'V_1026',
              particles = [ P.WP__plus__, P.ZM, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_7})

V_1027 = Vertex(name = 'V_1027',
              particles = [ P.WM__plus__, P.Z, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_7})

V_1028 = Vertex(name = 'V_1028',
              particles = [ P.WM__plus__, P.ZZ, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_7})

V_1029 = Vertex(name = 'V_1029',
              particles = [ P.WM__plus__, P.ZP, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_7})

V_1030 = Vertex(name = 'V_1030',
              particles = [ P.WM__plus__, P.ZM, P.G__minus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_7})

V_1031 = Vertex(name = 'V_1031',
              particles = [ P.W__plus__, P.Z, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_66})

V_1032 = Vertex(name = 'V_1032',
              particles = [ P.W__plus__, P.ZZ, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_66})

V_1033 = Vertex(name = 'V_1033',
              particles = [ P.W__plus__, P.ZP, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_66})

V_1034 = Vertex(name = 'V_1034',
              particles = [ P.W__plus__, P.ZM, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_66})

V_1035 = Vertex(name = 'V_1035',
              particles = [ P.WZ__plus__, P.Z, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_66})

V_1036 = Vertex(name = 'V_1036',
              particles = [ P.WZ__plus__, P.ZZ, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_66})

V_1037 = Vertex(name = 'V_1037',
              particles = [ P.WZ__plus__, P.ZP, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_66})

V_1038 = Vertex(name = 'V_1038',
              particles = [ P.WZ__plus__, P.ZM, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_66})

V_1039 = Vertex(name = 'V_1039',
              particles = [ P.WP__plus__, P.Z, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_66})

V_1040 = Vertex(name = 'V_1040',
              particles = [ P.WP__plus__, P.ZZ, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_66})

V_1041 = Vertex(name = 'V_1041',
              particles = [ P.WP__plus__, P.ZP, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_66})

V_1042 = Vertex(name = 'V_1042',
              particles = [ P.WP__plus__, P.ZM, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_66})

V_1043 = Vertex(name = 'V_1043',
              particles = [ P.WM__plus__, P.Z, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_66})

V_1044 = Vertex(name = 'V_1044',
              particles = [ P.WM__plus__, P.ZZ, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_66})

V_1045 = Vertex(name = 'V_1045',
              particles = [ P.WM__plus__, P.ZP, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_66})

V_1046 = Vertex(name = 'V_1046',
              particles = [ P.WM__plus__, P.ZM, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_66})

V_1047 = Vertex(name = 'V_1047',
              particles = [ P.Z, P.Z, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_65})

V_1048 = Vertex(name = 'V_1048',
              particles = [ P.Z, P.ZZ, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_65})

V_1049 = Vertex(name = 'V_1049',
              particles = [ P.Z, P.ZP, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_65})

V_1050 = Vertex(name = 'V_1050',
              particles = [ P.Z, P.ZM, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_65})

V_1051 = Vertex(name = 'V_1051',
              particles = [ P.ZZ, P.ZZ, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_65})

V_1052 = Vertex(name = 'V_1052',
              particles = [ P.ZZ, P.ZP, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_65})

V_1053 = Vertex(name = 'V_1053',
              particles = [ P.ZZ, P.ZM, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_65})

V_1054 = Vertex(name = 'V_1054',
              particles = [ P.ZP, P.ZP, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_65})

V_1055 = Vertex(name = 'V_1055',
              particles = [ P.ZP, P.ZM, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_65})

V_1056 = Vertex(name = 'V_1056',
              particles = [ P.ZM, P.ZM, P.G0, P.G0 ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_65})

V_1057 = Vertex(name = 'V_1057',
              particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_64})

V_1058 = Vertex(name = 'V_1058',
              particles = [ P.Z, P.ZZ, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_64})

V_1059 = Vertex(name = 'V_1059',
              particles = [ P.Z, P.ZP, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_64})

V_1060 = Vertex(name = 'V_1060',
              particles = [ P.Z, P.ZM, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_64})

V_1061 = Vertex(name = 'V_1061',
              particles = [ P.ZZ, P.ZZ, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_64})

V_1062 = Vertex(name = 'V_1062',
              particles = [ P.ZZ, P.ZP, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_64})

V_1063 = Vertex(name = 'V_1063',
              particles = [ P.ZZ, P.ZM, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_64})

V_1064 = Vertex(name = 'V_1064',
              particles = [ P.ZP, P.ZP, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_64})

V_1065 = Vertex(name = 'V_1065',
              particles = [ P.ZP, P.ZM, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_64})

V_1066 = Vertex(name = 'V_1066',
              particles = [ P.ZM, P.ZM, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_64})

V_1091 = Vertex(name = 'V_1091',
             particles = [ P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_32})

V_1092 = Vertex(name = 'V_1092',
             particles = [ P.G__minus__, P.G__plus__, P.h, P.h ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_31})

V_1093 = Vertex(name = 'V_1093',
             particles = [ P.G__minus__, P.G__plus__, P.h ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_68})

V_1094 = Vertex(name = 'V_1094',
              particles = [ P.a, P.a, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_6})

V_1095 = Vertex(name = 'V_1095',
              particles = [ P.a, P.aL, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_6})

V_1096 = Vertex(name = 'V_1096',
              particles = [ P.a, P.aR, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_6})

V_1097 = Vertex(name = 'V_1097',
              particles = [ P.aL, P.aL, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_6})

V_1098 = Vertex(name = 'V_1098',
              particles = [ P.aL, P.aR, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_6})

V_1099 = Vertex(name = 'V_1099',
              particles = [ P.aR, P.aR, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_6})

V_1100 = Vertex(name = 'V_1100',
              particles = [ P.a, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_3})

V_1101 = Vertex(name = 'V_1101',
              particles = [ P.aL, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_3})

V_1102 = Vertex(name = 'V_1102',
              particles = [ P.aR, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_3})
