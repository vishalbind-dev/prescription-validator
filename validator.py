import re
from datetime import datetime


def check_missing_fields(patient_name, doctor_name, prescription_date, medicine_text):
    missing_fields = []

    if patient_name.strip() == "":
        missing_fields.append("Patient Name")

    if doctor_name.strip() == "":
        missing_fields.append("Doctor Name")

    if prescription_date.strip() == "":
        missing_fields.append("Prescription Date")

    if medicine_text.strip() == "":
        missing_fields.append("Medicine Details")

    return missing_fields


def check_duplicate_medicines(medicine_list):
    medicine_names = []
    duplicate_medicines = []

    for medicine in medicine_list:
        name = medicine["name"].lower().strip()

        if name in medicine_names:
            if name not in duplicate_medicines:
                duplicate_medicines.append(name)
        else:
            medicine_names.append(name)

    return duplicate_medicines


def validate_dosage(dosage):
    dosage = dosage.strip()

    if dosage == "":
        return False

    pattern = r"^\d+(\.\d+)?\s*(mg|g|mcg|ml|tablet|tablets|capsule|capsules|drop|drops)$"

    if re.match(pattern, dosage.lower()):
        return True

    return False


def parse_schedule(schedule):
    schedule = schedule.lower().strip()

    frequency_words = {
        "once": 1,
        "twice": 2,
        "thrice": 3,
        "once daily": 1,
        "twice daily": 2,
        "three times daily": 3,
        "three times a day": 3,
        "four times daily": 4,
        "four times a day": 4
    }

    for word in frequency_words:
        if word in schedule:
            return frequency_words[word]

    number_pattern = r"(\d+)\s*(times|time)\s*(daily|a day)?"

    match = re.search(number_pattern, schedule)

    if match:
        return int(match.group(1))

    return 0


def parse_medicines(medicine_text):
    medicine_list = []

    lines = medicine_text.strip().split("\n")

    for line in lines:

        line = line.strip()

        if line == "":
            continue

        parts = line.split(",")

        if len(parts) >= 3:

            name = parts[0].strip()
            dosage = parts[1].strip()
            schedule = parts[2].strip()

            medicine = {
                "name": name,
                "dosage": dosage,
                "schedule": schedule
            }

            medicine_list.append(medicine)

    return medicine_list


def generate_alerts(medicine_list, duplicate_medicines):

    alerts = []

    if len(medicine_list) == 0:
        alerts.append("No valid medicine entries were found.")

    for medicine in medicine_list:

        name = medicine["name"]
        dosage = medicine["dosage"]
        schedule = medicine["schedule"]

        if not validate_dosage(dosage):
            alerts.append(
                "Dosage format issue found for " + name
            )

        frequency = parse_schedule(schedule)

        if frequency == 0:
            alerts.append(
                "Schedule could not be understood for " + name
            )

    for medicine in duplicate_medicines:
        alerts.append(
            "Duplicate medicine detected: " + medicine
        )

    if len(alerts) == 0:
        alerts.append(
            "No basic validation alerts were found. "
            "The result is only a format-based check and does not confirm medical safety."
        )

    return alerts


def save_report(patient_name, doctor_name, prescription_date,
                missing_fields, medicine_list, duplicate_medicines, alerts):

    try:
        file = open("reports/reports.txt", "a")

        file.write("\n")
        file.write("====================================\n")
        file.write("PRESCRIPTION VALIDATION REPORT\n")
        file.write("====================================\n")

        file.write("Patient Name: " + patient_name + "\n")
        file.write("Doctor Name: " + doctor_name + "\n")
        file.write("Prescription Date: " + prescription_date + "\n")

        file.write("\nMedicines:\n")

        for medicine in medicine_list:
            file.write(
                medicine["name"] + " | "
                + medicine["dosage"] + " | "
                + medicine["schedule"] + "\n"
            )

        file.write("\nMissing Fields:\n")

        if len(missing_fields) == 0:
            file.write("None\n")
        else:
            for field in missing_fields:
                file.write(field + "\n")

        file.write("\nDuplicate Medicines:\n")

        if len(duplicate_medicines) == 0:
            file.write("None\n")
        else:
            for medicine in duplicate_medicines:
                file.write(medicine + "\n")

        file.write("\nAlerts:\n")

        for alert in alerts:
            file.write(alert + "\n")

        file.write(
            "Report Generated: "
            + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            + "\n"
        )

        file.close()

    except Exception as error:
        print("Error while saving report:", error)


def validate_prescription(patient_name, doctor_name,
                          prescription_date, medicine_text):

    missing_fields = check_missing_fields(
        patient_name,
        doctor_name,
        prescription_date,
        medicine_text
    )

    medicine_list = parse_medicines(medicine_text)

    duplicate_medicines = check_duplicate_medicines(
        medicine_list
    )

    alerts = generate_alerts(
        medicine_list,
        duplicate_medicines
    )

    save_report(
        patient_name,
        doctor_name,
        prescription_date,
        missing_fields,
        medicine_list,
        duplicate_medicines,
        alerts
    )

    return {
        "missing_fields": missing_fields,
        "medicines": medicine_list,
        "duplicates": duplicate_medicines,
        "alerts": alerts
  }
