# SRSM V0.72 — Classification of Local Hermitian Corrections

Any translation-invariant Hermitian two-sector generator has

H(k) = h0(k) I + hx(k) sigma_x + hy(k) sigma_y + hz(k) sigma_z,

with real coefficient functions. Locality makes them analytic near k=0.

A representative expansion is

h0 = mu + alpha2 k^2 + ...
hx = v k + beta3 k^3 + ...
hy = eta k + eta3 k^3 + ...
hz = m + delta2 k^2 + ...

Maximum Hermiticity residual:

0.000000e+00

## Basis reduction

A constant internal rotation combines

v k sigma_x + eta k sigma_y

into

v_eff k sigma_x,

where

v_eff = sqrt(v^2 + eta^2) = 1.152128465.

Rotation residual:

2.330028e-16

Thus the second linear Pauli direction is not an independent infrared operator for one isolated species.

## Infrared scaling

Relative to the leading linear term, the measured coarse-graining powers were

mass: 1.000000
quadratic correction: -1.000000
cubic correction: -2.000000

Therefore:

- m sigma_z is relevant;
- v k sigma_x is the leading kinetic term;
- k^2 corrections are irrelevant;
- k^3 corrections are more strongly irrelevant.

A universal constant mu I is removable by a common phase rotation. A species-dependent or position-dependent identity term is instead a physical relevant potential.

## Symmetry filter

Exact massless chiral symmetry,

Gamma H Gamma = -H with Gamma = sigma_z,

forbids I and sigma_z terms while allowing sigma_x and sigma_y kinetic terms.

Breaking chiral symmetry permits the relevant mass m sigma_z.

After basis reduction and removal of a universal identity shift, the leading infrared generator is

H_IR(k) = v_eff k sigma_x + m sigma_z.

In position space,

H_IR = -i v_eff sigma_x partial_x + m sigma_z.

Because sigma_x anticommutes with sigma_z,

H_IR^2 = -v_eff^2 partial_x^2 + m^2.

Hence

(partial_t^2 - v_eff^2 partial_x^2 + m^2) Psi = 0.

The measured massless fractional dispersion correction scaled as

k^2.000259,

consistent with an O(k^2) relative correction.

## Conditional uniqueness statement

Within a two-sector translation-invariant vacuum, assume:

1. Hermiticity;
2. finite-range or exponentially local coupling;
3. analyticity near k=0;
4. one common adjacency orientation;
5. exact chiral symmetry in the massless vacuum;
6. equivalence under constant internal basis rotations;
7. no species-dependent relevant identity potential.

Then the unique leading nontrivial infrared kinetic generator is, up to normalization and basis choice,

H_IR = v k sigma_x,

with m sigma_z as the symmetry-breaking relevant deformation.

This is infrared uniqueness, not microscopic uniqueness. Many local lattice Hamiltonians lie in the same universality class.

The next step is the multidimensional classification. The directional kinetic matrices must be classified, and isotropic hyperbolicity should force a Clifford algebra.
