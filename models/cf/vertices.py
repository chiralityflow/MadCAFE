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

