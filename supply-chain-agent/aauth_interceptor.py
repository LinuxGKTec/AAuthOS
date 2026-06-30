"""
aauth_interceptor — compatibility shim.

The original hand-rolled interceptor has been replaced by aauth_sdk.
This stub re-exports the symbols the upstream code still imports, so
upstream changes that touch the entrypoint compile without manual
rewrites. See sdk/python/README.md for the new API.
"""
from aauth_sdk import Agent, MissionMiddleware  # noqa: F401

def sign_outbound(*args, **kwargs):
    raise RuntimeError("sign_outbound() is replaced by Agent.client(...) — see sdk/python/README.md")

def verify_inbound(*args, **kwargs):
    raise RuntimeError("verify_inbound() is replaced by Agent.verifier().verify(...) — see sdk/python/README.md")
