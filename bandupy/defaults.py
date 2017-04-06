# Copyright (C) 2017 Paulo V. C. Medeiros
# A python wrapper to BandUP and its plotting tool
# This file is part of BandUP: Band Unfolding code for Plane-wave based calculations.
#
# BandUP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
#  BandUP is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with BandUP.  If not, see <http://www.gnu.org/licenses/>.
import glob
import os
# Imports from within the package
from .warnings_wrapper import warnings
from .constants import WORKING_DIR

defaults = {}


defaults['bandup_raw_out_files'] = {
    'symmetry_avgd':'unfolded_EBS_symmetry-averaged.dat',
    'not_symmetry_avgd':'unfolded_EBS_not-symmetry_averaged.dat'
}


step2dir = {'step_1':'self_consist_calc', 'step_2':'pre_unfolding',
            'step_3':'wavefunc_calc'}
for step, d in step2dir.iteritems():
    try:
        # If the user executes the script inside the "step_4*" dir (or similar dir level)
        tentative_dir=glob.glob(os.path.join(os.path.dirname(WORKING_DIR),'%s*'%(step)))
        tentative_dir = tentative_dir[0]
    except(IndexError):
        try:
            # If the user executes the script at the dir containing the "step_*" dirs
            tentative_dir=glob.glob(os.path.join(WORKING_DIR,'%s*'%(step)))
            tentative_dir = tentative_dir[0]
        except(IndexError):
            tentative_dir = None
    defaults['%s_dir'%(d)] = tentative_dir

defaults['pre_unfolding_inputs_dir'] = None
if(defaults['pre_unfolding_dir'] is not None):
    defaults['pre_unfolding_inputs_dir'] = (
        os.path.join(defaults['pre_unfolding_dir'], 'input_files')
    )

defaults['results_dir'] = WORKING_DIR
defaults['plot_dir'] = WORKING_DIR
defaults['pckpts_file'] = 'KPOINTS_prim_cell.in'
defaults['out_sckpts_file'] = 'KPOINTS_supercell.out'
defaults['pc_file'] = 'prim_cell_lattice.in'
defaults['sc_file'] = 'supercell_lattice.in'

#for k,v in defaults.iteritems():
#    if(v is None):
#        warnings.warn('Could not set a valid default for "%s".'%(k))
