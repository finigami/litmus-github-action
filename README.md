# Litmus GitHub Action

A GitHub Action to run Litmus test suites with configurable browser settings and environment targeting.

## Prerequisites

- `LITMUS_API_KEY` should be stored in your repository secrets. API Key can be generated on the LitmusCheck platform under settings
- Valid Litmus suite ID

## Basic Usage

```yaml
name: Run Litmus Tests

on:
  workflow_dispatch:

jobs:
  run_litmus:
    name: "Run Litmus Suite"
    runs-on: ubuntu-latest
    steps:
      - name: Run Litmus Suite
        uses: finigami/litmus-github-action@master
        with:
          suite-id: "14f80918-0841-40b5-96bb-8eae0f2c366f"
        env:
          LITMUS_API_KEY: ${{ secrets.LITMUS_API_KEY}}
```

## Advanced Usage with Configuration

### With Browser Configuration

```yaml
name: Run Litmus Tests with Chrome Desktop

on:
  workflow_dispatch:

jobs:
  run_litmus:
    name: "Run Litmus Suite"
    runs-on: ubuntu-latest
    steps:
      - name: Run Litmus Suite
        uses: finigami/litmus-github-action@master
        with:
          suite-id: "14f80918-0841-40b5-96bb-8eae0f2c366f"
          config: '{"browser":"chrome","device":{"type":"desktop","device_config":{"os":"windows"}},"viewport":{"width":1920,"height":1080}}'
        env:
          LITMUS_API_KEY: ${{ secrets.LITMUS_API_KEY}}
```

### With Environment ID

```yaml
name: Run Litmus Tests on Specific Environment

on:
  workflow_dispatch:

jobs:
  run_litmus:
    name: "Run Litmus Suite"
    runs-on: ubuntu-latest
    steps:
      - name: Run Litmus Suite
        uses: finigami/litmus-github-action@master
        with:
          suite-id: "14f80918-0841-40b5-96bb-8eae0f2c366f"
          environment-id: "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
        env:
          LITMUS_API_KEY: ${{ secrets.LITMUS_API_KEY}}
```

### Complete Example with Both Config and Environment

```yaml
name: Run Litmus Tests - Complete Configuration

on:
  workflow_dispatch:

jobs:
  run_litmus:
    name: "Run Litmus Suite"
    runs-on: ubuntu-latest
    steps:
      - name: Run Litmus Suite
        id: litmus
        uses: finigami/litmus-github-action@master
        with:
          suite-id: "14f80918-0841-40b5-96bb-8eae0f2c366f"
          config: '{"browser":"chrome","device":{"type":"desktop","device_config":{"os":"windows"}},"viewport":{"width":1920,"height":1080}}'
          environment-id: "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
        env:
          LITMUS_API_KEY: ${{ secrets.LITMUS_API_KEY}}
      
      - name: Use Suite Results
        run: |
          echo "Suite completed with results: ${{ steps.litmus.outputs.suite-result }}"
```

## Input Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `suite-id` | ✅ Yes | - | ID of the Litmus suite to run |
| `api-key` | ✅ Yes | - | API key for Litmus authentication |
| `api-url` | ❌ No | `https://api.litmuscheck.com/api/v1/suite` | Base URL for the Litmus API |
| `config` | ❌ No | `{}` | Configuration object as JSON string for browser/device settings |
| `environment-id` | ❌ No | - | Environment ID (UUID) to target specific environment |

## Outputs

| Output | Description |
|--------|-------------|
| `suite-result` | Final suite run result as JSON containing test counts and status |