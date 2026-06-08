from datetime import datetime


def generate_report(
        recommendations,
        products):

    file_name = (
        "outputs/recommendation_report.txt"
    )

    with open(
            file_name,
            "w",
            encoding="utf-8") as file:

        file.write(
            "E-Commerce Recommendation Report\n"
        )

        file.write(
            "=" * 40 + "\n"
        )

        file.write(
            str(datetime.now()) + "\n\n"
        )

        for pid, score in recommendations:

            file.write(
                f"{products[pid]['name']} "
                f"Score:{score}\n"
            )

    print(
        "Report Generated Successfully"
    )