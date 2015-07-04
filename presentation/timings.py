
import numpy as np
import sympy as sm
from pydy.models import n_link_pendulum_on_cart
from opty.direct_collocation import Problem, ConstraintCollocator

sys = n_link_pendulum_on_cart(10, False, False)

print('Number of states: {}'.format(len(sys.states)))
print('Number of total parameters: {}'.format(len(sys.constants_symbols)))

sys.constants = {k: 1.0 for k in sys.constants_symbols}
sys.times = np.linspace(0.0, 100.0, num=10000)
sys.initial_conditions = {k: 0.0001 for k in sys.states}

sys.generate_ode_function(generator='cython')

#%time sys.integrate()

# NLP

states = sm.Matrix(sys.states)
state_derivs = states.diff()

eom_expr = sys.eom_method.mass_matrix_full * state_derivs - sys.eom_method.forcing_full

print('Number of operations in EoMs: {}'.format(sm.count_ops(eom_expr)))

c = ConstraintCollocator(eom_expr, sys.states, 10000, 0.01)

print('Number of nodes: {}'.format(c.num_collocation_nodes))
print('Number of constraints: {}'.format(c.num_constraints))
print('Number of free variables: {}'.format(c.num_free))
print('Number of non-zero Jacobian entries: {}'.format(len(c.jacobian_indices()[0])))

g = c.generate_constraint_function()
h = c.generate_jacobian_function()

#%timeit g(np.random.random(c.num_free))
#%timeit h(np.random.random(c.num_free))
