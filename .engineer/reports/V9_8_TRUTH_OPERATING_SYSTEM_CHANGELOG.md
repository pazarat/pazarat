# V9.8 Truth Operating System Changelog

## Problem fixed

V9.7 removed the first-contact cage, but the runtime still lacked a strong claim-permission mechanism. The model could receive truth surfaces but still overstate current state, first step, or execution readiness.

## What changed

- Added `truth-authority-gate`.
- Integrated truth authority into `plug-fast` and `open-neural-entry`.
- Replaced mandatory next actions with governed decision space.
- Kept model freedom: no first-contact templates and no forced answer shape.
- Removed file-size priority from File Matrix pulse selection.
- Added explicit value basis: content/cross-file truth alignment, not size or path alone.

## Intended behavior

For a project question, the model should:

1. understand the intent;
2. enter the control core;
3. use File Matrix / truth sweep to inspect content value;
4. check claim authority;
5. answer naturally within the claim permissions;
6. deepen if the answer requires stronger evidence.

## What this does not do

It does not script the answer. It does not force a first-contact path. It does not make Runtime visible as the project.
