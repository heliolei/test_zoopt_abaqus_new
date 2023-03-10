from driverConstants import *
from driverStandardMPI import StandardMPIAnalysis
import driverUtils, sys
options = {
    'SIMExt':'.sim',
    'ams':OFF,
    'analysisType':STANDARD,
    'applicationName':'analysis',
    'aqua':OFF,
    'beamSectGen':OFF,
    'biorid':OFF,
    'cavityTypes':[],
    'cavparallel':OFF,
    'complexFrequency':OFF,
    'contact':OFF,
    'cosimulation':OFF,
    'coupledProcedure':OFF,
    'cpus':100,
    'cse':OFF,
    'cyclicSymmetryModel':OFF,
    'directCyclic':OFF,
    'direct_solver':DMP,
    'dsa':OFF,
    'dynStepSenseAdj':OFF,
    'dynamic':OFF,
    'dynamic_load_balancing':ON,
    'fieldImport':OFF,
    'fieldImportExtList':['.sim', '.SMAManifest'],
    'fieldImportFiles':[],
    'filPrt':[],
    'fils':[],
    'finitesliding':OFF,
    'flexiblebody':OFF,
    'foundation':OFF,
    'geostatic':OFF,
    'geotech':OFF,
    'heatTransfer':OFF,
    'impJobExpVars':{},
    'importJobList':[],
    'importer':OFF,
    'importerParts':OFF,
    'includes':['./extractNeperInp/nodeInfo.txt', './extractNeperInp/elementInfo.txt', './extractNeperInp/elset_poly89.txt', './extractNeperInp/elset_poly62.txt', './extractNeperInp/elset_poly76.txt', './extractNeperInp/elset_poly77.txt', './extractNeperInp/elset_poly63.txt', './extractNeperInp/elset_poly88.txt', './extractNeperInp/elset_poly49.txt', './extractNeperInp/elset_poly75.txt', './extractNeperInp/elset_poly61.txt', './extractNeperInp/elset_poly100.txt', './extractNeperInp/elset_poly60.txt', './extractNeperInp/elset_poly74.txt', './extractNeperInp/elset_poly48.txt', './extractNeperInp/elset_poly70.txt', './extractNeperInp/elset_poly64.txt', './extractNeperInp/elset_poly58.txt', './extractNeperInp/elset_poly59.txt', './extractNeperInp/elset_poly65.txt', './extractNeperInp/elset_poly71.txt', './extractNeperInp/elset_poly98.txt', './extractNeperInp/elset_poly67.txt', './extractNeperInp/elset_poly73.txt', './extractNeperInp/elset_poly72.txt', './extractNeperInp/elset_poly66.txt', './extractNeperInp/elset_poly99.txt', './extractNeperInp/elset_poly6.txt', './extractNeperInp/elset_poly29.txt', './extractNeperInp/elset_poly15.txt', './extractNeperInp/elset_poly14.txt', './extractNeperInp/elset_poly28.txt', './extractNeperInp/elset_poly7.txt', './extractNeperInp/elset_poly5.txt', './extractNeperInp/elset_poly16.txt', './extractNeperInp/elset_poly17.txt', './extractNeperInp/elset_poly4.txt', './extractNeperInp/elset_poly13.txt', './extractNeperInp/elset_poly12.txt', './extractNeperInp/elset_poly1.txt', './extractNeperInp/elset_poly3.txt', './extractNeperInp/elset_poly10.txt', './extractNeperInp/elset_poly38.txt', './extractNeperInp/elset_poly39.txt', './extractNeperInp/elset_poly11.txt', './extractNeperInp/elset_poly2.txt', './extractNeperInp/elset_poly20.txt', './extractNeperInp/elset_poly34.txt', './extractNeperInp/elset_poly35.txt', './extractNeperInp/elset_poly21.txt', './extractNeperInp/elset_poly37.txt', './extractNeperInp/elset_poly23.txt', './extractNeperInp/elset_poly22.txt', './extractNeperInp/elset_poly36.txt', './extractNeperInp/elset_poly9.txt', './extractNeperInp/elset_poly32.txt', './extractNeperInp/elset_poly26.txt', './extractNeperInp/elset_poly27.txt', './extractNeperInp/elset_poly33.txt', './extractNeperInp/elset_poly8.txt', './extractNeperInp/elset_poly25.txt', './extractNeperInp/elset_poly31.txt', './extractNeperInp/elset_poly19.txt', './extractNeperInp/elset_poly18.txt', './extractNeperInp/elset_poly30.txt', './extractNeperInp/elset_poly24.txt', './extractNeperInp/elset_poly80.txt', './extractNeperInp/elset_poly94.txt', './extractNeperInp/elset_poly43.txt', './extractNeperInp/elset_poly57.txt', './extractNeperInp/elset_poly56.txt', './extractNeperInp/elset_poly42.txt', './extractNeperInp/elset_poly95.txt', './extractNeperInp/elset_poly81.txt', './extractNeperInp/elset_poly97.txt', './extractNeperInp/elset_poly83.txt', './extractNeperInp/elset_poly68.txt', './extractNeperInp/elset_poly54.txt', './extractNeperInp/elset_poly40.txt', './extractNeperInp/elset_poly41.txt', './extractNeperInp/elset_poly55.txt', './extractNeperInp/elset_poly69.txt', './extractNeperInp/elset_poly82.txt', './extractNeperInp/elset_poly96.txt', './extractNeperInp/elset_poly92.txt', './extractNeperInp/elset_poly86.txt', './extractNeperInp/elset_poly51.txt', './extractNeperInp/elset_poly45.txt', './extractNeperInp/elset_poly79.txt', './extractNeperInp/elset_poly78.txt', './extractNeperInp/elset_poly44.txt', './extractNeperInp/elset_poly50.txt', './extractNeperInp/elset_poly87.txt', './extractNeperInp/elset_poly93.txt', './extractNeperInp/elset_poly85.txt', './extractNeperInp/elset_poly91.txt', './extractNeperInp/elset_poly46.txt', './extractNeperInp/elset_poly52.txt', './extractNeperInp/elset_poly53.txt', './extractNeperInp/elset_poly47.txt', './extractNeperInp/elset_poly90.txt', './extractNeperInp/elset_poly84.txt', './extractNeperInp/nset_x1.txt', './extractNeperInp/nset_x0.txt', './extractNeperInp/nset_y0.txt', './extractNeperInp/nset_y1.txt', './extractNeperInp/nset_z0.txt', './extractNeperInp/nset_z1.txt', './extractNeperInp/Properties_poly89.inc', './extractNeperInp/Properties_poly62.inc', './extractNeperInp/Properties_poly76.inc', './extractNeperInp/Properties_poly77.inc', './extractNeperInp/Properties_poly63.inc', './extractNeperInp/Properties_poly88.inc', './extractNeperInp/Properties_poly49.inc', './extractNeperInp/Properties_poly75.inc', './extractNeperInp/Properties_poly61.inc', './extractNeperInp/Properties_poly100.inc', './extractNeperInp/Properties_poly60.inc', './extractNeperInp/Properties_poly74.inc', './extractNeperInp/Properties_poly48.inc', './extractNeperInp/Properties_poly70.inc', './extractNeperInp/Properties_poly64.inc', './extractNeperInp/Properties_poly58.inc', './extractNeperInp/Properties_poly59.inc', './extractNeperInp/Properties_poly65.inc', './extractNeperInp/Properties_poly71.inc', './extractNeperInp/Properties_poly98.inc', './extractNeperInp/Properties_poly67.inc', './extractNeperInp/Properties_poly73.inc', './extractNeperInp/Properties_poly72.inc', './extractNeperInp/Properties_poly66.inc', './extractNeperInp/Properties_poly99.inc', './extractNeperInp/Properties_poly6.inc', './extractNeperInp/Properties_poly29.inc', './extractNeperInp/Properties_poly15.inc', './extractNeperInp/Properties_poly14.inc', './extractNeperInp/Properties_poly28.inc', './extractNeperInp/Properties_poly7.inc', './extractNeperInp/Properties_poly5.inc', './extractNeperInp/Properties_poly16.inc', './extractNeperInp/Properties_poly17.inc', './extractNeperInp/Properties_poly4.inc', './extractNeperInp/Properties_poly13.inc', './extractNeperInp/Properties_poly12.inc', './extractNeperInp/Properties_poly1.inc', './extractNeperInp/Properties_poly3.inc', './extractNeperInp/Properties_poly10.inc', './extractNeperInp/Properties_poly38.inc', './extractNeperInp/Properties_poly39.inc', './extractNeperInp/Properties_poly11.inc', './extractNeperInp/Properties_poly2.inc', './extractNeperInp/Properties_poly20.inc', './extractNeperInp/Properties_poly34.inc', './extractNeperInp/Properties_poly35.inc', './extractNeperInp/Properties_poly21.inc', './extractNeperInp/Properties_poly37.inc', './extractNeperInp/Properties_poly23.inc', './extractNeperInp/Properties_poly22.inc', './extractNeperInp/Properties_poly36.inc', './extractNeperInp/Properties_poly9.inc', './extractNeperInp/Properties_poly32.inc', './extractNeperInp/Properties_poly26.inc', './extractNeperInp/Properties_poly27.inc', './extractNeperInp/Properties_poly33.inc', './extractNeperInp/Properties_poly8.inc', './extractNeperInp/Properties_poly25.inc', './extractNeperInp/Properties_poly31.inc', './extractNeperInp/Properties_poly19.inc', './extractNeperInp/Properties_poly18.inc', './extractNeperInp/Properties_poly30.inc', './extractNeperInp/Properties_poly24.inc', './extractNeperInp/Properties_poly80.inc', './extractNeperInp/Properties_poly94.inc', './extractNeperInp/Properties_poly43.inc', './extractNeperInp/Properties_poly57.inc', './extractNeperInp/Properties_poly56.inc', './extractNeperInp/Properties_poly42.inc', './extractNeperInp/Properties_poly95.inc', './extractNeperInp/Properties_poly81.inc', './extractNeperInp/Properties_poly97.inc', './extractNeperInp/Properties_poly83.inc', './extractNeperInp/Properties_poly68.inc', './extractNeperInp/Properties_poly54.inc', './extractNeperInp/Properties_poly40.inc', './extractNeperInp/Properties_poly41.inc', './extractNeperInp/Properties_poly55.inc', './extractNeperInp/Properties_poly69.inc', './extractNeperInp/Properties_poly82.inc', './extractNeperInp/Properties_poly96.inc', './extractNeperInp/Properties_poly92.inc', './extractNeperInp/Properties_poly86.inc', './extractNeperInp/Properties_poly51.inc', './extractNeperInp/Properties_poly45.inc', './extractNeperInp/Properties_poly79.inc', './extractNeperInp/Properties_poly78.inc', './extractNeperInp/Properties_poly44.inc', './extractNeperInp/Properties_poly50.inc', './extractNeperInp/Properties_poly87.inc', './extractNeperInp/Properties_poly93.inc', './extractNeperInp/Properties_poly85.inc', './extractNeperInp/Properties_poly91.inc', './extractNeperInp/Properties_poly46.inc', './extractNeperInp/Properties_poly52.inc', './extractNeperInp/Properties_poly53.inc', './extractNeperInp/Properties_poly47.inc', './extractNeperInp/Properties_poly90.inc', './extractNeperInp/Properties_poly84.inc'],
    'initialConditionsFile':OFF,
    'input':'example',
    'inputFormat':INP,
    'interpolExtList':['.odb', '.sim', '.SMAManifest'],
    'job':'example',
    'keyword_licenses':[],
    'lanczos':OFF,
    'libs':[],
    'magnetostatic':OFF,
    'massDiffusion':OFF,
    'materialresponse':OFF,
    'modifiedTet':OFF,
    'moldflowFiles':[],
    'moldflowMaterial':OFF,
    'mp_file_system':(DETECT, DETECT),
    'mp_head_node':('ps.lan', 'ps', '192.168.50.50', 'ip6-localhost'),
    'mp_host_list':(('ps', 100),),
    'mp_mode':MPI,
    'mp_mode_requested':MPI,
    'mp_mpi_validate':OFF,
    'mp_mpirun_path':'/home/cailei/usr/SIMULIA/EstProducts/2020/linux_a64/code/bin/SMAExternal/pmpi/bin/mpirun',
    'mp_rsh_command':'ssh -n -l cailei %H %C',
    'multiphysics':OFF,
    'noDmpDirect':[],
    'noMultiHost':[],
    'noMultiHostElemLoop':[],
    'no_domain_check':1,
    'outputKeywords':ON,
    'parameterized':OFF,
    'partsAndAssemblies':ON,
    'parval':OFF,
    'pgdHeatTransfer':OFF,
    'postOutput':OFF,
    'preDecomposition':ON,
    'restart':OFF,
    'restartEndStep':OFF,
    'restartIncrement':0,
    'restartStep':0,
    'restartWrite':OFF,
    'rezone':OFF,
    'runCalculator':OFF,
    'simPack':OFF,
    'soils':OFF,
    'soliter':OFF,
    'solverTypes':['DIRECT'],
    'standard_parallel':ALL,
    'staticNonlinear':ON,
    'steadyStateTransport':OFF,
    'step':ON,
    'stepSenseAdj':OFF,
    'stressExtList':['.odb', '.sim', '.SMAManifest'],
    'subGen':OFF,
    'subGenLibs':[],
    'subGenTypes':[],
    'submodel':OFF,
    'substrLibDefs':OFF,
    'substructure':OFF,
    'symmetricModelGeneration':OFF,
    'tempNoInterpolExtList':['.fil', '.odb', '.sim', '.SMAManifest'],
    'thermal':OFF,
    'tmpdir':'/tmp',
    'tracer':OFF,
    'transientSensitivity':OFF,
    'unfold_param':OFF,
    'unsymm':OFF,
    'user':'umat.f',
    'visco':OFF,
    'xplSelect':OFF,
}
analysis = StandardMPIAnalysis(options)
status = analysis.run()
sys.exit(status)
