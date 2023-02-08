import sys

initialIncSize = sys.argv[1]
totalTime = sys.argv[2]
minIncSize = sys.argv[3]
maxIncSize = sys.argv[4]
dispZ = sys.argv[5]
frequency = sys.argv[6]


inpFile = open("example_rp.inp","w")


inpFile.write("""*Heading
*Preprint, echo=NO, model=NO, history=NO, contact=NO
** *****************************************************************
** PARTS
** *****************************************************************
** always use the default name: Part-1
**
*Part, name=Part-1
**
** **********************************************
** Node information will be read from the following file
** **********************************************
*Include, input=./extractNeperInp/nodeInfo.txt
**
** to declare the RP node
**
11881, 0.0,  0.0,  15.0
**
** ***********************************************
** Element information will be read from the following file
** **********************************************
*Include, input=./extractNeperInp/elementInfo.txt
**
** **********************************************
** list all element sets for each grains and create sections
** for material assignments
** **********************************************
**Grain 89
**
*Include, input=./extractNeperInp/elset_poly89.txt
*Solid Section, elset=poly89,controls=EC-1,material=Properties_poly89
**
**Grain 62
**
*Include, input=./extractNeperInp/elset_poly62.txt
*Solid Section, elset=poly62,controls=EC-1,material=Properties_poly62
**
**Grain 76
**
*Include, input=./extractNeperInp/elset_poly76.txt
*Solid Section, elset=poly76,controls=EC-1,material=Properties_poly76
**
**Grain 77
**
*Include, input=./extractNeperInp/elset_poly77.txt
*Solid Section, elset=poly77,controls=EC-1,material=Properties_poly77
**
**Grain 63
**
*Include, input=./extractNeperInp/elset_poly63.txt
*Solid Section, elset=poly63,controls=EC-1,material=Properties_poly63
**
**Grain 88
**
*Include, input=./extractNeperInp/elset_poly88.txt
*Solid Section, elset=poly88,controls=EC-1,material=Properties_poly88
**
**Grain 49
**
*Include, input=./extractNeperInp/elset_poly49.txt
*Solid Section, elset=poly49,controls=EC-1,material=Properties_poly49
**
**Grain 75
**
*Include, input=./extractNeperInp/elset_poly75.txt
*Solid Section, elset=poly75,controls=EC-1,material=Properties_poly75
**
**Grain 61
**
*Include, input=./extractNeperInp/elset_poly61.txt
*Solid Section, elset=poly61,controls=EC-1,material=Properties_poly61
**
**Grain 100
**
*Include, input=./extractNeperInp/elset_poly100.txt
*Solid Section, elset=poly100,controls=EC-1,material=Properties_poly100
**
**Grain 60
**
*Include, input=./extractNeperInp/elset_poly60.txt
*Solid Section, elset=poly60,controls=EC-1,material=Properties_poly60
**
**Grain 74
**
*Include, input=./extractNeperInp/elset_poly74.txt
*Solid Section, elset=poly74,controls=EC-1,material=Properties_poly74
**
**Grain 48
**
*Include, input=./extractNeperInp/elset_poly48.txt
*Solid Section, elset=poly48,controls=EC-1,material=Properties_poly48
**
**Grain 70
**
*Include, input=./extractNeperInp/elset_poly70.txt
*Solid Section, elset=poly70,controls=EC-1,material=Properties_poly70
**
**Grain 64
**
*Include, input=./extractNeperInp/elset_poly64.txt
*Solid Section, elset=poly64,controls=EC-1,material=Properties_poly64
**
**Grain 58
**
*Include, input=./extractNeperInp/elset_poly58.txt
*Solid Section, elset=poly58,controls=EC-1,material=Properties_poly58
**
**Grain 59
**
*Include, input=./extractNeperInp/elset_poly59.txt
*Solid Section, elset=poly59,controls=EC-1,material=Properties_poly59
**
**Grain 65
**      
*Include, input=./extractNeperInp/elset_poly65.txt
*Solid Section, elset=poly65,controls=EC-1,material=Properties_poly65
**
**Grain 71
**
*Include, input=./extractNeperInp/elset_poly71.txt
*Solid Section, elset=poly71,controls=EC-1,material=Properties_poly71
**
**Grain 98
**
*Include, input=./extractNeperInp/elset_poly98.txt
*Solid Section, elset=poly98,controls=EC-1,material=Properties_poly98
**
**Grain 67
**
*Include, input=./extractNeperInp/elset_poly67.txt
*Solid Section, elset=poly67,controls=EC-1,material=Properties_poly67
**
**Grain 73
**
*Include, input=./extractNeperInp/elset_poly73.txt
*Solid Section, elset=poly73,controls=EC-1,material=Properties_poly73
**
**Grain 72
**
*Include, input=./extractNeperInp/elset_poly72.txt
*Solid Section, elset=poly72,controls=EC-1,material=Properties_poly72
**
**Grain 66
**
*Include, input=./extractNeperInp/elset_poly66.txt
*Solid Section, elset=poly66,controls=EC-1,material=Properties_poly66
**
**Grain 99
**
*Include, input=./extractNeperInp/elset_poly99.txt
*Solid Section, elset=poly99,controls=EC-1,material=Properties_poly99
**
**Grain 6
**
*Include, input=./extractNeperInp/elset_poly6.txt
*Solid Section, elset=poly6,controls=EC-1,material=Properties_poly6
**
**Grain 29
**
*Include, input=./extractNeperInp/elset_poly29.txt
*Solid Section, elset=poly29,controls=EC-1,material=Properties_poly29
**
**Grain 15
**
*Include, input=./extractNeperInp/elset_poly15.txt
*Solid Section, elset=poly15,controls=EC-1,material=Properties_poly15
**
**Grain 14
**
*Include, input=./extractNeperInp/elset_poly14.txt
*Solid Section, elset=poly14,controls=EC-1,material=Properties_poly14
**
**Grain 28
**
*Include, input=./extractNeperInp/elset_poly28.txt
*Solid Section, elset=poly28,controls=EC-1,material=Properties_poly28
**
**Grain 7
**
*Include, input=./extractNeperInp/elset_poly7.txt
*Solid Section, elset=poly7,controls=EC-1,material=Properties_poly7
**
**Grain 5
**
*Include, input=./extractNeperInp/elset_poly5.txt
*Solid Section, elset=poly5,controls=EC-1,material=Properties_poly5
**
**Grain 16
**
*Include, input=./extractNeperInp/elset_poly16.txt
*Solid Section, elset=poly16,controls=EC-1,material=Properties_poly16
**
**Grain 17
**
*Include, input=./extractNeperInp/elset_poly17.txt
*Solid Section, elset=poly17,controls=EC-1,material=Properties_poly17
**
**Grain 4
**
*Include, input=./extractNeperInp/elset_poly4.txt
*Solid Section, elset=poly4,controls=EC-1,material=Properties_poly4
**
**Grain 13
**
*Include, input=./extractNeperInp/elset_poly13.txt
*Solid Section, elset=poly13,controls=EC-1,material=Properties_poly13
**
**Grain 12
**
*Include, input=./extractNeperInp/elset_poly12.txt
*Solid Section, elset=poly12,controls=EC-1,material=Properties_poly12
**
**Grain 1
**
*Include, input=./extractNeperInp/elset_poly1.txt
*Solid Section, elset=poly1,controls=EC-1,material=Properties_poly1
**
**Grain 3
**
*Include, input=./extractNeperInp/elset_poly3.txt
*Solid Section, elset=poly3,controls=EC-1,material=Properties_poly3
**
**Grain 10
**
*Include, input=./extractNeperInp/elset_poly10.txt
*Solid Section, elset=poly10,controls=EC-1,material=Properties_poly10
**
**Grain 38
**
*Include, input=./extractNeperInp/elset_poly38.txt
*Solid Section, elset=poly38,controls=EC-1,material=Properties_poly38
**
**Grain 39
**
*Include, input=./extractNeperInp/elset_poly39.txt
*Solid Section, elset=poly39,controls=EC-1,material=Properties_poly39
**
**Grain 11
**
*Include, input=./extractNeperInp/elset_poly11.txt
*Solid Section, elset=poly11,controls=EC-1,material=Properties_poly11
**
**Grain 2
**
*Include, input=./extractNeperInp/elset_poly2.txt
*Solid Section, elset=poly2,controls=EC-1,material=Properties_poly2
**
**Grain 20
**
*Include, input=./extractNeperInp/elset_poly20.txt
*Solid Section, elset=poly20,controls=EC-1,material=Properties_poly20
**
**Grain 34
**
*Include, input=./extractNeperInp/elset_poly34.txt
*Solid Section, elset=poly34,controls=EC-1,material=Properties_poly34
**
**Grain 35
**
*Include, input=./extractNeperInp/elset_poly35.txt
*Solid Section, elset=poly35,controls=EC-1,material=Properties_poly35
**
**Grain 21
**
*Include, input=./extractNeperInp/elset_poly21.txt
*Solid Section, elset=poly21,controls=EC-1,material=Properties_poly21
**
**Grain 37
**
*Include, input=./extractNeperInp/elset_poly37.txt
*Solid Section, elset=poly37,controls=EC-1,material=Properties_poly37
**
**Grain 23
**
*Include, input=./extractNeperInp/elset_poly23.txt
*Solid Section, elset=poly23,controls=EC-1,material=Properties_poly23
**
**Grain 22
**
*Include, input=./extractNeperInp/elset_poly22.txt
*Solid Section, elset=poly22,controls=EC-1,material=Properties_poly22
**
**Grain 36
**
*Include, input=./extractNeperInp/elset_poly36.txt
*Solid Section, elset=poly36,controls=EC-1,material=Properties_poly36
**
**Grain 9
**
*Include, input=./extractNeperInp/elset_poly9.txt
*Solid Section, elset=poly9,controls=EC-1,material=Properties_poly9
**
**Grain 32
**
*Include, input=./extractNeperInp/elset_poly32.txt
*Solid Section, elset=poly32,controls=EC-1,material=Properties_poly32
**
**Grain 26
**
*Include, input=./extractNeperInp/elset_poly26.txt
*Solid Section, elset=poly26,controls=EC-1,material=Properties_poly26
**
**Grain 27
**
*Include, input=./extractNeperInp/elset_poly27.txt
*Solid Section, elset=poly27,controls=EC-1,material=Properties_poly27
**
**Grain 33
**
*Include, input=./extractNeperInp/elset_poly33.txt
*Solid Section, elset=poly33,controls=EC-1,material=Properties_poly33
**
**Grain 8
**
*Include, input=./extractNeperInp/elset_poly8.txt
*Solid Section, elset=poly8,controls=EC-1,material=Properties_poly8
**
**Grain 25
**
*Include, input=./extractNeperInp/elset_poly25.txt
*Solid Section, elset=poly25,controls=EC-1,material=Properties_poly25
**
**Grain 31
**
*Include, input=./extractNeperInp/elset_poly31.txt
*Solid Section, elset=poly31,controls=EC-1,material=Properties_poly31
**
**Grain 19
**
*Include, input=./extractNeperInp/elset_poly19.txt
*Solid Section, elset=poly19,controls=EC-1,material=Properties_poly19
**
**Grain 18
**
*Include, input=./extractNeperInp/elset_poly18.txt
*Solid Section, elset=poly18,controls=EC-1,material=Properties_poly18
**
**Grain 30
**
*Include, input=./extractNeperInp/elset_poly30.txt
*Solid Section, elset=poly30,controls=EC-1,material=Properties_poly30
**
**Grain 24
**
*Include, input=./extractNeperInp/elset_poly24.txt
*Solid Section, elset=poly24,controls=EC-1,material=Properties_poly24
**
**Grain 80
**
*Include, input=./extractNeperInp/elset_poly80.txt
*Solid Section, elset=poly80,controls=EC-1,material=Properties_poly80
**
**Grain 94
**
*Include, input=./extractNeperInp/elset_poly94.txt
*Solid Section, elset=poly94,controls=EC-1,material=Properties_poly94
**
**Grain 43
**
*Include, input=./extractNeperInp/elset_poly43.txt
*Solid Section, elset=poly43,controls=EC-1,material=Properties_poly43
**
**Grain 57
**
*Include, input=./extractNeperInp/elset_poly57.txt
*Solid Section, elset=poly57,controls=EC-1,material=Properties_poly57
**
**Grain 56
**
*Include, input=./extractNeperInp/elset_poly56.txt
*Solid Section, elset=poly56,controls=EC-1,material=Properties_poly56
**
**Grain 42
**
*Include, input=./extractNeperInp/elset_poly42.txt
*Solid Section, elset=poly42,controls=EC-1,material=Properties_poly42
**
**Grain 95
**
*Include, input=./extractNeperInp/elset_poly95.txt
*Solid Section, elset=poly95,controls=EC-1,material=Properties_poly95
**
**Grain 81
**
*Include, input=./extractNeperInp/elset_poly81.txt
*Solid Section, elset=poly81,controls=EC-1,material=Properties_poly81
**
**Grain 97
**
*Include, input=./extractNeperInp/elset_poly97.txt
*Solid Section, elset=poly97,controls=EC-1,material=Properties_poly97
**
**Grain 83
**
*Include, input=./extractNeperInp/elset_poly83.txt
*Solid Section, elset=poly83,controls=EC-1,material=Properties_poly83
**
**Grain 68
**
*Include, input=./extractNeperInp/elset_poly68.txt
*Solid Section, elset=poly68,controls=EC-1,material=Properties_poly68
**
**Grain 54
**
*Include, input=./extractNeperInp/elset_poly54.txt
*Solid Section, elset=poly54,controls=EC-1,material=Properties_poly54
**
**Grain 40
**
*Include, input=./extractNeperInp/elset_poly40.txt
*Solid Section, elset=poly40,controls=EC-1,material=Properties_poly40
**
**Grain 41
**
*Include, input=./extractNeperInp/elset_poly41.txt
*Solid Section, elset=poly41,controls=EC-1,material=Properties_poly41
**
**Grain 55
**
*Include, input=./extractNeperInp/elset_poly55.txt
*Solid Section, elset=poly55,controls=EC-1,material=Properties_poly55
**
**Grain 69
**
*Include, input=./extractNeperInp/elset_poly69.txt
*Solid Section, elset=poly69,controls=EC-1,material=Properties_poly69
**
**Grain 82
**
*Include, input=./extractNeperInp/elset_poly82.txt
*Solid Section, elset=poly82,controls=EC-1,material=Properties_poly82
**
**Grain 96
**
*Include, input=./extractNeperInp/elset_poly96.txt
*Solid Section, elset=poly96,controls=EC-1,material=Properties_poly96
**
**Grain 92
**
*Include, input=./extractNeperInp/elset_poly92.txt
*Solid Section, elset=poly92,controls=EC-1,material=Properties_poly92
**
**Grain 86
**
*Include, input=./extractNeperInp/elset_poly86.txt
*Solid Section, elset=poly86,controls=EC-1,material=Properties_poly86
**
**Grain 51
**
*Include, input=./extractNeperInp/elset_poly51.txt
*Solid Section, elset=poly51,controls=EC-1,material=Properties_poly51
**
**Grain 45
**
*Include, input=./extractNeperInp/elset_poly45.txt
*Solid Section, elset=poly45,controls=EC-1,material=Properties_poly45
**
**Grain 79
**
*Include, input=./extractNeperInp/elset_poly79.txt
*Solid Section, elset=poly79,controls=EC-1,material=Properties_poly79
**
**Grain 78
**
*Include, input=./extractNeperInp/elset_poly78.txt
*Solid Section, elset=poly78,controls=EC-1,material=Properties_poly78
**
**Grain 44
**
*Include, input=./extractNeperInp/elset_poly44.txt
*Solid Section, elset=poly44,controls=EC-1,material=Properties_poly44
**
**Grain 50
**
*Include, input=./extractNeperInp/elset_poly50.txt
*Solid Section, elset=poly50,controls=EC-1,material=Properties_poly50
**
**Grain 87
**
*Include, input=./extractNeperInp/elset_poly87.txt
*Solid Section, elset=poly87,controls=EC-1,material=Properties_poly87
**
**Grain 93
**
*Include, input=./extractNeperInp/elset_poly93.txt
*Solid Section, elset=poly93,controls=EC-1,material=Properties_poly93
**
**Grain 85
**
*Include, input=./extractNeperInp/elset_poly85.txt
*Solid Section, elset=poly85,controls=EC-1,material=Properties_poly85
**
**Grain 91
**
*Include, input=./extractNeperInp/elset_poly91.txt
*Solid Section, elset=poly91,controls=EC-1,material=Properties_poly91
**
**Grain 46
**
*Include, input=./extractNeperInp/elset_poly46.txt
*Solid Section, elset=poly46,controls=EC-1,material=Properties_poly46
**
**Grain 52
**
*Include, input=./extractNeperInp/elset_poly52.txt
*Solid Section, elset=poly52,controls=EC-1,material=Properties_poly52
**
**Grain 53
**
*Include, input=./extractNeperInp/elset_poly53.txt
*Solid Section, elset=poly53,controls=EC-1,material=Properties_poly53
**
**Grain 47
**
*Include, input=./extractNeperInp/elset_poly47.txt
*Solid Section, elset=poly47,controls=EC-1,material=Properties_poly47
**
**Grain 90
**
*Include, input=./extractNeperInp/elset_poly90.txt
*Solid Section, elset=poly90,controls=EC-1,material=Properties_poly90
**
**Grain 84
**
*Include, input=./extractNeperInp/elset_poly84.txt
*Solid Section, elset=poly84,controls=EC-1,material=Properties_poly84
**
**
*End Part
** *****************************************************************
** ASSEMBLY
** *****************************************************************
*Assembly, name=Assembly
**  
*Instance, name=Part-1-1, part=Part-1
*End Instance
**
**
** list all node sets here by reading from the neper file
**
**
*Include, input=./extractNeperInp/nset_x1.txt
**
*Include, input=./extractNeperInp/nset_x0.txt
**
*Include, input=./extractNeperInp/nset_y0.txt
**
*Include, input=./extractNeperInp/nset_y1.txt
**
*Include, input=./extractNeperInp/nset_z0.txt
**
*Include, input=./extractNeperInp/nset_z1.txt
**
**
** to delcare node set for RP
**
*Nset, nset=disp-load,instance=Part-1-1
11881,
**
** to declare element set and surface set for coupling
** the elset should be z1
*Nset, nset=_s_Surf-3_S2, instance=Part-1-1
11551, 11552, 11553, 11554, 11555, 11556, 11557, 11558, 11559, 11560,
11561, 11562, 11563, 11564, 11565, 11566, 11567, 11568, 11569, 11570,
11571, 11572, 11573, 11574, 11575, 11576, 11577, 11578, 11579, 11580,
11581, 11582, 11583, 11584, 11585, 11586, 11587, 11588, 11589, 11590,
11591, 11592, 11593, 11594, 11595, 11596, 11597, 11598, 11599, 11600,
11601, 11602, 11603, 11604, 11605, 11606, 11607, 11608, 11609, 11610,
11611, 11612, 11613, 11614, 11615, 11616, 11617, 11618, 11619, 11620,
11621, 11622, 11623, 11624, 11625, 11626, 11627, 11628, 11629, 11630,
11631, 11632, 11633, 11634, 11635, 11636, 11637, 11638, 11639, 11640,
11641, 11642, 11643, 11644, 11645, 11646, 11647, 11648, 11649, 11650,
11651, 11652, 11653, 11654, 11655, 11656, 11657, 11658, 11659, 11660,
11661, 11662, 11663, 11664, 11665, 11666, 11667, 11668, 11669, 11670,
11671, 11672, 11673, 11674, 11675, 11676, 11677, 11678, 11679, 11680,
11681, 11682, 11683, 11684, 11685, 11686, 11687, 11688, 11689, 11690,
11691, 11692, 11693, 11694, 11695, 11696, 11697, 11698, 11699, 11700,
11701, 11702, 11703, 11704, 11705, 11706, 11707, 11708, 11709, 11710,
11711, 11712, 11713, 11714, 11715, 11716, 11717, 11718, 11719, 11720,
11721, 11722, 11723, 11724, 11725, 11726, 11727, 11728, 11729, 11730,
11731, 11732, 11733, 11734, 11735, 11736, 11737, 11738, 11739, 11740,
11741, 11742, 11743, 11744, 11745, 11746, 11747, 11748, 11749, 11750,
11751, 11752, 11753, 11754, 11755, 11756, 11757, 11758, 11759, 11760,
11761, 11762, 11763, 11764, 11765, 11766, 11767, 11768, 11769, 11770,
11771, 11772, 11773, 11774, 11775, 11776, 11777, 11778, 11779, 11780,
11781, 11782, 11783, 11784, 11785, 11786, 11787, 11788, 11789, 11790,
11791, 11792, 11793, 11794, 11795, 11796, 11797, 11798, 11799, 11800,
11801, 11802, 11803, 11804, 11805, 11806, 11807, 11808, 11809, 11810,
11811, 11812, 11813, 11814, 11815, 11816, 11817, 11818, 11819, 11820,
11821, 11822, 11823, 11824, 11825, 11826, 11827, 11828, 11829, 11830,
11831, 11832, 11833, 11834, 11835, 11836, 11837, 11838, 11839, 11840,
11841, 11842, 11843, 11844, 11845, 11846, 11847, 11848, 11849, 11850,
11851, 11852, 11853, 11854, 11855, 11856, 11857, 11858, 11859, 11860,
11861, 11862, 11863, 11864, 11865, 11866, 11867, 11868, 11869, 11870,
11871, 11872, 11873, 11874, 11875, 11876, 11877, 11878, 11879, 11880
**
** create surface
*Surface, type=NODE, name=s_Surf-3, internal
_s_Surf-3_S2, 1
**
** to add constraint coupling
**
** Constraint: Constraint-1
*Coupling, constraint name=Constraint-1, ref node=disp-load, surface=s_Surf-3
*Kinematic
**
*End Assembly
**
** ELEMENT CONTROLS
**
*Section Controls, name=EC-1, ELEMENT DELETION=YES
1., 1., 1.
** *****************************************************************
** MATERIALS
** *****************************************************************
**Grain 89 material properties
*Material, name=Properties_poly89
*Include, input=./extractNeperInp/Properties_poly89.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 62 material properties
*Material, name=Properties_poly62
*Include, input=./extractNeperInp/Properties_poly62.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 76 material properties
*Material, name=Properties_poly76
*Include, input=./extractNeperInp/Properties_poly76.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 77 material properties
*Material, name=Properties_poly77
*Include, input=./extractNeperInp/Properties_poly77.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 63 material properties
*Material, name=Properties_poly63
*Include, input=./extractNeperInp/Properties_poly63.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 88 material properties
*Material, name=Properties_poly88
*Include, input=./extractNeperInp/Properties_poly88.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 49 material properties
*Material, name=Properties_poly49
*Include, input=./extractNeperInp/Properties_poly49.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 75 material properties
*Material, name=Properties_poly75
*Include, input=./extractNeperInp/Properties_poly75.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 61 material properties
*Material, name=Properties_poly61
*Include, input=./extractNeperInp/Properties_poly61.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 100 material properties
*Material, name=Properties_poly100
*Include, input=./extractNeperInp/Properties_poly100.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 60 material properties
*Material, name=Properties_poly60
*Include, input=./extractNeperInp/Properties_poly60.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 74 material properties
*Material, name=Properties_poly74
*Include, input=./extractNeperInp/Properties_poly74.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 48 material properties
*Material, name=Properties_poly48
*Include, input=./extractNeperInp/Properties_poly48.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 70 material properties
*Material, name=Properties_poly70
*Include, input=./extractNeperInp/Properties_poly70.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 64 material properties
*Material, name=Properties_poly64
*Include, input=./extractNeperInp/Properties_poly64.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 58 material properties
*Material, name=Properties_poly58
*Include, input=./extractNeperInp/Properties_poly58.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 59 material properties
*Material, name=Properties_poly59
*Include, input=./extractNeperInp/Properties_poly59.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 65 material properties
*Material, name=Properties_poly65
*Include, input=./extractNeperInp/Properties_poly65.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 71 material properties
*Material, name=Properties_poly71
*Include, input=./extractNeperInp/Properties_poly71.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 98 material properties
*Material, name=Properties_poly98
*Include, input=./extractNeperInp/Properties_poly98.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 67 material properties
*Material, name=Properties_poly67
*Include, input=./extractNeperInp/Properties_poly67.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 73 material properties
*Material, name=Properties_poly73
*Include, input=./extractNeperInp/Properties_poly73.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 72 material properties
*Material, name=Properties_poly72
*Include, input=./extractNeperInp/Properties_poly72.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 66 material properties
*Material, name=Properties_poly66
*Include, input=./extractNeperInp/Properties_poly66.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 99 material properties
*Material, name=Properties_poly99
*Include, input=./extractNeperInp/Properties_poly99.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 6 material properties
*Material, name=Properties_poly6
*Include, input=./extractNeperInp/Properties_poly6.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 29 material properties
*Material, name=Properties_poly29
*Include, input=./extractNeperInp/Properties_poly29.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 15 material properties
*Material, name=Properties_poly15
*Include, input=./extractNeperInp/Properties_poly15.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 14 material properties
*Material, name=Properties_poly14
*Include, input=./extractNeperInp/Properties_poly14.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 28 material properties
*Material, name=Properties_poly28
*Include, input=./extractNeperInp/Properties_poly28.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 7 material properties
*Material, name=Properties_poly7
*Include, input=./extractNeperInp/Properties_poly7.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 5 material properties
*Material, name=Properties_poly5
*Include, input=./extractNeperInp/Properties_poly5.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 16 material properties
*Material, name=Properties_poly16
*Include, input=./extractNeperInp/Properties_poly16.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 17 material properties
*Material, name=Properties_poly17
*Include, input=./extractNeperInp/Properties_poly17.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 4 material properties
*Material, name=Properties_poly4
*Include, input=./extractNeperInp/Properties_poly4.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 13 material properties
*Material, name=Properties_poly13
*Include, input=./extractNeperInp/Properties_poly13.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 12 material properties
*Material, name=Properties_poly12
*Include, input=./extractNeperInp/Properties_poly12.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 1 material properties
*Material, name=Properties_poly1
*Include, input=./extractNeperInp/Properties_poly1.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 3 material properties
*Material, name=Properties_poly3
*Include, input=./extractNeperInp/Properties_poly3.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 10 material properties
*Material, name=Properties_poly10
*Include, input=./extractNeperInp/Properties_poly10.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 38 material properties
*Material, name=Properties_poly38
*Include, input=./extractNeperInp/Properties_poly38.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 39 material properties
*Material, name=Properties_poly39
*Include, input=./extractNeperInp/Properties_poly39.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 11 material properties
*Material, name=Properties_poly11
*Include, input=./extractNeperInp/Properties_poly11.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 2 material properties
*Material, name=Properties_poly2
*Include, input=./extractNeperInp/Properties_poly2.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 20 material properties
*Material, name=Properties_poly20
*Include, input=./extractNeperInp/Properties_poly20.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 34 material properties
*Material, name=Properties_poly34
*Include, input=./extractNeperInp/Properties_poly34.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 35 material properties
*Material, name=Properties_poly35
*Include, input=./extractNeperInp/Properties_poly35.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 21 material properties
*Material, name=Properties_poly21
*Include, input=./extractNeperInp/Properties_poly21.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 37 material properties
*Material, name=Properties_poly37
*Include, input=./extractNeperInp/Properties_poly37.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 23 material properties
*Material, name=Properties_poly23
*Include, input=./extractNeperInp/Properties_poly23.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 22 material properties
*Material, name=Properties_poly22
*Include, input=./extractNeperInp/Properties_poly22.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 36 material properties
*Material, name=Properties_poly36
*Include, input=./extractNeperInp/Properties_poly36.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 9 material properties
*Material, name=Properties_poly9
*Include, input=./extractNeperInp/Properties_poly9.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 32 material properties
*Material, name=Properties_poly32
*Include, input=./extractNeperInp/Properties_poly32.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 26 material properties
*Material, name=Properties_poly26
*Include, input=./extractNeperInp/Properties_poly26.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 27 material properties
*Material, name=Properties_poly27
*Include, input=./extractNeperInp/Properties_poly27.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 33 material properties
*Material, name=Properties_poly33
*Include, input=./extractNeperInp/Properties_poly33.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 8 material properties
*Material, name=Properties_poly8
*Include, input=./extractNeperInp/Properties_poly8.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 25 material properties
*Material, name=Properties_poly25
*Include, input=./extractNeperInp/Properties_poly25.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 31 material properties
*Material, name=Properties_poly31
*Include, input=./extractNeperInp/Properties_poly31.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 19 material properties
*Material, name=Properties_poly19
*Include, input=./extractNeperInp/Properties_poly19.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 18 material properties
*Material, name=Properties_poly18
*Include, input=./extractNeperInp/Properties_poly18.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 30 material properties
*Material, name=Properties_poly30
*Include, input=./extractNeperInp/Properties_poly30.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 24 material properties
*Material, name=Properties_poly24
*Include, input=./extractNeperInp/Properties_poly24.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 80 material properties
*Material, name=Properties_poly80
*Include, input=./extractNeperInp/Properties_poly80.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 94 material properties
*Material, name=Properties_poly94
*Include, input=./extractNeperInp/Properties_poly94.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 43 material properties
*Material, name=Properties_poly43
*Include, input=./extractNeperInp/Properties_poly43.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 57 material properties
*Material, name=Properties_poly57
*Include, input=./extractNeperInp/Properties_poly57.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 56 material properties
*Material, name=Properties_poly56
*Include, input=./extractNeperInp/Properties_poly56.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 42 material properties
*Material, name=Properties_poly42
*Include, input=./extractNeperInp/Properties_poly42.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 95 material properties
*Material, name=Properties_poly95
*Include, input=./extractNeperInp/Properties_poly95.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 81 material properties
*Material, name=Properties_poly81
*Include, input=./extractNeperInp/Properties_poly81.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 97 material properties
*Material, name=Properties_poly97
*Include, input=./extractNeperInp/Properties_poly97.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 83 material properties
*Material, name=Properties_poly83
*Include, input=./extractNeperInp/Properties_poly83.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 68 material properties
*Material, name=Properties_poly68
*Include, input=./extractNeperInp/Properties_poly68.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 54 material properties
*Material, name=Properties_poly54
*Include, input=./extractNeperInp/Properties_poly54.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 40 material properties
*Material, name=Properties_poly40
*Include, input=./extractNeperInp/Properties_poly40.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 41 material properties
*Material, name=Properties_poly41
*Include, input=./extractNeperInp/Properties_poly41.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 55 material properties
*Material, name=Properties_poly55
*Include, input=./extractNeperInp/Properties_poly55.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 69 material properties
*Material, name=Properties_poly69
*Include, input=./extractNeperInp/Properties_poly69.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 82 material properties
*Material, name=Properties_poly82
*Include, input=./extractNeperInp/Properties_poly82.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 96 material properties
*Material, name=Properties_poly96
*Include, input=./extractNeperInp/Properties_poly96.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 92 material properties
*Material, name=Properties_poly92
*Include, input=./extractNeperInp/Properties_poly92.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 86 material properties
*Material, name=Properties_poly86
*Include, input=./extractNeperInp/Properties_poly86.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 51 material properties
*Material, name=Properties_poly51
*Include, input=./extractNeperInp/Properties_poly51.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 45 material properties
*Material, name=Properties_poly45
*Include, input=./extractNeperInp/Properties_poly45.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 79 material properties
*Material, name=Properties_poly79
*Include, input=./extractNeperInp/Properties_poly79.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 78 material properties
*Material, name=Properties_poly78
*Include, input=./extractNeperInp/Properties_poly78.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 44 material properties
*Material, name=Properties_poly44
*Include, input=./extractNeperInp/Properties_poly44.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 50 material properties
*Material, name=Properties_poly50
*Include, input=./extractNeperInp/Properties_poly50.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 87 material properties
*Material, name=Properties_poly87
*Include, input=./extractNeperInp/Properties_poly87.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 93 material properties
*Material, name=Properties_poly93
*Include, input=./extractNeperInp/Properties_poly93.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 85 material properties
*Material, name=Properties_poly85
*Include, input=./extractNeperInp/Properties_poly85.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 91 material properties
*Material, name=Properties_poly91
*Include, input=./extractNeperInp/Properties_poly91.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 46 material properties
*Material, name=Properties_poly46
*Include, input=./extractNeperInp/Properties_poly46.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 52 material properties
*Material, name=Properties_poly52
*Include, input=./extractNeperInp/Properties_poly52.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 53 material properties
*Material, name=Properties_poly53
*Include, input=./extractNeperInp/Properties_poly53.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 47 material properties
*Material, name=Properties_poly47
*Include, input=./extractNeperInp/Properties_poly47.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 90 material properties
*Material, name=Properties_poly90
*Include, input=./extractNeperInp/Properties_poly90.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**Grain 84 material properties
*Material, name=Properties_poly84
*Include, input=./extractNeperInp/Properties_poly84.inc
**
**
** 127 - 5 = 122
*DEPVAR,delete=122
127
**  number of state dependent variables, must be larger than (or equal
**  to) ten times total number of slip systems in all sets, plus
**  five, plus the additional number of state variables users
**  introduced for their own single crystal model
**
**   For example, {110}<111> has twelve slip systems.  There are
**   12*10+5=113 state dependent variables.
** ----------------------------------------------------------------
**
** ********************************************************************
** STEP: Step-1
** ********************************************************************
*Step, name=Step-1, nlgeom=YES, inc=100000000
*Static
"""+str(initialIncSize)+""", """+str(totalTime)+""", """+str(minIncSize)+""", """+str(maxIncSize)+"""
**
** BOUNDARY CONDITIONS
**
** for example, bottom edge maybe x0 node sets,
**              top edge maybe x1 node sets
** this should be checked carefully
**
** Name: BC-1 Type: Symmetry/Antisymmetry/Encastre
*Boundary
z0, ENCASTRE
** Name: BC-2 Type: Displacement/Rotation
** *Boundary
** z1, 1, 1
** z1, 2, 2
** z1, 3, 3, 4.0
** z1, 4, 4
** z1, 5, 5
** z1, 6, 6
*Boundary
disp-load, 1,1
disp-load, 2,2
disp-load, 3,3,"""+str(dispZ)+"""
disp-load, 4,4
disp-load, 5,5
disp-load, 6,6
**
** OUTPUT REQUESTS
**
*Restart, write, frequency=0
**
** FIELD OUTPUT: F-Output-1
**
*Output, field, frequency="""+str(frequency)+"""
*Node Output
CF, RF, U
*Element Output, directions=YES
LE, PE, PEEQ, PEMAG, S, SDV, STATUS
*Contact Output
CDISP, CSTRESS
**
** HISTORY OUTPUT: load-disp
**
*Output, history
*Node Output, nset=disp-load
RF3, U3
** HISTORY OUTPUT: H-Output-1
**
*Output, history, variable=PRESELECT
*End Step
""")

inpFile.close()