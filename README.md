### litmus-github-action

## To run this github action, calling repo must pass suite_id.
## LITMUS_API_KEY should be stored in Git Repo as secrets.

Steps:
1. Create .github/workflows folder in repo.
2. Create workflow_file.yml
3. Sample of the file is given below

<workflow_file.yml>

name: litmus-github-action

on:
  workflow_dispatch:

jobs:
  run_litmus:
    name: "Run Litmus"
    runs-on: ubuntu-latest
    steps:
      - name: Run Litmus Suite
        uses: finigami/litmus-github-action@master
        with:
          suite-id: "14f80918-0841-40b5-96bb-8eae0f2c366f"
        env:
          LITMUS_API_KEY: ${{ secrets.LITMUS_API_KEY}}
