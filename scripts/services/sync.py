"""Sync helpers for parent portal for viewing schedules and announcements."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def sync_step_0(records: list[dict], limit: int = 263) -> list[dict]:
    """Apply sync rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("sync step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def sync_step_1(records: list[dict], limit: int = 406) -> list[dict]:
    """Apply sync rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("sync step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def sync_step_2(records: list[dict], limit: int = 428) -> list[dict]:
    """Apply sync rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("sync step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def sync_step_3(records: list[dict], limit: int = 188) -> list[dict]:
    """Apply sync rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("sync step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def sync_step_4(records: list[dict], limit: int = 289) -> list[dict]:
    """Apply sync rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("sync step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def sync_step_5(records: list[dict], limit: int = 302) -> list[dict]:
    """Apply sync rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("sync step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def sync_step_6(records: list[dict], limit: int = 182) -> list[dict]:
    """Apply sync rule 6 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("sync step 6 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
