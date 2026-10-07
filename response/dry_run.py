def execute_response(action, target, dry_run=True):
    if dry_run:
        return {
            "success": True,
            "executed": False,
            "dry_run": True,
            "action": action,
            "target": target,
            "message": (
                "DRY RUN: Action was simulated. "
                "No real containment action was performed."
            )
        }

    return {
        "success": False,
        "executed": False,
        "dry_run": False,
        "action": action,
        "target": target,
        "message": (
            "Live response actions are disabled until "
            "additional safety controls are configured."
        )
    }
