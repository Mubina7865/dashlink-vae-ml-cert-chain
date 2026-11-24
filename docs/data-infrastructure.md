# Data & Compute Infrastructure (P1/S1 decisions, recorded 2026-11-23)

- Repo: public, github.com/Mubina7865/dashlink-vae-ml-cert-chain, default branch `main`.
- Python: 3.13.2 (doc requires 3.11+; downgrade path to 3.12 recorded if wheel conflicts arise).
- DVC remote: DagsHub (OAuth via GitHub; no cloud credentials). Local + remote copies policy per risk register.
- Compute: university GPU (primary), Google Colab (fallback). VAE scale compatible with both.
- Raw dataset: DASHlink curated 4-class set, obtained pre-project; verified via SHA-256 (see data/README.md).
- External raw tail data (Tail_682..687 zips): excluded from registry; located outside repo.
- ED-324 access: no institutional Draft 7 access; snapshot strategy = Aug 2025 FAA Tech Exchange
  objective tables + ER-022/ER-027 + WG-114 public status pages. Draft-7 gap to be recorded
  in docs/standards-mapping-plan.md.
