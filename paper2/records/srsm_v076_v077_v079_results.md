# SRSM Paper 2 — V0.76, V0.77, and V0.79 result records

## V0.76: exact quadratic gauge Hessian

A symmetric frame perturbation on a periodic lattice uses the gauge map δh_μν = k̂_μ ξ_ν + k̂_ν ξ_μ, with k̂_μ = 2 sin(q_μ/2). The quadratic kernel is the lattice massless Fierz–Pauli/linearized-Einstein operator.

- maximum ||KG|| residual: 4.702996997461e-16
- gauge-generator rank: 4
- gauge-null count: 4
- smallest absolute gauge-fixed eigenvalue: 9.494102871751e-01
- physical massless modes: TT_plus and TT_cross
- modeled nonmetric gaps: 1.25, 1.6, and 2.1

This closes the quadratic gauge-Hessian problem only.

## V0.77: nonlinear finite-difference candidate

The direct local finite-difference continuation does not close exactly at finite spacing because the discrete derivative does not obey an exact Leibniz rule.

- N=128 gauge-algebra residual: 1.562371876410e-03
- fitted convergence order: 1.991552
- Leibniz residual: 2.487178627366e-03
- Leibniz convergence order: 2.007172

The candidate is rejected as an exact microscopic nonlinear realization. Its continuum convergence does not invalidate the V0.76 quadratic result.

## V0.79: tetrad–connection prototype

The quadratic prototype contains an independent tetrad, Lorentz connection, simplicity reduction, auxiliary torsion sector, saturation mode, and canonical Gauss, spatial-diffeomorphism, and Hamiltonian constraints.

- phase-space degree count: 18 - 2(7) = 4, or two configuration-space modes
- smallest torsion-block eigenvalue: 2.013493178681
- relative difference between the torsion-eliminated metric kernel and V0.76: 5.779038089253e-17
- physical massless modes: TT_plus and TT_cross
- prototype gaps: torsion 2.4, simplicity 2.8, saturation 2.1

These gaps are model parameters, not predictions. Exact nonlinear constraint closure remains open.