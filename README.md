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
          suite-id: "your-suite-id"
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
          suite-id: "your-suite-id"
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
          suite-id: "your-suite-id"
          environment-id: "your-environment-id"
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
          suite-id: "your-suite-id"
          config: '{"browser":"chrome","device":{"type":"desktop","device_config":{"os":"windows"}},"viewport":{"width":1920,"height":1080}}'
          environment-id: "your-environment-id"
        env:
          LITMUS_API_KEY: ${{ secrets.LITMUS_API_KEY}}
      
      - name: Use Suite Results
        run: |
          echo "Suite completed with results: ${{ steps.litmus.outputs.suite-result }}"
```

### With Tag Filter

```yaml
name: Run Litmus Tests with Tag Filter

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
          suite-id: "your-suite-id"
          tag-filter-condition: "contains_any"
          tag-list: '["prod", "smoke"]'
        env:
          LITMUS_API_KEY: ${{ secrets.LITMUS_API_KEY}}
```

### With Emails Override

```yaml
name: Run Litmus Tests with Email Override

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
          suite-id: "your-suite-id"
          emails: '["test@example.com", "team@example.com"]'
        env:
          LITMUS_API_KEY: ${{ secrets.LITMUS_API_KEY}}
```

### Complete Example with All Options

```yaml
name: Run Litmus Tests - All Options

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
          suite-id: "your-suite-id"
          config: '{"browser":"chrome","device":{"type":"desktop","device_config":{"os":"windows"}},"viewport":{"width":1920,"height":1080}}'
          environment-id: "your-environment-id"
          tag-filter-condition: "contains_any"
          tag-list: "prod,smoke"
          emails: "test@example.com,team@example.com"
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
| `tag-filter-condition` | ❌ No | - | Tag filter condition: `contains_any` or `does_not_contain_any` |
| `tag-list` | ❌ No | - | List of tags (JSON array string or comma-separated list) |
| `emails` | ❌ No | - | Email addresses to override suite config emails (JSON array string or comma-separated list) |

## Outputs

| Output | Description |
|--------|-------------|
| `suite-result` | Final suite run result as JSON containing test counts and status |