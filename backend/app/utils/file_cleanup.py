import os
import time


def cleanup_generated_files(
    folder="generated",
    max_age_hours=1
):

    now = time.time()

    max_age_seconds = (
        max_age_hours * 3600
    )

    for filename in os.listdir(folder):

        path = os.path.join(
            folder,
            filename
        )

        if not os.path.isfile(path):
            continue

        file_age = (
            now - os.path.getmtime(path)
        )

        if file_age > max_age_seconds:

            try:
                os.remove(path)
            except Exception:
                pass