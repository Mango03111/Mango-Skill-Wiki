---
name: vllm-ascend-contribution
description: Guide AI agents through the vllm-ascend contribution workflow. Use when preparing, reviewing, committing, or opening vllm-ascend changes, including DCO Signed-off-by commits, PR title/body conventions, local lint/CI/test selection, documentation changes, multi-node test additions, and E2E/nightly hardware CI trigger comments.
---

# vLLM Ascend Contribution

## Source of Truth

Use this workflow for the `vllm-project/vllm-ascend` repository. Before making a real submission, recheck the official docs or workflow files when possible, because CI labels, runner names, model versions, and test matrices can change.

Primary references:

- `https://docs.vllm.ai/projects/ascend/en/latest/developer_guide/contribution/index.html`
- `https://docs.vllm.ai/projects/ascend/en/latest/developer_guide/contribution/testing.html`
- `https://docs.vllm.ai/projects/ascend/en/latest/developer_guide/contribution/doc_writing.html`
- `https://docs.vllm.ai/projects/ascend/en/latest/developer_guide/contribution/multi_node_test.html`
- `https://docs.vllm.ai/projects/ascend/en/latest/developer_guide/contribution/nightly_ci_test.html`
- `https://docs.vllm.ai/projects/ascend/en/latest/developer_guide/contribution/e2e_ci_test.html`

## Contribution Workflow

1. Identify the change scope: code, kernel/op, test, CI, docs, model tutorial, or multi-node/nightly test config.
2. Keep edits focused. Avoid unrelated formatting, generated artifacts, and local debugging fields.
3. Run the narrowest useful local checks first, then broader checks when the change touches shared behavior.
4. Commit with DCO sign-off.
5. Open a PR whose title uses the required vllm-ascend prefix and whose body answers the template.
6. Trigger E2E/nightly hardware CI only when needed, and use targeted comments before adding labels.

## Local Setup and Checks

vllm-ascend build support is effectively Linux-only because `torch_npu` supports Linux, but linting and basic tests can be prepared on Linux, Windows, or macOS.

Run lint:

```bash
cd ~/vllm-project/
python3 -m venv .venv
source ./.venv/bin/activate
git clone https://github.com/vllm-project/vllm-ascend.git
cd vllm-ascend
pip install -r requirements-lint.txt
bash format.sh
```

Run local CI after lint setup:

```bash
cd ~/vllm-project/
git clone --branch <vllm_version_from_docs_or_repo> https://github.com/vllm-project/vllm.git
cd vllm
pip install -r requirements/build.txt
VLLM_TARGET_DEVICE="empty" pip install .
cd ../vllm-ascend

# Linux
pip install -r requirements-dev.txt

# Non-Linux fallback if needed
cat requirements-dev.txt | grep -Ev '^#|^--|^$|^-r' | while read PACKAGE; do pip install "$PACKAGE"; done
cat requirements.txt | grep -Ev '^#|^--|^$|^-r' | while read PACKAGE; do pip install "$PACKAGE"; done

bash format.sh ci
```

Use focused tests:

- Unit tests mirror source paths and start with `test_`, for example `vllm_ascend/worker/worker.py` -> `tests/ut/worker/test_worker.py`.
- Unit tests use Python `unittest` style and should mock device-related functions so they can run on CPU.
- CPU unit test command: `TORCH_DEVICE_BACKEND_AUTOLOAD=0 pytest -sv tests/ut`.
- Single file example: `pytest -sv tests/ut/test_ascend_config.py`.
- PR E2E tests cannot run on CPU; run them on Ascend hardware with `VLLM_USE_MODELSCOPE=true pytest -sv tests/e2e/pull_request/...`.
- Nightly single-node model tests can use `CONFIG_YAML_PATH=<config>.yaml VLLM_USE_MODELSCOPE=true pytest -sv tests/e2e/nightly/single_node/models/scripts/test_single_node.py`.
- Docs doctest command: `/vllm-workspace/vllm-ascend/tests/e2e/run_doctests.sh`.
- Docs linkcheck command: `make -C docs linkcheck SPHINXOPTS="-W --keep-going"`.

In the PR body, report the exact commands run and results. If hardware or full E2E tests were not run, state the limitation and what substitute checks were run.

## Commit Rules

All commits must include a DCO `Signed-off-by:` line. Use Git's sign-off flag:

```bash
git commit -s -m "Short imperative summary"
```

or:

```bash
git commit -s
```

Rules for AI agents:

- Do not create a commit unless the user asked for one or the workflow explicitly requires it.
- Verify `git config user.name` and `git config user.email` before committing; ask the user if identity is missing or wrong.
- Do not forge another person's `Signed-off-by`.
- If amending one commit, use `git commit --amend -s`.
- If multiple existing commits lack sign-off, use an interactive or scripted rebase only with user approval.
- Keep the commit message concise and imperative. The official docs require sign-off, not Conventional Commit syntax.

## PR Title Rules

Only PRs with supported vllm-ascend title prefixes are expected to be reviewed. Use one or more exact prefixes followed by a concise summary:

```text
[BugFix] Fix scheduler state leak during graph mode
[Core][Kernel] Reduce NPU memory use in attention path
[Doc] Add Qwen tutorial deployment notes
```

Allowed prefixes:

- `[Attention]` for new features or optimizations in attention.
- `[Communicator]` for new features or optimizations in communicators.
- `[ModelRunner]` for new features or optimizations in model runner.
- `[Platform]` for new features or optimizations in platform.
- `[Worker]` for new features or optimizations in worker.
- `[Core]` for core vllm-ascend logic such as platform, attention, communicators, or model runner.
- `[Kernel]` for compute kernel and op changes.
- `[BugFix]` for bug fixes.
- `[Doc]` for documentation fixes and improvements.
- `[Test]` for tests.
- `[CI]` for build or continuous integration improvements.
- `[Misc]` only when no other category fits; use sparingly.

If a PR spans multiple categories, include every relevant prefix.

## PR Body Rules

Fill the repository PR template directly:

- `What this PR does / why we need it?`: summarize the change, rationale, and linked issue such as `Fixes #123` when applicable.
- `Does this PR introduce any user-facing change?`: answer explicitly. Documentation-only changes are not considered user-facing by the template.
- `How was this patch tested?`: list CI/local commands and results. If tests were not added or run, explain why.

Add reviewer-useful notes only when they reduce review effort: risk areas, compatibility behavior, hardware assumptions, model/config assumptions, and follow-up work intentionally left out.

## E2E CI Comment Trigger

Use per-test E2E triggering to avoid running the full hardware suite during iterative debugging.

Post the comment first:

```text
/e2e tests/e2e/pull_request/one_card/test_foo.py
/e2e tests/e2e/pull_request/two_card/test_bar.py::test_case
/e2e path1 path2 path3
```

Then add the `ready` label. The label triggers the workflow and reads the existing `/e2e` comment.

Rules:

- Comment paths must be valid pytest paths relative to the repository root.
- The comment must be posted before adding `ready`. If the label was added first, remove and re-add it after posting the comment.
- Only the PR author or write/admin collaborators can trigger tests by comment.
- Only contributors with Triage role or maintainers with Write role can add labels; otherwise ask a maintainer.
- Pushing a new commit re-runs the workflow using the existing `/e2e` comment.
- Path routing is automatic: `two_card` -> A3 two-card, `four_card` -> A3 four-card, `_310p` -> 310P runners, otherwise one-card A2.

## Nightly CI Comment Trigger

Use PR-triggered nightly CI for broader hardware validation against the PR HEAD commit.

Post one comment first:

```text
/nightly
/nightly all
/nightly test_custom_op qwen3-32b
```

Then add the `nightly-test` label. The label triggers `Nightly-A2` or `Nightly-A3` and reads the existing `/nightly` comment.

Rules:

- Test names are case-sensitive and must match the workflow matrix `name` fields.
- Prefer targeted test names over `/nightly all`, especially on A3 where hardware concurrency is limited.
- The comment must be posted before adding `nightly-test`.
- Pushing a new commit re-runs the workflow with the existing `/nightly` comment.
- The A2 `doc-test` job runs only on scheduled or manual dispatch events, not PR-triggered nightly runs.

## Documentation Changes

For model tutorials, start from `docs/source/_templates/Model-Deployment-Tutorial-Template.md`.

For testable `model-code` blocks:

- Use them under `docs/source/tutorials/models/`; this is the directory scanned by default.
- Include required options: `block_name`, `converter_tag`, and `test_case_path`.
- Keep `test_case_path` repository-relative and inside the repo.
- Put `{{ generated }}` where converter output should be inserted.
- Supported `converter_tag` values include `single_node`, `multi_node`, `external_dp_template`, `external_dp_launch`, and `external_dp_proxy`.
- After generation, inspect the generated shell for runnable env vars and command-line parameters.

Useful docs commands:

```bash
python3 tools/docs_codegen/cli.py
python3 tools/docs_codegen/cli.py --doc docs/source/tutorials/models/<doc>.md
python3 tools/docs_codegen/cli.py --block docs/source/tutorials/models/<doc>.md::<block_name> --dry-run --stdout
python3 -m pip install -r docs/requirements-docs.txt
make -C docs clean
make -C docs html
python3 -m http.server -d docs/_build/html 8000
```

Do not commit local preview output such as `docs/_build/` unless the repository explicitly tracks a generated file.

## Multi-Node Test Changes

Use multi-node tests for distributed scenarios such as large-model DP or disaggregated prefill.

Contribution steps:

1. If custom weights are required, upload them to the ModelScope `vllm-ascend` organization or ask the documented maintainer for access.
2. Add an internal DP config under `tests/e2e/nightly/multi_node/internal_dp/config/`, or an external DP config under `tests/e2e/nightly/multi_node/external_dp/config/`.
3. Include essential YAML fields such as `test_name`, `model`, `num_nodes`, `npu_per_node`, shared envs, per-node `deployment`, and `benchmarks`.
4. Add the case to `.github/workflows/schedule_nightly_test_a3.yaml`.
5. In the workflow matrix, set `name`, `config_file_path`, `size`, and, for external DP, `config_base_path: tests/e2e/nightly/multi_node/external_dp/config/`.
6. For local no-Kubernetes runs, set `cluster_hosts`, `LWS_WORKER_INDEX`, `CONFIG_YAML_PATH`, and `CONFIG_BASE_PATH` manually.
7. Remove local-only `cluster_hosts` edits before submitting unless they are part of a committed test environment.

## Final Pre-PR Checklist

Before pushing or opening the PR, verify:

- The worktree contains only intended changes.
- Lint, local CI, unit tests, docs tests, or hardware tests were run as appropriate.
- Every commit has `Signed-off-by:`.
- The PR title uses exact supported prefixes.
- The PR body template is complete and includes test evidence.
- E2E/nightly trigger comments, if used, were posted before labels.
- Any inability to run NPU or multi-node tests is clearly documented.
