
import numpy as np
import sympy as sm
from pydy.models import n_link_pendulum_on_cart
from opty.direct_collocation import Problem, ConstraintCollocator

sys = n_link_pendulum_on_cart(10, True, True)

states = sm.Matrix(sys.states)
state_derivs = states.diff()

eom_expr = sys.eom_method.mass_matrix_full * state_derivs - sys.eom_method.forcing_full

c = ConstraintCollocator(eom_expr, sys.states, 10000, 0.01)
g = c.generate_constraint_function()
h = c.generate_jacobian_function()

%timeit g(np.random.random(c.num_free))
%timeit h(np.random.random(c.num_free))

c.num_collocation_nodes
c.num_constraints
c.num_parameters
c.num_unknown_input_trajectories
c.num_free

sm.count_ops(eom_expr)

len(c.jacobian_indices()[0])

len(states)
len(sys.constants_symbols)
len(sys.specifieds_symbols)

sys.constants = {k: 1.0 for k in sys.constants_symbols}
sys.times = np.linspace(0.0, 100.0, num=10000)
sys.specifieds = {k: 0.0 for k in sys.specifieds_symbols}
sys.initial_conditions = {k: 0.0001 for k in sys.states}

sys.generate_ode_function(generator='cython')

%time sys.integrate()
