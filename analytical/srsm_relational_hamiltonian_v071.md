# SRSM V0.71 — Local Hermitian Generator from Adjacency and Saturation

## Construction

Let B0 be the oriented incidence operator of the relational graph. Assign each edge e the saturation-dependent availability amplitude

w_e = (1 - chi_e)^(n_sigma/2),

and define

B = W B0,

where W is diagonal in edge space.

Let the complete amplitude state contain two conjugate sectors,

Psi = (psi_plus, psi_minus)^T.

The minimal local Hermitian adjacency generator is

H = [[m I, c B^dagger],
     [c B, -m I]].

Measured Hermiticity residual:

0.000000e+00

## Squared generator

The generator obeys

H^2 = diag(m^2 I + c^2 B^dagger B,
           m^2 I + c^2 B B^dagger).

Measured factorization residual:

0.000000e+00

Because i d_t Psi = H Psi,

d_t^2 Psi = -H^2 Psi.

Therefore each sector obeys a graph Klein-Gordon equation. The finite-difference verification residual was

4.111442e-06.

## Long-wavelength limit

For a uniform ring,

omega^2(k) = m^2 + 4 c^2 w^2 sin^2(ka/2)/a^2.

At small k,

omega^2(k) = m^2 + c_eff^2 k^2 - c_eff^2 a^2 k^4/12 + O(k^6),

with

c_eff = c (1-chi_0)^(n_sigma/2).

For the tested vacuum,

c_eff = 0.965304056.

The measured fractional dispersion correction scaled as

|omega/(c_eff k)-1| proportional to k^1.998491,

consistent with the expected k^2 lattice correction.

## Reversibility

The exact amplitude evolution is

Psi(t) = exp(-i H t) Psi(0).

Maximum norm residual:

1.554312e-15

Forward-backward recovery error:

3.060836e-15

## Saturation-weighted spatial operator

The spatial operator is

L_chi = B0^dagger diag((1-chi_e)^n_sigma) B0.

It is positive because

v^dagger L_chi v = ||B v||^2 >= 0.

The smallest computed eigenvalue was

-5.005911e-16,

consistent with the constant graph mode.

For slowly varying saturation, the continuum principal operator is

-div[c^2 (1-chi)^n_sigma grad].

## Universal principal symbol

Different species share one emergent causal geometry when their graph operators differ only by a scalar normalization:

L_s = Z_s L.

Universal proportional-operator residual:

1.644775e-16

After adding a species-specific local defect:

1.222906e-02

Thus a common incidence operator is the microscopic condition for a shared principal symbol and one light cone.

## Result

Relational adjacency plus saturation availability gives B.

A doubled phase-bearing state plus locality and Hermiticity gives

H = [[m I, c B^dagger],
     [c B, -m I]].

Squaring H yields a positive weighted graph Laplacian and hence a hyperbolic infrared equation.

This is a constructive derivation, not yet a uniqueness theorem. Additional local Hermitian terms remain possible. The next step is to classify all symmetry-allowed local corrections and determine which are infrared relevant.
