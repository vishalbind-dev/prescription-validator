from flask import Flask, render_template, request
from validator import validate_prescription

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/validate", methods=["POST"])
def validate():
    patient_name = request.form.get("patient_name", "")
    doctor_name = request.form.get("doctor_name", "")
    prescription_date = request.form.get("prescription_date", "")
    medicine_text = request.form.get("medicine_text", "")

    result = validate_prescription(
        patient_name,
        doctor_name,
        prescription_date,
        medicine_text
    )

    return render_template(
        "index.html",
        result=result,
        old_patient_name=patient_name,
        old_doctor_name=doctor_name,
        old_date=prescription_date,
        old_medicine_text=medicine_text
    )


if __name__ == "__main__":
    app.run(debug=True)
