# PCE API

Execution layer for AI governance that validates decision stability before execution.

## Overview

This API provides a simple interface to validate whether a decision is structurally safe before being executed.

## Endpoint

POST /validate

## Example

Input:
{
  "value": 0.3
}

Output:
{
  "status": "SUSPEND"
}
