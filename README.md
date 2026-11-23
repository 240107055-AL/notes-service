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

## Rollback

Argo CD deploys what is on the `main` branch, from the `k8s` folder.
To roll back, undo the commit that deployed the bad version, with a new commit:

    git log --oneline -- k8s
    git revert <commit>
    git push

Argo CD deploys the previous version within three minutes. Do not use
`kubectl rollout undo`: self-heal would put the bad version back.
