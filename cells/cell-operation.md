# Cell operation guide

Use this guide to run any cell consistently.

## Inputs

- `data/cell-catalog.json`
- `cells/cell.schema.json`
- `cells/agent-system-prompt.md`

## Workflow

1. Select a `cellId` from `data/cell-catalog.json`.
2. Load the matching cell object.
3. Validate the object against `cells/cell.schema.json`.
4. Render `cells/agent-system-prompt.md` with the selected cell values.
5. Run the cell agent using the rendered prompt.
6. Record outputs and feedback for the same `cellId`.

## Required outputs

- Objective for the selected cell
- Action plan tied to its dimension and function
- Execution result and feedback loop notes
