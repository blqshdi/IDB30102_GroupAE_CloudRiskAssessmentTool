
# ==========================================
# CLOUD INFORMATION SECURITY RISK TOOL
# ==========================================

import time


# ==========================================
# OPTIONS
# ==========================================

assets = [
    "Cloud Database",
    "Cloud Storage",
    "Cloud Application",
    "Cloud Backup",
    "Cloud API"
]

threats = [
    "Unauthorised Access",
    "Data Exposure",
    "Malware",
    "Data Loss",
    "Denial of Service"
]

vulnerabilities = [
    "Weak Authentication",
    "Misconfigured Permissions",
    "Unpatched Software",
    "Excessive Privileges",
    "Insufficient Backup"
]


# ==========================================
# RISK CLASSIFICATION
# ==========================================

def risk_level(score):

    if score <= 4:
        return "Low"

    elif score <= 9:
        return "Medium"

    elif score <= 16:
        return "High"

    else:
        return "Very High"


# ==========================================
# CHOOSE FROM A LIST
# ==========================================

def choose_option(title, options):

    print("\n" + title)

    for i in range(len(options)):
        print(i + 1, ".", options[i])

    while True:

        try:
            choice = int(input("Choose: "))

            if 1 <= choice <= len(options):
                return options[choice - 1]

            print("Invalid choice. Please choose a valid number.")

        except ValueError:

            print("Please enter a number.")


# ==========================================
# GET SCORE FROM 1-5
# ==========================================

def get_rating(title):

    while True:

        try:

            rating = int(input(title))

            if 1 <= rating <= 5:
                return rating

            print("Please enter a number from 1 to 5.")

        except ValueError:

            print("Please enter a number.")


# ==========================================
# ASSESS RISK
# ==========================================

def assess_risk():

    asset = choose_option(
        "Select Asset",
        assets
    )

    threat = choose_option(
        "Select Threat",
        threats
    )

    vulnerability = choose_option(
        "Select Vulnerability",
        vulnerabilities
    )

    print("\nLikelihood: 1 = Rare, 5 = Almost Certain")
    likelihood = get_rating("Likelihood (1-5): ")

    print("\nImpact: 1 = Low, 5 = Severe")
    impact = get_rating("Impact (1-5): ")

    # Risk calculation
    score = likelihood * impact

    # Risk classification
    level = risk_level(score)

    print("\n================================")
    print("           RISK RESULT")
    print("================================")

    print("Asset         :", asset)
    print("Threat        :", threat)
    print("Vulnerability :", vulnerability)
    print("Likelihood    :", likelihood)
    print("Impact        :", impact)
    print("Risk Score    :", score)
    print("Risk Level    :", level)

    print("================================")

    return {
        "asset": asset,
        "threat": threat,
        "vulnerability": vulnerability,
        "score": score,
        "level": level
    }


# ==========================================
# PRIORITISE RISKS
# ==========================================

def prioritise(risks):

    # Highest risk score first
    risks.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    print("\n================================")
    print("        RISK PRIORITISATION")
    print("================================")

    for i in range(len(risks)):

        print(
            "Priority", i + 1,
            "|",
            risks[i]["asset"],
            "| Score:",
            risks[i]["score"],
            "|",
            risks[i]["level"]
        )

    print("================================")


# ==========================================
# EVALUATION
# ==========================================

def evaluate():

    print("\n================================")
    print("        PROTOTYPE EVALUATION")
    print("================================")

    # --------------------------------------
    # TEST 1 & 2:
    # Risk Score and Classification
    # --------------------------------------

    tests = [
        (1, 1, 1, "Low"),
        (2, 2, 4, "Low"),
        (1, 5, 5, "Medium"),
        (2, 4, 8, "Medium"),
        (2, 5, 10, "High"),
        (3, 4, 12, "High"),
        (4, 4, 16, "High"),
        (4, 5, 20, "Very High"),
        (5, 5, 25, "Very High")
    ]

    correct_score = 0
    correct_level = 0

    # Start processing time
    start = time.perf_counter()

    for likelihood, impact, expected_score, expected_level in tests:

        # Calculate score
        score = likelihood * impact

        # Determine risk level
        level = risk_level(score)

        # Check score
        if score == expected_score:
            correct_score += 1

        # Check classification
        if level == expected_level:
            correct_level += 1

    # End processing time
    end = time.perf_counter()

    total = len(tests)

    # Calculate percentages
    score_accuracy = (
        correct_score / total
    ) * 100

    classification_accuracy = (
        correct_level / total
    ) * 100

    # --------------------------------------
    # DISPLAY SCORE RESULTS
    # --------------------------------------

    print("\n1. RISK SCORE CORRECTNESS")
    print(
        round(score_accuracy, 2),
        "%"
    )

    print("\n2. RISK CLASSIFICATION ACCURACY")
    print(
        round(classification_accuracy, 2),
        "%"
    )

    # --------------------------------------
    # PROCESSING TIME
    # --------------------------------------

    print("\n3. PROCESSING TIME")
    print(
        round(end - start, 8),
        "seconds"
    )

    # --------------------------------------
    # TEST 3:
    # RISK PRIORITISATION
    # --------------------------------------

    print("\n4. RISK PRIORITISATION")

    # Expected ranking from manual baseline
    expected_risks = [
        {
            "asset": "Cloud Database",
            "score": 20
        },
        {
            "asset": "Cloud API",
            "score": 12
        },
        {
            "asset": "Cloud Storage",
            "score": 8
        }
    ]

    # Test data given to the prototype
    test_risks = [
        {
            "asset": "Cloud Storage",
            "score": 8
        },
        {
            "asset": "Cloud Database",
            "score": 20
        },
        {
            "asset": "Cloud API",
            "score": 12
        }
    ]

    # Automatically determine risk level
    for risk in test_risks:

        risk["level"] = risk_level(
            risk["score"]
        )

    # Sort using the prototype
    prioritise(test_risks)

    # --------------------------------------
    # CHECK PRIORITISATION
    # --------------------------------------

    correct_positions = 0

    for i in range(len(expected_risks)):

        if (
            test_risks[i]["asset"]
            ==
            expected_risks[i]["asset"]
        ):

            correct_positions += 1

    prioritisation_agreement = (
        correct_positions
        /
        len(expected_risks)
    ) * 100

    print(
        "\nPrioritisation Agreement:",
        round(
            prioritisation_agreement,
            2
        ),
        "%"
    )

    print("================================")


# ==========================================
# MAIN MENU
# ==========================================

risks = []


while True:

    print("\n")
    print("================================")
    print("   CLOUD RISK ASSESSMENT TOOL")
    print("================================")

    print("1. Assess Risk")
    print("2. Prioritise Risks")
    print("3. Run Evaluation")
    print("4. Exit")

    print("================================")

    choice = input("Choose: ")

    # --------------------------------------
    # OPTION 1
    # --------------------------------------

    if choice == "1":

        risk = assess_risk()

        risks.append(risk)

    # --------------------------------------
    # OPTION 2
    # --------------------------------------

    elif choice == "2":

        if len(risks) == 0:

            print(
                "\nNo risks assessed yet."
            )

        else:

            prioritise(risks)

    # --------------------------------------
    # OPTION 3
    # --------------------------------------

    elif choice == "3":

        evaluate()

    # --------------------------------------
    # OPTION 4
    # --------------------------------------

    elif choice == "4":

        print("\nThank you!")

        break

    # --------------------------------------
    # INVALID OPTION
    # --------------------------------------

    else:

        print(
            "\nInvalid choice. Please try again."
        )
