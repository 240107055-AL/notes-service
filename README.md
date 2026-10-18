# Notes service

## What it does
A tiny HTTP service: `GET /` greets, `GET /notes` returns the notes,
`GET /healthz` returns 200 for health checks.

## How to run
`./scripts/run.sh`

## How to test
`./scripts/test.sh` prints `TESTS: n/n`.

## Port
Listens on `$PORT`, default 8080.
