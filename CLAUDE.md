# myoffice-skills

Office workflows, presentations, source understanding and developer-facing productivity skills.

## Repository ownership

| Repository | Owns |
| --- | --- |
| `concept-skills` | Software concepts, semantic modeling, knowledge organization, and visual learning. |
| `cloud-concept-skills` | Huawei Cloud operations, billing, controlled provisioning, and account onboarding. |
| `myoffice-skills` | Office workflows, presentations, source notes, repository guidance, and Agent DX tooling. |

## Directory contract

| Directory | Contract |
| --- | --- |
| `skills/en/<name>/`, `skills/zh-CN/<name>-cn/` | Self-contained install payloads, including required `references/`, assets and runtime scripts. |
| `qa/` | Private local validation, fixtures and reports; ignored by Git and absent from public checkouts. |
| `catalog.yml` | Tracked discovery metadata used by QA and publishing tools. |
| `docs/` | Concise local notes and examples; ignored by Git and never required by QA or distribution. |
| `tools/`, `.githooks/`, `.github/` | Repository tooling, local commit/push gates and CI. |

Learning copies, downloaded repositories, process notes, raw outputs and generated eval workspaces
belong outside the checkout, normally in a task-specific temporary directory. Delete them when no
longer needed. Preserve runtime `skills/**/references/` and maintained fixtures/examples.

## Change and release rules

- Update the owning repository; keep sibling projects independent and link rather than copy their skills.
- Keep localized pairs, declared source versions and `catalog.yml` consistent; the catalog is the public version record. English uses the base
  name and `language: en`; Chinese adds `-cn` and `language: zh-CN`. Paired `translation_of` values
  name each other. Translate prose while preserving commands, safety gates and observable behavior.
  The repository `VERSION` and per-skill catalog versions have separate scopes.
- Run `./tools/validate-all.sh` for public package checks; it must work without `qa/`.
  Run `./tools/validate-all.sh --local-qa` only for available local QA; no behavioral or live-service result is implied by public checks.
- Set `git config core.hooksPath .githooks` once per checkout. Ignore rules and commit/push/CI hygiene checks
  keep local-only files out of Git, including files added with force.
- Commit and publish only within user authorization. ClawHub receives English payloads only;
  GitHub retains both languages. Verify remote contents before announcing a release.
- Treat credentials, local installs and caches as local-only. Keep only the current release notes;
  rewriting Git history or deleting remote releases requires explicit user authorization.
- Keep `qa/`, `docs/`, analysis material and generated reports local; exclude them even when force-added.

## Office-specific rules

- `presentation-making-cn` and `brand-ui-design-cn` are Chinese-only catalog entries. Preserve
  explicitly requested standalone locales and invocation policies instead of fabricating translations.
- Keep presentation and interface templates/assets with their owning skill; research copies and
  source-project clones do not belong in the repository.
- Preserve explicit-only invocation where declared. Update marketplace grouping and the README
  with changes to the bilingual pair; do not ship QA or development reports inside payloads.
