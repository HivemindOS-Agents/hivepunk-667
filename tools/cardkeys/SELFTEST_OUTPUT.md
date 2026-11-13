# Self-test of cardkeys

Written by HivemindOS from the self-test runner's record after the last commit to this folder. It is replaced at every run, and a copy written by the agent is not kept.

- Result: **passed**
- Ran: 2026-11-13T10:57:27Z
- Run: https://github.com/HivemindOS-Agents/bee-self-test/actions/runs/43413105426

What it printed (what failed first, then its last lines):

~~~
PASS: no unexpected dataset identifiers in column 1
PASS: all rows have non-empty read_status
PASS: README mentions all three dataset cards
PASS: check_live --offline exits 0 and reports every live value NOT_READ
PASS: check_live exits 0 with 'verdict match' when live sizes equal local sizes
PASS: check_live exits 1 with 'verdict MISMATCH' when a live size differs
PASS: check_live --bogus exits 2 with a usage line
PASS: all checks succeeded
~~~
