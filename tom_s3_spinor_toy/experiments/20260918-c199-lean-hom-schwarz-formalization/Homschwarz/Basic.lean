/- C199: formalization of THEOREM.md's E1 escape criterion (rev 8).

Statement: for finite-dimensional vector spaces V, W each carrying an
action of an arbitrary index set of "generators" (a Lie algebra, a group,
or anything else -- all that matters is each generator acts as a linear
endomorphism), if an EQUIVARIANT linear isomorphism V ~ W exists, the
three equivariant-Hom spaces Hom(V,V), Hom(V,W), Hom(W,W) all have the
SAME dimension. Contrapositive: a strict Cauchy-Schwarz-style inequality
on these dimensions proves no equivariant isomorphism exists -- exactly
the fact THEOREM.md's E1 escape condition relies on.

No reference to this project's specific G2/SU(3)/Spin(8) matrices: the
proof is a general linear-algebra fact about composing with a linear
equivalence, needing no Schur's lemma or representation-theory library. -/

import Mathlib.LinearAlgebra.FiniteDimensional.Basic
import Mathlib.LinearAlgebra.Basis.VectorSpace
import Mathlib.Algebra.Module.Submodule.Basic

open Module

variable {k : Type*} [Field k]
variable {V W : Type*} [AddCommGroup V] [Module k V] [AddCommGroup W] [Module k W]
variable {ι : Type*}

/-- `φ : V →ₗ[k] W` is *equivariant* w.r.t. generator actions `ρV`, `ρW`
if it intertwines every generator's action. -/
def IsEquivariant (ρV : ι → Module.End k V) (ρW : ι → Module.End k W)
    (φ : V →ₗ[k] W) : Prop :=
  ∀ i, φ ∘ₗ ρV i = ρW i ∘ₗ φ

/-- Pointwise form of `IsEquivariant`, the shape actually usable by `simp`. -/
theorem IsEquivariant.apply {ρV : ι → Module.End k V} {ρW : ι → Module.End k W}
    {φ : V →ₗ[k] W} (h : IsEquivariant ρV ρW φ) (i : ι) (v : V) :
    φ (ρV i v) = ρW i (φ v) :=
  LinearMap.congr_fun (h i) v

/-- The equivariant-Hom space `Hom_h(V,W)`, as a submodule of the full
linear-map space -- the object THEOREM.md calls
`dim Hom_h(channel_i, channel_j)`. -/
def EquivHom (ρV : ι → Module.End k V) (ρW : ι → Module.End k W) :
    Submodule k (V →ₗ[k] W) where
  carrier := {φ | IsEquivariant ρV ρW φ}
  zero_mem' := by intro i; simp
  add_mem' := by
    intro φ ψ hφ hψ i
    simp only [Set.mem_setOf_eq, IsEquivariant] at hφ hψ ⊢
    simp [LinearMap.add_comp, LinearMap.comp_add, hφ i, hψ i]
  smul_mem' := by
    intro c φ hφ i
    simp only [Set.mem_setOf_eq, IsEquivariant] at hφ ⊢
    simp [LinearMap.smul_comp, LinearMap.comp_smul, hφ i]

@[simp] theorem mem_EquivHom {ρV : ι → Module.End k V} {ρW : ι → Module.End k W}
    (φ : V →ₗ[k] W) : φ ∈ EquivHom ρV ρW ↔ IsEquivariant ρV ρW φ := Iff.rfl

/-- An equivariant linear equivalence `V ≃ W`: a vector-space isomorphism
that also intertwines every generator's action. -/
structure EquivariantEquiv (ρV : ι → Module.End k V) (ρW : ι → Module.End k W) where
  toEquiv : V ≃ₗ[k] W
  equivariant : IsEquivariant ρV ρW toEquiv.toLinearMap

namespace EquivariantEquiv

variable {ρV : ι → Module.End k V} {ρW : ι → Module.End k W}

/-- Pointwise form of equivariance: `f (ρV i x) = ρW i (f x)` for every `x`. -/
theorem apply_gen (f : EquivariantEquiv ρV ρW) (i : ι) (x : V) :
    f.toEquiv (ρV i x) = ρW i (f.toEquiv x) :=
  f.equivariant.apply i x

/-- The inverse of an equivariant equivalence is equivariant too. -/
theorem symm_equivariant (f : EquivariantEquiv ρV ρW) :
    IsEquivariant ρW ρV f.toEquiv.symm.toLinearMap := by
  intro i
  ext w
  show f.toEquiv.symm (ρW i w) = ρV i (f.toEquiv.symm w)
  apply f.toEquiv.injective
  rw [f.toEquiv.apply_symm_apply, f.apply_gen i (f.toEquiv.symm w),
    f.toEquiv.apply_symm_apply]

/-- Pointwise form of `symm_equivariant`. -/
theorem symm_apply_gen (f : EquivariantEquiv ρV ρW) (i : ι) (w : W) :
    f.toEquiv.symm (ρW i w) = ρV i (f.toEquiv.symm w) :=
  f.symm_equivariant.apply i w

/-- Postcomposing an equivariant endomorphism of `V` with `f` lands in
`EquivHom ρV ρW`. -/
theorem compLeft_mem (f : EquivariantEquiv ρV ρW) {φ : V →ₗ[k] V}
    (hφ : φ ∈ EquivHom ρV ρV) : (f.toEquiv.toLinearMap ∘ₗ φ) ∈ EquivHom ρV ρW := by
  intro i
  ext v
  have key : φ (ρV i v) = ρV i (φ v) := hφ.apply i v
  simp [key, f.apply_gen]

/-- Precomposing an equivariant map `V → W` with `f⁻¹` lands in
`EquivHom ρW ρW`. -/
theorem compRight_mem (f : EquivariantEquiv ρV ρW) {ψ : V →ₗ[k] W}
    (hψ : ψ ∈ EquivHom ρV ρW) :
    (ψ ∘ₗ f.toEquiv.symm.toLinearMap) ∈ EquivHom ρW ρW := by
  intro i
  ext w
  have key : f.toEquiv.symm (ρW i w) = ρV i (f.toEquiv.symm w) := f.symm_apply_gen i w
  have key2 : ψ (ρV i (f.toEquiv.symm w)) = ρW i (ψ (f.toEquiv.symm w)) := hψ.apply i _
  simp [key, key2]

/-- Composing on the left with `f`, as a linear map `Hom(V,V) → Hom(V,W)`. -/
def compLeftHom (f : EquivariantEquiv ρV ρW) :
    EquivHom ρV ρV →ₗ[k] EquivHom ρV ρW where
  toFun φ := ⟨f.toEquiv.toLinearMap ∘ₗ (φ : V →ₗ[k] V), f.compLeft_mem φ.2⟩
  map_add' φ ψ := by ext v; simp
  map_smul' c φ := by ext v; simp

/-- Composing on the right with `f⁻¹`, as a linear map `Hom(V,W) → Hom(W,W)`. -/
def compRightHom (f : EquivariantEquiv ρV ρW) :
    EquivHom ρV ρW →ₗ[k] EquivHom ρW ρW where
  toFun ψ := ⟨(ψ : V →ₗ[k] W) ∘ₗ f.toEquiv.symm.toLinearMap, f.compRight_mem ψ.2⟩
  map_add' φ ψ := by ext v; simp
  map_smul' c φ := by ext v; simp

/-- `compLeftHom` is a linear EQUIVALENCE `Hom(V,V) ≃ Hom(V,W)` (inverse:
compose on the left with `f⁻¹`). -/
def compLeftEquiv (f : EquivariantEquiv ρV ρW) :
    EquivHom ρV ρV ≃ₗ[k] EquivHom ρV ρW where
  toLinearMap := f.compLeftHom
  invFun ψ := ⟨f.toEquiv.symm.toLinearMap ∘ₗ (ψ : V →ₗ[k] W), by
    intro i
    ext v
    have key : (ψ : V →ₗ[k] W) (ρV i v) = ρW i ((ψ : V →ₗ[k] W) v) := ψ.2.apply i v
    simp [key, f.symm_apply_gen]⟩
  left_inv φ := by
    apply Subtype.ext
    ext v
    simp [compLeftHom]
  right_inv ψ := by
    apply Subtype.ext
    ext v
    simp [compLeftHom]

/-- `compRightHom` is a linear EQUIVALENCE `Hom(V,W) ≃ Hom(W,W)` (inverse:
compose on the right with `f`). -/
def compRightEquiv (f : EquivariantEquiv ρV ρW) :
    EquivHom ρV ρW ≃ₗ[k] EquivHom ρW ρW where
  toLinearMap := f.compRightHom
  invFun χ := ⟨(χ : W →ₗ[k] W) ∘ₗ f.toEquiv.toLinearMap, by
    intro i
    ext v
    have key : (χ : W →ₗ[k] W) (ρW i (f.toEquiv v)) = ρW i ((χ : W →ₗ[k] W) (f.toEquiv v)) :=
      χ.2.apply i (f.toEquiv v)
    simp [f.apply_gen, key]⟩
  left_inv ψ := by
    apply Subtype.ext
    ext v
    simp [compRightHom]
  right_inv χ := by
    apply Subtype.ext
    ext w
    simp [compRightHom]

/-- **Main lemma.** An equivariant isomorphism `V ≃ W` forces the three
equivariant-Hom spaces `Hom(V,V)`, `Hom(V,W)`, `Hom(W,W)` to have EQUAL
dimension. This is the only fact `E1` (THEOREM.md rev 8, section 3) needs. -/
theorem finrank_eq [FiniteDimensional k V] [FiniteDimensional k W]
    (f : EquivariantEquiv ρV ρW) :
    finrank k (EquivHom ρV ρV) = finrank k (EquivHom ρV ρW) ∧
    finrank k (EquivHom ρV ρW) = finrank k (EquivHom ρW ρW) :=
  ⟨(f.compLeftEquiv).finrank_eq, (f.compRightEquiv).finrank_eq⟩

end EquivariantEquiv

/-- **E1's escape criterion, formalized.** A strict Cauchy-Schwarz-style
inequality on the equivariant-Hom dimensions PROVES no equivariant
isomorphism `V ≃ W` can exist -- this is exactly what THEOREM.md's `E1`
row cites to justify "`M` genuinely distinguishes the channels." -/
theorem no_equivariant_equiv_of_finrank_sq_lt
    {ρV : ι → Module.End k V} {ρW : ι → Module.End k W}
    [FiniteDimensional k V] [FiniteDimensional k W]
    (h : (finrank k (EquivHom ρV ρW)) ^ 2 <
         finrank k (EquivHom ρV ρV) * finrank k (EquivHom ρW ρW)) :
    IsEmpty (EquivariantEquiv ρV ρW) := by
  constructor
  intro f
  obtain ⟨h1, h2⟩ := f.finrank_eq
  rw [h1, ← h2, pow_two] at h
  exact absurd h (lt_irrefl _)
