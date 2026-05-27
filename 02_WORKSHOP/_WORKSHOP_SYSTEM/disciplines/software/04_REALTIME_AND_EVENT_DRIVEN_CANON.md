# Realtime and Event-Driven Canon

Realtime is a project decision, not a default. Operational systems must evaluate whether realtime or events are required.

A local realtime/event standard should define:
- event ownership,
- dispatch guarantees,
- client resync/reconnect behavior,
- authorization of subscriptions,
- duplicate/stale event handling,
- outbox or delivery consistency if required,
- scale-out strategy,
- tests and observability.
