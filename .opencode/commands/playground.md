---
description: Start the Sloperator playground server in the background
---

Start the Sloperator playground server on port $ARGUMENTS (use 8080 when no
port is given).

Current TCP listeners:

!`lsof -nP -iTCP -sTCP:LISTEN`

Check the listener list above for an existing Sloperator server on the
requested port first. If one is already listening, report it and do nothing.
Otherwise start `uv run playground/server.py <port>` in the background.
