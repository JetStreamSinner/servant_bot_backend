from typing import Dict, Any


def get_app_settings() -> Dict[str, Any]:
    title = "Router service"
    docs_url = "/docs"
    return {
        "application_kwargs": {
            "title": title,
            "docs_url": docs_url
        },
        "allowed_hosts": ["*"],
        "datasource_uri": ""
    }
