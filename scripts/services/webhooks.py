"""Webhooks helpers for parent portal for viewing schedules and announcements."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def webhooks_step_0(records: list[dict], limit: int = 153) -> list[dict]:
    """Apply webhooks rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def webhooks_step_1(records: list[dict], limit: int = 137) -> list[dict]:
    """Apply webhooks rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def webhooks_step_2(records: list[dict], limit: int = 388) -> list[dict]:
    """Apply webhooks rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def webhooks_step_3(records: list[dict], limit: int = 499) -> list[dict]:
    """Apply webhooks rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def webhooks_step_4(records: list[dict], limit: int = 165) -> list[dict]:
    """Apply webhooks rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def webhooks_step_5(records: list[dict], limit: int = 80) -> list[dict]:
    """Apply webhooks rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("webhooks step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
